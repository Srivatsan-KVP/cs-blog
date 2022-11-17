textarea = null;
const updateTextArea = () => {
    textarea.style.height = '1px'
    if (textarea.getAttribute('disabled') == null)
        textarea.style.height = `calc(${textarea.scrollHeight}px - 2.5rem)`
    else
        textarea.style.height = `${textarea.scrollHeight}px`
}


title = null, content = null
const has_changed = () => {
    post_btn = document.querySelector('#post .submit')
    if (post_btn != undefined) {
        if (title.dataset.init != title.value || content.value != content.innerHTML)
            post_btn.classList.remove('disabled')
        else
            post_btn.classList.add('disabled')
    }
}

const editPost = btn => {
    if (validateForm('post')) {
        error = document.querySelector('#post .error')
        success = document.querySelector('#post .success')
        error.innerText = ''
        success.innerText = ''

        submitForm({
            'title': title.value,
            'content': content.value,
            'form': 'blog',
            'method': 'edit'
        }, btn, (res) => { 
            if (res.valid) {
                success.innerText = 'Changes saved successfully!'
                title.dataset.init = title.value
                content.innerHTML = content.value
                has_changed()
            }
                
            else
                error.innerText = res.message
        }, () => { error.innerText = 'Something went wrong! Please try again!!' })
    }
}

const deleteBlog = btn => {
    error = document.querySelector('.modal#delete_modal .error')
    error.innerText = ''

    submitForm({
        'form': 'blog',
        'method': 'delete'
    }, btn, (res) => { 
        if (res.valid)
            location.pathname = '/blog/'
        else
            error.innerText = res.message
    }, () => { error.innerText = 'Something went wrong! Please try again!!' })
}


const postReply = btn => {
    if (validateForm('reply_modal')) {
        error = document.querySelector('.modal#reply_modal .error')
        error.innerText = ''

        submitForm({
            'form': 'reply',
            'method': 'post',
            'content': document.querySelector('.modal#reply_modal textarea').value,
        }, btn, (res) => { 
            if (res.valid)
                location.reload()
            else
                error.innerText = res.message
        }, () => { error.innerText = 'Something went wrong! Please try again!!' })
    }
}



window.addEventListener('load', () => {
    textarea = document.querySelector('#post textarea')
    title = document.querySelector('#post input')
    content = document.querySelector('#post textarea')

    title.addEventListener('keyup', has_changed)
    content.addEventListener('keyup', has_changed)

    updateTextArea()
})