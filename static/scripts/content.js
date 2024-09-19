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
    // console.log("clicked on submit button")
    const doneQuizNum = $('#quiz-form input[type="radio"]:checked').length;
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
    
    if (doneQuizNum === 0) {
      $('.quiz .result').removeClass('hide');
      $('.quiz .result').addClass('show');
      $('.quiz .result').text('Please Select Options');
      $('.quiz .result').css('color', '#6F42C1');

    } else {
      $.ajax({
        url: quizFormUrl,
        type: 'POST',
        data: quizJson,
        contentType: 'application/json',
        success: function (response) {
          quizScore(response);
        },
        error: () => {
          alert('Quiz Service failed! Try Again');
        }
      });
    }
  });

  // getting the keyword search for concepts on pressing enter
  $('#search_input').keydown(function (event) {
    if (event.keyCode === 13) {
      event.preventDefault();
      const keyword = $(this).val().replace(' ', '_');
      let searchUrl;
      if (!keyword) {
        searchUrl = 'http://' + window.location.hostname + ':5001/api/concepts';
      }
      else {
        searchUrl = 'http://' + window.location.hostname + ':5001/api/concepts_search/' + keyword;
      }

      $.ajax({
        url: searchUrl,
        type: 'GET',
        success: (response) => {
          $('.list ul ').empty();
          return matchedConcepts(response);
        },
        error: () => {
          alert('Search Service failed! Try Again');
        }
      });
    }
  });

  // getting the keyword search for concepts on clicking search icon
  $('.search .search_icon').click(function () {
    const keyword = $('#search_input').val().replace(' ', '_');
    let searchUrl;
    if (!keyword) {
      searchUrl = 'http://' + window.location.hostname + ':5001/api/concepts';
    }
    else {
      searchUrl = 'http://' + window.location.hostname + ':5001/api/concepts_search/' + keyword;
    }

    $.ajax({
      url: searchUrl,
      type: 'GET',
      success: (response) => {
        $('.list ul ').empty();
        return matchedConcepts(response);
      },
      error: () => {
        alert('Search Service failed! Try Again');
      }
    });
  });
});

function quizScore (data) {
  const score = data.score;
  const total = data.total;
  // console.log("function called")
  $('.quiz .result').removeClass('hide');
  $('.quiz .result').addClass('show');
  if (score === total) {
    $('.quiz .result').css({
      color: 'green'
    });
    $('#quiz-form .submit').addClass('hide');
  } else{
    $('.quiz .result').css({
      color: 'red'
    });
  }
  $('.quiz .result').text(score + ' correct out of ' + total);
}

function matchedConcepts (data) {
  if (!data.length) {
    const input = $('#search_input').val();
    $('.list ul').css('border', 'none');
    $('.list ul').append('<p>No Results found for '+input+'</p>');
    $('.list ul p').css({
      width: '200px',
      margin: '0 auto'
    });
  }else {
    data.sort((a, b) => a.priority - b.priority);
    $('.list ul').append(
      data.map((concept) => {
        return `<li><a href="/concept/${concept.name}" data-name="${concept.name}">${concept.name}</a></li>`
      })
      );
  }
}