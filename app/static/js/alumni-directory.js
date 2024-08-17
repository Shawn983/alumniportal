// Example function to load alumni data - This would realistically be loaded from a server
document.addEventListener("DOMContentLoaded", function() {
    const alumniList = document.getElementById("alumniList");
    // Example data - replace with actual data fetching logic
    const alumniData = [
        { fullName: 'John Doe', class: '10/05', openToCollab: true, id: 1 },
        { fullName: 'Jane Smith', class: '12/15', openToCollab: false, id: 2 },
        // Add more alumni data here
    ];

    alumniData.forEach(alumni => {
        const entry = document.createElement("div");
        entry.innerHTML = `<strong>${alumni.fullName}</strong> (${alumni.class}) `;
        if (alumni.openToCollab) {
            const button = document.createElement("button");
            button.textContent = "Collaborate";
            button.onclick = () => showForm(alumni.id);
            entry.appendChild(button);
        }
        alumniList.appendChild(entry);
    });
});

function showForm(alumniId) {
    const form = document.getElementById("collabForm");
    form.style.display = "block"; // Show the form
    form.onsubmit = (event) => submitRequest(event, alumniId);
}

function submitRequest(event, alumniId) {
    event.preventDefault(); // Prevent form submission from reloading the page
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const description = document.getElementById("description").value;
    console.log(`Request submitted for alumni ID ${alumniId} by ${name} (${email}): ${description}`);
    // Here you would send data to the server to notify the alumni via email
}
