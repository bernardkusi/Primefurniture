let bars=document.getElementsByClassName('bars')[0];
let nav=document.querySelector('nav');

bars.addEventListener('click',()=>{
    nav.classList.toggle('navactive');
    // alert('clicked');
});