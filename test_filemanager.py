from victory1 import get_random_ppl_names, get_date_str
import random

def test_get_random_ppl_names():
    result = get_random_ppl_names()
    assert len(result) == 5

def test_get_date_str():
    data = '06.06.1799'
    expected_str_date = 'шестое июня 1799 года'
    assert get_date_str(data) == expected_str_date