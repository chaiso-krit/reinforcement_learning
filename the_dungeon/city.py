__author__ = 'nuok'
from location import Location


class City(Location):
    def __init__(self, config):
        Location.__init__(self, config)
        self.inventory_price = config['inventory_price']
        self.extra_price = config['extra_price']

    def sell(self, player):
        player_inventory = player.get_inventory()
        extra = 0
        if len(player_inventory.keys()) > 2:
            extra = self.extra_price
        for inventory in player_inventory:
            player.add_money(self.get_total_price(inventory, player_inventory[inventory]))
            player.add_money(extra)
        player.clear_inventory()

    def get_total_price(self, inventory, quantity):
        return self.inventory_price[inventory] * quantity

    def get_action(self):
        return {'sell': self.sell}

if __name__ == '__main__':
    main_city = {'name': 'main_city',
                 'neighbor': ['dun_1', 'dun_2'],
                 'inventory_price': {'apple': 10, 'banana': 15, 'orange': 20},
                 'extra_price': 30}
    city = City(main_city)
    print city.name
    print city.get_movable_location()

    import json
    json.dump(main_city, open('main_city.config', 'w'))