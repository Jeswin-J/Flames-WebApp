var slideIndex = 0;
var slides = document.getElementsByClassName("slide");

function showNextSlide() {
    if (slides.length > 0 && slideIndex < slides.length - 1) {
        slides[slideIndex].style.display = "none";
        slideIndex++;
        slides[slideIndex].style.display = "block";
    } 
    else if (slides.length > 0 && slideIndex === slides.length - 1) {
        slides[slideIndex].style.display = "block";
    }
}


var slideDuration = 1800;
var intervalID = setInterval(showNextSlide, slideDuration);
window.onload = function() {
    var slideshow = document.getElementsByClassName("slideshow")[0];
    if (slideshow && slides.length > 0) {
        slideshow.style.display = "block";
        slides[slideIndex].style.display = "block";
        
    }
};