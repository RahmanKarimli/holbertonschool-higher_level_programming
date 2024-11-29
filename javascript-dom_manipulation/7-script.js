#!/usr/bin/node
/* Write a JavaScript script that fetches and
    lists the `title` for all movies by using URL
*/

let ul = document.getElementById('list_movies')

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => data.results.forEach((elem) => {
    let li = document.createElement('li')
    li.textContent = elem.title
    ul.appendChild(li)
  }));
