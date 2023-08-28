import pytest
from loto_game import Player, Lottogame

@pytest.fixture
def player():
    return Player('Игрок')

@pytest.fixture
def computer():
    return Player('Компьютер')

@pytest.fixture
def lottogame(player, computer):
    game = Lottogame()
    game.player = player
    game.computer = computer
    return game

def test_player_mark_number(player):
    player.card = [1, 2, 3, 4, 5]
    assert player.mark_number(3) == True
    assert player.card == [1, 2, 'x', 4, 5]

def test_player_mark_number_not_found(player):
    player.card = [1, 2, 3, 4, 5]
    assert player.mark_number(6) == False
    assert player.card == [1, 2, 3, 4, 5]

def test_player_is_winner(player):
    player.card = ['x', 'x', 'x', 'x', 'x']
    assert player.is_winner() == True

def test_player_is_not_winner(player):
    player.card = [1, 2, 3, 4, 5]
    assert player.is_winner() == False

def test_lottogame_draw_number(lottogame):
    lottogame.numbers = [1, 2, 3, 4, 5]
    assert lottogame.draw_number() == 5
    assert lottogame.numbers == [1, 2, 3, 4]

# Пример теста для обработки варианта ответа "нет"
def test_lottogame_process_no_marked_number(capsys, lottogame):
    lottogame.computer.card = [5, 6, 7, 8, 9]
    lottogame.process_no_marked_number(3)
    captured = capsys.readouterr()
    assert "Такого числа нет ни на вашей карточке, ни на карточке компьютера." in captured.out

# Пример теста для обработки варианта ответа "да"
def test_lottogame_process_player_choice(capsys, lottogame):
    lottogame.player.card = [3, 4, 5, 6, 7]
    lottogame.computer.card = [8, 9, 10, 11, 12]
    lottogame.process_player_choice(5)
    captured = capsys.readouterr()
    assert "Число отмечено успешно." in captured.out

# Пример теста для обработки выигрыша
def test_lottogame_start_game_winner(capsys, lottogame, mocker):
    mocker.patch('random.shuffle')
    mocker.patch('builtins.input', side_effect=['да', 'нет'])
    lottogame.player.card = ['x', 'x', 'x', 'x', 'x']
    lottogame.start_game()
    captured = capsys.readouterr()
    assert "Победитель: Игрок" in captured.out

# Пример теста для обработки проигрыша
def test_lottogame_start_game_loser(capsys, lottogame, mocker):
    mocker.patch('random.shuffle')
    mocker.patch('builtins.input', side_effect=['нет', 'да'])
    lottogame.player.card = [1, 2, 3, 4, 5]
    lottogame.computer.card = ['x', 'x', 'x', 'x', 'x']
    lottogame.start_game()
    captured = capsys.readouterr()
    assert "Победитель: Компьютер" in captured.out