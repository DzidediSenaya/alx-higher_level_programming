#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log("Characters in " + movieData.title + ":");

    const characterUrls = movieData.characters;

    const fetchCharacterName = (url) => {
      request(url, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else if (charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        } else {
          console.error("Error fetching character data. Status code: " + charResponse.statusCode);
        }
      });
    };

    characterUrls.forEach((url) => {
      fetchCharacterName(url);
    });
  } else {
    console.error("Error fetching movie data. Status code: " + response.statusCode);
  }
});
