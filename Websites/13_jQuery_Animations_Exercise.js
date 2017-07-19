//For each of the friends in the array, add them to the body, change  txt of h1 //element and hide and fadeIn each name one by one
//Modify all the <p> elements to add "is an studdo"

//screen size is the image size

//jQuery selectors, timers and events
var arrfriends = ["Shyam", "Gopal", "Mukund"];
console.log(arrfriends);
console.log(arrfriends.length);
$maxindex = arrfriends.length;

$("html").mousemove(
    function(event)
    {
        $("#Hello-Customers").offset(
            {
                left: event.pageX,
                top:event.pageY  
            }
        );


    }
    );

    var getRandomNumber = function (size) {
        return Math.floor(Math.random() * size);
    };

    var width = 400;
    var height = 400;

    //treasure coordinates
    var target =
    {
        x: 0,//getRandomNumber(width),
        y: 0 //getRandomNumber(height)
    };

    var getDistance = function (event, target) {
        var diffx = event.offsetX - target.x;
        var diffy = event.offsetY - target.y;
        console.log(diffx);
        console.log(diffy);

        return Math.sqrt((diffx * diffx) + (diffy * diffy));
    };

var timeUp = function () {
        alert("time up");
};
var timeOutId = setTimeout(timeUp, 3000);

var clickedEvent = function(event) {
    console.log("click = " + event.pageX + " " + event.pageY);
    
    var distance = getDistance(event, target);
    $("#distance").text("you are " + distance);


};

var leftOffset = 0;

//move the heading around
var moveHeading = function () {

    $("#Hello-Customers").offset({left: leftOffset});

    leftOffset++;
    if(leftOffset > 200)
    {
        leftOffset = 0;
    }

};

setInterval(moveHeading, 30);

for(var i = 0; i < $maxindex; i++)
{	
	//Change the h1 element's text
	$("h1").text("My friends");
	
	//$("body").hide();
    //concatenate in jQuery is with a +
   //jQuery selectors
	$("body").append("<p id=\"friends" + i + "\">" + arrfriends[i] + " is a studdo" + "</p>");
	//$("div > p").hide().fadeIn(3000);
	$("#friends" + i).hide();
    $("#friends" + i).fadeIn(3000);
    //$("#friends" + i).delay(3000);
    
    //$("#friends" + i).fadeOut(3000);
    //$("#friends" + i).delay(3000);
    //$("#friends").show(1000);
    //whole body element
	//$("body").fadeIn();
	//all 'p' elements
	//$("p").append(" is a studdo");	
    
}
//Style
//$(".friends").show(1000);

clearTimeout(timeOutId);
//dont miss the hash
$("#mybutton").click(clickedEvent);


