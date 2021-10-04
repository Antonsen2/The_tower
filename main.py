


class Character:

    def __init__(self, name, weapon, hp):
        self.hp = hp
        self.name = name
        self.weapon = weapon

class Player(Character):

    def __init__(self, name, weapon, hp):
        super().__init__(name, weapon, hp)
        self.inventory = "hej"
        self.current_floor = 0


class Npc:
    pass


class Map:

    def __init__(self):
        self.floors = [
            {"description": "This is the first floor of the tower"},
            {"description": "room2"},
            {"description": "room3"}

        ]
        self.map = [self.floors[0]["description"]], [self.floors[1]["description"]], [self.floors[2]["description"]]


class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player("glenn", "axe", 100)


        #print(self.player.hit_points)
        #print(self.map.map[0])

    def climb(self, command):
        if self.player.current_floor > len(self.map.map) -1:
            print("You can't go there")

        if command == "climb" and self.player.current_floor != len(self.map.map) -1:
            print("climbing...")
            #return self.map.map[current_floor+1]
            self.player.current_floor +=1
        else:
            print("You are on the top floor")



def main():

    game = Game()
    #game.move()
    player = Player("glenn", "axe", 100)
    #print(player.inventory)
    running = True
    while running:
        # command = "move"
         #print(game.move(command, 2))
        command = "climb"
        game.climb(command)
        print(game.player.current_floor)
        game.climb(command)
        print(game.player.current_floor)

        running = False

if __name__ == '__main__':

   main()


