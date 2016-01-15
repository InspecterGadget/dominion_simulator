__author__ = 'stevenkerr'


class Copper:
    def __init__(self):
       self.cost = 0
       self.treasure = 1
       self.grouping = 'Treasure'
       self.draw_cards = 0
       self.gain_actions = 0
       self.victory = 0
       self.name = 'Copper'
       self.bank_name = 'coppers'


class Estate:
    def __init__(self):
        self.cost = 2
        self.treasure = 0
        self.grouping = 'Victory'
        self.draw_cards = 0
        self.gain_actions = 0
        self.victory = 1
        self.name = 'Estate'


class Silver:
    def __init__(self):
        self.cost = 3
        self.treasure = 2
        self.grouping = 'Treasure'
        self.draw_cards = 0
        self.gain_actions = 0
        self.victory = 0
        self.name = 'Silver'


class Gold:
    def __init__(self):
        self.cost = 6
        self.treasure = 3
        self.grouping = 'Treasure'
        self.draw_cards = 0
        self.gain_actions = 0
        self.victory = 0
        self.name = 'Gold'


class Province:
    def __init__(self):
        self.cost = 8
        self.treasure = 0
        self.grouping = 'Victory'
        self.draw_cards = 0
        self.gain_actions = 0
        self.victory = 6
        self.name = 'Province'


class Duchy:
    def __init__(self):
        self.cost = 5
        self.treasure = 0
        self.grouping = 'Victory'
        self.draw_cards = 0
        self.gain_actions = 0
        self.victory = 3
        self.name = 'Duchy'


class Smithy:
    def __init__(self):
        self.cost = 4
        self.treasure = 0
        self.grouping = 'Action'
        self.draw_cards = 3
        self.gain_actions = 0
        self.gain_buys = 0
        self.gain_treasure = 0
        self.victory = 0
        self.name = 'Smithy'

    def execute_action(self, turn, none):
        standard_action_execute(turn,self)


class Village:
    def __init__(self):
        self.cost = 3
        self.treasure = 0
        self.grouping = 'Action'
        self.draw_cards = 1
        self.gain_actions = 2
        self.gain_buys = 0
        self.gain_treasure = 0
        self.victory = 0
        self.name = 'Village'

    def execute_action(self, turn, none):
        standard_action_execute(turn,self)


class Laboratory:
    def __init__(self):
        self.cost = 5
        self.treasure = 0
        self.grouping = 'Action'
        self.draw_cards = 2
        self.gain_actions = 1
        self.gain_buys = 0
        self.gain_treasure = 0
        self.victory = 0
        self.name = 'Laboratory'

    def execute_action(self, turn, none):
        standard_action_execute(turn,self)


class Market:
    def __init__(self):
        self.cost = 5
        self.treasure = 0
        self.grouping = 'Action'
        self.draw_cards = 1
        self.gain_actions = 1
        self.gain_buys = 1
        self.gain_treasure = 1
        self.victory = 0
        self.name = 'Market'

    def execute_action(self, turn, none):
        standard_action_execute(turn,self)


class Moneylender:
    def __init__(self):
        self.cost = 4
        self.treasure = 0
        self.grouping = 'Action'
        self.draw_cards = 0
        self.gain_actions = 0
        self.gain_buys = 0
        self.gain_treasure = 0
        self.victory = 0
        self.name = 'Money Lender'

    def execute_action(self, turn, none):
        standard_action_execute(turn,self)
        copper_in_hand = turn.player.check_for_card_type(turn.player.hand, 'Copper')
        if copper_in_hand > 0:
            turn.player.trash_card(turn.player.hand, 'Copper')
            turn.treasure += 3


class Woodcutter:
    def __init__(self):
        self.cost = 3
        self.treasure = 0
        self.grouping = 'Action'
        self.draw_cards = 0
        self.gain_actions = 0
        self.gain_buys = 1
        self.gain_treasure = 2
        self.victory = 0
        self.name = 'Woodcutter'

    def execute_action(self, turn, none):
        standard_action_execute(turn,self)


class Festival:
    def __init__(self):
        self.cost = 5
        self.treasure = 0
        self.grouping = 'Action'
        self.draw_cards = 0
        self.gain_actions = 2
        self.gain_buys = 1
        self.gain_treasure = 2
        self.victory = 0
        self.name = 'Festival'

    def execute_action(self, turn, none):
        standard_action_execute(turn,self)


class Remodel:
    def __init__(self):
        self.cost = 4
        self.treasure = 0
        self.grouping = 'Action'
        self.draw_cards = 0
        self.gain_actions = 0
        self.gain_buys = 0
        self.gain_treasure = 0
        self.victory = 0
        self.name = 'Remodel'

    def execute_action(self, turn, trash_gain):
        standard_action_execute(turn,self)
        trash_card = trash_gain[0]
        gain_card = trash_gain[1]
        trash_card_inst = name_to_inst_dict[trash_card]
        gain_card_inst = name_to_inst_dict[gain_card]
        if trash_card_inst.cost +2 >= gain_card_inst.cost:
            turn.player.trash_card(turn.player.hand,trash_card)
            turn.player.gain_card(gain_card_inst,trash_card_inst.cost + 2)



class Workshop:
    def __init__(self):
        self.cost = 3
        self.treasure = 0
        self.grouping = 'Action'
        self.draw_cards = 0
        self.gain_actions = 0
        self.gain_buys = 0
        self.gain_treasure = 0
        self.victory = 0
        self.name = 'Workshop'

    def execute_action(self, turn, gain_card):
        standard_action_execute(turn,self)
        gain_card = name_to_inst_dict[gain_card]
        if gain_card.cost <= 4:
            turn.player.gain_card(gain_card,4)


class Feast:
    def __init__(self):
        self.cost = 4
        self.treasure = 0
        self.grouping = 'Action'
        self.draw_cards = 0
        self.gain_actions = 0
        self.gain_buys = 0
        self.gain_treasure = 0
        self.victory = 0
        self.name = 'Feast'

    def execute_action(self,turn, gain_card):
        standard_action_execute(turn,self)
        gain_card = name_to_inst_dict[gain_card]
        if gain_card.cost <= 5:
            turn.player.gain_card(gain_card,5)
            turn.player.trash_card(turn.player.played_actions,'Feast')

class Chapel:
    def __init__(self):
        self.cost = 2
        self.treasure = 0
        self.grouping = 'Action'
        self.draw_cards = 0
        self.gain_actions = 0
        self.gain_buys = 0
        self.gain_treasure = 0
        self.victory = 0
        self.name = 'Chapel'


    def execute_action(self,turn, cards_to_trash):
        standard_action_execute(turn,self)
        if len(cards_to_trash) <= 4:
            for x in range(0,len(cards_to_trash)):
              # card_to_trash = name_to_inst_dict[cards_to_trash[x]]
                turn.player.trash_card(turn.player.hand,cards_to_trash[x])


def standard_action_execute(turn,action):
    turn.player.draw_cards(action.draw_cards)
    turn.actions_remaining += (action.gain_actions - 1)
    turn.buys_remaining += (action.gain_buys)
    turn.treasure += (action.gain_treasure)

kingdom_cards = ['Village','Chapel','Workshop','Smithy','Money Lender', 'Remodel', 'Feast','Market', 'Festival', 'Laboratory']
standard_supply = ['Copper', 'Silver', 'Gold', 'Estate', 'Duchy', 'Province']
all_cards_in_play_list = kingdom_cards + standard_supply
name_to_inst_dict = {'Copper':Copper(), 'Duchy':Duchy(), 'Estate':Estate(), 'Gold':Gold(), 'Silver':Silver(),
                     'Province':Province(), 'Laboratory' :Laboratory(),'Market':Market(), 'Smithy':Smithy(),
                     'Village': Village(),'Money Lender': Moneylender(), 'Woodcutter': Woodcutter(),
                     'Festival': Festival(), 'Remodel':Remodel(), 'Workshop': Workshop(), 'Feast' : Feast(),
                     'Chapel' : Chapel()}
bank = {'Copper': 40, 'Estate': 8, 'Silver': 40, 'Duchy' : 8, 'Gold' : 25, 'Province' : 8, 'Money Lender' :10}
trash = {'Copper': 0, 'Estate': 0, 'Silver': 0, 'Village': 0, 'Smithy' :0, 'Duchy' : 0, 'Gold' : 0, 'Province' : 0}
