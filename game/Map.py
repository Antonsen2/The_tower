
class Map:

    def __init__(self):
        self.floors = [
            {"name": "You are now on ground floor",
             "items": ["i1", "i5"],
             "challenge": ["id1"]
             },
            {"name": "You are now on floor 1",
             "items": [""],
             "challenge": ["id2"]
             },
            {"name": "You are now on floor 2",
             "items": [],
             "challenge": ["id3"]
             },
            {"name": "You are now on floor 3",
             "items": [],
             "challenge": ["id4"]
             },
            {"name": "You are now on floor 4",
             "items": [],
             "challenge": ["id5"]
             },
            {"name": "You are now on floor 5",
             "items": [],
             "challenge": ["id6"]
             },
            {"name": "You are now on floor 6",
             "items": [],
             "challenge": ["id7"]
             },
            {"name": "You are now on floor 7",
             "items": [],
             "challenge": ["id8"]
             },
        ]
        self.map2 = []
        [self.map2.append(self.floors[x]) for x in range(8)]






