import difflib
from pathlib import Path

# IGNORE
BASE_DIR = Path(__file__).resolve().parent
with open(BASE_DIR / 'english_words.txt') as f:
    words: list[str] = f.read().split('\n')


def similarity(str1, str2) -> float:
    return difflib.SequenceMatcher(None, str1, str2).ratio() * 100


# IGNORE


# WORK HERE
def spell_check(text: str) -> str:
    pass

# WORK HERE
