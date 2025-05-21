name = "Sneha"
console.log(name)
var name;

/*
JavaScript hoists the variable declarations(but not the initializations) to the top of the scope
So code behaves like
var name;
name = "Sneha"
console.log(name)

But let and const variables don't support hoisting
Because they are placed in temporal dead zones(TDZ) from the start of the block until their declaration is encountered
This means we can't access them before their declaration, even though JS knows about these variables
This is made to avoid use of variables before they are properly initialized or declared

However var allows accidental use of undefined values which is considered a bad practice
*/