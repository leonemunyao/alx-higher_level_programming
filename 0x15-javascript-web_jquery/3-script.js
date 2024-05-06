// JavaScript Script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header in file 3-main.html:
// No using document.querySelector to select the HTML tag.
// You must use the jQuery API
$('DIV#red_header').click(function () {
    $('header').addClass('red');
});
