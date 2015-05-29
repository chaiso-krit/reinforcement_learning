__author__ = 'nuok'


class Location:
    def __init__(self, config):
        self.location_list = config['neighbor']
        self.name = config['name']

    def get_name(self):
        return self.name

    def get_movable_location(self):
        return self.location_list