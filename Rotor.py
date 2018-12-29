import CircularLinkedList
import Reflector
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
    def travel_left(self, eInput):
        temp = self.rightCol.search_by_num(eInput)
        output = self.leftCol.search(temp)
        return output
    def travel_right(self, eInput):
        temp = self.leftCol.search_by_num(eInput)
        output = self.rightCol.search(temp)
        return output
    def display(self):
        print("Left Col: ")
        self.leftCol.display()
        print()
        print("Right Col: ")
        self.rightCol.display()
    def rotate_right(self):
        self.rightCol.rotate()
        self.leftCol.rotate()
    def check_notch(self, notch):
        if notch is self.notch:
            return True
        else:
            return False

    
    
# def main():
    
#     mirror = Reflector.Reflector()
#     ada = Rotor()
#     ada.set_rotor("rotorI.txt")
#     ada.display()
#     print("rotated twice ")
#     ada.rotate_right()
#     ada.rotate_right()
#     ada.rotate_right()
#     ada.rotate_right()
#     ada.rotate_right()
#     ada.rotate_right()
#     ada.rotate_right()
#     a
  
# if __name__== "__main__":
#     main()
                
                
