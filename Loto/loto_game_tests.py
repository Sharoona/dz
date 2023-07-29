import pytest
from loto_game import Player, LottoGame


@pytest.fixture
def players():
    player = Player('Игрок')
    computer = Player('Компьютер')
    return player, computer

def test_generate_card(players):
    player, computer = players
    player.generate_card()
    computer.generate_card()
    assert len(player.card) == 15
    assert len(computer.card) == 15

def test_mark_number(players):
    player, computer = players
    player.card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert player.mark_number(8) is True
    assert player.card == [1, 2, 3, 4, 5, 6, 7, 'X', 9, 10, 11, 12, 13, 14, 15]

    assert player.mark_number(20) is False
    assert player.card == [1, 2, 3, 4, 5, 6, 7, 'X', 9, 10, 11, 12, 13, 14, 15]

def test_draw_number():
    lotto_game = LottoGame()
    assert isinstance(lotto_game.draw_number(), int)

def test_display_card(capsys):
    player = Player('Игрок')
    player.card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    player.display_card()

    captured = capsys.readouterr()
    expected_output = "Игрока карточка:\n[1, 2, 3, 4, 5]\n[6, 7, 8, 9, 10]\n[11, 12, 13, 14, 15]\n"
    assert captured.out == expected_output





