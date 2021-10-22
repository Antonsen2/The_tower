items = [
    {
        "id": "i1",
        "name": "chest",
        "description": "a chest that you can open",
        "lock": "puzzle",
        "contains": ["i2", "i3"],
        "pick_up": False,
        "equippable": False,
        "container": True,
        "visible": True


    },
    {
        "id": "i2",
        "name": "knife",
        "description": "a small but sharp knife",
        "bonus_ap": 10,
        "pick_up": True,
        "equippable": True,
        "container": False,
        "visible": True

    },
    {
        "id": "i3",
        "name": "potion",
        "description": "a health potion that can heal you",
        "heals": 10,
        "pick_up": True,
        "equippable": False,
        "container": False,
        "visible": True
    }]
