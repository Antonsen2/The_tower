from threading import Timer
from data.item_data import items
from utils import item_creator


class FloorChallenge:
    def __init__(self, current_floor, npc):
        self.current_floor = current_floor
        self.enemy = npc
        self.t = Timer(120, self.out_of_time)
        self.in_time = True
        self.item = items
        self.puzzle_complete = False
        self.chest = []

    def print_current_challenge(self):
        if self.enemy:
            print("there is a", self.enemy.name, "standing in front of the stair to the next level")
        if not self.enemy and self.current_floor == 7:
            print("The final boss is defeated, and the game is complete, good job! ")
        if not self.enemy:
            print("The enemy is defeated you can now climb up")

    def chest_challenge(self):
        self.t.start()
        print("you have 2 minutes to answer this")
        while self.in_time or self.puzzle_complete:
            answer = input("The foolish man wastes me, The average man spends me,"
                           " And wise man invests me, Yet all men succumb to me. What am I? ").lower()
            if answer == "time" and self.in_time:
                print("input successful, the chest opens")
                self.puzzle_complete = True
                self.t.cancel()
                break
            elif answer != "4" and self.in_time:
                print("wrong answer try again")
            else:
                print("The challenge is failed")
                self.t.cancel()

    def out_of_time(self):
        self.t.cancel()
        print("\nout of time")
        print("press any key to continue")
        self.in_time = False

    def create_chest(self, current_floor):
        for item in current_floor.items:
            if item.container:
                for i in item.contains:
                    self.chest.append(item_creator(i))

    def open_chest(self, current_floor, player):
        for item in current_floor.items:
            if item.name == "chest":
                if item.visible:
                    self.chest_challenge()
                    self.create_chest(current_floor)
                    if self.puzzle_complete:
                        chest_open = True
                    else:
                        chest_open = False
                    item.visible = False
                    current_floor.items.remove(item)
                    while chest_open and len(self.chest) > 0:
                        for item1 in self.chest:
                            print(f"the chest contains: a {item1.name}")
                        command1 = input("You can get the items or close to chest: ")

                        match command1.lower().split():
                            case ["none"] | ["close"] | ["stop"]:
                                chest_open = False
                            case ["knife"] | ["get", "knife"]:
                                for item1 in self.chest:
                                    if item1.name in command1:
                                        self.chest.remove(item1)
                                        player.inventory.append(item1)
                            case ["potion"] | ["get", "potion"]:
                                for item2 in self.chest:
                                    if item2.name in command1:
                                        self.chest.remove(item2)
                                        player.inventory.append(item2)
                            case _:
                                print(f"I dont understand {command1}")
                    print("poof the chest magically disappears")
