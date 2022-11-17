from django.shortcuts import render as dj_render, redirect
from django.http import JsonResponse, HttpResponse

from server.models import *

from .forms import *
from server import auth, blog

import uuid

INVALID_FORM = JsonResponse({ 'valid': False, 'message': 'The form submission was invalid! Please try again!' })

def __logged(req):
    if req.session.get('email', False):
        if len(User.objects.filter(email=req.session['email'], activated=True)) > 0:
            return True

        del req.session['email']
    return False

def render(req, template_name, context={}, status=200):
    context['logged_in'] = __logged(req)
    return dj_render(req, template_name, context, status=status)



# Create your views here.
def Home(req):
    return render(req, 'frontend/index.html')



def Logout(req):
    if req.session.get('email', False):
        del req.session['email']
    return redirect('/')



def Blog(req):
    if req.method == 'POST':
        form = BlogForm(req.POST)

        if not __logged(req): return HttpResponse(req, 403)
        if not form.is_valid(): return INVALID_FORM

        blog.create_blog(form.cleaned_data, req.session['email'])
        return JsonResponse({ 'valid': True })

    blogs = [
        { 'uid': post.uid.hex, 'author': post.user.name, 'nickname': post.user.nickname, 'title': post.title, }
        for post in Post.objects.all().order_by('-pk')
    ]
    return render(req, 'frontend/blog.html', { 'blogs': blogs })



def Blog_Post(req, uid):
    if len(uid) != 32: return  HttpResponse(req, 404)

    post = Post.objects.filter(uid=uuid.UUID(uid))
    if len(post) == 0: return HttpResponse(req, 404)
    post = post[0]

    if req.method == 'POST':
        if not __logged(req): return HttpResponse(req, 403)
        if not req.POST.get('form') and not req.POST.get('method'): return HttpResponse(req, 400)

        if req.POST['form'] == 'blog':
            if post.user.email != req.session['email']: return HttpResponse(req, 403)

            if req.POST['method'] == 'edit':
                form = BlogForm(req.POST)
                if not form.is_valid(): return INVALID_FORM
                blog.edit_blog(form.cleaned_data, uid)
                return JsonResponse({'valid': True})
            
            if post.user.email != req.session['email']: return HttpResponse(req, 403)
            blog.remove_blog(uid)
            return JsonResponse({ 'valid': True })

        if req.POST['method'] == 'post':
            form = ReplyForm(req.POST)
            if not form.is_valid(): return INVALID_FORM
            blog.post_reply(form.cleaned_data, uid, req.session['email'])
            return JsonResponse({ 'valid': True })

    replies = [{ 
        'name': reply.user.name,
        'nickname': reply.user.nickname,
        'content': reply.content 
    } for reply in Reply.objects.filter(post=post).order_by('pk')]
    return render(req, 'frontend/post.html', {
        'author': post.user.name,
        'nickname': post.user.nickname,
        'is_author': (post.user.email == req.session.get('email', '')),
        'title': post.title,
        'content': post.content,
        'replies': replies,
    })



def Auth(req):
    if req.method == 'POST':
        if not req.POST.get('form', False):
            return HttpResponse(req, 400)
        
        if req.POST['form'] == 'login':
            form = LoginForm(req.POST)
            if form.is_valid(): res = auth.login(form.cleaned_data)

        else:
            form = SignupForm(req.POST)
            if form.is_valid(): res = auth.signup(form.cleaned_data)
        
        if not form.is_valid(): return INVALID_FORM

        if res['valid']: req.session['email'] = form.cleaned_data['email']
        return JsonResponse(res)


    if __logged(req): return redirect('/')
    return dj_render(req, 'frontend/auth.html', { 'logged_in': False })