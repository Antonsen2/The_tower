from game.Character import Npc
from threading import Timer
from data.item_data import items


class FloorChallenge:
    def __init__(self, current_floor, npc):
        self.current_floor = current_floor
        self.enemy = npc
        self.t = Timer(3, self.test)
        self.in_time = True
        self.items = items
        self.puzzle_complete = False

    def print_current_challenge(self):
        print("there is a", self.enemy.name, "stopping you from climbing up")

    def test(self):
        self.t.cancel()
        print("\nout of time")
        self.in_time = False
       # ToDo Write this method more user friendly.



    def chest_challenge(self):

        in_time = True
        self.t.start()
        print("you have 3 seconds to answer this")
        while self.in_time and not self.puzzle_complete:
            answer = input("what is 2+2?")

            if answer == "4" and self.in_time:
                print("input successful, the chest opens")
                self.puzzle_complete = True
                self.t.cancel()
            elif answer != "4":
                print("wrong answer try agian")









# from pytimedinput import timedInput
#
# def main():
#     while True:
#         userText, timedOut = timedInput("What is 2 + 2: ", 3)
#         if (timedOut):
#             print("Timed out when waiting for input.")
#             #print(f"User-input so far: '{userText}'")
#         else:
#             if userText == "4":
#                 break
#     print(f"User-input: '{userText}'")
#
#
# if __name__ == '__main__':
#     main()



# from pytimedinput import timedInput
# import random
#
#
# def main():
#     questions = [('What is 2 + 2', '4'), ('What is 3 * 3', '9')]
#     while True:
#         question, answer = random.choice(questions)
#         userText, timedOut = timedInput(question + ": ", 3)
#         if (timedOut):
#             print("Timed out when waiting for input.")
#             #print(f"User-input so far: '{userText}'")
#         else:
#             if userText == answer:
#                 break
#     print(f"User-input: '{userText}'")
#
#
# if __name__ == '__main__':
#     main()
