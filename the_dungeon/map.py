__author__ = 'nuok'
from city import City
from dungeon import Dungeon


class Map:
    def __init__(self, config_data):
        locations = {}

        # init city
        for city in config_data['cities']:
            locations[city['name']] = City(city)

        # init dungeon
        for dungeon in config_data['dungeons']:
            locations[dungeon['name']] = Dungeon(dungeon)

        self.locations = locations
        self.current_location = self.locations['main_city']

    def get_current_location_name(self):
        return self.current_location.get_name()

    def get_neighbor(self):
        return self.current_location.get_movable_location()

    def move(self, location_name, player):
        for neighbor in self.get_neighbor():
            if location_name in neighbor:
                self.current_location = self.locations[location_name]
                return True
        return False

    def make_move_action(self, location_name):
        return lambda player: self.move(location_name, player)

    def get_current_action(self):
        action_dic = self.current_location.get_action()
        for location in self.get_neighbor():
            action_dic['move_' + location] = self.make_move_action(location)
        return action_dic