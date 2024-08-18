document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');

    // Event listeners for login and register forms
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        loginUser();
    });

    registerForm.addEventListener('submit', function(event) {
        event.preventDefault();
        registerUser();
    });

    // Function to log in the user
    function loginUser() {
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        fetch('/login', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({email, password})
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                window.location.href = '/profile';  // Redirect to profile page
            } else {
                alert('Login failed: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error logging in:', error);
            alert('Login failed. Please try again.');
        });
    }

    // Function to register the user
    function registerUser() {
        const fullname = document.getElementById('fullname').value;
        const email = document.getElementById('regEmail').value;
        const password = document.getElementById('regPassword').value;
        const confirmPassword = document.getElementById('confirmPassword').value;

        if (password !== confirmPassword) {
            alert('Passwords do not match!');
            return;
        }

        fetch('/register', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({fullname, email, password})
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('Registration successful!');
                window.location.href = '/profile';  // Redirect to profile page
            } else {
                alert('Registration failed: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error registering:', error);
            alert('Registration failed. Please try again.');
        });
    }

    // Show the registration form and hide the login form
    window.showRegisterForm = function () {
        loginForm.style.display = 'none';
        registerForm.style.display = 'block';
    }

    // Hide the registration form and show the login form
    window.hideRegisterForm = function () {
        registerForm.style.display = 'none';
        loginForm.style.display = 'block';
    }
});
