
class Map:

    def __init__(self):
        self.floors = [
            {"name": "You are now on ground floor",
             "items": ["i1"],
             "challenge": "id1"
             },
            {"name": "You are now on floor 1",
             "items": ["i2"],
             "challenge": "id2"
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
        [self.map2.append(self.floors[x]) for x in range(7)]





