#!/usr/bin/node
/* JavaScript script that updates the text color
  of the `header` element to red (`#FF0000`)
  when the user clicks on the tag.
*/
let header = document.querySelector('header');
let div = document.getElementById('red_header');
div.addEventListener('click', () => {
  header.style.color = '#FF0000'
});
