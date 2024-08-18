document.addEventListener("DOMContentLoaded", function() {
    fetch('/api/alumni')
    .then(response => response.json())
    .then(alumniData => {
        const alumniList = document.getElementById("alumniList");
        alumniData.forEach(alumni => {
            const entry = document.createElement("div");
            entry.innerHTML = `<strong>${alumni.fullName}</strong> (${alumni.class}) `;
            if (alumni.openToCollab) {
                const button = document.createElement("button");
                button.textContent = "Collaborate";
                button.addEventListener('click', () => showCollabForm(alumni.fullName, alumni.email));
                entry.appendChild(button);
            }
            alumniList.appendChild(entry);
        });
    })
    .catch(error => console.error('Error loading alumni data:', error));
});

function showCollabForm(fullName, email) {
    const collabForm = document.getElementById('collabForm');
    document.getElementById('alumniName').value = fullName;
    document.getElementById('alumniEmail').value = email;
    collabForm.style.display = 'block';
}

const collabForm = document.getElementById('collabForm');
if (collabForm) {
    collabForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = {
            requestorName: document.getElementById('requestorName').value,
            requestorContactNumber: document.getElementById('requestorContactNumber').value,
            requestorEmail: document.getElementById('requestorEmail').value,
            description: document.getElementById('description').value,
            alumniName: document.getElementById('alumniName').value,
            alumniEmail: document.getElementById('alumniEmail').value
        };

        fetch('/submit-collab-request', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(formData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok.');
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
            alert('Collaboration request sent!');
            document.getElementById('collabForm').style.display = 'none';  // Hide form after success
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('Failed to send collaboration request.');
        });
    });
}
