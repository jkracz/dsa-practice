var MyQueue = function () {
    this.arr1 = [];
    this.arr2 = [];
};

/**
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function (x) {
    // add an item to the back
    this.arr1.push(x);
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function () {
    // remove and return first item
    for (let i = this.arr1.length - 1; i >= 0; --i) {
        this.arr2.push(this.arr1[i]);
    }
    const firstRemovedElement = this.arr2.pop();
    this.arr1 = [];
    for (let j = this.arr2.length - 1; j >= 0; --j) {
        this.arr1.push(this.arr2[j]);
    }
    this.arr2 = [];
    return firstRemovedElement;
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function () {
    // return first item
    for (let i = this.arr1.length - 1; i >= 0; --i) {
        this.arr2.push(this.arr1[i]);
    }
    const firstElement = this.arr2[this.arr2.length - 1];
    this.arr2 = [];
    return firstElement;
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function () {
    if (this.arr1.length === 0) {
        return true;
    }
    return false;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */

// var MyQueue = function() {
//     this.stack1 = []
//     this.stack2 = []
//     this.front = null
// };

// /** 
//  * @param {number} x
//  * @return {void}
//  */
// MyQueue.prototype.push = function(x) {
//     if(this.stack1.length == 0) {
//         this.front = x
//     }
//     this.stack1.push(x)
// };

// /**
//  * @return {number}
//  */
// MyQueue.prototype.pop = function() {
//     if(this.stack2.length == 0) {
//         while(this.stack1.length !=0) {
//             this.stack2.push(this.stack1.pop())
//         }
//     }
//     return this.stack2.pop()
// };

// /**
//  * @return {number}
//  */
// MyQueue.prototype.peek = function() {
//     return this.stack2.length == 0 ? this.front : this.stack2[this.stack2.length-1]
// };

// /**
//  * @return {boolean}
//  */
// MyQueue.prototype.empty = function() {
//     return this.stack1.length == 0 && this.stack2.length == 0
// };

var obj = new MyQueue();
obj.push(1);
obj.push(2);
obj.push(3);
console.log(obj.pop());
console.log(obj.pop());
console.log(obj.pop());
console.log(obj);
// var param_2 = obj.pop();
// var param_3 = obj.peek();
console.log(obj.empty());
