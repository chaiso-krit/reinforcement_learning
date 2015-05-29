__author__ = 'nuok'
import json
from map import Map
from player import Player


class Game:
    def __init__(self, config_filename):
        data = json.load(open(config_filename, 'r'))

        # init map
        self.map = Map(data)

        # init player
        self.player = Player(data['player'])

    def get_current_location_name(self):
        return self.map.get_current_location_name()

    def get_action(self):
        return self.get_action_dic().keys()

    def get_action_dic(self):
        return self.map.get_current_action()

    def play_action(self, action):
        action_dic = self.get_action_dic()
        action_dic[action](self.player)

    def get_player(self):
        return self.player

    def get_status(self):
        status = self.player.get_status()
        status['current_location'] = self.get_current_location_name()
        return status

if __name__ == '__main__':
    game = Game('config/level_1.config')

    print game.get_action()
    print game.get_status()

    game.play_action('move_dun_1')

    print game.get_status()
    print game.get_action()

    for iter in xrange(20):
        game.play_action('attack')
        print game.get_status()
    print game.get_status()

