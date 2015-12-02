__author__ = 'stevenkerr'


def manual_option_action_choice(mora,turn):
    if mora == 'Manual':
        print "Actions remaining: ", turn.actions_remaining
        print "Available actions: ", turn.actions_available
        print "Hand: ", turn.player.print_list_name(turn.player.hand)
        action = raw_input("Choose action card to play ")
    else:
        action = action_choice(turn)

    return action


def action_choice(player_info):
    villages_in_hand = check_for_card_type(player_info.hand,'Village')
    if villages_in_hand > 0:
        action = 'Village'
    else:
        action = 'Smithy'
    return action


def execute_action_strategy(turn,action):

    if action.name == 'Remodel':
        strategy = []
        strategy_trash = raw_input("Choose card to upgrade ")
        strategy_gain = raw_input("Choose card to gain ")
        strategy.append(strategy_trash)
        strategy.append(strategy_gain)
    elif action.name == 'Workshop':
        strategy = raw_input("Choose card to gain ")
    elif action.name == 'Feast':
        strategy = raw_input("Choose card to gain ")
    elif action.name == 'Chapel':
        x = 0
        strategy = []
        while x < 4:
            trash_card = raw_input("Choose a card to trash")
            if trash_card == 'None':
                break
            else:
                strategy.append(trash_card)
                x += 1

    else:
        strategy = 'none'

    return strategy


def check_for_card_type(list,looking_for):
    number_found = 0
    for x in range(0,len(list)):
        if list[x] == looking_for:
            number_found += 1
    return number_found

def buy_choice(player_info):
   smithies_for_player = check_player_for_card_type(player_info, 'Smithy')
   villages_for_player = check_player_for_card_type(player_info, 'Village')
   t = player_info.treasure
   if t >= 8:
       buy = 'Province'

   elif t >= 5 and player_info.bank['Province'] <= 4 and player_info.bank['Duchy'] >0:
      buy = 'Duchy'

   elif t >= 6:
       buy = 'Gold'

   elif t>= 4 and smithies_for_player <2:
       buy = 'Smithy'

   elif t >=3 and villages_for_player < 0:
       buy = 'Village'

   elif t >= 3:
      buy = 'Silver'

   else:
       buy = 'None'

   return buy


def check_player_for_card_type(player_info, card_type):
   in_hand = check_for_card_type(player_info.hand, card_type)
   in_deck = check_for_card_type(player_info.deck, card_type)
   in_discard = check_for_card_type(player_info.discard, card_type)
   in_played_actions = check_for_card_type(player_info.actions_played, card_type)
   total = in_deck + in_discard + in_hand + in_played_actions

   return total


