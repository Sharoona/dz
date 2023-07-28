import random


class Player:
    def __init__(self, name):
        self.name = name
        self.card = []

    def generate_card(self):
        self.card = random.sample(range(1, 91), 15)

    def display_card(self):
        print(f"{self.name}а карточка:")
        for i in range(0, len(self.card), 5):
            print(self.card[i:i + 5])

    def mark_number(self, number):
        if number in self.card:
            self.card[self.card.index(number)] = 'X'
            return True  # Число найдено и отмечено
        return False  # Число не найдено

    def is_winner(self):
        return 'X' not in self.card


class LottoGame:
    def __init__(self):
        self.player = Player('Игрок')
        self.computer = Player('Компьютер')
        self.numbers = list(range(1, 91))
        self.winner = None

    def start_game(self):
        random.shuffle(self.numbers)
        self.player.generate_card()
        self.computer.generate_card()
        self.winner = None

        while not self.winner:
            number = self.draw_number()
            print("Следующий бочонок:", number)
            self.player.display_card()
            self.computer.display_card()

            user_choice = input("Вы хотите отметить это число на карточке? (да/нет): ")
            if user_choice.lower() == 'да':
                marked = self.player.mark_number(number)
                if marked:
                    print("Число отмечено успешно.")
                    if self.player.is_winner():
                        self.winner = self.player.name
                        break
                else:
                    print("Такого числа нет на вашей карточке. Вы проиграли!")
                    self.winner = self.computer.name
                    break
            else:
                marked = self.player.mark_number(number)
                if marked:
                    print("Это число есть на вашей карточке. Вы проиграли!")
                    self.winner = self.computer.name
                    break

    def draw_number(self):
        return self.numbers.pop()

    def announce_winner(self):
        print("Конец игры!")
        print(f"Победитель: {self.winner}")


# Старт игры
game = LottoGame()
game.start_game()
game.announce_winner()