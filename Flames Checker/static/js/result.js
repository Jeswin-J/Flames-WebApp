document.addEventListener("DOMContentLoaded", function() {
    var relation = document.querySelector(".result").textContent.trim();
    var imagePath = '';
  
    if (relation === 'LOVE') 
    {
        imagePath = 'http://localhost:5000/static/images/1.png';
    } 
    else if (relation === 'ENEMY') 
    {
        imagePath = 'http://localhost:5000/static/images/2.png';
    } 
    else if (relation === 'AFFECTION') 
    {
        imagePath = 'http://localhost:5000/static/images/3.png';
    } 
    else if (relation === 'FRIENDSHIP') 
    {
        imagePath = 'http://localhost:5000/static/images/4.png';
    } 
    else if (relation === 'MARRIAGE') 
    {
        imagePath = 'http://localhost:5000/static/images/5.png';
    }   
    else if (relation === 'SISTER') 
    {
        imagePath = 'http://localhost:5000/static/images/6.png';
    } 
    else 
    {
        imagePath = 'default.png';
    }
  
    document.body.style.backgroundImage = 'url(' + imagePath + ')';
  });
  