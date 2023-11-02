$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results; // Extract the movie array from the JSON data

    const ul = $('#list_movies'); // Select the UL element

    // Loop through the movies and append each title to the UL
    $.each(movies, function (index, movie) {
      ul.append($('<li>' + movie.title + '</li>'));
    });
  });
});

