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
    
    // Helper function to fetch character names
    const fetchCharacterName = (url) => {
      request(url, (error, response, body) => {
        if (error) {
          console.error(error);
        } else if (response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    };
    
    // Fetch and print character names
    characterUrls.forEach((url) => {
      fetchCharacterName(url);
    });
  }
});
