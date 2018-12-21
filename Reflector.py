class Reflector():
    def __init__(self):
        self.wall = {0:24, 24:0, 1:17, 17:1, 2:20, 20:2,
        3:7, 7:3, 4:16, 16:4, 5:18, 18:5, 6:11, 11:6,
        8:15, 15:8, 9:23, 23:9, 10:13, 13:10, 12:14, 14:12,
        19:25, 25:19, 21:22, 22:21}
    def find_opposite(self, uValue):
        assert uValue <= 25 and uValue >= 0
        return self.wall[uValue]
        
def main():
    rWall = Reflector()
     
    print(rWall.find_opposite(25))
  
if __name__== "__main__":
    main()