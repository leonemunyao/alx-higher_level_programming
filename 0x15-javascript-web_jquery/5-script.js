// JavaScript Script that adds a <li> element to a list when the user clicks on the tag DIV#add_item in file 5-main.html:
// The new element must be: <li>Item</li>. The element must be added to UL.my_list.
// Can't use document.querySelector to select the HTML tag.
// You must use the jQuery API
$('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
});
