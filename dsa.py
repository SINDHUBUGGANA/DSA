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



