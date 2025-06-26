import random
import string

from assignments.search import find_element


def generate_random_list(size: int = 100) -> list[int]:
    return [
        random.randint(-100, 100)
        for _ in range(size)
    ]


def generate_random_list_str(size: int = 100) -> list[str]:
    words: list[str] = [
        ''.join(random.sample(string.ascii_letters, random.randint(5, 30)))
        for _ in range(30)
    ]

    return random.choices(words, k=100)


def test_search() -> None:
    random_list: list[int] = generate_random_list()

    for element in random_list:
        assert find_element(element, random_list) == random_list.index(element)


def test_non_existing_element() -> None:
    random_list: list[int] = generate_random_list()

    assert find_element(101, random_list) == -1


def test_strings() -> None:
    random_list: list[str] = generate_random_list_str()

    for element in random_list:
        assert find_element(element, random_list) == random_list.index(element)


def test_strings_non_existing_element() -> None:
    random_list: list[str] = generate_random_list_str()

    assert find_element('', random_list) == -1
