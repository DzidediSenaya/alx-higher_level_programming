#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);

    const characterUrls = movieData.characters;

    // Function to fetch and print character names by index
    const fetchCharacterName = (index) => {
      if (index < characterUrls.length) {
        request(characterUrls[index], (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else if (charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
            fetchCharacterName(index + 1);
          }
        });
      }
    };

    console.log("Characters in " + movieData.title + ":");
    fetchCharacterName(0);
  }
});
