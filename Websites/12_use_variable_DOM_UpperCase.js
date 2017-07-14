function changeToUpperCase()
{
	var name = document.getElementById('Hello-Customers');
	var varuppercase = name.innerHTML.toUpperCase();
	return varuppercase;
}

document.getElementById('Hello-Customers').innerHTML = changeToUpperCase();
console.log(document.getElementById('Hello-Customers').innerHTML);