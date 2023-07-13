# В модуле написать тесты для встроенных функций filter, map, sorted,
# а также для функций из библиотеки math: pi, sqrt, pow, hypot. Чем больше тестов на каждую функцию - тем лучше
import math

def is_even(x):
    return x % 2 == 0

def test_filter():
    numbers = range(10)

    # Тестирование фильтрации только четных чисел
    chet_numbers = list(filter(is_even, numbers))
    assert chet_numbers == [0, 2, 4, 6, 8]

    # Тестирование фильтрации только нечетных чисел
    nechet_numbers = list(filter(lambda x: not is_even(x), numbers))
    assert nechet_numbers == [1, 3, 5, 7, 9]

    # Тестирование пустого списка после фильтрации
    empty_list = list(filter(is_even, []))
    assert empty_list == []


def test_pi_value():
    assert math.isclose(math.pi, 3.141592653589793, rel_tol=1e-9)

def test_pi_type():
    assert isinstance(math.pi, float)

def test_pi_greater_than_three():
    assert math.pi > 3

def test_sqrt_positive_number():
    assert math.sqrt(4) == 2

def test_sqrt_zero():
    assert math.sqrt(0) == 0

def test_hypot():
    # Тестирование положительных значений
    assert math.hypot(3, 4) == 5.0
    assert math.hypot(5, 12) == 13.0

    # Тестирование нулевых значений
    assert math.hypot(0, 0) == 0.0

    # Тестирование отрицательных значений
    assert math.hypot(-3, -4) == 5.0
    assert math.hypot(-5, -12) == 13.0

    # Тестирование комбинации положительных и отрицательных значений
    assert math.hypot(3, -4) == 5.0

    # Тестирование значений с плавающей точкой
    assert math.isclose(math.hypot(1.2, 2.4), 2.664583, abs_tol=1e-6)

    # Тестирование больших значений
    assert math.hypot(1e100, 1e100) == 1.414213562373095e+100



