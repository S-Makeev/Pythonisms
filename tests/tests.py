import time
from decorator import timing_decorator
from dunder import MyList
from generator import even_numbers_generator

def test_timing_decorator(capsys):
    @timing_decorator
    def slow_function():
        time.sleep(2)
    
    slow_function()
    captured_output = capsys.readouterr().out
    assert "Function 'slow_function' took" in captured_output


def test_my_list_length():
    my_list = MyList([1, 2, 3, 4, 5])
    assert len(my_list) == 5

    my_list = MyList([])
    assert len(my_list) == 0


def test_even_numbers_generator():
    evens = even_numbers_generator(10)
    generated_nums = list(evens)
    assert generated_nums == [2, 4, 6, 8, 10]

    evens = even_numbers_generator(20)
    generated_nums = list(evens)
    assert generated_nums == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
