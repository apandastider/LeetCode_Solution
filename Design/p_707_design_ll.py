'''
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 
 '''

class ListNode:
    
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        
        self.head = None
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        elif index == 0:
            return self.head.val
        
        else:
            curr_node = self.head
            for _ in range(index):
                curr_node = curr_node.next
            # print(curr_node.val)
            return curr_node.val

    def addAtHead(self, val: int) -> None:
        curr_node = ListNode(val = val)
        curr_node.next = self.head
        
        self.head = curr_node
        
        self.size += 1
        # print(self.size)

    def addAtTail(self, val: int) -> None:
        curr_node = self.head
        
        if curr_node is None:
            self.head = ListNode(val = val)
        else:    
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = ListNode(val = val)
        
        self.size += 1
        # print(self.size)
    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
#             curr_node = self.head
            
#             while curr_node is not None:
#                 curr_node = curr_node.next
#             curr_node.next = ListNode(val = val)
            self.addAtTail(val = val)
            # self.size += 1
        elif index == 0:
            self.addAtHead(val = val)
            # self.size += 1
            
        elif index > 0 and index < self.size:
            counter = 0
            curr_node = self.head
            while counter != index - 1:
                curr_node = curr_node.next
                counter += 1
            
            right_side = curr_node.next
            curr_node.next = None
            curr_node.next = ListNode(val = val, next = right_side)
            
            self.size += 1
        # print(self.size)
    def deleteAtIndex(self, index: int) -> None:
        size = self.size
        if index == 0:
            curr_node = self.head.next
            self.head = curr_node
            size -= 1
        # elif index == self.size - 1:
            # while 
            
        elif index > 0 and index <= self.size - 1:
            curr_node = self.head
            counter = 0
            
            for _ in range(index-1):
                curr_node = curr_node.next
                # print(curr_node.val)
            curr_node.next = curr_node.next.next
            # print(self.head.next.val)
            size -= 1
            # print(self.size)
        self.size = size
        # print(self.size)
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
