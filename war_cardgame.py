import random
suits = ('Hearts', 'diamonds', 'spades', 'clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'joker', 'queen', 'king', 'ace')
values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'joker':11, 'queen':12, 'king':13, 'ace':14}
class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + 'of' + self.suit

class deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_top(self):
        return self.all_cards.pop(0)

    def add(self,newcard):
        if type(newcard) == type([]):
            self.all_cards.extend(newcard)
        else:
            self.all_cards.append(newcard)

    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards'

player_one_name = input("player 1 name??")
player_two_name = input("player 2 name??")

player_one = player(player_one_name)
player_two = player(player_two_name)
newdeck = deck()
newdeck.shuffle()

for i in range(26):
    player_one.add(newdeck.deal_one())
    player_two.add(newdeck.deal_one())

game = True
round = 0
while game:
    round +=1
    print (f'round {round}')
    if len(player_one.all_cards)==0:
        print (f'{player_one_name} out of cards. {player_two_name} wins')
        game = False
        break
    if len(player_two.all_cards) == 0:
        print (f'{player_two_name} out of cards. {player_one_name} wins')
        game = False
        break
    player_one_card=[]
    player_one_card.append(player_one.remove_top())

    player_two_card=[]
    player_two_card.append(player_two.remove_top())

    war = True
    while war:
        if player_one_card[-1].value > player_two_card[-1].value:
            player_one.add(player_one_card)
            player_one.add(player_two_card)
            war = False
        elif player_one_card[-1].value < player_two_card[-1].value:
            player_two.add(player_one_card)
            player_two.add(player_two_card)
            war = False
        else:
            print ("WAR")
            if len(player_one.all_cards) < 5:
                print(f'{player_one_name} unable to declare war so {player_two_name} wins')
                game = False
                break
            elif len(player_two.all_cards) < 5:
                print(f'{player_two_name} unable to declare war so {player_one_name} wins')
                game = False
                break
            else:
                for num in range(5):
                    player_one_card.append(player_one.remove_top())
                    player_two_card.append(player_two.remove_top())




