//with empty text() is to retrieve the text
//to put it back into html use text(newtexttobereplaced)

function changeToUpperCase()
{
	var heading = $("#Hello-Customers").text();
	console.log(heading);
	
	var varuppercase = heading.toUpperCase();
	return varuppercase;
}


$("#Hello-Customers").text(changeToUpperCase());