class Plugboard():
    def __init__(self):
        aLetter = {}
        bLetter = {}
        cLetter = {}
        dLetter = {}
        eLetter = {}
        fLetter = {}
        gLetter = {}
        hLetter = {}
        iLetter = {}
        jLetter = {}
        kLetter = {}
        lLetter = {}
        mLetter = {}
        nLetter = {}
        oLetter = {}
        pLetter = {}
        qLetter = {}
        rLetter = {}
        sLetter = {}
        tLetter = {}
        uLetter = {}
        vLetter = {}
        wLetter = {}
        xLetter = {}
        yLetter = {}
        zLetter = {}
        self.collection = [aLetter, bLetter, cLetter, dLetter,
        eLetter, fLetter, gLetter , hLetter ,iLetter , jLetter, 
        kLetter, lLetter , mLetter , nLetter ,oLetter, pLetter, 
        qLetter ,rLetter , sLetter , tLetter ,uLetter, vLetter,
        wLetter ,xLetter , yLetter , zLetter ]

    def connect(self, uInput):
        assert len(uInput) == 2
        uOne = uInput[0]
        uTwo = uInput[1]

        uNumOne = ord(uOne) - 97
        uNumTwo = ord(uTwo) - 97
        
        if not self.collection[uNumOne] and not self.collection[uNumTwo]:
            self.collection[uNumOne][uOne] = uTwo
            self.collection[uNumTwo][uNumTwo] = uOne
        else:    
            print(str(uOne) + " has a pair or " + str(uTwo) + " has a pair") 
    def convert(self, uInput):
        uNum = ord(uInput) - 97
        if self.collection[uNum][uInput]:
            return self.collection[uNum][uInput]
        else:
            return uInput
    

def main():
    board = Plugboard()
    x ='a'
    board.connect("ab")
    x = board.convert(x)
    print(x)
  
if __name__== "__main__":
    main()
        
    # self.wall = ['a', 'b', 'c', 'd', 'e', 'f',
    #     'g', 'd', 'i', 'j', 'k', 'g', 'm', 
    #     'k', 'm', 'i', 'e', 'b', 'f', 't',
    #     'c', 'v', 'v', 'j', 'a', 't']
    # def find_opposite(uValue):
    #     assert uValue <= 25 and uValue >= 0
    #     target = self.wall[uValue]
    #     wallMax = len(self.wall) -1
    #     for x in range(uValue, wallMax):
    #         if self.wall[x] is target:
    #             return x
        
