from data.item_data import items
from item import Item

def item_creator(item_id):
    for item in items:
        if item["id"] == item_id:
            item_object = Item(**item)
            return item_object
