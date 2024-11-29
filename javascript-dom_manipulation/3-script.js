#!/usr/bin/node
/* Write a JavaScript script that toggles the class
 of the `header` element when the user clicks
 on the tag id `toggle_header`
*/
let toggle_header = document.getElementById('toggle_header')
let header = document.querySelector('header')

toggle_header.addEventListener('click', () => {
  if (header.classList.length === 0) {
    header.classList.add('red')
  } else if (header.classList.contains('red')) {
    header.classList.replace('red', 'green')
  } else if (header.classList.contains('green')) {
    header.classList.replace('green', 'red')
  }
});
