import CircularLinkedList
class Rotor():
    def __init__(self):
        self.leftCol = CircularLinkedList.CircularLinkedList()
        self.rightCol = CircularLinkedList.CircularLinkedList()
        self.notch = None
    def set_rotor(self, fileName):
        count = 0
        with open(fileName) as file_object:
            for line in file_object:
                column = line.split(" ")
                if count is 0:
                    for x in reversed(column):
                        self.leftCol.insert_start(x)
                if count is 1:
                    for x in reversed(column):
                        self.rightCol.insert_start(x)
                if count is 2:
                    self.notch = column
                count = count + 1
    def display(self):
        print("Left Col: ")
        self.leftCol.display()
        print()
        print("Right Col: ")
        self.rightCol.display()
    def check_notch(self, notch):
        if notch is self.notch:
            return True
        else:
            return False

    
    
def main():
    ada = Rotor()
    ada.set_rotor("rotorI.txt")
    print("Checking out if rotor one notch is X")
    print(ada.check_notch('X'))
    print("Checking by letter ")
    print(ada.rightCol.search('K'))
    print("Checking by number")
    ada.rightCol.display()
    print(ada.rightCol.search_by_num(2))
    
  
if __name__== "__main__":
    main()
                
                
