class Counter {
    constructor() {
      this.count = 0; // private-like property (by convention)
    }
  
    // Getter to access the count
    get value() {
      return this.count;
    }
  
    // Setter to set a specific value (optional, can add validation)
    // set value(newValue) {
    //   if (typeof newValue === 'number' && newValue >= 0) {
    //     this._count = newValue;
    //   } else {
    //     console.log('Please provide a non-negative number');
    //   }
    // }
  
    // Method to increment the counter
    increment() {
      this.count++;
    }
  
    // Method to decrement the counter
    decrement() {
      if (this.count > 0) {
        this.count--;
      }
    }
  }
  
  // Usage
  const myCounter = new Counter();
  
  console.log(myCounter.value); // 0
  myCounter.increment();
  console.log(myCounter.value); // 1
  myCounter.decrement();
  console.log(myCounter.value); // 0
  
  myCounter.value = 5;
  console.log(myCounter.value); // 5
  
  myCounter.value = -2; // Invalid
  