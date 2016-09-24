from random import shuffle

class Card:

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

class Deck:

    def __init__(self):
        self.card_list = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = {'A': 1,
                 '2': 2,
                 '3': 3,
                 '4': 4,
                 '5': 5,
                 '6': 6,
                 '7': 7,
                 '8': 8,
                 '9': 9,
                 '10': 10,
                 'J': 10,
                 'Q': 10,
                 'K': 10
                 }
        for suit in suits:
            for rank, value in ranks.items():
                self.card_list.append(Card(suit, rank, value))

    def size(self):
        return len(self.card_list)

    def shuffle_cards(self):
        shuffle(self.card_list)
        return self.card_list

    # def show_cards(self):
    #     for card in self.card_list:
    #         print (card.rank, card.suit)

    def new_card(self):
        return self.card_list.pop()


class Hand:

    def __init__(self, owner):
        self.player_hand = []
        self.player_hand_value = 0
        self.owner = owner

    def deal_card(self):
        new_card = deck.new_card()
        self.player_hand.append(new_card)


    def show_hand(self):
        for card in self.player_hand:
            print (card.rank, card.suit)

    def add_value(self):
        for card in self.player_hand:
            self.player_hand_value += card.value
        print (self.player_hand_value)

    def play(self):
        new_card = deck.new_card()
        print ("You have {}".format(self.player_hand_value))
        if self.player_hand_value > 21:
            print ("BUST! You lose!")
            return False
        choice = input("Would you like to [h]it or [s]tand? \n>")
        if choice == "h":
            self.player_hand.append(new_card)
            self.player_hand_value += new_card.value
            return True
        elif choice != "h":
            pass

    def dealer_move(self):
        new_card = deck.new_card()
        if self. player_hand_value < 17:
            self.player_hand.append(new_card)
            self.player_hand_value += new_card.value
            return True
        else:
            return False

    def end_of_game(self):
        if player1_hand.player_hand_value > dealer_hand.player_hand_value:
            print ("Congrats! You win!")
        elif dealer_hand.player_hand_value > 21:
            print ("Dealer has busted! You win!")
        else:
            print ("The dealer has won.")


class Player:

    def __init__(self, name):
        self.hand = Hand(name)


class Game:

    def __init__(self, chips):
        self.chips = 100

    def total_chips(self):
        return self.chips

    def add_chips(self, amount):
        self.chips = self.chips + amount


player1 = Player("Player 1")
dealer = Player("Dealer")
deck = Deck()

player1_hand = Hand(player1)
dealer_hand = Hand(dealer)

deck.shuffle_cards()
player1_hand.deal_card()
dealer_hand.deal_card()

player1_hand.deal_card()

dealer_hand.deal_card()
print ("Player 1 Hand")
player1_hand.show_hand()
print ("Dealer Hand")
dealer_hand.show_hand()
player1_hand.add_value()
dealer_hand.add_value()

while player1_hand.play():
    print ("Player 1 Hand")
    player1_hand.show_hand()
    print ("")
    print ("Dealer Hand")
    dealer_hand.show_hand()
    dealer_hand.dealer_move()
