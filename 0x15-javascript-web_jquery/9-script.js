// JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello..
// You can't use document.querySelector to select the HTML tag.
// You must use the jQuery API
// The translation of “Hello” must be displayed in the HTML tag DIV#hello

$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
    }
);
