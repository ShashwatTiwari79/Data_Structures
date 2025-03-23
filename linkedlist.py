class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    def insert_at_index(self, data,index):
        if index == 0:
            self.insertAtBegin(data)
            return
        position = 0
        current_node = self.head
        while current_node is not None and position < index-1:
            current_node = current_node.next
            position += 1
            
        if current_node is None:
            print("Index out of range")
            return 
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
    def updateNode(self,value,index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = value
        else:
            while current_node is not None and position is not index:
                position += 1
                current_node = current_node.next
            if current_node is not None:
                current_node.data = value
            else:
                print("Index out of range")
    def remove_first_node(self):
        if self.head is None:
            print("List is empty")
            return 
        else:
            self.head = self.head.next
    def remove_last_node(self):
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        current_node.next = None
    def remove_node_at_index(self,index):
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        position = 0
        if index == 0:
            self.remove_first_node()
            return
        else:
            while current_node is not None and current_node.next is not None and position < index-1:
                current_node = current_node.next
                position += 1
            if current_node is not None or current_node.next is not None:
                current_node.next = current_node.next.next
                
            else:
                print("Index out of range")
    def remove_node(self,data):
        current_node = self.head
        if current_node.data == data:
            self.remove_first_node()
            return
        while current_node.next is not None and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next is None:
            print("Node not found")
            return
        else:
            current_node.next = current_node.next.next
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    def size_of_ll(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0
print("You can perform the following:-")
print("1. Insert at the begining")
print("2. Insert at index")
print("3. Insert at end")
print("4. Update the node")
print("5. Remove first node")
print("6. Remove last node")
print("7. Remove node of a index")
print("8. Remove node by the value")
print("9. Display the linked list")
print("10. Size of linked list")
llist = LinkedList()

idx = 0
value = 0
check = True
while check:
    choice = input("Enter your choice:-")
    if choice == '1':
        value = input("Enter the value:-")
        llist.insertAtBegin(value)
    elif choice == '2':
        idx = int(input("Enter the index of insertion:-"))
        value = input("Enter the value to be inserted at that index:-")
        llist.insert_at_index(value,idx)
    elif choice == '3':
        value = input("Insert at end:-")
        llist.insertAtEnd(value)
    elif choice == '4':
        idx = int(input("Enter the index where node is to be updated:-"))
        value = input("Insert value to be updated:-")
        llist.updateNode(value,idx)
    elif choice == '5':
        llist.remove_first_node()
    elif choice == '6':
        llist.remove_last_node()
    elif choice == '7':
        idx = int(input("Enter the index value where the node is to be deleted:-"))
        llist.remove_node_at_index(idx)
    elif choice == '8':
        value = input("Enter the node which is to be removed:-")
        llist.remove_node(value)
    elif choice == '9':
        llist.display()
    elif choice == '10':
        freq = llist.size_of_ll()
        print(freq)
    else :
        print("Wrong choice enter again")
    check = input("Do you want to continue or not (Y/N):-")
    if check.lower() == 'n':
        print("Thank you...")
        break

            

#llist.insertAtBegin(10)
#llist.insertAtEnd(20)
#llist.insertAtEnd(30)
#llist.insertAtEnd(40)
#llist.insert_at_index(25,2)

#print("Node Data:")
#llist.display()
#print("\n remove first node:")
#llist.remove_first_node()
#llist.display()
#print("\n remove last node:")
#llist.remove_last_node()
#llist.display()
#print("\n remove node at index 2:")
#llist.remove_node_at_index(2)
#llist.display()
#print("\nUpdate node value at index 0:")
#llist.updateNode(100,0)
#llist.display()
#print("\nSize of linked list:")
#print(llist.size_of_ll())

