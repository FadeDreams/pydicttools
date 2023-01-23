from pydictutils.pydictutils import *
import asyncio
import pytest

def test_concat_dict():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    expected_output = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert concat_dict(dict1, dict2) == expected_output

def test_key_exists():
    dict1 = {'a': 1, 'b': 2}
    assert key_exists(dict1, 'a') == True
    assert key_exists(dict1, 'c') == False

def test_value_exists():
    dict1 = {'a': 1, 'b': 2}
    assert value_exists(dict1, 1) == True
    assert value_exists(dict1, 3) == False

def test_clone():
    dict1 = {'a': 1, 'b': 2}
    assert clone(dict1) == dict1

def test_is_empty():
    dict1 = {'a': 1, 'b': 2}
    assert is_empty(dict1) == False

def test_get_value_from_dict():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': {'b': {'c': 'value1'}}}
    assert get_value_from_dict(dict1, 'a') == 1
    assert get_value_from_dict(dict1, 'c') == None
    assert get_value_from_dict(dict2, 'a.b.c') == 'value1'

    
def test_is_subset():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 1, 'b': 2, 'c': 3}
    assert is_subset(dict1, dict2) == True
    assert is_subset(dict2, dict1) == False

def test_sort_dict_by_key():
    dict1 = {"c": 3, "a": 1, "b": 2}
    expected_output = {'a': 1, 'b': 2, 'c': 3}
    assert sort_dict_by_key(dict1) == expected_output

def extract_value(key: str, value: int) -> int:
    return value

def test_sort_dict_by_custom_key():
    my_dict = {'a': 3, 'b': 1, 'c': 2}

    expected_output = {'b': 1, 'c': 2, 'a': 3}
    assert sort_dict_by_custom_key(my_dict, extract_value) == expected_output

def test_iterate_dict():
    my_dict = {'a': 3, 'b': 1, 'c': 2}
    expected_output = [('a', 3), ('b', 1), ('c', 2)]
    assert list(iterate_dict(my_dict)) == expected_output

# @pytest.mark.asyncio
# async def test_clone_async():
    # # original object to be cloned
    # original = {
            # "a": 1,
            # "b": [2, 3, 4],
            # "c": {"d": 5, "e": 6}
            # }
    # async with asyncio.get_event_loop() as loop:
        # task = asyncio.create_task(clone(original))
        # cloned = await task
        # loop.run_until_complete(task)
    # assert cloned == original

@pytest.mark.asyncio
async def test_clone_async():
    # original object to be cloned
    original = {
            "a": 1,
            "b": [2, 3, 4],
            "c": {"d": 5, "e": 6}
            }
    cloned = await clone_async(original)
    assert cloned == original
