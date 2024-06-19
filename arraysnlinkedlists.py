#SINDHU BUGGANA
#NOTES
"""Data Structures:
A data structure is a way of organizing and storing data so that it can be accessed and modified efficiently. Different types of data structures are suited to different kinds of applications, and some are highly specialized to specific tasks
"""
"""

TIME COMPLEXITY:
Time complexity is often expressed using Big O notation. Big O notation provides an upper bound on the time an algorithm will take to run, ensuring that it will not exceed this time for large inputs.
O(1) -      Constant Time:      The runtime does not change with the input size.
O(log n) -  Logarithmic Time:   The runtime increases logarithmically as the input size increases.
O(n) -      Linear Time:        The runtime increases linearly with the input size.
O(n log n) -Linearithmic Time:  The runtime increases in proportion to n log n.
O(n^2) -    Quadratic Time:     The runtime increases quadratically with the input size.
O(2^n) -    Exponential Time:   The runtime doubles with each additional input element.

"""
"""2///Basic Data Structures

Arrays
Linked Lists
Stacks
Queues
lets go through this first"""

print("arrays\n")

# ARRAYS:collection of items stored at contiguous memory locations.
'''Characteristics:
Fixed size (in most languages, size is determined at creation)
Fast access time (O(1) for accessing elements by index)
Slow insertion and deletion (O(n) for inserting/deleting at arbitrary positions)

Operations:
Accessing Elements: O(1)
Insertion: O(n)
Deletion: O(n)'''

s= [0,1,2,3,4]

print(s)

# Accessing elements (O(1))
print(s[0])  # Output 0

# Modifying elements
s[1] = 2
print(s)  

# Inserting elements (O(n))
s.append(6)  # Adds 6 to the end
print(s)  # Output

# Deleting elements  (O(n))
s.pop(2)  # Removes the element at index 2
print(s)  # Output 

print("singular linked list\n")
# Linked Lists:A linked list is a linear data structure where each element is a separate object called a node. Each node contains two items: the data and a reference (or link) to the next node in the sequence.

'''Types:

Singly Linked List: Each node points to the next node.
Doubly Linked List: Each node points to both the next and the previous nodes.
Circular Linked List: The last node points back to the first node.
Characteristics:

Dynamic size
Efficient insertions and deletions (O(1) for inserting/deleting at the head)
Slow access time (O(n) for accessing elements by index)
Operations:

Traversal: O(n) -->Traversal refers to the process of visiting each node in the linked list from the head to the last node.
Insertion: O(1) if inserting at the head
Deletion: O(1) if deleting at the head'''

#SINGLE LL

class Node:
    def __init__(self,data):
        self.data= data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head= None

    def append(self, data): #insertion at tail
        new_node= Node(data)
        if not self.head:
            self.head= new_node
            return
        last= self.head
        while last.next:
            last = last.next
        last.next=new_node

    def traversal(head):
        current = head
        while current:
            print(current.data, end= " ")
            current= current.next
        print()
    
    def insertathead(LinkedList, data):
        new_node= Node(data)
        new_node.next= LinkedList.head
        LinkedList.head= new_node

    def deleteathead(LinkedList):
        if not LinkedList.head :
            return
        LinkedList.head= LinkedList.head.next

    def deleteattail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head= None
            return
        second_last= self.head
        while second_last.next.next:
            second_last= second_last.next
        second_last.next= None
    
    def instertatposition(self,data,position):
        new_node= Node(data)
        if position ==0:
            new_node.next=self.head
            self.head=new_node
            return
        current= self.head
        for _ in range ( position - 1):
            if not current:
                raise IndexError("Position out of bounds")
            current= current.next
        new_node.next = current.next
        current.next = new_node

    def deleteatposition(self,position):
        if not self.head:
            return
        if position == 0:
            self.head = self.head.next
            return
        current= self.head
        for _ in range ( position - 1):
            if not current or not current.next:
                raise IndexError("Position out of bounds")
            current= current.next
        if not current.next:
            raise ImportError("Position out of bounds")
        current.next= current.next.next

    def printing(self):
        current=self.head
        while current:
            print(current.data, end=" ")
            current= current.next
        print()

I1 = LinkedList()
I1.append(1)
I1.append(2)
I1.append(3)
I1.printing()
I1.insertathead(1)
I1.printing()
I1.deleteathead()
I1.printing()
I1.instertatposition(4,2)
I1.printing()
I1.deleteattail()
I1.printing()
I1.deleteatposition(1)
I1.printing()


print("double linked list\n")


#Double Linked List
'''Doubly Linked List:

Each node has next and prev pointers.
insert_at_head updates the prev pointer of the old head to the new node.
delete_at_head updates the prev pointer of the new head to None.

A doubly linked list is a type of linked list in which each node contains three fields:

Data Field: Stores the value or data.
Next Pointer: A pointer/reference to the next node in the sequence.
Previous Pointer: A pointer/reference to the previous node in the sequence.
This structure allows traversal in both forward and backward directions, providing more flexibility compared to singly linked lists.

Operations on Doubly Linked Lists
Insertion:

At the Head: Insert a new node at the beginning of the list.
At the Tail: Insert a new node at the end of the list.
At a Specific Position: Insert a new node at a given position in the list.
Deletion:

At the Head: Remove the node at the beginning of the list.
At the Tail: Remove the node at the end of the list.
At a Specific Position: Remove the node at a given position in the list.
Traversal:

Forward Traversal: Traverse the list from the head to the tail.
Backward Traversal: Traverse the list from the tail to the head (if needed).
Get Operation: Retrieve the value of the node at a specific position.

Put Operation: Update the value of the node at a specific position.

Advantages
Bidirectional Traversal: Easy to traverse in both directions.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_head(data)
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

    def delete_at_head(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_at_tail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None

    def get(self, position):
        current = self.head
        for _ in range(position):
            if not current:
                return None
            current = current.next
        return current.data if current else None

    def put(self, position, data):
        current = self.head
        for _ in range(position):
            if not current:
                return
            current = current.next
        if current:
            current.data = data

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Usage
dll = DoublyLinkedList()
dll.insert_at_head(1)
dll.insert_at_tail(2)
dll.insert_at_position(3, 1)
dll.print_list()
print(dll.get(1))
dll.put(1, 4)
dll.print_list()
dll.delete_at_head()
dll.delete_at_tail()
dll.print_list()


print("circular linked list\n")

'''
Circular Linked List:

The last node's next pointer points to the head.
insert_at_head traverses to the last node to update its next pointer to the new head.
delete_at_head updates the next pointer of the last node to the new head and handles the special case when the list becomes empty.

Circular Linked List
A circular linked list is a type of linked list in which the last node points back to the first node, forming a circular structure. This can be either a singly circular linked list or a doubly circular linked list. Here, we'll focus on singly circular linked lists.

Operations on Circular Linked Lists
Insertion:

At the Head: Insert a new node at the beginning of the list. The new node's next pointer points to the old head, and the last node's next pointer points to the new head.
At the Tail: Insert a new node at the end of the list. The new node's next pointer points to the head, and the old last node's next pointer points to the new node.
At a Specific Position: Insert a new node at a given position in the list.
Deletion:

At the Head: Remove the node at the beginning of the list. The last node's next pointer is updated to point to the new head.
At the Tail: Remove the node at the end of the list. The second last node's next pointer is updated to point to the head.
At a Specific Position: Remove the node at a given position in the list.

Traversal:
Traverse the list starting from the head and continue until you reach the head again.
Get Operation: Retrieve the value of the node at a specific position.

Put Operation: Update the value of the node at a specific position.

Advantages
Efficient Use of Space: No need for a sentinel node or tail pointer.
Cyclic Nature: Useful for applications requiring circular data structures (e.g., round-robin scheduling).

Disadvantages
Complexity: Slightly more complex to implement and maintain compared to singly linked lists.
Traversal: Care must be taken to avoid infinite loops during traversal.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_head(data)
            return
        current = self.head
        for _ in range(position - 1):
            if current.next == self.head:
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_at_head(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

    def delete_at_tail(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next
        prev.next = self.head

    def get(self, position):
        if not self.head:
            return None
        current = self.head
        for _ in range(position):
            if current.next == self.head:
                return None
            current = current.next
        return current.data

    def put(self, position, data):
        if not self.head:
            return
        current = self.head
        for _ in range(position):
            if current.next == self.head:
                return
            current = current.next
        if current:
            current.data = data

    def print_list(self):
        if not self.head:
            print("The list is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

# Usage
cll = CircularLinkedList()
cll.insert_at_head(1)
cll.insert_at_tail(2)
cll.insert_at_position(3, 1)
cll.print_list()
print(cll.get(1))
cll.put(1, 4)
cll.print_list()
cll.delete_at_head()
cll.delete_at_tail()
cll.print_list()
