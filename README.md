## Assignments

In assignments directory some code is written and you have to add stuff in them.

Assignments are given below **(click on highlighted text)**:

1. [Search](#search)
2. [Mysterious Man](#mysterious-man)
3. [Spell Check](#spell-check)

---

### Search

Define function that finds element in list.

don't use existing methods for list such as: ```list.index()```.

function should be without a side effect **(your code should not modify original list)**.

```find_element``` Function takes 2 parameters:

1. ```element``` - search element.
2. ```search_in``` - list in which this element should exist.

function should return index of the element.

if element is not present in list return ```-1```.

your function should wor on ```any``` data type

[Write you code here](./assignments/search.py)

---

### Mysterious Man

There is a Mysterious man in a room and you have to find him!
You are somewhere in a room you have to find a mysterious man and say what is the least steps to take to reach this man
from your position.
you don't know the length and content of the room, so you cannot:

- use search functions, such as ```list.index()``` and your implemented ```find_element()```

you uncover the room as you move through it.

you know your position.
function ```mysterious_man``` takes two parameters:

1. ```room``` - that is list of strings
2. ```your_position``` - that is an index of your position

from your position you can either move left or right.

- mysterious man is represented by string that is emoji ```'😒'```
- Empty space is represented by an empy string ```''```

**NOTE**

mysterious man can be in the same position as you, so don't forget to check that too!

find the man and return how many steps it took you to find him
**(try to find him as fast as you can, but ensure your algorithm works for every possible input)**

[Write you code here](./assignments/mysterious_man.py)

---

### Spell Check

Implement a function that checks a text and returns corrected text.
there is a list of words (that is taken from file ```english_words.txt```, you can ignore this part),
first of all implement a function that finds closest ```word``` in ```words``` list to passed ```word```
you have to define a function called ```find_closest``` that will take 1 parameter and return 1 closest word to it:

1. ```word``` - find the closest word to this word from words list, use ```similarity``` function to determine how
   similar are words

```similarity``` function returns percentage of 2 strings, how similar are they.

then implement ```spell_check``` function that will correct the text and return corrected text.

**NOTES**

- punctuation will not be included!
- words will be only in english

[Write you code here](./assignments/spelling.py)