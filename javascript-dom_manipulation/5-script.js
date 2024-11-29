#!/usr/bin/node
/* Write a JavaScript script that updates the text
    of the `header` element to `New Header!!!`
*/

let update_header = document.getElementById('update_header')
let header = document.querySelector('header')

update_header.addEventListener('click', () => {
  header.innerText = 'New Header!!!'
})
