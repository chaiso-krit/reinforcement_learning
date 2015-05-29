__author__ = 'nuok'
from location import Location
import random


class Dungeon(Location):
    def __init__(self, config):
        Location.__init__(self, config)
        self.victory_chance = config['victory_chance']
        self.reward = config['reward']
        self.exp_reward = config['exp_reward']
        self.penalty = config['penalty']
        self.drop_object = config['drop_object']

    def attack(self, player):
        if random.random() <= self.get_victory_chance(player):
            player.add_money(self.reward)
            player.add_exp(self.exp_reward)
            player.add_inventory(self.drop_object)
        else:
            player.add_money(self.penalty)

    def get_victory_chance(self, player=None):
        if player is not None:
            return self.victory_chance + (player.get_level()-1) * 0.05
        else:
            return self.victory_chance

    def get_action(self):
        return {'attack': self.attack}

if __name__ == '__main__':
    dun_data = {'name': 'dun_1',
                'neighbor': ['main_city'],
                'victory_chance': 0.9,
                'reward': 10,
                'penalty': -5,
                'exp_reward': 0,
                'drop_object': ''}
    dun = Dungeon(dun_data)
    print dun.name
    print dun.get_movable_location()
    print dun.attack()