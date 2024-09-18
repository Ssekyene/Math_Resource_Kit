$(document).ready(function() {
  // click listening event for the concept list blocks
  $('.list li').click(function() {
    c_name = $(this).find('a').attr("data-name") 
    window.location.href = '/concept/' + c_name
  });

  $('#quiz-form').on('submit', function(event) {
    
  });
});