import random

monsters = [
    {
        "id": ["id1"],
        "name": "Skeleton",
        "hp": random.randrange(80, 120),
        "ap": random.randrange(10, 15),
        "drop": ["i3", "i5"]

    },
    {
        "id": ["id2"],
        "name": "Zombie",
        "hp": random.randrange(120, 170),
        "ap": random.randrange(20, 25),
        "drop": ["i11", "i3"]

    },
    {
        "id": ["id3"],
        "name": "Vampire",
        "hp": random.randrange(170, 200),
        "ap": random.randrange(20, 30),
        "drop": ["i3", "i13", "i6"]
    },
    {
        "id": ["id4"],
        "name": "Wraith",
        "hp": random.randrange(200, 230),
        "ap": random.randrange(25, 35),
        "drop": ["i7", "i3"]
    },
    {
        "id": ["id5"],
        "name": "Demon",
        "hp": random.randrange(230, 250),
        "ap": random.randrange(30, 40),
        "drop": ["i3", "i8", "i14", "i15"]
    },
    {
        "id": ["id6"],
        "name": "giant",
        "hp": random.randrange(250, 270),
        "ap": random.randrange(35, 45),
        "drop": ["i9", "i10", "i3", "i3"]
    },
    {
        "id": ["id7"],
        "name": "Hydra",
        "hp": random.randrange(270, 300),
        "ap": random.randrange(40, 50),
        "drop": ["i17", "i3", "i3"]
    },
    {
        "id": ["id8"],
        "name": "Dragon",
        "hp": 400,
        "ap": random.randrange(50, 70),
        "drop": []
    }
    ]


