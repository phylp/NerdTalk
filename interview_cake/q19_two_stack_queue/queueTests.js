
describe("Interview Cake Question 19:", function() {
  const Stack = require('./stack');
  const Queue = require('./twoStackQueue');
  let q;

  describe("Queue with 2 Stacks =>", function() {
    beforeEach(function() {
      q =  new Queue();
    });

    it("should create exactly 2 stacks upon instantiation", () => {
      expect(q.length).toEqual(2);
      expect(q[0] instanceof Stack).toBe(true);
      expect(q[1] instanceof Stack).toBe(true);
      expect(q.state).toEqual([[], []]);
    });
    
    it("should be able to enqueue on a single stack", () => {
      q.enqueue('alpha');
      q.enqueue('bravo');
      q.enqueue('charlie');
      expect(q.elementsLength).toEqual(3);
      expect(q.state).toEqual([['alpha','bravo','charlie'], []]);
    });

    it("should exhibit FIFO queueing with one stack", () => {
      q.enqueue('a');
      q.dequeue();
      expect(q.elementsLength).toEqual(0)
      expect(q.state).toEqual([[], []]);
    });

    it("should exhibit FIFO queueing with two stacks", () => {
      q.enqueue('a');
      q.enqueue('b');
      q.dequeue();
      expect(q.state).toEqual([[], ['b']]);
    });

    it("should be able to enqueue and dequeue - long example", () => {
      q.enqueue('a');
      q.enqueue('b');
      q.enqueue('c');
      q.dequeue();
      q.enqueue('d')
      q.dequeue();
      q.dequeue();
      expect(q.state).toEqual([[], ['d']]);
    });
  });
});
