$(document).ready(function() {
  $('.list li').click(function() {
    c_name = $(this).find('a').attr("data-name") 
    window.location.href = '/concept/' + c_name
  });
});