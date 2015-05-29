__author__ = 'nuok'


class Player:
    def __init__(self, config):
        self.__exp = 0
        self.__money = 0
        self.__inventory = {}
        self.__exp_levels = config['exp_level']

    def get_level(self):
        level = 1
        for exp_level in self.__exp_levels:
            if self.__exp < exp_level:
                return level
            else:
                level += 1

    def add_exp(self, exp):
        self.__exp += exp

    def add_money(self, money):
        self.__money += money

    def add_inventory(self, drop_object):
        if not drop_object:
            return False
        if drop_object in self.__inventory:
            self.__inventory[drop_object] += 1
        else:
            self.__inventory[drop_object] = 1
        return True

    def get_inventory(self):
        return self.__inventory

    def clear_inventory(self):
        self.__inventory = {}

    def get_status(self):
        return {'level': self.get_level(),
                'exp': self.__exp,
                'money': self.__money,
                'inventory': self.get_inventory()}

if __name__ == "__main__":
    player_data = {'exp_level': [5, 10, 20, 40, 80, 160]}
    player = Player(player_data)

    print player.get_inventory()
    player.add_inventory('apple')

    print player.get_inventory()
    player.add_inventory('banana')

    print player.get_inventory()
    player.add_inventory('')

    print player.get_inventory().keys()