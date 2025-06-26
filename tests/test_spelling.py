from assignments.spelling import spell_check


def test_spelling_1() -> None:
    text: str = '''
    welcome to ou really good water park
    '''.strip()

    correct: str = '''
    welcome to our really good water park
    '''.strip()
    assert spell_check(text) == correct


def test_spelling_2() -> None:
    text: str = '''
    sametimes I sonder howw coool the technilogy could be
    '''.strip()

    correct: str = '''
    sometimes I wonder how cool the technology could be
    '''.strip()
    assert spell_check(text) == correct


def test_spelling_3() -> None:
    text: str = '''
    wen king ordered his troops to attak nights declind his orderss
    '''.strip()

    correct: str = '''
    when king ordered his troops to attack knights declined his orders
    '''.strip()
    assert spell_check(text) == correct
