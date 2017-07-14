var appendDOM = function()
{
	for(var i = 0; i < 3; i++)
	{
		var hobby = prompt("State one hobby");
		$("body").append("<p>" + hobby + "<p>");
	}
};

appendDOM();