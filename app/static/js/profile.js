document.addEventListener('DOMContentLoaded', function () {
    // Fetch and populate profile data
    fetch('/api/profile')
    .then(response => response.json())
    .then(profile => {
        document.getElementById('fullname').value = profile.fullname;
        document.getElementById('graduationDate').value = profile.graduationDate;
        document.getElementById('classNumber').value = profile.classNumber;
        document.getElementById('contributions').value = profile.contributions;
        document.getElementById('email').value = profile.email;
        document.getElementById('openToCollaboration').checked = profile.openToCollaboration;
    })
    .catch(error => console.error('Error fetching profile:', error));

    // Handle form submission to update profile
    const profileForm = document.getElementById('profileForm');
    profileForm.addEventListener('submit', function(event) {
        event.preventDefault();
        updateProfile();
    });

    function updateProfile() {
        const fullname = document.getElementById('fullname').value;
        const graduationDate = document.getElementById('graduationDate').value;
        const classNumber = document.getElementById('classNumber').value;
        const contributions = document.getElementById('contributions').value;
        const openToCollaboration = document.getElementById('openToCollaboration').checked;

        fetch('/api/update-profile', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                fullname,
                graduationDate,
                classNumber,
                contributions,
                openToCollaboration
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('Profile updated successfully!');
            } else {
                alert('Failed to update profile: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error updating profile:', error);
            alert('Failed to update profile. Please try again.');
        });
    }

    // Show the change password form
    window.showChangePasswordForm = function () {
        document.getElementById('changePasswordForm').style.display = 'block';
    }

    // Hide the change password form
    window.hideChangePasswordForm = function () {
        document.getElementById('changePasswordForm').style.display = 'none';
    }

    // Handle form submission to change password
    const passwordForm = document.getElementById('passwordForm');
    passwordForm.addEventListener('submit', function(event) {
        event.preventDefault();
        changePassword();
    });

    function changePassword() {
        const currentPassword = document.getElementById('currentPassword').value;
        const newPassword = document.getElementById('newPassword').value;
        const confirmNewPassword = document.getElementById('confirmNewPassword').value;

        if (newPassword !== confirmNewPassword) {
            alert('New passwords do not match!');
            return;
        }

        fetch('/api/change-password', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                currentPassword,
                newPassword
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('Password updated successfully!');
                hideChangePasswordForm();
            } else {
                alert('Failed to update password: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error updating password:', error);
            alert('Failed to update password. Please try again.');
        });
    }
});




document.addEventListener('DOMContentLoaded', function () {
    // Load collaboration requests dynamically
    fetchCollaborationRequests();
});

function fetchCollaborationRequests() {
    fetch('/api/get-collab-requests')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.querySelector('#collabRequests tbody');
        tableBody.innerHTML = ''; // Clear existing rows
        data.forEach(request => {
            const row = tableBody.insertRow();
            row.insertCell(0).textContent = request.requestor_full_name;
            row.insertCell(1).textContent = request.requestor_contact_number;
            row.insertCell(2).textContent = request.requestor_email;
            row.insertCell(3).textContent = request.description;
            row.insertCell(4).textContent = request.date_of_request;
        });
    })
    .catch(error => console.error('Error loading collaboration requests:', error));
}
