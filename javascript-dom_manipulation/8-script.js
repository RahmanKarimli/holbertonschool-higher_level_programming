#!/usr/bin/node
/* Write a JavaScript script that fetches from URL
    and displays the value of `hello` from that fetch
    in the HTML element with id `hello`.
*/

document.addEventListener('DOMContentLoaded', () => {
  let div = document.getElementById('hello')

  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => response.json())
    .then((data) => div.innerText = data.hello)
})
