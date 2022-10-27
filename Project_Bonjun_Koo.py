import random
import tkinter as tk


class Gui:
    """
    A class to create a GUI for one game of Texas Holdem.

    """
    def __init__(self, title='Texas Holdem'):
        """This constructor for the class initializes all the text for labels (cards, money, etc)
        and buttons, creating them as StringVar() or IntVar() instances. Then, for every player/bot it groups their respective
        StringVars and IntVars into 1 list, then appends that list into a main list of labels that has the collective lists
        of each player's labels.

        """
        self.setup_gui(title)
        self.round_counter = 0
        self.player_number = tk.IntVar()
        self.player_labels = []

        self.user_first_card = tk.StringVar()
        self.user_second_card = tk.StringVar()
        self.user_money = tk.IntVar()
        self.user_bet_amount = tk.IntVar()
        self.bet_amount = tk.IntVar()

        self.p1_first_card = tk.StringVar()
        self.p1_second_card = tk.StringVar()
        self.p1_money = tk.StringVar()
        self.p1_bet = tk.StringVar()
        self.p1 = [self.p1_first_card, self.p1_second_card, self.p1_money, self.p1_bet, 1]
        self.player_labels.append(self.p1)

        self.p2_first_card = tk.StringVar()
        self.p2_second_card = tk.StringVar()
        self.p2_money = tk.StringVar()
        self.p2_bet = tk.StringVar()
        self.p2 = [self.p2_first_card, self.p2_second_card, self.p2_money, self.p2_bet, 2]
        self.player_labels.append(self.p2)

        self.p3_first_card = tk.StringVar()
        self.p3_second_card = tk.StringVar()
        self.p3_money = tk.StringVar()
        self.p3_bet = tk.StringVar()
        self.p3 = [self.p3_first_card, self.p3_second_card, self.p3_money, self.p3_bet, 3]
        self.player_labels.append(self.p3)

        self.p4_first_card = tk.StringVar()
        self.p4_second_card = tk.StringVar()
        self.p4_money = tk.StringVar()
        self.p4_bet = tk.StringVar()
        self.p4 = [self.p4_first_card, self.p4_second_card, self.p4_money, self.p4_bet, 4]
        self.player_labels.append(self.p4)

        self.p5_first_card = tk.StringVar()
        self.p5_second_card = tk.StringVar()
        self.p5_money = tk.StringVar()
        self.p5_bet = tk.StringVar()
        self.p5 = [self.p5_first_card, self.p5_second_card, self.p5_money, self.p5_bet, 5]
        self.player_labels.append(self.p5)

        self.p6_first_card = tk.StringVar()
        self.p6_second_card = tk.StringVar()
        self.p6_money = tk.StringVar()
        self.p6_bet = tk.StringVar()
        self.p6 = [self.p6_first_card, self.p6_second_card, self.p6_money, self.p6_bet, 6]
        self.player_labels.append(self.p6)

        self.p7_first_card = tk.StringVar()
        self.p7_second_card = tk.StringVar()
        self.p7_money = tk.StringVar()
        self.p7_bet = tk.StringVar()
        self.p7 = [self.p7_first_card, self.p7_second_card, self.p7_money, self.p7_bet, 7]
        self.player_labels.append(self.p7)

        self.p8_first_card = tk.StringVar()
        self.p8_second_card = tk.StringVar()
        self.p8_money = tk.StringVar()
        self.p8_bet = tk.StringVar()
        self.p8 = [self.p8_first_card, self.p8_second_card, self.p8_money, self.p8_bet, 8]
        self.player_labels.append(self.p8)

        self.p9_first_card = tk.StringVar()
        self.p9_second_card = tk.StringVar()
        self.p9_money = tk.StringVar()
        self.p9_bet = tk.StringVar()
        self.p9 = [self.p9_first_card, self.p9_second_card, self.p9_money, self.p9_bet, 9]
        self.player_labels.append(self.p9)

        self.com_card_1 = tk.StringVar()
        self.com_card_2 = tk.StringVar()
        self.com_card_3 = tk.StringVar()
        self.com_card_4 = tk.StringVar()
        self.com_card_5 = tk.StringVar()
        self.winner = tk.StringVar()

        self.get_number()
        self.root.mainloop()

    def setup_gui(self, title: str) -> None:
        """initializes the GUI for the player. Creates the dimensions and color for the window.

        Args:
            title : the title of the GUI
        """
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry('950x580')
        self.root.resizable(0,0)
        self.root.config(bg='LightSteelBlue4')

    def get_number(self) -> None:
        """Sets up the first screen for the GUI window. It creates the labels/buttons/entry for the initial screen whose
        purpose is to receive the number of bot players the user wishes to play against.

        Returns: None
        """
        self.player_num_text = tk.Label(self.root, text='Enter # of Bots You Wish to Play Against (1-9)')
        self.player_num_text.place(x=190, y=150)
        self.player_num_text.config(font=('Helvetica bold', 20))

        self.player_number.set('')
        self.num_entry = tk.Entry(self.root, textvariable=self.player_number, width = 10)
        self.num_entry.place(x=420, y=220)

        self.enter_button = tk.Button(self.root, text="Enter", height = 3, width = 10, command=lambda: self.initialize_labels())
        self.enter_button.place(x=412, y=275)

    def initialize_labels(self) -> None:
        """Sets up the second screen for the GUI window. It creates the labels that represent the players' cards, bets,
        names, and money. It also creates a entry box for the bet amount the user wishes to use. The second screen will
        only initialize when the user inputs a valid number (1-9) of bot players. It also creates the label boxes for
        the community cards.

        Returns: None
        """
        if self.player_number.get() > 9 or self.player_number.get() < 1:
            pass
        else:
            self.player_num_text.destroy()
            self.num_entry.destroy()
            self.enter_button.destroy()

            self.fold = tk.Button(self.root, text="Fold", height=1, width=10, command=lambda: self.player_folds())
            self.bet = tk.Button(self.root, text="Bet", height=1, width=10, command=lambda: self.player_bets(self.bet_amount.get()))
            self.bet_amount.set("Enter Amount")
            self.bet_amount_entry = tk.Entry(self.root, textvariable=self.bet_amount, width = 13)
            self.check = tk.Button(self.root, text="Check", height=1, width=10, command=lambda: self.player_checks())
            self.play_again = tk.Button(self.root, text="Play Again?", height=1, width=10, command=lambda: self.plays_again())
            self.quit_button = tk.Button(self.root, text="Quit", height=1, width=10, command=lambda: self.player_quits())
            self.winner_label = tk.Label(self.root,textvariable=self.winner, height=3, width=30)

            self.user_name = tk.Label(self.root, text = "User", font=35)
            self.user_1_card_label = tk.Label(self.root, textvariable=self.user_first_card, height=8, width=10,relief='solid')
            self.user_2_card_label = tk.Label(self.root, textvariable=self.user_second_card, height=8, width=10,relief='solid')
            self.user_money_label = tk.Label(self.root, textvariable=self.user_money, height=1, width=5,relief='solid')
            self.user_bet_label = tk.Label(self.root, textvariable=self.user_bet_amount, height=1, width=5,relief='solid')

            self.p1_name = tk.Label(self.root, text="Player1", font=25)
            self.p1_1_card_label = tk.Label(self.root, textvariable=self.p1_first_card, height=5, width=8,relief='solid')
            self.p1_2_card_label = tk.Label(self.root, textvariable=self.p1_second_card, height=5, width=8,relief='solid')
            self.p1_money_label = tk.Label(self.root, textvariable=self.p1_money, height=1, width=5,relief='solid')
            self.p1_bet_label = tk.Label(self.root, textvariable=self.p1_bet, height=1, width=5, relief='solid')

            self.p2_name = tk.Label(self.root, text="Player2", font=25)
            self.p2_1_card_label = tk.Label(self.root, textvariable=self.p2_first_card, height=5, width=8,relief='solid')
            self.p2_2_card_label = tk.Label(self.root, textvariable=self.p2_second_card, height=5, width=8,relief='solid')
            self.p2_money_label = tk.Label(self.root, textvariable=self.p2_money, height=1, width=5,relief='solid')
            self.p2_bet_label = tk.Label(self.root, textvariable=self.p2_bet, height=1, width=5, relief='solid')

            self.p3_name = tk.Label(self.root, text="Player3", font=25)
            self.p3_1_card_label = tk.Label(self.root, textvariable=self.p3_first_card, height=5, width=8,relief='solid')
            self.p3_2_card_label = tk.Label(self.root, textvariable=self.p3_second_card, height=5, width=8,relief='solid')
            self.p3_money_label = tk.Label(self.root, textvariable=self.p3_money, height=1, width=5,relief='solid')
            self.p3_bet_label = tk.Label(self.root, textvariable=self.p3_bet, height=1, width=5, relief='solid')

            self.p4_name = tk.Label(self.root, text="Player4", font=25)
            self.p4_1_card_label = tk.Label(self.root, textvariable=self.p4_first_card, height=5, width=8,relief='solid')
            self.p4_2_card_label = tk.Label(self.root, textvariable=self.p4_second_card, height=5, width=8,relief='solid')
            self.p4_money_label = tk.Label(self.root, textvariable=self.p4_money, height=1, width=5,relief='solid')
            self.p4_bet_label = tk.Label(self.root, textvariable=self.p4_bet, height=1, width=5, relief='solid')

            self.p5_name = tk.Label(self.root, text="Player5", font=25)
            self.p5_1_card_label = tk.Label(self.root, textvariable=self.p5_first_card, height=5, width=8,relief='solid')
            self.p5_2_card_label = tk.Label(self.root, textvariable=self.p5_second_card, height=5, width=8,relief='solid')
            self.p5_money_label = tk.Label(self.root, textvariable=self.p5_money, height=1, width=5,relief='solid')
            self.p5_bet_label = tk.Label(self.root, textvariable=self.p5_bet, height=1, width=5, relief='solid')

            self.p6_name = tk.Label(self.root, text="Player6", font=25)
            self.p6_1_card_label = tk.Label(self.root, textvariable=self.p6_first_card, height=5, width=8,relief='solid')
            self.p6_2_card_label = tk.Label(self.root, textvariable=self.p6_second_card, height=5, width=8,relief='solid')
            self.p6_money_label = tk.Label(self.root, textvariable=self.p6_money, height=1, width=5,relief='solid')
            self.p6_bet_label = tk.Label(self.root, textvariable=self.p6_bet, height=1, width=5, relief='solid')

            self.p7_name = tk.Label(self.root, text="Player7", font=25)
            self.p7_1_card_label = tk.Label(self.root, textvariable=self.p7_first_card, height=5, width=8,relief='solid')
            self.p7_2_card_label = tk.Label(self.root, textvariable=self.p7_second_card, height=5, width=8,relief='solid')
            self.p7_money_label = tk.Label(self.root, textvariable=self.p7_money, height=1, width=5,relief='solid')
            self.p7_bet_label = tk.Label(self.root, textvariable=self.p7_bet, height=1, width=5, relief='solid')

            self.p8_name = tk.Label(self.root, text="Player8", font=25)
            self.p8_1_card_label = tk.Label(self.root, textvariable=self.p8_first_card, height=5, width=8,relief='solid')
            self.p8_2_card_label = tk.Label(self.root, textvariable=self.p8_second_card, height=5, width=8,relief='solid')
            self.p8_money_label = tk.Label(self.root, textvariable=self.p8_money, height=1, width=5,relief='solid')
            self.p8_bet_label = tk.Label(self.root, textvariable=self.p8_bet, height=1, width=5, relief='solid')

            self.p9_name = tk.Label(self.root, text="Player9", font=25)
            self.p9_1_card_label = tk.Label(self.root, textvariable=self.p9_first_card, height=5, width=8,relief='solid')
            self.p9_2_card_label = tk.Label(self.root, textvariable=self.p9_second_card, height=5, width=8,relief='solid')
            self.p9_money_label = tk.Label(self.root, textvariable=self.p9_money, height=1, width=5,relief='solid')
            self.p9_bet_label = tk.Label(self.root, textvariable=self.p9_bet, height=1, width=5, relief='solid')

            self.com_card_label = tk.Label(self.root, text="Community Cards", font=25)
            self.com_card_1_label = tk.Label(self.root, textvariable=self.com_card_1, height=5, width=8, relief='solid')
            self.com_card_2_label = tk.Label(self.root, textvariable=self.com_card_2, height=5, width=8, relief='solid')
            self.com_card_3_label = tk.Label(self.root, textvariable=self.com_card_3, height=5, width=8, relief='solid')
            self.com_card_4_label = tk.Label(self.root, textvariable=self.com_card_4, height=5, width=8, relief='solid')
            self.com_card_5_label = tk.Label(self.root, textvariable=self.com_card_5, height=5, width=8, relief='solid')

            self.position_labels()

    def position_labels(self) -> None:
        """Positions every text/label/entry box to fit in the GUI window. Then it starts the Game.

        Returns: None
        """
        self.bet.place(x=630, y=440)
        self.check.place(x=630, y=480)
        self.fold.place(x=630, y=520)
        self.play_again.place(x=235, y=480)
        self.quit_button.place(x=235,y=520)
        self.bet_amount_entry.place(x=630,y=400)
        self.winner_label.place(x=168, y=400)

        self.p4_name.place(x=190, y=10)
        self.p4_1_card_label.place(x=150, y=40)
        self.p4_2_card_label.place(x=220, y=40)
        self.p4_money_label.place(x=170, y=127)
        self.p4_bet_label.place(x=220,y=127)

        self.p5_name.place(x=438, y=10)
        self.p5_1_card_label.place(x=400, y=40)
        self.p5_2_card_label.place(x=470, y=40)
        self.p5_money_label.place(x=420, y=127)
        self.p5_bet_label.place(x=470,y=127)

        self.p6_name.place(x=686, y=10)
        self.p6_1_card_label.place(x=650, y=40)
        self.p6_2_card_label.place(x=720, y=40)
        self.p6_money_label.place(x=670, y=127)
        self.p6_bet_label.place(x=720,y=127)

        self.p1_name.place(x=70, y=430)
        self.p1_1_card_label.place(x=30, y=460)
        self.p1_2_card_label.place(x=100, y=460)
        self.p1_money_label.place(x=55,y=545)
        self.p1_bet_label.place(x=100,y=545)

        self.p2_name.place(x=70, y=280)
        self.p2_1_card_label.place(x=30, y=310)
        self.p2_2_card_label.place(x=100, y=310)
        self.p2_money_label.place(x=55,y=395)
        self.p2_bet_label.place(x=100, y=395)

        self.p3_name.place(x=68, y=130)
        self.p3_1_card_label.place(x=30, y=160)
        self.p3_2_card_label.place(x=100, y=160)
        self.p3_money_label.place(x=55,y=245)
        self.p3_bet_label.place(x=100,y=245)

        self.p7_name.place(x=820, y=120)
        self.p7_1_card_label.place(x=855, y=150)
        self.p7_2_card_label.place(x=785, y=150)
        self.p7_money_label.place(x=805, y=235)
        self.p7_bet_label.place(x=855,y=235)

        self.p8_name.place(x=820, y=270)
        self.p8_1_card_label.place(x=855, y=300)
        self.p8_2_card_label.place(x=785, y=300)
        self.p8_money_label.place(x=805, y=385)
        self.p8_bet_label.place(x=855,y=385)

        self.p9_name.place(x=820, y=420)
        self.p9_1_card_label.place(x=855, y=450)
        self.p9_2_card_label.place(x=785, y=450)
        self.p9_money_label.place(x=805, y=535)
        self.p9_bet_label.place(x=855,y=535)

        self.user_name.place(x=448, y=380)
        self.user_1_card_label.place(x=390, y=415)
        self.user_2_card_label.place(x=470, y=415)
        self.user_money_label.place(x=420, y=550)
        self.user_bet_label.place(x=470, y=550)

        self.com_card_label.place(x=399, y=180)
        self.com_card_1_label.place(x=295, y=240)
        self.com_card_2_label.place(x=365, y=240)
        self.com_card_3_label.place(x=435, y=240)
        self.com_card_4_label.place(x=505, y=240)
        self.com_card_5_label.place(x=575, y=240)

        self.quit_button["state"] = 'disabled'
        self.play_again["state"] = 'disabled'
        self.start_game()

    def start_game(self) -> None:
        """Starts the first game by initializing the player object instances, the game deck, and community cards. It
        then sets each bot players' cards to '?' and displays each player's money and bets.

        Returns: None
        """
        self.bet["state"] = 'normal'
        self.check["state"] = 'normal'
        self.fold["state"] = 'normal'

        self.game_deck = card_deck()
        self.community = Games()
        self.list_of_players = create_players(self.player_number.get())
        self.list_of_players = initialize_game(self.list_of_players, self.game_deck, self.community)

        count = 0
        pre_bet(self.list_of_players)
        while count < self.player_number.get():
            temp_list = self.player_labels[count]
            temp_list[0].set('?')
            temp_list[1].set('?')
            temp_list[2].set(self.list_of_players[count].money)
            temp_list[3].set(self.list_of_players[count].bet)
            count += 1

        self.user_first_card.set(self.list_of_players[-1].hand[0])
        self.user_second_card.set(self.list_of_players[-1].hand[1])
        self.user_money.set(self.list_of_players[-1].money)

    def player_folds(self) -> None:
        """It disables the player's in game action buttons and calls the function check_round() to act further on the
        fold.

        Returns: None
        """
        self.bet["state"] = 'disabled'
        self.check["state"] = 'disabled'
        self.fold["state"] = 'disabled'
        self.check_round('F')

    def player_bets(self, bet_value) -> None:
        """If the player bets, this function is called upon. It adds the desired bet amount to the user's bets, and
        subtracts it from their current money. It then updates the bet and money display on the GUI. It then calls the
        check_round() function to take futher action.

        Returns: None
        """
        if bet_value > self.list_of_players[-1].money:
            self.bet_amount.set("Too Much")
        else:
            self.list_of_players[-1].bet += bet_value
            self.list_of_players[-1].money -= bet_value

            self.user_bet_amount.set(self.list_of_players[-1].bet)
            self.user_money.set(self.list_of_players[-1].money)
            if self.round_counter < 1:
                self.bet_amount.set("Enter Bet")
            elif self.round_counter == 1:
                self.bet_amount.set("Final Bet!!")
            self.check_round("B")

    def player_checks(self) -> None:
        """If the player checks, their bet is set to 0 and calls the check_round() function.

        Returns: None
        """
        self.list_of_players[-1].bet = 0
        self.check_round('C')

    def plays_again(self) -> None:
        """If the player clicks the play again button. It cycles through the current list of players and finds all the
        bot players who ran out of money and removes them from the list of players. It also removes their respective labels
        from the label list.

        Returns: None
        """
        copy_list = self.list_of_players.copy()
        for player in copy_list:
            player.reset_hand()
            if player.money <= 0:
                copy_labels = self.player_labels.copy()
                self.list_of_players.remove(player)
                id_num = player.player_id
                for id_check in copy_labels:
                    if id_num == id_check[-1]:
                        for label in id_check[:-1]:
                            label.set('')
                        self.player_labels.remove(id_check)
                self.player_number.set(self.player_number.get() - 1)

        self.community.reset_community()
        self.game_deck.setDeck()
        self.list_of_players = initialize_game(self.list_of_players, self.game_deck, self.community)

        self.user_first_card.set(self.list_of_players[-1].hand[0])
        self.user_second_card.set(self.list_of_players[-1].hand[1])
        self.new_game_display()

    def new_game_display(self) -> None:
        """Restarts the display for the bots' cards/bet/money and community cards. It also changes the state of the buttons
        respective to the phase in the game. It disables the quit and play again button so that it cant be pushed during
        the game.

        Returns: None
        """
        count = 0
        pre_bet(self.list_of_players)
        while count < self.player_number.get():
            temp_list = self.player_labels[count]
            temp_list[0].set('?')
            temp_list[1].set('?')
            temp_list[2].set(self.list_of_players[count].money)
            temp_list[3].set(self.list_of_players[count].bet)
            count += 1

        self.bet_amount.set("Enter Amount")
        self.com_card_1.set('')
        self.com_card_2.set('')
        self.com_card_3.set('')
        self.com_card_4.set('')
        self.com_card_5.set('')

        self.bet["state"] = 'normal'
        self.check["state"] = 'normal'
        self.fold["state"] = 'normal'
        self.quit_button["state"] = 'disabled'
        self.play_again["state"] = 'disabled'

    def player_quits(self) -> None:
        """If the player clicks the quit button, the GUI window/root is destroyed and closed.

        Returns: None
        """
        self.root.destroy()

    def check_round(self, move) -> None:
        """After every move, it checks which round it is and calls a function respective to which round it is. If the player's
        action is to fold, it calls all rounds' respective function to skip the betting phases.

        Returns: None
        """
        if self.round_counter == 0:
            if move == 'F':
                self.gui_round_one()
                self.gui_round_two()
                self.gui_round_three('F')
                self.round_counter = 0
            else:
                self.gui_round_one()
                self.round_counter += 1
        elif self.round_counter == 1:
            if move == 'F':
                self.gui_round_two()
                self.gui_round_three('F')
                self.round_counter = 0
            else:
                self.check["state"] = 'disabled'
                self.gui_round_two()
                self.round_counter += 1
        elif self.round_counter == 2:
            if move == 'F':
                self.gui_round_three('F')
                self.round_counter = 0
            else:
                self.check["state"] = 'disabled'
                self.gui_round_three('n')
                self.round_counter = 0

    def gui_round_one(self) -> None:
        """When called, it adds the community cards to each player's hands. It the reveals the first 3 community cards.
        It also ranks each player's hands and makes bets accordingly for each bot. It then calls to update the bet display

        Returns: None
        """
        for player in self.list_of_players:
            for card in self.community.community_cards:
                player.add_cards(card)

        rank_five_cards(self.list_of_players)
        make_bet(self.list_of_players[:-1])
        self.com_card_1.set(self.community.community_cards[0])
        self.com_card_2.set(self.community.community_cards[1])
        self.com_card_3.set(self.community.community_cards[2])
        self.check["state"] = 'disabled'

        self.update_bets()

    def gui_round_two(self) -> None:
        """This function adds two more cards to the community cards, and then adds them to each player's hand, ranks them
        and makes bets according to each bot's ranks. It then updates the visuals for the bets.

        Returns: None
        """
        community_count = 0
        while community_count < 2:
            card = random.choice(self.game_deck.deck)
            self.community.community_cards.append(card)
            self.game_deck.deck.remove(card)
            community_count += 1

        self.com_card_4.set(self.community.community_cards[3])
        self.com_card_5.set(self.community.community_cards[4])

        for player in self.list_of_players:
            for card in self.community.community_cards[3:]:
                player.hand.append(card)

        rank_five_cards(self.list_of_players)
        make_bet(self.list_of_players[:-1])
        self.update_bets()

    def gui_round_three(self, command) -> None:
        """It gathers each player's bets and puts them into the pot. It then gets the winner/winners from each game. It
        updates the winner text label and updates the winner and losers money and bets.

        Returns: None
        """
        self.community.pot = 0
        for player in self.list_of_players:
            self.community.pot += player.bet
        if command == 'F':
            x = get_winner(self.list_of_players[:-1], self.community.pot)
        else:
            x = get_winner(self.list_of_players, self.community.pot)
        winner_str = ''
        for player in x:
            winner_str = winner_str + "P" + str(player.player_id) + ' '
        self.winner.set("Winner/Winners:  " + winner_str)
        count = 0
        while count < self.player_number.get():
            temp_list = self.player_labels[count]
            temp_list[0].set(self.list_of_players[count].hand[0])
            temp_list[1].set(self.list_of_players[count].hand[1])
            temp_list[2].set(self.list_of_players[count].money)
            temp_list[3].set(0)
            count += 1

        self.user_money.set(self.list_of_players[-1].money)
        self.user_bet_amount.set(0)
        self.bet["state"] = 'disabled'
        self.check["state"] = 'disabled'
        self.fold["state"] = 'disabled'
        self.quit_button["state"] = 'normal'
        self.play_again["state"] = 'normal'
        if self.list_of_players[-1].money <= 0:
            self.play_again["state"] = 'disabled'

    def update_bets(self) -> None:
        """After every player move, the function updates the bot players' bet and money label in the GUI

        Returns: None
        """
        count = 0
        while count < self.player_number.get():
            temp_list = self.player_labels[count]
            self.root.after(100)
            temp_list[2].set(self.list_of_players[count].money)
            temp_list[3].set(self.list_of_players[count].bet)
            count += 1


class Player:
    """
    A class to represent a player.

    Attributes:
        player_id (int) = The player's ID Number.
        money (int) = The amount of money a player currently has.
        hand (list) = The hand (cards) of the player.
        rank (int) = The ranking of the current hand.
        bet (int) = The amount the player is currently betting.
        comparison_card (int/str) = The number of the ranked cards. For ex, a 3 of a kind of 5's would return 5 as the num.
        kicker_card (int/str) = The number of the decider unranked card.
    """
    def __init__(self, player_id=0, money=10, hand=None, rank=0, bet=0, comparison_card='', kicker_card=''):
        """
        The constructor for the Player Class.

        Args:
            player_id (int) = The player's ID Number.
            money (int) = The amount of money a player currently has.
            hand (list) = The hand (cards) of the player.
            rank (int) = The ranking of the current hand.
            bet (int) = The amount the player is currently betting.
            comparison_card (int/str) = The number of the ranked cards. For ex, a 3 of a kind of 5's would return 5 as the num.
            kicker_card (int/str) = The number of the decider unranked card.
        """
        if hand is None:
            hand = []
        self.player_id = player_id
        self.money = money
        self.hand = hand
        self.rank = rank
        self.bet = bet
        self.comparison_card = comparison_card
        self.kicker_card = kicker_card

    def add_cards(self, cards) -> None:
        """
        The function to add cards to the player's hand.

        Args:
            cards (str) : the card you wish to add to the player's hand.

        Returns:
            None
        """
        self.hand.append(cards)

    def reset_hand(self) -> None:
        """
        The function to reset the player's hand, rank, bet, cards for a new game.

        Returns:
            None
        """
        self.hand = []
        self.rank = 0
        self.bet = 0
        self.comparison_card = ''
        self.kicker_card = ''


class card_deck:
    """
    This is a class for the card deck being used in the game.

    Attributes:
        deck (list) = The deck of cards.
    """
    def __init__(self, deck = None):
        """
        The constructor for card_deck class.

        Args:
            deck (list) = The deck of cards.
        """
        self.setDeck()

    def setDeck(self) -> None:
        """
        The function to set a new game deck with a full deck

        Returns:
            None
        """
        deck_of_cards = []
        suit_list = ['H', 'D', 'S', 'C']
        for suit in suit_list:
            card_num = 1
            while card_num < 14:
                deck_of_cards.append(str(suit + str(card_num)))
                card_num += 1
        self.deck = deck_of_cards


class Games:
    """
    This is a class for the community cards in each game.

    Attributes:
        community_cards (list) = the cards in the community pile.
    """
    def __init__(self, community_cards = None, pot=0):
        """
        The constructor for Games class.

        Args:
            community_cards (list) = the cards in the community pile.
        """
        if community_cards is None:
            community_cards = []
        self.community_cards = community_cards
        self.pot = 0

    def reset_community(self) -> None:
        """
        The function to reset the community cards for a new game

        Returns:
            None
        """
        self.community_cards = []


def pre_bet(list_of_players) -> None:
    """
    initializes the bets for each bot player by adding setting a hard bet to each of the bots.

    Args:
        list_of_players (list) : list of players

    Returns:
        None
    """
    for player in list_of_players[:-1]:
        player.bet += 1
        player.money -= 1


def rank_five_cards(list_of_players) -> None:
    """
    Ranks each player's hand and gives them a ranking from 0-9 based on their hand. 0 being the best and 9 being the worst

    Args:
        list_of_players (list) : list of players


    Returns:
        None
    """
    for player in list_of_players:
        if royal_flush(player):
            player.rank = 0
        elif straight_flush(player):
            player.rank = 1
        elif four_kind(player):
            player.rank = 2
        elif full_house(player):
            player.rank = 3
        elif flush(player):
            player.rank = 4
        elif straight(player):
            player.rank = 5
        elif three_kind(player):
            player.rank = 6
        elif two_pair(player):
            player.rank = 7
        elif pair(player):
            player.rank = 8
        elif high_card(player):
            player.rank = 9


def royal_flush(player) -> bool:
    """
    Checks if a player's hand is a royal flush

    checks if the hand contains 10-13 and 1, then compares each of those number's suit. If the suit is the same, then
    there is a royal flush

    Args:
        player : the player instance

    Returns:
        True if the hand is a royal flush and false if it not.
    """
    card_suits = list(map(lambda card: card[0], player.hand))
    unique_suits = []
    same_suit = False
    for suit in card_suits:
        if suit not in unique_suits:
            unique_suits.append(suit)

    final_suit = list(filter((lambda x: card_suits.count(x) >= 5), unique_suits))

    if len(final_suit) == 1:
        same_suit = True

    if same_suit:
        check_royal_flush = list(filter((lambda x: x[0] == final_suit[0]), player.hand))
        check_nums = list(map(lambda x: int(x[1:]), check_royal_flush))
        check_nums.sort()
        if [1, 10, 11, 12, 13] == check_nums:
            return True
        else:
            return False
    else:
        return False


def straight_flush(player) -> bool:
    """
    Checks if a player has a straight flush

    checks if it is a straight by comparing if there is a consecutive group of 5 numbers. Then checks if they are all the
    same suit.

    Args:
        player : player instance

    Returns:
        True if the hand is a straight flush and false if not
    """
    card_suits = list(map(lambda card: card[0], player.hand))

    unique_suits = []
    same_suit = False
    for suit in card_suits:
        if suit not in unique_suits:
            unique_suits.append(suit)

    final_suit = list(filter((lambda x: card_suits.count(x) >= 5), unique_suits))

    if len(final_suit) == 1:
        same_suit_cards = list(filter(lambda card: card[0] == final_suit[0], player.hand))
        same_suit = True

    if same_suit:
        return straight(player, same_suit_cards)


def four_kind(player) -> bool:
    """
    Checks if a hand contains four of a kind by checking if there is a number that repeats itself 4 times in a hand.

    Args:
        player: player instance

    Returns:
        True if the hand is a four of a kind, false if not
    """
    card_nums = list(map(lambda card: int(card[1:]), player.hand))
    four_nums = list(filter(lambda num: card_nums.count(num) == 4, card_nums))

    if len(four_nums) == 4:
        player.comparison_card = four_nums[0]
        return True
    else:
        return False


def full_house(player) -> bool:
    """
    Checks if a hand is a full house

    checks if there is a group of 3 same cards, and a group of 2 same cards. If there is both, it is a full house.

    Args:
        player: player instance

    Returns:
        True if it is a full house, false if not
    """

    card_nums = list(map(lambda card: int(card[1:]), player.hand))
    three_group = list(filter(lambda num: card_nums.count(num) == 3, card_nums))
    two_group = list(filter(lambda num: card_nums.count(num) == 2, card_nums))

    if len(three_group) == 3 and len(two_group) >= 2:
        player.comparison_card = three_group[0]
        return True
    else:
        return False


def flush(player) -> bool:
    """
    Checks if a hand is a Flush

    checks if there is a group of 5 or more cards with the same suit

    Args:
        player: player instance

    Returns:
        True if it is a flush, false if not
    """

    card_suits = list(map(lambda card: card[0], player.hand))

    unique_suits = []
    same_suit = False
    for suit in card_suits:
        if suit not in unique_suits:
            unique_suits.append(suit)

    final_suit = list(filter((lambda x: card_suits.count(x) >= 5), unique_suits))

    if len(final_suit) == 1:
        same_suit = True

    if same_suit:
        flush_cards = list(filter(lambda card: card[0] in final_suit, player.hand))
        flush_nums = list(map(lambda card: int(card[1:]), flush_cards))
        flush_nums.sort()
        if 1 in flush_nums:
            player.comparison_card = 1
        else:
            player.comparison_card = flush_nums[-1]
        return True


def straight(player, player_hand = None) -> bool:
    """
    Checks if a hand is a straight

    checks if there is a group of 5 consecutive cards.

    Args:
        player: player instance
        player_hand : the player's hand

    Returns:
        True if it is a straight false if not
    """

    if player_hand is None:
        player_hand = player.hand

    card_nums = list(map(lambda card: int(card[1:]), player_hand))
    card_nums.sort()
    straight_cards_check = list(filter(lambda num: card_nums[card_nums.index(num) - 1] == num - 1 and card_nums[card_nums.index(num) + 1] == num + 1, card_nums[1:-1]))

    if straight_cards_check:
        straight_cards_check.append(straight_cards_check[0] - 1)
        straight_cards_check.append(straight_cards_check[-2] + 1)
    if len(straight_cards_check) == 5 and straight_cards_check != [2, 3, 4, 1, 5]:
        copy_list = straight_cards_check.copy()
        copy_list.sort()
        counter = 1
        check = True
        for num in copy_list[0:-1]:
            if num + 1 != copy_list[counter]:
                check = False
                break
            counter += 1
        if check is not False:
            player.comparison_card = straight_cards_check[-1]
            return True
    elif straight_cards_check == [11, 12, 10, 13] and 1 in card_nums:
        player.comparison_card = 1
        return True
    else:
        return False


def three_kind(player) -> bool:
    """
    Checks if a hand is a three of a kind by checking if there is a group of 3 same cards.

    Args:
        player: player instance

    Returns:
        True if it is a three of a kind, false if not
    """

    card_nums = list(map(lambda card: int(card[1:]), player.hand))
    three_group = list(filter(lambda num: card_nums.count(num) == 3, card_nums))

    if three_group:
        player.comparison_card = three_group[0]
        return True
    else:
        return False


def two_pair(player) -> bool:
    """
    Checks if a hand is a two pair

    checks if there are 2 groups of 2 of the same cards.

    Args:
        player: player instance

    Returns:
        True if it is a two pair, false if not
    """

    card_nums = list(map(lambda card: int(card[1:]), player.hand))
    pair_group = list(filter(lambda num: card_nums.count(num) == 2, card_nums))

    if len(pair_group) >= 4:
        pair_group.sort()
        if 1 in pair_group:
            player.comparison_card = 1
            player.kicker_card = pair_group[-1]
        else:
            player.comparison_card = pair_group[-1]
            player.kicker_card = pair_group[0]
        return True
    else:
        return False


def pair(player) -> bool:
    """
    Checks if a hand is a pair

    checks if there is a group of 2 same cards.

    Args:
        player: player instance

    Returns:
        True if it is a pair, false if not
    """

    card_nums = list(map(lambda card: int(card[1:]), player.hand))
    pair_group = list(filter(lambda num: card_nums.count(num) == 2, card_nums))
    non_pairs = list(filter(lambda num: card_nums.count(num) != 2, card_nums))
    non_pairs.sort()

    if len(pair_group) >= 2:
        if 1 in pair_group:
            player.comparison_card = 1
        else:
            player.comparison_card = pair_group[0]

        if 1 in non_pairs:
            player.kicker_card = 1
        else:
            player.kicker_card = non_pairs[-1]
        return True
    else:
        return False


def high_card(player) -> bool:
    """
    Identifies the highest ranking card in the player's hand

    Args:
        player: player instance

    Returns:
        True if it is a high card, false if not.
    """

    card_nums = list(map(lambda card: int(card[1:]), player.hand))
    card_nums.sort()

    if 1 in card_nums:
        player.comparison_card = 1
    else:
        player.comparison_card = card_nums[-1]
    return True


def get_winner(list_of_players, pot):
    """
    Finds the winner between each player for each game

    Orders each player based on their ranking and deciding whether or not a tie breaker is needed. If needed, it calls
    a tie-breaker function on two+ players who are tied, and it not, it returns a single winner

    Args:
        list_of_players (list) : list of player instances

    Returns:
        player : the winner
    """
    rank_counter = -1
    winner_list = []

    while len(winner_list) == 0:
        for player in list_of_players:
            if player.rank == rank_counter + 1:
                winner_list.append(player)
        rank_counter += 1

    if len(winner_list) == 1:
        print("Winner:", winner_list[0].player_id)
        winner_list[0].money += pot
        return winner_list
    else:
        winners = tie_breaker(winner_list, rank_counter)
        if len(winners) > 1:
            pot = round(pot/len(winners), 2)
        for player in winners:
            player.money += pot
            print("Winner: Player", player.player_id)
        return winners


def initialize_game(list_of_players, game_deck, community) -> list:
    """
    Initializes the Game.

    Adds 2 random cards (no repeats) to each player's hands and the community cards

    Args:
        list_of_players (list) : list of players
        game_deck (instance) : the deck of cards instance
        community (instance) : the community cards instance

    Returns:
        list of player instances
    """
    for player in list_of_players:
        cards_added = 0
        while cards_added < 2:
            card = random.choice(game_deck.deck)
            player.add_cards(card)
            game_deck.deck.remove(card)
            cards_added += 1

    community_count = 0
    while community_count < 3:
        card = random.choice(game_deck.deck)
        community.community_cards.append(card)
        game_deck.deck.remove(card)
        community_count += 1

    return list_of_players


def print_hands(list_of_players, community) -> None:
    """
    Prints the hands and community card of the current game

    Args:
        list_of_players (list) : list of players
        community (class instance) : the community card instance

    Returns:
        None
    """
    for player in list_of_players:
        print("Player", str(player.player_id) + ":", player.hand[:2], "Player Rank:", player.rank)
    print("Community Cards:", community.community_cards)


def print_players(list_of_players) -> None:
    """
    Prints all players' id, rank, and bet

    Args:
        list_of_players (list) : list of players

    Returns:
        None
    """
    for player in list_of_players:
        print('Player', str(player.player_id) + ' Total Bet $' + str(player.bet))


def make_bet(list_of_players) -> None:
    """
    Makes a bet for each player based on their current ranking

    Args:
        list_of_players (list) : list of player instances

    Returns:
        None
    """
    for player in list_of_players:
        if player.money == 0:
            pass
        elif player.rank == 8 or player.rank == 9:
            if player.money < 1:
                player.bet += player.money
                player.money = 0
            else:
                player.money -= 1
                player.bet += 1
        elif player.rank == 7 or player.rank == 6:
            if player.money < 2:
                player.money -= player.money
                player.bet = 0
            else:
                player.money -= 2
                player.bet += 2
        elif player.rank == 5 or player.rank == 4:
            if player.money < 3:
                player.bet += player.money
                player.money = 0
            else:
                player.money -= 3
                player.bet += 3
        elif player.rank == 3 or player.rank == 2:
            if player.money < 4:
                player.bet += player.money
                player.money = 0
            else:
                player.money -= 4
                player.bet += 4
        elif player.rank == 1 or player.rank == 0:
            if player.money < 5:
                player.bet += player.money
                player.money = 0
            else:
                player.money -= 5
                player.bet += 5


def create_players(player_num) -> list:
    """
    Creates players based on how many people the user requests

    Args:
        player_num (int) : the number of players

    Returns:
        list of player instances
    """
    player_list = list(map(lambda x: Player(x), range(1, player_num+1)))
    player_list.append(Player("User"))
    return player_list


def tie_breaker(tie_list, rank_counter) -> list:
    """
    Calls a specific tie-breaker function based on the tied players' rankings

    Args:
        tie_list (list) : A list of tied players who have the same ranking. ex, [player1 has straight, player2 has straight]
        rank_counter (list) : the number for which rank the players' are tied at

    Returns:
        list : list of winner/winners
    """
    one_comparisons = [2, 3, 4, 6]
    if rank_counter == 0:
        return tie_list
    elif rank_counter == 1 or rank_counter == 5:
        return straight_tie(tie_list)
    elif rank_counter in one_comparisons:
        return one_compare_tie(tie_list)
    elif rank_counter == 7 or rank_counter == 8:
        return pair_ties(tie_list)
    elif rank_counter == 9:
        return high_tie(tie_list)


def high_tie(tie_list) -> list:
    """
    Checks to see who the winner is between players who have no combinations so the highest card is compared.

    Args:
        tie_list (list) : A list of players who are tied in ranking

    Returns:
        list : a list of winners
    """
    players_hands = {}
    benchmark_compare = []
    hold_winners = []
    final_winners = []

    for player in tie_list:
        hand = []
        for card in player.hand:
            hand.append(int(card[1:]))
            benchmark_compare.append(int(card[1:]))
        players_hands[player.player_id] = sorted(hand)

    benchmark = players_hands[tie_list[0].player_id]
    for num in benchmark:
        if benchmark_compare.count(num) > 1:
            while benchmark_compare.count(num) != 0:
                benchmark_compare.remove(num)

    benchmark_compare.sort()
    if 1 not in benchmark_compare:
        for player in players_hands:
            if benchmark_compare[-1] in players_hands[player]:
                hold_winners.append(player)
    else:
        for player in players_hands:
            if 1 in players_hands[player]:
                hold_winners.append(player)

    for player in tie_list:
        if player.player_id in hold_winners:
            final_winners.append(player)

    return final_winners


def pair_ties(tie_list) -> list:
    """
    Checks to see who the winner is between players who have two pair or pair

    Args:
        tie_list (list) : A list of players who are tied in ranking

    Returns:
        list : a list of winners
    """
    compare_card = list(map(lambda player: player.comparison_card, tie_list))
    compare_card.sort()
    if 1 in compare_card:
        compared_players = list(filter(lambda player: player.comparison_card == 1, tie_list))
    else:
        compared_players = list(filter(lambda player: player.comparison_card == compare_card[-1], tie_list))

    compare_kicker = list(map(lambda player: player.kicker_card, tie_list))
    compare_kicker.sort()

    if len(compared_players) == 1:
        return compared_players
    else:
        if 1 in compare_kicker:
            compared_players = list(filter(lambda player: player.kicker_card == 1, tie_list))
        else:
            compared_players = list(filter(lambda player: player.kicker_card == compare_kicker[-1], tie_list))
        return compared_players


def one_compare_tie(tie_list) -> list:
    """
    Compares people who are tied for four of a kind, full house, flush, three of a kind, or highcard

    Compares and finalizes a winner between people who have a tie rank. This compares ranks who only need 1 card to be
    compared without comparing a kicker card. The highest card wins, but if they have the same cards, it is a tie.

    Args:
        tie_list (list) : list of players who are tied.

    Returns:
        list = returns a list of the highest ranking person
    """
    compare_card = list(map(lambda player: player.comparison_card, tie_list))
    compare_card.sort()
    if 1 in compare_card:
        final_winner = list(filter((lambda player: player.comparison_card == 1), tie_list))
    else:
        final_winner = list(filter((lambda player: player.comparison_card == compare_card[-1]), tie_list))

    return final_winner


def straight_tie(tie_list) -> list:
    """
    Compares ties for straight flush and straight

    Compares the highest card of the straight and whichever player has the highest card wins

    Args:
        tie_list (list) : List of tied players

    Returns:
        list : returns a list of winners
    """
    compare_card = []
    for player in tie_list:
        compare_card.append(player.comparison_card)
    compare_card.sort()
    final_winner = list(filter((lambda player: player.comparison_card == compare_card[-1]), tie_list))
    return final_winner


def main() -> None:
    """
    Initiates the User Interface for Texas Holdem

    Returns:
        None
    """
    TH = Gui()


if __name__ == '__main__':
    main()
