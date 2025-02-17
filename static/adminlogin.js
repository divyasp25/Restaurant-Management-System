const loginForm = document.getElementById('login-form');
const errorMessage = document.getElementById('error-message');

loginForm.addEventListener('submit', (event) => {
    event.preventDefault(); 
    const username = loginForm.elements.username.value;
    const password = loginForm.elements.password.value;

    // Basic form validation (optional)
    if (username === '' || password === '') {
        errorMessage.textContent = 'Please enter username and password.';
        return;
    }

    // Send data to server using AJAX or Fetch API
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username,
            password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (!data.success) {
            errorMessage.textContent = data.message;
        } else {
            window.location.href = '/adminlogin/manager';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
