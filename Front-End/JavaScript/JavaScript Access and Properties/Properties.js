function Person(name) {
    this.name = name;
}

Person.prototype.greet = function() {
    console.log("Hello, my name is " + this.name);
};

Person.prototype.age = 25; // Adding new property using prototype

let p1 = new Person("Bob");

p1.greet(); // Hello, my name is Bob
console.log(p1.age); // 25