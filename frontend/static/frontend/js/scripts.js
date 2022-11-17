window.addEventListener('load', () => {
    a = document.querySelector(`#nav a[href='${location.pathname}']`)
    if (a != undefined) {
        a.classList.add('active')
        a.setAttribute('href', '#')
    }
})

const validateForm = form_id => {
    valid = true
    document.getElementById(form_id).querySelectorAll('input, textarea').forEach(inp => {
        if (!inp.checkValidity()) {
            valid = false
            inp.classList.add('invalid')
        }
        else
            inp.classList.remove('invalid')
    })
    return valid
}

const submitForm = (data, submit_btn, success, error) => {
    data.csrfmiddlewaretoken = document.querySelector(`input[name='csrfmiddlewaretoken']`).value
    submit_btn.classList.add('disabled')

    $.ajax({
        method: 'POST',
        url: location.pathname,
        data: data,
        success: (res) => { submit_btn.classList.remove('disabled');  success(res) },
        error: () => {
            submit_btn.classList.remove('disabled')
            error()
        }
    })
}

const showModal = id => { document.querySelector(`.modal#${id}`).classList.add('active') }
const hideModal = id => { document.querySelector(`.modal#${id}`).classList.remove('active') }