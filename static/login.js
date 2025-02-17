const registrationForm = document.getElementById('registration-form');
const errorMessage = document.getElementById('error-message');
registrationForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    const username = document.getElementById('username').value;
    const tableno = document.getElementById('tableno').value;
    const phn_no = document.getElementById('phn_no').value;
    if (tableno < 1 || tableno > 6) {
        errorMessage.textContent = "Please enter table number properly";
    } else {
        // Send data to Flask using AJAX (replace with your Flask endpoint)
        fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username,
                tableno,
                phn_no
            })
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) { // Check for success response from Flask
                    window.location.href = `/welcome/${username}`; // Redirect with username
                } else {
                    console.error(data.error); // Handle errors
                }
            })
            .catch(error => console.error(error));
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const goToOtherPageButton = document.getElementById('goToOtherPage');

    goToOtherPageButton.addEventListener('click', function () {
        window.location.href = '/adminlogin';
    });
});
