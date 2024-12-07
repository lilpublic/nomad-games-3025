

define mr = Character("Маргулан", color="#bfe02b")
define kn = Character("Кенжетай", color="#ff9d00")
define bb = Character("Бибигуль", color="#ff5988")
define bt = Character("Батырхан", color="#e0c22d")
define tl = Character("Толеген", color="#cb78ff")
define zh = Character("Женiс", color="#78a0ff")
define kl = Character("Калдыораз", color="#78a0ff")


define org = Character("Организатор")
define y = Character("Я")
define z = Character("???")


image mr neutral = "ing_neutral2.png"
image mr neutral2 = "ing_neutral.png"
image mr blush = "ing_blush.png"
image mr happy = "ing_neutral-3.png"


image kn neutral = "tr_neutral.png"
image kn neutral2 = "tr_neutral2.png"
image kn neutral3 = "tr_neutral3.png"
image kn neutral4 = "tr_neutral4.png"

image kl neutral = "kl_neutral.png"
image kl neutral2 = "kl_neutral2.png"
image kl smile = "kl_smile.png"


image zh neutral = "zh_neutral.png"
image zh neutral2 = "zh_neutral2.png"

image bt neutral = "bt_neutral.png"
image bt neutral2 = "bt_neutral2.png"

image tl neutral = "bh_neutral2.png"
image tl neutral2 = "bh_neutral.png"

image yurt = "yurt.png"

image yurt_inside = "yurt_inside.png"
image yurt_inside2 = "yurt_inside2.png"
image stadium = "stadium.png"


define audio.zhen = "audio/zhen.mp3"
define audio.prod = "audio/prod.mp3"
define audio.kenzh = "audio/kenzh.mp3"
define audio.scary = "audio/scary.mp3"
define audio.mech = "audio/mech.mp3"
define audio.basic = "audio/basic.mp3"
define audio.sudoku = "audio/sudoku.mp3"
define audio.dream = "audio/dream.mp3"
define audio.buh = "audio/buh.mp3"
define audio.crowd = "audio/crowd-talking-138493.mp3"


define audio.tada = "audio/tada.mp3"
define audio.punch = "audio/punch.mp3"
define audio.applause = "audio/applause.mp3"
define audio.gallop = "audio/loshad-bejit-ryisyu.mp3"
define audio.crash = "audio/mixkit-dramatic-metal-explosion-impact-1687.wav"

define audio.neigh = "audio/horse-neigh-261131.mp3"

init python:
    from copy import deepcopy
    class sudoku_class:
        def __init__(self, solution, puzzle):
            self.x = 0
            self.y = 0
            self.solution = solution
            self.active = deepcopy(puzzle)
            self.puzzle = puzzle
            self.current = 0
        def move(self, direction):
            if self.current:
                if self.puzzle[self.y][self.x] == 0:
                    self.active[self.y][self.x] = self.current
                self.current = 0

            if direction == "w":
                self.y -= 1
            elif direction == "s":
                self.y += 1
            elif direction == "a":
                self.x -= 1
            elif direction == "d":
                self.x += 1

            x_len = len(self.puzzle)-1
            y_len = len(self.puzzle[0])-1
            if self.x < 0:
                self.x = 0
            if self.y < 0:
                self.y = 0
            if self.x > x_len:
                self.x = x_len
            if self.y > y_len:
                self.y = y_len

        def set(self, x, y):
            if self.current:
                if self.puzzle[self.y][self.x] == 0:
                    self.active[self.y][self.x] = self.current
                self.current = 0
            self.x, self.y = x, y
        def number_entered(self, number):
            self.current = number


style sudoku_button:
    background "#2C2C2C"
style sudoku_text:
    align (.5,.5)
    color "#ff00a6"
    size 50
screen sudoku(g):
    modal True
    style_prefix "sudoku"
    key "w" action Function(g.move, "w")
    key "s" action Function(g.move, "s")
    key "a" action Function(g.move, "a")
    key "d" action Function(g.move, "d")

    # key "0" action Function(g.number_entered, 0)
    key ["1", "K_KP1"] action Function(g.number_entered, 1)
    key ["2", "K_KP2"] action Function(g.number_entered, 2)
    key ["3", "K_KP3"] action Function(g.number_entered, 3)
    key ["4", "K_KP4"] action Function(g.number_entered, 4)
    if len(g.puzzle) > 4:
        key ["5", "K_KP5"] action Function(g.number_entered, 5)
        key ["6", "K_KP6"] action Function(g.number_entered, 6)
        if len(g.puzzle) > 6:
            key ["7", "K_KP7"] action Function(g.number_entered, 7)
            key ["8", "K_KP8"] action Function(g.number_entered, 8)
            key ["9", "K_KP9"] action Function(g.number_entered, 9)
    fixed fit_first True align .5,.5:
        vbox spacing 0:
            for y in range(0,len(g.puzzle)):
                hbox spacing 0:
                    for x in range(0,len(g.puzzle[0])):
                        frame xysize 100,100 padding 8,8 background None:
                            button xfill True yfill True:
                                if g.puzzle[y][x] == 0:
                                    action Function(g.set, x, y)
                                    if g.active[y][x]:
                                        text str(g.active[y][x])
                                else:
                                    background "#111112"
                                    text str(g.active[y][x])
        if len(g.puzzle) < 5:
            add "#00d5ff" xsize 2 xalign .5
            add "#00d5ff" ysize 2 yalign .5
        elif len(g.puzzle) < 7:
            add "#00d5ff" xsize 2 xalign .5
            add "#00d5ff" ysize 2 yalign .333
            add "#00d5ff" ysize 2 yalign .666
        else:
            add "#00d5ff" xsize 2 xalign .333
            add "#00d5ff" xsize 2 xalign .668
            add "#00d5ff" ysize 2 yalign .333
            add "#00d5ff" ysize 2 yalign .668


        frame:
            xysize 100,100 anchor .0,.0
            pos g.x*100, g.y*100
            if g.puzzle[g.y][g.x] == 0:
                background "#00ddff"
                if g.current:
                    text str(g.current)
            else:
                background "#ff00a6"

    if g.active == g.solution:
        frame align .0,.5 background "#111112" padding 40,40:
            vbox align .5,.5 spacing 40:
                text "Точно!"
                button align .5,.5:
                    text "Далее"
                    action Return()


default sudoku_4x4 = sudoku_class(
    solution = [
        [1, 3, 4, 2],
        [4, 2, 3, 1],
        [3, 1, 2, 4],
        [2, 4, 1, 3],
    ],
    puzzle = [
        [0, 0, 4, 2],
        [4, 2, 3, 0],
        [0, 1, 0, 0],
        [0, 4, 1, 0],
    ],
)
default sudoku_6x6 = sudoku_class(
    solution = [
        [2, 4, 1, 6, 3, 5],
        [3, 6, 5, 2, 4, 1],
        [5, 1, 4, 3, 6, 2],
        [6, 3, 2, 5, 1, 4],
        [1, 5, 3, 4, 2, 6],
        [4, 2, 6, 1, 5, 3],
    ],
    puzzle = [
        [2, 4, 0, 0, 3, 5],
        [0, 6, 0, 0, 0, 1],
        [5, 0, 4, 3, 6, 0],
        [6, 3, 0, 0, 0, 4],
        [1, 5, 3, 4, 0, 6],
        [4, 2, 6, 0, 5, 3],
    ],
)

default sudoku_2 = sudoku_class(
    solution = [
        [3, 1, 6, 5, 2, 4],
        [5, 4, 2, 3, 6, 1],
        [4, 3, 1, 6, 5, 2],
        [6, 2, 5, 4, 1, 3],
        [2, 5, 3, 1, 4, 6],
        [1, 6, 4, 2, 3, 5],
    ],
    puzzle = [
        [3, 0, 6, 5, 2, 0],
        [0, 4, 2, 3, 0, 1],
        [4, 0, 1, 6, 5, 0],
        [6, 2, 0, 0, 1, 3],
        [0, 0, 3, 0, 4, 6],
        [0, 0, 4, 0, 0, 0],
    ],
)


label start:
     scene black
     org "Дорогие друзья, уважаемые гости, я приветствую вас на Всемирных Играх Кочевников 3025!"
     play sound applause


     scene stadium with dissolve
     show bt neutral2 with dissolve
     play music prod fadein 1.0




org "Сегодня мы собрались здесь, чтобы открыть грандиозное событие, которое объединяет нас в стремлении к высотам."
org "Вдохновляет на свершения и укрепляет дух единства и дружбы."
org "Каждый из вас проделал огромный путь, чтобы оказаться здесь."
org "Сегодня мы будем аплодировать вашим победам, сопереживать неудачам и вдохновляться вашим мужеством!"
org "Давайте вместе наполним эти дни духом честной борьбы, яркими эмоциями и искренними аплодисментами!"
org "С гордостью объявляю начало игр кочевников!"

play sound applause
stop music fadeout 2.0

show bt neutral
"..."
jump intro
