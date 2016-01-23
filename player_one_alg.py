___author__ = 'stevenkerr'


def action_choice(player_info):
    labs = check_for_card_type(player_info.hand, 'Laboratory')
    feasts = check_for_card_type(player_info.hand, 'Feast')
    markets = check_for_card_type(player_info.hand, 'Market')
    if labs > 0:
        action = 'Laboratory'
    elif markets > 0:
        action = 'Market'

    elif feasts > 0:
        action = 'Feast'
    else:
        action = 'Chapel'

    return action


def execute_action_strategy(player_info, action):
    if action.name == 'Remodel':
        strategy = []
        strategy_trash = raw_input("Choose card to upgrade ")
        strategy_gain = raw_input("Choose card to gain ")
        strategy.append(strategy_trash)
        strategy.append(strategy_gain)
    elif action.name == 'Workshop':
        strategy = raw_input("Choose card to gain ")
    elif action.name == 'Feast':
        if player_info.bank['Province'] > 4 and player_info.bank['Laboratory'] > 0:
            strategy = 'Laboratory'
        elif player_info.bank['Duchy'] > 0:
            strategy = 'Duchy'
        else:
            strategy = 'Estate'
    elif action.name == 'Chapel':
        strategy = []
        estates = player_info.hand['Estate']
        coppers = player_info.hand['Copper']
        coppers_for_player = check_player_for_card_type(player_info, 'Copper')
        for x in range(0, estates):
            strategy.append('Estate')


    else:
        strategy = 'None'
    return strategy


def check_for_card_type(list, looking_for):
    number_found = 0
    for x in range(0, len(list)):
        if list[x] == looking_for:
            number_found += 1
    return number_found


def buy_choice(player_info):
    smithies_for_player = check_player_for_card_type(player_info, 'Smithy')
    villages_for_player = check_player_for_card_type(player_info, 'Village')
    silvers_for_player = check_player_for_card_type(player_info, 'Silver')
    chapels_for_player = check_player_for_card_type(player_info, 'Chapel')
    t = player_info.treasure
    if t >= 8:
        buy = 'Province'

    elif t >= 5 and player_info.bank['Province'] <= 3 and player_info.bank['Duchy'] > 0:
        buy = 'Duchy'

    elif t >=2 and player_info.bank['Province'] <=2 and player_info.bank['Estate'] >= 1:
        buy = 'Estate'

    elif t >= 6:
        buy = 'Gold'

    elif t >= 5 and player_info.bank['Laboratory'] > 7:
        buy = 'Laboratory'
    elif t >=5:
        buy = 'Market'

    elif t == 4 and player_info.bank['Feast'] > 9:
        buy = 'Feast'

    elif t >= 3:
        buy = 'Silver'

    elif t >= 2 and chapels_for_player == 0 and check_player_for_card_type(player_info,'Silver' < 1):
        buy = 'Chapel'
    elif t >= 2 and player_info.bank['Province'] < 4 and player_info.bank['Estate'] > 0:
        buy = 'Estate'

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