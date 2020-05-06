"""

Simplified Monopoly in Python for ACM Blog Article

"""


import random

board = []
players = []


class Place:
    def __init__(self, name, cost, rent):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.position = len(board)
        self.owned = False
        board.append(self)
    
    def show(self):
        on = []
        for p in players:
            if p.position == self.position:
                on.append(p.name)

        print(self.name + str(on), end = "\t")

class Player:
    def __init__(self):
        self.money = 2000
        self.position = 0
        self.name = "P" + str(len(players))
        self.places = []
        players.append(self)

    def turn(self):
        print("Turn of " + self.name)
        print("You have " + str(self.money))
        print("1) View Places Owned")
        print("2) Roll Dice")

        choice = input()
        print(choice)

        if (int(choice) == 1):
            for p in self.places:
                print(p.name + "\t" + p.cost + "\t" + p.rent)

        if (int(choice) == 2):
            diceno = random.randint(1,4)
            print("dice shows " + str(diceno))
            if (self.position + diceno < len(board)):
                self.position += diceno
            
            else:
                self.position = self.position + diceno - len(board)
           
            if board[self.position].owned:
                for player in players:
                    if board[self.position] in player.places:
                        self.money -= board[self.position].rent
                        player.money += board[self.position].rent
                        print("Paid rent to " + player.name)
                       
            else:
                print(board[self.position].name + "\t" + str(board[self.position].cost))
                print("1) Buy Place")
                print("2) Pass")

                ch2 = input("")
               
                if (int(ch2) == 1):
                    self.money -= board[self.position].cost
                    board[self.position].owned = True
                    self.places.append(board[self.position])


def print_board():
    for i in range(6):
        board[i].show()
    
    print()


p1 = Place("place1", 200, 10)
p2 = Place("place2", 250, 12)
p3 = Place("place3", 300, 15)
p4 = Place("place4", 320, 18)
p5 = Place("place5", 350, 20)
p6 = Place("place6", 380, 30)


pl1 = Player()
pl2 = Player()

while(pl1.money != 0 and pl2.money != 0):
    for p in players:
        print_board()
        p.turn()
