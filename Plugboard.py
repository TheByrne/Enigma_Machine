import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - \
- %(message)s')
class Plugboard():
    def __init__(self):
        self.board={}
        self.connections = None
    def connect_plugs(self):
        logging.debug(self.connections)
        assert self.connections is not None
        for x in self.connections:
            logging.debug(x)
            self.board[x[0]]= x[1]
            self.board[x[1]]= x[0]
        logging.debug(self.board)
    def check_repeats(self):
        plugs = sorted(self.connections)
        for x in range(1, len(self.connections)):
            if plugs[x] == plugs[x-1]:
                return True
        return False
    def convert(self, uInput):
        uNum = ord(uInput) - 97
        if self.collection[uNum][uInput]:
            return self.collection[uNum][uInput]
        else:
            return uInput
    def get_connections(self, uConnections):
        # uConnections = input("Enter connections \"AB FD PC\" ")
        uConnections = uConnections.upper()
        testLength = uConnections.replace(" ", "")
        self.connections = uConnections.split(" ")
        
        if len(testLength) % 2 is not 0:
            logging.critical('String not correct')
        logging.debug(self.connections)
    def from_enigma(self, enigmaOutput):
        logging.debug(self.board)
        logging.debug(enigmaOutput)
        if enigmaOutput in self.board.keys():
            return self.board[enigmaOutput]
        else:
            return enigmaOutput
    def from_user(self, uInput):
        uInput = uInput.upper()
        plugWire = self.from_enigma(uInput)
        return ord(plugWire) - 65
     

        
  