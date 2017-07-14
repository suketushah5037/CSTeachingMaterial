//DOM - Document object model, lets you access the HTML in a webpage
//jQuery a JS library - to choose elements in HTML and change them


//Get the heading and display it on the console
//DOM
var page_heading = document.getElementById("Hello-Customers");
console.log(page_heading.innerHTML);

var newHeading = prompt("Enter a new page heading");
page_heading.innerHTML = newHeading;


