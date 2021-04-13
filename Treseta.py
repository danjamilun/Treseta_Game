import random
from random import shuffle


class Card:

    def __init__(self, num, col):
        self._num = num
        self._col = col

    def __str__(self):  
        return self._num + self._col


class Deck:

    def __init__(self):  
        self.COLOR_VALUE = ['Bate', 'Špade', 'Dinare', 'Kupe']
        self.number = ['As', '2', '3', '4', '5',
                       '6', '7', 'Fanat', 'Konj', 'Kralj']
        self.deck = [Card(num, col)
                     for col in self.COLOR_VALUE for num in self.number]

    def __str__(self):
        return str(self.deck)

    def get_card(self):  
        if len(self.deck) < 1:
            return None
        card = random.choice(self.deck)  
        self.deck.remove(card)  
        return card

    def get_card_value(self, card):  
        
        type_card = card._num
        card_value = {'3': 10, '2': 9, 'As': 8, 'Kralj': 7,
                      'Konj': 6, 'Fanat': 5, '7': 4, '6': 3, '5': 2, '4': 1}
        return card_value[type_card]

    
    def get_card_color(self, card):
        type_card = card._col
        color_card = {
            "Bate": 1,
            "Špade": 2,
            "Dinare": 3,
            "Kupe": 4,
        }
        return color_card[type_card]

    def compare_cards(self, card1, card2):  
        if(self.get_card_color(card1) == self.get_card_color(card2)):  
            if self.get_card_value(card1) > self.get_card_value(card2):
                return card1
            elif self.get_card_value(card1) < self.get_card_value(card2):
                return card2
        else: 
            return card1

    def __len__(self):
        return len(self.deck)

    def shuffle(self):  
        shuffle(self.deck)


class Player:
    def __init__(self, name):
        self.win_hand = 0  
        self.hand = []  
        self.name = name

    def get_name(self):

        return self.name

    def see_cards(self): 
        for card in self.hand:
            print(card)

    def get_card_from_hand(self, number_of_card):  
        return self.hand[number_of_card - 1]

    def add_card_to_hand(self, card):
        if card != None:
            self.hand.append(card)

    def remove_card_from_hand(self, card):  
        self.hand.remove(card)

    def hand_counter(self):  
        self.win_hand += 1

    def len_hand(self):  
        return len(self.hand)

    def get_hand_counter(self):  
        return self.win_hand


class Treseta:
    name1 = input("Igrač 1 : vaše ime?")
    player1 = Player(name1)
    player2 = Player("Komp") 
    deck = Deck()
    deck.shuffle()  

    while(player1.len_hand() < 4 and player2.len_hand() < 4):
        player1_card = deck.get_card()
        player2_card = deck.get_card()
        player1.add_card_to_hand(player1_card)
        player2.add_card_to_hand(player2_card)

    while True:
        if (player1.len_hand() < 4 and player2.len_hand() < 4):
            player1_card = deck.get_card()
            player2_card = deck.get_card()
            player1.add_card_to_hand(player1_card)
            player2.add_card_to_hand(player2_card)

        if player1.len_hand() == 0 or player2.len_hand() == 0:  
            print("Kraj igre !")
            print(name1, " ima ", player1.get_hand_counter())
            print("Komp", " ima ", player2.get_hand_counter())
            print("---------------------------------------")
            if player1.get_hand_counter() > player2.get_hand_counter():
                print(name1, " pobjeđuje!")
            elif player1.get_hand_counter() < player2.get_hand_counter():
                print("Komp pobjeđuje!")
            else:
                print(" :( ")
            break

        else:
            print("koju kartu zelite baciti : 1, 2, 3, 4 *(unesite brojem) ",
                  player1.see_cards())
            number_of_card = input()
            player1_card = player1.get_card_from_hand(
                int(number_of_card))  
            player1.remove_card_from_hand(player1_card)
            temp = False
            for card in player2.hand:
                if(deck.get_card_color(card) == deck.get_card_color(player1_card)):  
                    player2_card = card
                    player2.remove_card_from_hand(player2_card)
                    temp = True
            if(temp == False):  
                if(player2.len_hand() == 1):
                    player2_card = player2.hand.pop(0)

                else:
                    player2_card = random.choice(player2.hand)
                    player2.remove_card_from_hand(player2_card)

            if deck.compare_cards(player1_card, player2_card) == player1_card:  
                player1.hand_counter()  
            else:
                player2.hand_counter()  


if __name__ == '__main__':
    Treseta()
