class Map:

    def __init__(self):
        self.floors = [
            {"name": "You are now on floor 0",
             "items": [],
             "challenge": ""
             },
            {"name": "You are now on floor 1",
             "items": [],
             "challenge": ""
             },
            {"name": "You are now on floor 2",
             "items": [],
             "challenge": ""
             },
            {"name": "You are now on floor 3",
             "items": [],
             "challenge": ""
             },
            {"name": "You are now on floor 4",
             "items": [],
             "challenge": ""
             },
            {"name": "You are now on floor 5",
             "items": [],
             "challenge": ""
             },
            {"name": "You are now on floor 6",
             "items": [],
             "challenge": ""
             },
            {"name": "You are now on floor 7",
             "items": [],
             "challenge": ""
             },
        ]
        self.map2 = []
        [self.map2.append(self.floors[x]["name"]) for x in range(7)]

