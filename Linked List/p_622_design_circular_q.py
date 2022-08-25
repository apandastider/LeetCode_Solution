'''
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language.
'''
class ListNode():
    
    def __init__(self, val = None, next = None):
        
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.head = None
        self.size = 0
        self.last = None

    def enQueue(self, value: int) -> bool:
        if self.size >= self.k:
            return False
        else:
            
            if self.size == 0:
                self.head = ListNode(val = value)
                self.last = value
                 
            else:
                new_value = ListNode(val = value)
                self.last = value
                curr_node = self.head
                counter = 0
                while counter < self.size - 1:
                    curr_node = curr_node.next
                    counter += 1
                curr_node.next = new_value
                new_value.next = self.head
            self.size += 1
            return True
        

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        else:
            curr_node = self.head
            self.head = curr_node.next
            self.size -= 1
            return True
        
        

    def Front(self) -> int:
        if self.size == 0:
            return -1 
        else:
            return self.head.val
            
        
    def Rear(self) -> int:
        if self.size == 0:
            return -1 
        else:
            # curr_node = self.head
            # counter = 0
            # while counter < self.size - 1:
            #     curr_node = curr_node.next
            #     counter += 1
            # return curr_node.val
            return self.last
            
    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
