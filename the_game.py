import random
import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{}:{}".format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print("timer off")


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        lines = [[], [], [], [], [], [], [], [], []]
        lines[0].append('┌─────────┐')
        lines[1].append(f'│{self.rank[0] if values[self.rank] > 9 else values[self.rank]}        │')
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append(f'│    {self.suit}    │')
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append(f'│        {self.rank[0] if values[self.rank] > 9 else values[self.rank]}│')
        lines[8].append('└─────────┘')
        result = ''
        for num in range(9):
            result += ''.join(lines[num])
            result += '\n'
        return result


class Dealer:

    def __init__(self):
        self.dealer_cards = []

    def take_card(self):
        self.dealer_cards.append(deck.take_top())

    def remove_dealer_cards(self):
        self.dealer_cards = []

    def print_dealer_cards(self, dealer_cards, hidden=True):
        lines = [[], [], [], [], [], [], [], [], []]
        print("dealer cards:")
        # if hidden == False:
         #   print(f"dealer's sum is {self.return_dealer_sum(num_of_minus=dealer.is_there_A())}{' - BUSTED!' if self.return_dealer_sum(num_of_minus=dealer.is_there_A()) > 21 else ''}{' - BLACKJACK!!!!' if self.return_dealer_sum(num_of_minus=dealer.is_there_A()) == 21 and len(dealer_cards) == 2 else ''}")
        i = 1
        for card in dealer_cards:
            if i == 2 and hidden is True:
                lines[0].append('┌─────────┐')
                lines[1].append('│░░░░░░░░░│')
                lines[2].append('│░░░░░░░░░│')
                lines[3].append('│░░░░░░░░░│')
                lines[4].append('│░░░ ? ░░░│')
                lines[5].append('│░░░░░░░░░│')
                lines[6].append('│░░░░░░░░░│')
                lines[7].append('│░░░░░░░░░│')
                lines[8].append('└─────────┘')
            else:
                lines[0].append('┌─────────┐')
                lines[1].append(f'│{card.rank[0] if values[card.rank] > 9 else values[card.rank]}        │')
                lines[2].append('│         │')
                lines[3].append('│         │')
                lines[4].append(f'│    {card.suit}    │')
                lines[5].append('│         │')
                lines[6].append('│         │')
                lines[7].append(f'│        {card.rank[0] if values[card.rank] > 9 else values[card.rank]}│')
                lines[8].append('└─────────┘')
            i += 1
        result = ''
        for num in range(9):
            result += ''.join(lines[num])
            result += '\n'
        return result

    def return_dealer_sum(self, num_of_minus=0):
        dealer_sum = 0
        dealer_sum -= 10*num_of_minus
        for card in self.dealer_cards:
            dealer_sum += card.value
        return dealer_sum

    def is_there_A(self):
        aces = 0
        for card in self.dealer_cards:
            if card.value == 11:
                aces += 1
        return aces

class Player:

    def __init__(self, player_name, player_money):
        self.player_cards = []
        self.player_name = player_name
        self.player_money = int(player_money)

    def take_card(self):
        self.player_cards.append(deck.take_top())

    def remove_player_cards(self):
        self.player_cards = []

    def print_player_cards(self, player_cards):
        lines = [[], [], [], [], [], [], [], [], []]
        print(f"{self.player_name} cards:")
        # print(f"your sum is {self.return_player_sum(num_of_minus=player1.is_there_A())}{' - BUSTED!' if self.return_player_sum(num_of_minus=player1.is_there_A()) > 21 else ''}{' - BLACKJACK!!!!' if self.return_player_sum(num_of_minus=player1.is_there_A()) == 21 and len(player_cards) == 2 else ''}")
        for card in player_cards:
            lines[0].append('┌─────────┐')
            lines[1].append(f'│{card.rank[0] if values[card.rank] > 9 else values[card.rank]}        │')
            lines[2].append('│         │')
            lines[3].append('│         │')
            lines[4].append(f'│    {card.suit}    │')
            lines[5].append('│         │')
            lines[6].append('│         │')
            lines[7].append(f'│        {card.rank[0] if values[card.rank] > 9 else values[card.rank]}│')
            lines[8].append('└─────────┘')
        result = ''
        for i in range(9):
            result += ''.join(lines[i])
            result += '\n'
        return result

    def return_player_sum(self, num_of_minus=0):
        player_sum = 0
        player_sum -= 10*num_of_minus
        for card in self.player_cards:
            player_sum += card.value
        return player_sum

    def is_there_A(self):
        aces = 0
        for card in self.player_cards:
            if card.value == 11:
                aces += 1
        return aces

class Deck:

    def __init__(self):
        self.deck_cards = []
        for i in range(4):
            for suit in suits:
                for rank in ranks:
                    self.deck_cards.append(Card(rank, suit))

    def print_deck(self):
        print("\nDECK CARDS:")
        for card in self.deck_cards:
            print(card)
        print(f"there are {len(self.deck_cards)} cards")

    def shuffle(self):
        random.shuffle(self.deck_cards)

    def take_top(self):
        return self.deck_cards.pop(0)


suits = ['♠', '♦', '♥', '♣']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

print("\n\nWELCOME TO THE BLACK JACK GAME!\n")

dealer = Dealer()

while True:
    name = input("ENTER YOUR NAME: ")
    money = input(f"HEY {name.upper()}, HOW MUCH MONEY DO YOU WANT TO DEPOSIT? ")
    try:
        int(money)
        break
    except:
        print("TRY AGAIN - ENTER A NUMBER PLEASE!\n")
        continue
    money = int(money)

player1 = Player(name, money)
print(f"DEPOSIT SUCCEED! YOUR BALANCE IS: ${money}. LET'S START TO PLAY BLACKJACK!\n")
# countdown(3)

game_on = True
while game_on:
    dealer.remove_dealer_cards()
    player1.remove_player_cards()
    deck = Deck()
    deck.shuffle()

    dealer.take_card()
    dealer.take_card()
    player1.take_card()
    player1.take_card()

    player_busted = False
    dealer_busted = False

    winner = ''

    to_exit = False
    player_turn = True
    player_h_or_s = True
    dealer_turn = True

    while player_turn:
        print(f"\n{player1.player_name.upper()}, YOUR BALANCE IS: ${player1.player_money}")
        bet = input("ENTER YOUR BET: (type 'exit' to end the game)")
        if bet.upper() == "EXIT":
            to_exit = True
            player_h_or_s = False
            dealer_turn = False
            game_on = False
            break
        try:
            int(bet)
        except:
            print("TRY AGAIN - ENTER A NUMBER PLEASE!\n")
            continue
        if int(bet) > player1.player_money:
            print("TRY AGAIN - YOU DON'T HAVE ENOUGH MONEY FOR THIS BET!")
            continue
        bet = int(bet)
        while player_h_or_s:
            print('\n')
            print(dealer.print_dealer_cards(dealer.dealer_cards))
            print(player1.print_player_cards(player1.player_cards))
            player_choice = input(f"{player1.player_name.upper()}- type H for hit or S for stand!\n")
            if player_choice.upper() == 'H':
                player1.take_card()
                if player1.return_player_sum(num_of_minus=0) == 21:
                    print(player1.print_player_cards(player1.player_cards))
                    player_h_or_s = False
                    player_turn = False
                elif player1.return_player_sum(num_of_minus=player1.is_there_A()) > 21:
                    print(player1.print_player_cards(player1.player_cards))
                    player_busted = True
                    winner = 'dealer'
                    player_h_or_s = False
                    player_turn = False
            elif player_choice.upper() == 'S':
                player_h_or_s = False
                player_turn = False
            else:
                print("\nTRY AGAIN! UNVALID TYPE!\n")
                continue
    while dealer_turn:
        print(player1.print_player_cards(player1.player_cards))
        print(dealer.print_dealer_cards(dealer.dealer_cards, hidden=False))
        if player_busted == False:
            if dealer.return_dealer_sum(num_of_minus=dealer.is_there_A()) > 16 and dealer.return_dealer_sum(num_of_minus=dealer.is_there_A()) < 21:
                dealer_turn = False
            elif dealer.return_dealer_sum(num_of_minus=dealer.is_there_A()) > 21:
                dealer_busted = True
                dealer_turn = False
                winner = player1.player_name
            elif dealer.return_dealer_sum(num_of_minus=0) == 21:
                dealer_turn = False
            else:
                time.sleep(1.5)
                dealer.take_card()
        else:
            dealer_turn = False

    if to_exit == True:
        print("GOODBYE!")
    else:
        if player_busted == False and dealer_busted == False:
            if dealer.return_dealer_sum() < player1.return_player_sum():
                print(f"THE ROUND IS OVER! THE WINNER IS {player1.player_name.upper()}!\nYOU WON ${bet}!")
                player1.player_money += bet
            elif dealer.return_dealer_sum() > player1.return_player_sum():
                print(f"THE ROUND IS OVER! THE WINNER IS THE DEALER!\nYOU LOST ${bet}!")
                player1.player_money -= int(bet)
            else:
                print(f"THE ROUND IS OVER! TIE!")
        else:
            if winner == 'dealer':
                print(f"THE ROUND IS OVER! THE WINNER IS THE DEALER!\nYOU LOST ${bet}!")
                player1.player_money -= bet
            else:
                print(f"THE ROUND IS OVER! THE WINNER IS {player1.player_name.upper()}!\nYOU WON ${bet}!")
                player1.player_money += bet
        if player1.player_money == 0:
            print("YOU DON'T HAVE MONEY TO PLAY WITH! SEE YOU NEXT TIME (:")
            break










