import random

monsters = [
    {
        "id": ["id1"],
        "name": "Skeleton",
        "hp": random.randrange(80, 120),
        "ap": random.randrange(15, 20),
        "drop": ["i3", "i11"]

    },
    {
        "id": ["id2"],
        "name": "Zombie",
        "hp": random.randrange(120, 170),
        "ap": random.randrange(20, 25),
        "drop": ["i4", "i3"]

    },
    {
        "id": ["id3"],
        "name": "Vampire",
        "hp": random.randrange(200, 250),
        "ap": random.randrange(25, 30),
        "drop": ["i3", "i13", "i4"]
    },
    {
        "id": ["id4"],
        "name": "Wraith",
        "hp": random.randrange(270, 300),
        "ap": random.randrange(30, 35),
        "drop": ["i6", "i7", "i3"]
    },
    {
        "id": ["id5"],
        "name": "Demon",
        "hp": random.randrange(300, 350),
        "ap": random.randrange(35, 40),
        "drop": ["i3", "i8", "i14", "i15"]
    },
    {
        "id": ["id6"],
        "name": "giant",
        "hp": random.randrange(350, 400),
        "ap": random.randrange(40, 45),
        "drop": ["i9", "i10", "i3"]
    },
    {
        "id": ["id7"],
        "name": "Hydra",
        "hp": random.randrange(400, 450),
        "ap": random.randrange(45, 50),
        "drop": ["i17", "i3"]
    },
    {
        "id": ["id8"],
        "name": "Dragon",
        "hp": 500,
        "ap": random.randrange(50, 100),
        "drop": []
    }
    ]


