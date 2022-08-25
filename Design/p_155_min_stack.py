'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = 0
        self.mins = []
        

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        self.mins.append(val if not self.mins else min(val,self.mins[-1]))


    def pop(self) -> None:
        top = self.stack.pop()
        self.mins.pop()
        return top
    
    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
