var canvas = document.getElementById("canvasid");
var ctx = canvas.getContext("2d");

//canvas in html cant use it with jQuery
//var ctx = $("#canvasid  ").getContext("2d");

//https://www.sitepoint.com/introduction-to-jcanvas-jquery-meets-html5-canvas/

//css-tricks - named colors and hex equivalents
ctx.fillStyle = "Red";
ctx.fillRect(0,0, 10,10);
ctx.lineWidth = 4;
ctx.strokeRect(0, 0, 10, 10);

//all required to draw a line
ctx.lineWidth = 4;
ctx.strokeStyle = "Green";
ctx.beginPath();
ctx.moveTo(100, 100);
ctx.lineTo(200, 200);
ctx.stroke();
console.log(ctx);

//draw a robot

//arc = ctx.arc, ctx.stroke- set center coordinate and radius
//full circle is 2pi radians
