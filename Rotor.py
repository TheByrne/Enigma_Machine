import CircularLinkedList
class Rotor():
    def __init__(self):
        self.leftCol = CircularLinkedList.CircularLinkedList()
        self.rightCol = CircularLinkedList.CircularLinkedList()
    def set_rotor(self, fileName):
        count = 0
        with open(fileName) as file_object:
            for line in file_object:
                if count is 0:
                    for x in reversed(line):
                        self.leftCol.insert_start(x)
                if count is 1:
                    for x in reversed(line):
                        self.rightCol.insert_start(x)
                count = count + 1
    def display(self):
        print("Left Col: ")
        self.leftCol.display()
        print()
        print("Right Col: ")
        self.rightCol.display()
    
def main():
    ada = Rotor()
    ada.set_rotor('rotorI.txt')
    ada.display()
  
if __name__== "__main__":
    main()
                
                
