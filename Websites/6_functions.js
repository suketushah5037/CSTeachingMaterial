//rollcaller is the function's name
var rollcaller = function(noofstudents)
{	
	//Cannot be local
	//var noofstudents = 15; 

	for(var rollcall =0; rollcall < noofstudents; rollcall++)
	{
		console.log("Hi! " + rollcall + " is very much here.")
	}
	return 1;
};

//15 = noofstudents and is a parameter
rollcaller(15);
//returns 1
//logs 1 from the return value
console.log(rollcaller(15));


//rollcaller function call does not return everything hence it is undefined

//return early to break execution and use multiple returns in if conditions to return different values based on the flow

//return value could be used to add something like Math.random()*10
//function with early return - when some conditions fail and you want to
//skip some logic you can do it

//in if-else use return

//I am not calling this and hence can lie around there
//Exercise: Call it
//function declaration, i do not have access to the answer till i store it in
//a variable
function(score)
{				
	if(score<3)	
	{ 
		return	"Bronze";
	} 
	if(score<7)	
	{							
		return	"Silver";
	} 
	return	"Gold";		
};

//storing it in a variable is function expression 