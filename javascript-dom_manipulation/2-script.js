#!/usr/bin/node
/* Write a JavaScript script
that adds the class red
to the header element
when the user clicks on the tag with id red_header
*/

let div = document.getElementById('red_header')
let header = document.querySelector('header')

div.addEventListener('click', () => {
  header.classList.add('red')
})
