#!/usr/bin/node
/* Write a JavaScript script that adds a `li` element
    to a list when the user clicks on the element with id `add_item`
*/

let add_item = document.getElementById('add_item')
let my_list = document.querySelector('ul')

add_item.addEventListener('click', () => {
  let item = document.createElement('li')
  item.innerText = 'Item'
  my_list.appendChild(item)
})
