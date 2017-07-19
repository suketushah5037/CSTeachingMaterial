//many types in one
//Person object

//The	Principles	of	Object-Oriented	JavaScript	[No	Starch Press,	2014]
var Person = {

    name: "Gowri",
    Office: "CG",
    Kids: 2
};


Person.routeToOff = function () {
    console.log("get info from google maps and show it");
    console.log(this.name, this.Office);
};

Person.routeToOff();

var Person = function (name, office, num) {
    this.name = name;
    this.Office = office;
    this.Kids = num;

    console.log("in the person constructor");

    console.log(this.name);
};


Person.prototype.routetoOff = function () {
    console.log(this.name);
    console.log("member function - your individual route to office");
}
var construct = new Person("joker", "JB", 5);

construct.routetoOff();
construct;