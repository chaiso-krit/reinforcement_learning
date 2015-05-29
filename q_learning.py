__author__ = 'nuok'
from the_dungeon.game import Game
import random
import time


class QLearning:
    def __init__(self, Q, learning_rate=0.001, discount_factor=0.7):
        self.Q = Q
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.current_state = None

    def set_current_state(self, current_state):
        self.current_state = current_state
        self.add_state(current_state)

    def update(self, action, reward, next_state):
        if self.current_state is None:
            print 'Must set current state first.'
            return
        self.update_action(self.current_state, action, self.calculate_return(reward, next_state))
        self.current_state = next_state

    def update_action(self, state, action, return_value):
        self.add_action(state, action)
        self.Q[state][action] += self.learning_rate*(return_value - self.Q[state][action])

    def calculate_return(self, reward, next_state):
        return reward + self.discount_factor*self.get_discounted_reward(next_state)

    def get_discounted_reward(self, next_state):
        self.add_state(next_state)
        if len(self.Q[next_state].keys()) == 0:
            return 0
        else:
            return max(self.Q[next_state].values())

    def add_state(self, state):
        if state not in self.Q:
            self.Q[state] = {}

    def add_action(self, state, action):
        self.add_state(state)
        if action not in self.Q[state]:
            self.Q[state][action] = 0.0

    def print_policy(self):
        for state in self.Q:
            print state
            for action in self.Q[state]:
                print '\t', action, "-> %.2f" % (self.Q[state][action])

    def get_optimal_action(self):
        if not self.Q[self.current_state]:
            return None
        else:
            return max(self.Q[self.current_state], key=self.Q[self.current_state].get)

    def get_action_from_e_greedy(self, action_list, epsilon=0.8):
        if self.get_optimal_action() is not None and random.random() <= epsilon:
            return self.get_optimal_action()
        else:
            return random.choice(action_list)

if __name__ == "__main__":
    game = Game('the_dungeon/config/level_1.config')

    learning = QLearning({})
    learning.set_current_state(game.get_current_location_name())
    current_status = game.get_status()
    for iter_1 in xrange(2000):
        for iter_2 in xrange(2000):
            action_list = game.get_action()
            selected_action = learning.get_action_from_e_greedy(action_list)

            game.play_action(selected_action)

            new_status = game.get_status()
            learning.update(selected_action, new_status['money']-current_status['money'], game.get_current_location_name())
            current_status = new_status

            #print selected_action
            #print learning.Q
            #time.sleep(0.3)
    learning.print_policy()
