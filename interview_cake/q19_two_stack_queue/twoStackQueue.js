// Implement a queue ↴ with 2 stacks.↴ Your queue should have an enqueue and a dequeue method and it should be "first in first out"(FIFO).
// Optimize for the time cost of mm calls on your queue.These can be any mix of enqueue and dequeue calls.
// Assume you already have a stack implementation and it gives O(1)O(1) time push and pop

const Stack = require('./stack');

class Queue extends Array {
    constructor() {
        super()
        this.push(new Stack());
        this.push(new Stack());
        this.stack1 = this[0];
        this.stack2 = this[1];
    }

    swapStacks(){
        if (this.stack1.peek()) {
            while (this.stack1.peek())
                this.stack2.push(this.stack1.pop());
        }
        else {
            while (this.stack2.peek())
                this.stack1.push(this.stack2.pop())
        }
    };

    enqueue(item) {
        if (this.stack2.peek())
            this.swapStacks();
        this.stack1.push(item);
    }

    dequeue() {
        //take top item from stack2 if possible
        if (this.stack2.peek()) {
            let dequeuedValue = this.stack2.pop();
        }
        else {
            let returnItem;
            this.swapStacks();
            returnItem = this.stack2.pop();
            return returnItem;
        }
    };

    inspect(){ return [this.stack1, this.stack2]; }

    get state(){return [this.stack1, this.stack2];}

    get elementsLength() { return this.stack1.length + this.stack2.length; }
};

module.exports = Queue;

