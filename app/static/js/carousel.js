document.addEventListener("DOMContentLoaded", function() {
    let slideIndex = 1;  // Start from the first slide
    let slides = document.getElementsByClassName("carousel-slide")[0].children; // Get all slides
    let slideInterval;

    // Function to display the correct slide
    function showSlides(n) {
        if (n > slides.length) { 
            slideIndex = 1; // Reset to the first slide if exceeding the number of slides
        }  
        if (n < 1) { 
            slideIndex = slides.length; // Set to the last slide if going below the first one
        }
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";  // Hide all slides
        }
        slides[slideIndex - 1].style.display = "block";  // Display the appropriate slide
    }

    // Function to change slides
    function plusSlides(n) {
        clearInterval(slideInterval); // Stop the automatic slideshow
        showSlides(slideIndex += n); // Increment or decrement the slide index
        slideInterval = setInterval(function() { plusSlides(1) }, 7000); // Restart the automatic slideshow
    }

    // Attach events to buttons
    document.querySelector('.prev').addEventListener('click', function() {
        plusSlides(-1);
    });

    document.querySelector('.next').addEventListener('click', function() {
        plusSlides(1);
    });

    // Function to start the carousel
    function startCarousel() {
        showSlides(slideIndex); // Show the initial slide
        slideInterval = setInterval(function() { plusSlides(1) }, 7000); // Start automatic slideshow
    }

    startCarousel(); // Initialize the carousel
});
