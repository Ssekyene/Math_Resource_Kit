$(document).ready(function () {
  // click listening event for the concept list blocks
  $('.list li').click(function () {
    const conceptName = $(this).find('a').attr('data-name');
    window.location.href = '/concept/' + conceptName;
  });

  $('.quiz .disclose').click(function () {
    if ($('.quiz section').hasClass('hide')) {
      $('.quiz section').removeClass('hide');
      $('.quiz section').addClass('show');
      $(this).text('Hide quiz');
    } else {
      $('.quiz section').removeClass('show');
      $('.quiz section').addClass('hide');
      $(this).text('Show quiz');
    }
  });

  // generating data from the quiz form for ajax post
  $('#quiz-form').on('submit', function (event) {
    event.preventDefault();
    console.log("clicked on submit button")
    const formData = {};
    const conceptId = $(this).data('concept_id');

    $('#quiz-form input[type="radio"]:checked').each(function () {
      const quizId = $(this).attr('name');
      const selectedAns = $(this).val();
      formData[quizId] = selectedAns;
    });

    // sending quiz form data via ajax
    const quizJson = JSON.stringify(formData);
    const quizFormUrl = 'http://' + window.location.hostname + ':5001/api/concepts/' + conceptId + '/quizzes';
    $.ajax({
      url: quizFormUrl,
      type: 'POST',
      data: quizJson,
      contentType: 'application/json',
      success: function (response) {
        quizScore(response);
      },
      error: () => {
        alert('Quiz submition failed');
      }
    });
  });
});

function quizScore (data) {
  const score = data.score;
  const total = data.total;
  console.log("function called")
  
  $('.quiz .result').removeClass('hide');
  $('.quiz .result').addClass('show');
  if (score === total) {
    $('.quiz .result').css({
      color: 'green'
    });
    $('#quiz-form .submit').addClass('hide');
  }
  $('.quiz .result').text(score + ' correct out of ' + total);
}
