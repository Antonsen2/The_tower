from floor import Floor
from data.floor_data import floors


class Map:

    def __init__(self):

        floor_objects = [Floor(**f) for f in floors]
        self.map2 = [floor_objects[x] for x in range(8)]

    def get_current_room(self, x):
        return self.map2[x]
