import random

class Cell:
    def __init__(self, number):
        self.number = number
        self.state_cell = False
        self.sym = ' '

class Board:
    def __init__(self):
        self.board = [Cell(i) for i in range(1, 10)]

    def change_sate_cell(self, number, symbol):
        cell = self.board[number - 1]
        if not cell.state_cell:
            cell.sym = symbol
            cell.state_cell = True
            return True
        else:
            print("Ошибка: Клетка занята, попробуйте другую клетку")
            return False


    def display(self):
        print()
        for i in range(0, 9, 3):
            row = [cell.sym for cell in self.board[i:i+3]]
            print(f" {row[0]} | {row[1]} | {row[2]} ")
            if i < 6:
                print("---|---|---")
        print()

    def check_end_game(self):
        for i in range(0, 9, 3):
            row = self.board[i:i + 3]
            if row[0].sym == row[1].sym == row[2].sym == 'x':
                print("Победили крестики!")
                return True
            elif row[0].sym == row[1].sym == row[2].sym == 'o':
                print("Победили нолики!")
                return True

        if self.board[0].sym == self.board[3].sym == self.board[6].sym != ' ':
            print(f"Победили {'крестики' if self.board[0].sym == 'x' else 'нолики'}!")
            return True
        if self.board[1].sym == self.board[4].sym == self.board[7].sym != ' ':
            print(f"Победили {'крестики' if self.board[1].sym == 'x' else 'нолики'}!")
            return True
        if self.board[2].sym == self.board[5].sym == self.board[8].sym != ' ':
            print(f"Победили {'крестики' if self.board[2].sym == 'x' else 'нолики'}!")
            return True

        if self.board[0].sym == self.board[4].sym == self.board[8].sym != ' ':
            print(f"Победили {'крестики' if self.board[0].sym == 'x' else 'нолики'}!")
            return True

        if self.board[2].sym == self.board[4].sym == self.board[6].sym != ' ':
            print(f"Победили {'крестики' if self.board[2].sym == 'x' else 'нолики'}!")
            return True

        if all(cell.sym != ' ' for cell in self.board):
            print("Ничья!")
            return True
        return False

class Player:
    def __init__(self, name):
        self.name = name
        self.class_game = ''
        self.quantity_wins = 0

    def make_move(self, board):
        while True:
            try:
                move = int(input(f"\n{self.name}, введите номер клетки (1–9): "))
                if 1 <= move <= 9:
                    if board.change_sate_cell(move, self.class_game):
                        break

                else:
                    print("Введите число от 1 до 9.")
            except ValueError:
                print("Введите число.")
        board.display()

class Game:
    def __init__(self, player1, player2, board):
        self.state_game = board.check_end_game()
        self.gamers = [player1, player2]
        self.board = board

    def single_move(self):
        self.gamers[0].make_move(self.board)
        return self.state_game

    def one_game(self):
        flag_move = True
        while not self.board.check_end_game():
            if flag_move:
                self.gamers[0].make_move(self.board)
                flag_move = False
            else:
                self.gamers[1].make_move(self.board)
                flag_move = True

    def main_game(self):
        while True:
            self.board = Board()
            flag_move = True
            last_move = None
            while not self.board.check_end_game():
                if flag_move:
                    self.gamers[0].make_move(self.board)
                    last_move = self.gamers[0]
                    flag_move = False
                else:
                    self.gamers[1].make_move(self.board)
                    last_move = self.gamers[1]
                    flag_move = True

            if last_move == self.gamers[0]:
                self.gamers[0].quantity_wins += 1
            else:
                self.gamers[1].quantity_wins += 1

            print(f"\nСчет: ({self.gamers[1].name}) {self.gamers[1].quantity_wins} : {self.gamers[0].quantity_wins} ({self.gamers[0].name})")
            check_end = int(input("\nРеванш? 1-да 0-нет: "))
            if check_end == 1:
                continue
            else:
                break

print("Начало игры!")
board = Board()
board.display()

player_1 = Player('Костя')
player_2 = Player('Ваня')

x_or_o = random.choice(['x', 'o'])
player_1.class_game = x_or_o
if player_1.class_game == 'x':
    print(f"Игрок {player_1.name} играет за крестики")
    player_2.class_game = 'o'
    print(f"Игрок {player_2.name} играет за нолики")
else:
    player_2.class_game = 'x'
    print(f"Игрок {player_1.name} играет за нолики")
    print(f"Игрок {player_2.name} играет за крестики")

game = Game(player_1, player_2, board)
game.main_game()



