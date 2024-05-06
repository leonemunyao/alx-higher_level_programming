// A JavaScript script that adds, removes and clears LI elements from a list when the user clicks:
// The new element must be: <li>Item</li>
// The new element must be added to UL.my_list
// When the user clicks on DIV#add_item: a new element is added to the list
// When the user clicks on DIV#remove_item: a last element is removed to the list
// When the user clicks on DIV#clear_list: all elements of the list are removed
// You can't use document.querySelector to select the HTML tag
// You must use the jQuery API
// The Script must work when it is imported from the HEAD tag.

$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
$('DIV#remove_item').click(function () {
  $('UL.my_list li').last().remove();
});
$('DIV#clear_list').click(function () {
  $('UL.my_list').empty();
});
