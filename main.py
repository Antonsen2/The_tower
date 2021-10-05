


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
        self.main_command = None
        self.sub_command = None

        self.running = True


    def run(self):
        while self.running:
            self.print_floor_info()
            self.user_input()
        print("Thanks for playing the game")

    def print_floor_info(self):
        current_room = self.map.map[self.player.current_floor]
        print(current_room)

    def climb(self):
        if self.player.current_floor > len(self.map.map) -1:
            print("You can't go there")

        if self.main_command == "climb" and self.player.current_floor != len(self.map.map) -1:
            if self.sub_command == "up":
                return self.map.map[self.player.current_floor + 1]
            elif self.sub_command == "down":
                return self.map.map[self.player.current_floor - 1]
        else:
            print("You are on the top floor")

    def user_input(self):
        command = input("what to do? ")
        command_parts = command.split()
        self.main_command = None
        self.sub_command = None
        if len(command_parts) > 0:
            self.main_command = command_parts[0].lower()
            if len(command_parts) > 1:
                self.sub_command = command_parts[1].lower()

    def use_user_input(self):
        if self.main_command == "climb":
            self.climb()




def main():

    game = Game()
    game.run()
    #game.move()
    #player = Player("glenn", "axe", 100)
    #print(player.inventory)
   # running = True
    #while running:
        #command = input("Would you like to climb? ")
        #print(Game.user_input(self.command))
        # command = command.split()
        # main_command = command[0]
        # sub_command = command[1]
        # print(main_command)
        # print(sub_command)
        # game.climb(command)
        # print(game.player.current_floor)
        # game.climb(command)
        # print(game.player.current_floor)

        #running = False

if __name__ == '__main__':

   main()


