import Rotor
import Reflector
import Plugboard
import logging
class Enigma():
    def __init__(self):
        self.rotorLeft = Rotor.Rotor()
        self.rotorCenter = Rotor.Rotor()
        self.rotorRight = Rotor.Rotor()
        self.mirror = Reflector.Reflector()
        self.board = Plugboard.Plugboard()
    def init_Rotors(self):
        self.rotorLeft.set_rotor("rotorI.txt")
        self.rotorCenter.set_rotor("rotorII.txt")
        self.rotorRight.set_rotor("rotorIII.txt")
    def traverse_left(self, pInput):
       # self.rotorRight.rotate_right()
       self.rotate_rotors()
       temp = self.rotorRight.travel_left(pInput)
       logging.debug("number coming out oof right: "+str(temp))
       cent = self.rotorCenter.travel_left(temp)
       logging.debug("number coming out oof center: "+str(cent))
       temp = self.rotorLeft.travel_left(cent)
       logging.debug("number coming out oof left: "+str(temp))
       return temp
    def traverse_right(self, rInput):
        logging.debug("Traveling Right")
        temp = self.rotorLeft.travel_right(rInput)
        logging.debug("number coming out oof left: "+str(temp))
        cent = self.rotorCenter.travel_right(temp)
        logging.debug("number coming out oof center: "+str(cent))
        temp = self.rotorRight.travel_right(cent)
        logging.debug("number coming out oof right: "+str(temp))
        return temp
    def rotate_rotors(self):
        if self.rotorCenter.notch is self.rotorCenter.leftCol.head.dataVal \
        and self.rotorRight.notch is self.rotorRight.leftCol.head.dataVal:
            self.rotorCenter.rotate_right()
            self.rotorRight.rotate_right()
            self.rotorLeft.rotate_right()
        elif self.rotorRight.notch is self.rotorRight.leftCol.head.dataVal:
            self.rotorRight.rotate_right()
            self.rotorCenter.rotate_right()
        else:
            self.rotorRight.rotate_right()
        
    def display(self):
        print("Left")
        self.rotorLeft.display()
        print("Center ")
        self.rotorCenter.display()
        print("Right")
        self.rotorRight.display()
        print()
    def start(self, uString):
        sEncrypt = uString.upper()
        encrypt = ord(sEncrypt[0])
        encrypt = encrypt - 65
        answer=""
        encrypt = self.board.from_user(sEncrypt)
        temp = self.traverse_left(encrypt)
        refl = self.mirror.find_opposite(temp)
        addChar = self.traverse_right(refl)
        answer = answer + self.board.from_enigma(chr(addChar+65))
        #print("Your Encryption is: "+answer)
        return answer



# def main():
#     turing = Enigma()
#     turing.init_Rotors()
#     #turing.display()
#     sEncrypt = input("Character or 0 to quit ").upper()
#     turing.board.get_connections()
#     turing.board.connect_plugs()
    # encrypt = ord(sEncrypt[0])
    # encrypt = encrypt - 65
    # answer=""
    # print(encrypt)
    # answer=""
    # while sEncrypt[0] is not '0':
    #     encrypt = turing.board.from_user(sEncrypt)
    #     temp = turing.traverse_left(encrypt)
    #     refl = turing.mirror.find_opposite(temp)
    #     addChar = turing.traverse_right(refl)
    #     answer = answer + turing.board.from_enigma(chr(addChar+65))
    #     print("Your Encryption is: "+answer)
    #     sEncrypt = input("Character or 0 to quit ").upper()
    #     encrypt = ord(sEncrypt[0])-65

# if __name__== "__main__":
#     main()