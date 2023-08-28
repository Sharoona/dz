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
            self.card[self.card.index(number)] = 'x'
            return True  # Число найдено и отмечено
        return False  # Число не найдено

    def is_winner(self):
        return 'x' not in self.card

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.name == other.name and self.card == other.card
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

class Lottogame:
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
                marked_player = self.player.mark_number(number)
                marked_computer = self.computer.mark_number(number)
                if marked_player:
                    print("Число отмечено успешно.")
                    if self.player.is_winner():
                        self.winner = self.player
                else:
                    print("Такого числа нет на вашей карточке. Вы проиграли!")
                    self.winner = self.computer
            elif user_choice.lower() == 'нет':
                marked_computer = self.computer.mark_number(number)
                if marked_computer:
                    print("Это число есть на карточке компьютера.")
                else:
                    print("Такого числа нет ни на вашей карточке, ни на карточке компьютера.")
    def __eq__(self, other):
        if isinstance(other, Lottogame):
            return self.player == other.player and self.computer == other.computer and self.numbers == other.numbers and self.winner == other.winner
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def draw_number(self):
        return self.numbers.pop()

    def announce_winner(self):
        print("Конец игры!")
        print(f"Победитель: {self.winner}")

    def __str__(self):
        return "Лотоигра"



# Старт игры
if __name__ == "__main__":
    game = Lottogame()
    game.start_game()
    game.announce_winner()