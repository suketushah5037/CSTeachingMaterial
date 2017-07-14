
var fading = function(option) 
{
	if(option == 0)
	{
		$("h1").fadeOut(3000);
	}
	else
	{
		$("h1").fadeIn(3000);	
	}
};

fading(0);
console.log("fade out");
var id = setTimeout(fading, 10000);
fading(1);
console.log("fade in");
console.log(id);

clearTimeout(id);