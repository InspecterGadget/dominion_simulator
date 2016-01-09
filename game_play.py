__author__ = 'stevenkerr'
import card_classes
from player_one_turn import take_turn
from random import shuffle
bank = card_classes.bank
trash = card_classes.trash
name_to_inst_dict = card_classes.name_to_inst_dict

class Player:
    def __init__(self):
        self.deck = []
        self.hand = []
        self.discard = []
        self.played_actions = []


    def print_list_name(self, n_list):
        n_list_print = []
        for x in range (0,len(n_list)):
            n_list_print.append(n_list[x].name)
        print n_list_print


    def shuffle_discards(self):
        self.deck.extend(self.discard)
        shuffle(self.deck)
        self.discard = []


    def draw_cards(self, num):
        for x in range(0,num):
            if len(self.deck) == 0:
                if len(self.discard) ==0:
                    break
                self.shuffle_discards()
            card_type = self.deck.pop(0)
            self.hand.append(card_type)



    def victory_count(self):
        count = 0
        for x in range(0,len(self.deck)):
            victory_points = self.deck[x].victory
            count = victory_points + count
        for x in range(0,len(self.discard)):
            victory_points = self.discard[x].victory
            count = victory_points + count
        for x in range(0,len(self.hand)):
            victory_points = self.hand[x].victory
            count += victory_points
        return count


    def check_player_for_card_type(self,card_type):
        in_hand = self.check_for_card_type(self.hand,card_type)
        in_deck = self.check_for_card_type(self.deck,card_type)
        in_discard = self.check_for_card_type(self.discard,card_type)
        in_played_actions = self.check_for_card_type(self.played_actions,card_type)
        total = in_deck + in_discard + in_hand + in_played_actions

        return total

    def check_for_card_type(self,list,looking_for):
        number_found = 0
        for x in range(0,len(list)):
            if list[x].name == looking_for:
                number_found += 1
        return number_found


    def index_of_card_type(self,list,looking_for):
        for x in range(0,len(list)):
            if list[x].name == looking_for:
                index = x
        return index


    def discard_hand(self):
        self.discard.extend(self.hand)
        self.hand = []


    def gain_card(self,ctg,spending_max):
        if bank[ctg.name] > 0 and ctg.cost <= spending_max:
            bank[ctg.name] -= 1
            self.discard.append(ctg)
        elif bank[ctg.name] <= 0:
            print "There are no more ", ctg.name, " remaining in the bank"
        else:
            print "Insufficient funds"

    def discard_played_actions(self):
        self.discard.extend(self.played_actions)
        self.played_actions = []


    def trash_card(self,list,card):
            index = self.index_of_card_type(list,card)
            list.pop(index)
            trash[card] += 1

class Game_result():
    def __init__(self):
        self.player_one_turns = 0
        self.player_two_turns = 0
        self.player_one_points = 0
        self.player_two_points = 0

    def print_one_result(self):
        print "Player one turns = ", self.player_one_turns
        print "Player two turns = ", self.player_two_turns
        print "Player one points = ", self.player_one_points
        print "Player two points = ", self.player_two_points

    def determine_winner(self):
        if self.player_one_points > self.player_two_points:
            winner = 'Player 1'
        elif self.player_two_points > self.player_one_points:
            winner = 'Player 2'
        elif self.player_two_points == self.player_one_points and self.player_one_turns > self.player_two_turns:
            winner = 'Player 2'
        elif self.player_two_points == self.player_one_points:
            winner = 'Tie'
        else:
            winner = 'Error'
        return winner


    def sum_winners(self,winner_list):
        winner = self.determine_winner()
        winner_list[0] +=1
        if winner == 'Player 1':
            winner_list[1] += 1
        elif winner == 'Player 2':
            winner_list[2] += 1
        elif winner == 'Tie':
            winner_list[3] += 1
        else:
            winner_list[4] += 1
        return winner_list


def play_game(player_one, player_two):
    player_one_turns = 0
    player_two_turns = 0
    while check_game_not_over():
        if player_one_turns == 0 :
            player_one.shuffle_discards()
            player_two.shuffle_discards()
            player_one.draw_cards(5)
            player_two.draw_cards(5)
        take_turn(player_one,player_two,1)
        player_one_turns += 1
        if check_game_not_over():
            take_turn(player_two,player_one,2)
            player_two_turns += 1
    game_result = Game_result()
    game_result.player_one_turns = player_one_turns
    game_result.player_two_turns = player_two_turns
    game_result.player_one_points = player_one.victory_count()
    game_result.player_two_points = player_two.victory_count()
    return game_result


def check_game_not_over():
    if bank['Province'] > 0 and check_three_pile_finish() < 3:
        not_over = True
    else:
        not_over = False
    return not_over


def check_three_pile_finish():
    count = 0
    for x in range(0,len(card_classes.all_cards_in_play_list)):
        if bank[card_classes.all_cards_in_play_list[x]] <= 0:
            count += 1
    return count


def reset_bank():
    for x in range(0,10):
        bank[card_classes.kingdom_cards[x]] = 10
    bank['Province']  = 8
    bank['Duchy'] = 8
    bank['Gold'] = 25
    bank['Silver'] = 40
    bank['Estate'] = 8
    bank['Copper'] = 40
    return bank

def reset_trash():
    for x in range (0,len(card_classes.all_cards_in_play_list)):
        trash[card_classes.all_cards_in_play_list[x]] = 0


def new_game(player):
    copper = card_classes.Copper()
    estate = card_classes.Estate()
    player.deck = [copper,copper,copper,copper,copper,copper,copper,estate,estate,estate]
    player.hand = []
    player.discard = []
    player.played_actions = []
    return player


def print_winner_list(wl,r):
    round_average = (r/2)/wl[0]
    print "Total games played ", wl[0]
    print "Player 1 Wins ", wl[1]
    print "Play 2 Wins ", wl[2]
    print "Ties " , wl[3]
    print "Round average ", round_average

def play_game_two(num):
    player_one = Player()
    player_two = Player()
    winner_list = [0,0,0,0,0]
    rounds = 0

    for x in range(0,num):
        bank = reset_bank()
        trash = reset_trash()
        player_one = new_game(player_one)
        player_two = new_game(player_two)
        result_one = play_game(player_one,player_two)
        winner_list = result_one.sum_winners(winner_list)
        rounds += result_one.player_one_turns + result_one.player_two_turns
    print_winner_list(winner_list,rounds)
    print_winner_list(winner_list,rounds)

#How to run a game
play_game_two(10000)
