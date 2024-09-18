$(document).ready(function() {
  // click listening event for the concept list blocks
  $('.list li').click(function() {
    c_name = $(this).find('a').attr("data-name") 
    window.location.href = '/concept/' + c_name
  });
  
  // generating data from the quiz form for ajax post
  const formData = {}
  const concept_id = ''

  $('#quiz-form').on('submit', function(event) {
    event.preventDefault();
    concept_id = $(this).data('concept_id');
    
    $('#quiz-form input[type="radio"]:checked').each(function() {
      const quiz_id = $(this).attr('name')
      const selected_ans = $(this).val()
      formData[quiz_id] = selected_ans
    });
  });


  //sending quiz form data via ajax
  const quizJson = JSON.stringify(formData);
  quizFormUrl = 'http://' + window.location.hostname + ':5001/concepts/' + concept_id + '/quizzes';

  $.ajax({
    url: quizFormUrl,
    type: 'POST',
    data: quizJson,
    contentType: 'application/json',
    success: function(response) {
      quizScore(response);
    },
    error: () => {
      alert('Quiz submition failed');
    }
  });
});

function quizScore(data) {
  const score = data.score;
  const total = data.total;
  $('.quiz .result').addClass('show');
  if (score === total) {
    $('.quiz .result').css({
      'color': 'green',
      'border': '1px solid green'
    });
    $('#quiz-form .submit').addClass('hide');
  }
  $('.quiz .result').text(score + ' correct out of ' + total);
}