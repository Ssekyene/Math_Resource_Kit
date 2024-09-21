$(document).ready(function () {
  // Open the mobile nav menu
  $('.menu_icon').click(function() {
      $('.nav_links').addClass('active');
      $('.close_icon').addClass('active');
      $('body').addClass('nav_active');
    });
    
    // Close the mobile nav menu
    $('.close_icon').click(function() {
      $('.nav_links').removeClass('active');
      $('.close_icon').removeClass('active');
      $('body').removeClass('nav_active');
    });

    // click event for the logo
    $('div#header_logo').click(function() {
      window.location.href = '/home'
    });
});