$("document").ready(function() {
  console.log("before clicked");

  $('.menu_icon').click(function() {
    // alert();
    console.log("icon clicked");
    // toggleMenu();
    $('.nav_links').toggleClass('active');
  });  
});

function toggleMenu() {
  const navLinks = $('.nav_links');
  navLinks.classList.toggle('active');
}

function myFunction() {
  alert("Function is called!");
}