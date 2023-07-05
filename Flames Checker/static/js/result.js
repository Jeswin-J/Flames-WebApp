document.addEventListener("DOMContentLoaded", function() {
    var relation = document.querySelector(".result").textContent.trim();
    var imagePath = '';
  
    if (relation === 'LOVE') 
    {
        imagePath = '/static/images/1.png';
    } 
    else if (relation === 'ENEMY') 
    {
        imagePath = '/static/images/2.png';
    } 
    else if (relation === 'AFFECTION') 
    {
        imagePath = '/static/images/3.png';
    } 
    else if (relation === 'FRIENDSHIP') 
    {
        imagePath = '/static/images/4.png';
    } 
    else if (relation === 'MARRIAGE') 
    {
        imagePath = '/static/images/5.png';
    }   
    else if (relation === 'SISTER') 
    {
        imagePath = '/static/images/6.png';
    } 
    else 
    {
        imagePath = 'default.png';
    }
  
    document.body.style.backgroundImage = 'url(' + imagePath + ')';
  });
  