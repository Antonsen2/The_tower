from game.Character import Npc
from threading import Timer
from data.item_data import items


class FloorChallenge:
    def __init__(self, current_floor, npc):
        self.current_floor = current_floor
        self.enemy = npc
        self.t = Timer(3, self.test)
        self.in_time = True
        self.item = items
        self.puzzle_complete = False

    def print_current_challenge(self):
        if self.enemy:
            print("there is a", self.enemy.name, "stopping you from climbing up")

        else:
            print("The enemy is defeated you can now climb up")


    def test(self):
        self.t.cancel()
        print("\nout of time")
        print("press any key to continue")
        self.in_time = False

    def chest_challenge(self):
        self.t.start()
        print("you have 3 seconds to answer this")
        while self.in_time or not self.puzzle_complete:
            answer = input("what is 2+2?")
            if answer == "4" and self.in_time:
                print("input successful, the chest opens")
                self.puzzle_complete = True
                self.t.cancel()
                break
            elif answer != "4" and self.in_time:
                print("wrong answer try again")
            else:
                self.item[0]["visible"] = False
                print("The challenge is failed, the chest disappeared")

