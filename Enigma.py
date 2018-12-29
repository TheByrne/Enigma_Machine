import Rotor
import Reflector
class Enigma():
    def __init__(self):
        self.rotorLeft = Rotor.Rotor()
        self.rotorCenter = Rotor.Rotor()
        self.rotorRight = Rotor.Rotor()
        self.mirror = Reflector.Reflector()
    def init_Rotors(self):
        self.rotorLeft.set_rotor("rotorI.txt")
        self.rotorCenter.set_rotor("rotorII.txt")
        self.rotorRight.set_rotor("rotorIII.txt")
    def traverse_left(self, pInput):
       self.rotorRight.rotate_right()
       temp = self.rotorRight.travel_left(pInput)
       print("number coming out oof right: "+str(temp))
       cent = self.rotorCenter.travel_left(temp)
       print("number coming out oof center: "+str(cent))
       temp = self.rotorLeft.travel_left(cent)
       print("number coming out oof left: "+str(temp))
       return temp
    def traverse_right(self, rInput):
        print("Traveling Right")
        temp = self.rotorLeft.travel_right(rInput)
        print("number coming out oof left: "+str(temp))
        cent = self.rotorCenter.travel_right(temp)
        print("number coming out oof center: "+str(cent))
        temp = self.rotorRight.travel_right(cent)
        print("number coming out oof right: "+str(temp))
        return temp
    def display(self):
        print("left")
        self.rotorLeft.display()
        print("Center ")
        self.rotorCenter.display()
        print("right")
        self.rotorRight.display()
        print()

def main():
    turing = Enigma()
    turing.init_Rotors()
    turing.display()
    sEncrypt = input("Character or 0 to quit ").upper()
    encrypt = ord(sEncrypt[0])
    encrypt = encrypt - 65
    answer=""
    print(encrypt)
    while sEncrypt[0] is not '0':
        temp = turing.traverse_left(encrypt)
        refl = turing.mirror.find_opposite(temp)
        addChar = turing.traverse_right(refl)
        answer = answer + chr(addChar+65)
        print(answer)
        turing.display()
        sEncrypt = input("Character or 0 to quit ").upper()
        encrypt = ord(sEncrypt[0])-65

if __name__== "__main__":
    main()