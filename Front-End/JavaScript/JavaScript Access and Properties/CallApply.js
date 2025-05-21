function add(a,b){
    console.log(this.function + " of " + a + " and " + b + " is " + (a+b)) 
}

const method = {
    function : "Addition"
}

add.call(method, 2, 3)
add.apply(method, [2, 3])

//call takes arguments separately, apply takes an array of arguments