const login = btn => {
    if (validateForm('login_form')) {
        error = document.querySelector('.error')
        error.innerText = ''

        submitForm({
            'email': document.getElementById('login_email').value,
            'password': document.getElementById('login_pass').value,
            'form': 'login'
        }, btn, (res) => { 
            if (res.valid)
                location.pathname = '/blog/'
            else
                error.innerText = res.message
        }, () => { error.innerText = 'Something went wrong! Please try again!!' })
    }
}

const signup = btn => {
    if (validateForm('signup_form2')) {
        error = document.querySelector('.error')
        error.innerText = ''

        if (document.getElementById('signup_pass').value != document.getElementById('signup_cpass').value) {
            error.innerText = 'Passwords do not match!'
            return
        }

        submitForm({
            'name': document.getElementById('signup_name').value,
            'nickname': document.getElementById('signup_nickname').value,
            'email': document.getElementById('signup_email').value,
            'password': document.getElementById('signup_pass').value,
            'form': 'signup'
        }, btn, (res) => { 
            if (res.valid) {
                document.querySelector('.success').innerText = 'Your account has been created successfully! It will be activated within 1 or 2 days!!'
                document.getElementById('signup_name').value = ''
                document.getElementById('signup_nickname').value = ''
                document.getElementById('signup_email').value = ''
                document.getElementById('signup_pass').value = ''
                document.getElementById('signup_cpass').value = ''
            }
            else
                error.innerText = res.message
        }, () => { error.innerText = 'Something went wrong! Please try again!!' })
    }
}