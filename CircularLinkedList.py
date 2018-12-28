class Node():
    def __init__(self, dataVal = None):
        self.dataVal = dataVal
        self.next = None
class CircularLinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
    def insert_start(self, uValue):
        if self.head is None:
            self.head = Node(uValue)
            self.head.next = self.head
            self.size = self.size + 1
            
        elif self.head.next is self.head:
            temp = Node(uValue)
            temp.next = self.head
            self.head.next = temp
            self.head = temp
            
            self.size = self.size + 1
        else:
            temp = Node(uValue)
            temp.next = self.head
            search = self.head
            x = 0
            
            while x < self.size:
                if x is self.size - 1:
                    search.next = temp
                    self.head = temp
                    break
                
                x = x + 1
                search = search.next
            self.size = self.size + 1
    def display(self):
        search = self.head
        x =0
        if self.head is None:
            print('Empty List ')
        elif self.head.next is self.head:
            print(str(self.head.dataVal)) 
        else:
            while x < (self.size-1):
                print( str(search.dataVal) +" | ", end='')
                search = search.next
                x = x + 1
        print("")
    def search(self, target):
        search = self.head
        x = 0
        while x < (self.size -1):
                if target is search.dataVal:
                    return x
                search = search.next
                x = x + 1
    def search_by_num(self, number):
        search = self.head
        x = 0
        while x <= number and x < (self.size-1):
            if x is number:
                return search.dataVal
            search = search.next
            x = x + 1  
            
        
    def get_size(self):
        return self.size
    def rotate(self):
        self.head = self.head.next
    def rotate_left(self):
        search = self.head
        x = 0
        while x < self.size:
                if x is self.size -1:
                    self.head = search
                    break
                search = search.next
                x = x + 1

