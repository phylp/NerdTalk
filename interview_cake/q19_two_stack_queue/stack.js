class Stack extends Array {
    constructor() {
        super();
    }

    peek() {
        return this[this.length - 1];
    }

    inspect(){
        let result = [];
        for(var i = 0; i < this.length; i++) 
            result[i] = this[i]
        return result;
    }
};

module.exports = Stack;