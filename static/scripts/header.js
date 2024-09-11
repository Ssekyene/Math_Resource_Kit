// $("document").ready(function() {
//   console.log("before clicked");

//   $('.menu_icon').click(function() {
//     // alert();
//     console.log("icon clicked");
//     // toggleMenu();
//     $('.nav_links').toggleClass('active');
//   });  
// });

// function toggleMenu() {
//   const navLinks = $('.nav_links');
//   navLinks.classList.toggle('active');
// }

// function myFunction() { 
//   alert("Function is called!");
// }

$(document).ready(function () {
  // Open the mobile nav menu
  $('.menu_icon').click(function () {
      $('.nav_links').addClass('active');
      $('.close_icon').addClass('active');
      $('body').addClass('nav_active');
    });
    
    // Close the mobile nav menu
    $('.close_icon').click(function () {
      $('.nav_links').removeClass('active');
      $('.close_icon').removeClass('active');
      $('body').removeClass('nav_active');
    });
});