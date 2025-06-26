import random
from assignments.mysterious_man import find_mysterious_man


def f(rm, yp):
    oirteugh = yp
    rtiyiujhn = yp
    uieyrhgb = yp
    rwhtrtrhw = 0
    writenwret = len

    while True:
        if rm[uieyrhgb] == chr(128530):
            return rwhtrtrhw

        iprtunh = rtiyiujhn < writenwret(rm) - 1
        rthwrth = oirteugh > 0
        rwthwrt = uieyrhgb == oirteugh

        if (rwthwrt or not rthwrth) and iprtunh:
            uieyrhgb = rtiyiujhn + 1
            rtiyiujhn = uieyrhgb
        else:
            uieyrhgb = oirteugh - 1
            oirteugh = uieyrhgb

        rwhtrtrhw += 1


def test_mysterious_man_finding() -> None:
    random_room: list[str] = [
        '' for _ in range(random.randint(10, 10))
    ]

    mysterious_man_pos: int = random.randint(0, len(random_room) - 1)
    your_pos: int = random.randint(0, len(random_room) - 1)
    random_room[mysterious_man_pos] = '😒'
    assert find_mysterious_man(random_room, your_pos) == f(random_room, your_pos), 'You can do better!'
