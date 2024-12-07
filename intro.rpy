label intro:

     scene yurt with wipeleft

     play music dream fadein 1.0
     "Стадион оглушили аплодисменты."

     "Звучала приветственная речь моего кумира детства - Батырхана."

     "Когда-то он сам был наездником выступавшим на Играх, лучшим из лучшим."

     "Именно он вдохновил меня на мой путь и сегодня свершится мой дебют в Играх."

     "Если честно, я немного нервничал."

     "Все вокруг поддерживали и верили в меня, но это только наполняло меня тревогой. Я боялся подвести их ожидания."

     "Страшнее и волнительнее всего было то, что мне придется выступать на глазах моего кумира Батырхана."

     "До начала выступления оставалось десять минут."


     mr "Всё будет хорошо, главное - это  получать удовольствие от того, что делаешь!"

     show mr blush with dissolve
     "Я повернулся в сторону Маргулана."


     y "Спасибо..."

     show mr neutral
     "И тут я увидел как он треплет за шею свою механическую лошадь."
     "Он говорил эти слова ей."
     "Инженер покосился на меня."


     show mr neutral2
     mr "И ты не подведи. От тебя, конечно, мало что зависит, но в этом году очень крупные спонсоры."
     mr "Мне нужен контракт хотя бы с одним из них."

     show mr neutral
     y "Сделаю всё возможное!"


     show mr neutral2
     mr "Нет."
     mr "Ты должен сделать это."


     show mr neutral
     "Я сделал глубокий вздох."

     hide mr with dissolve




     "{cps=10}Три минуты.{/cps}"
     stop music fadeout 2.0

     "{cps=10}Две.{/cps}"

     "{cps=10}Одна.{/cps}"

     init:

         python:

             import math

             class Shaker(object):

                 anchors = {
                     'top' : 0.0,
                     'center' : 0.5,
                     'bottom' : 1.0,
                     'left' : 0.0,
                     'right' : 1.0,
                     }

                 def __init__(self, start, child, dist):
                     if start is None:
                         start = child.get_placement()
                     #
                     self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                     self.dist = dist    # maximum distance, in pixels, from the starting point
                     self.child = child

                 def __call__(self, t, sizes):
                     # Float to integer... turns floating point numbers to
                     # integers.
                     def fti(x, r):
                         if x is None:
                             x = 0
                         if isinstance(x, float):
                             return int(x * r)
                         else:
                             return x

                     xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                     xpos = xpos - xanchor
                     ypos = ypos - yanchor

                     nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                     ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                     return (int(nx), int(ny), 0, 0)

             def _Shake(start, time, child=None, dist=100.0, **properties):

                 move = Shaker(start, child, dist=dist)

                 return renpy.display.layout.Motion(move,
                               time,
                               child,
                               add_sizes=True,
                               **properties)

             Shake = renpy.curry(_Shake)
     init:
         $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)


     scene black with dissolve

     play sound gallop
     "{cps=10}...{/cps}"
     play sound neigh
     "{cps=10}...{/cps}" with Shake((0, 0, 0, 0), 3.0, dist=5)
     play sound crash

     scene presents with dissolve
     "{cps=10}{/cps}"









     scene black with dissolve
     "Тебя  зовут..."
     define pov = Character("[povname]")
     python:
          povname = renpy.input("Впишите свое имя!")
          povname = povname.strip()

          if not povname:
              povname = "Серик"


     "Меня зовут [povname]!"
     define x = Character("[povname]", color="ffffff")
     play music basic fadein 1.0

     "Я ведь даже не горел желанием здесь появляться."

"Но мой друг детства Калдыораз всегда был большим фанатом Батырхана."

"Ну, а я..."
"А я с ним всегда и  везде. Куда он без меня."

"Я никогда не любил эти Игры."
"Нет, не подумайте, просто я не люблю толпы людей и шум."

"Но эти Игры были особенными - мечта всей жизни моего друга исполнялась у меня на глазах."

"“Когда-нибудь я окажусь там!” говорил он в детстве и указывал рукой на всадников на конях с тушой козла."

"И он сдержал обещание - сегодня это был его день."

"Я - человек нелюдимый."
"Я отнекиваюсь от любых “давай встретимся, погуляем” тем, что я всегда занят работой."

"Я давно не виделся с Калдыоразом. Но пропустить это событие я никак не мог."

"Даже если мне становилось плохо и кружилась голова от нахождения в толпе уже спустя пять минут."

"Ну, и, возможно, отпуск взять стоило давно. Я не помню когда были мои последние выходные."

"Кокпар открывал программу фестиваля. Это была отличная новость."

"Мы договорились с другом, что после его выступления проведём остаток фестиваля вместе."

scene yurt_inside2 with dissolve

show kl neutral with dissolve
x "..."

x "...................."

show kl smile
kl "Ну, хотя бы у меня даже не было возможности облажаться."

show kl neutral
x "Ты себя видел вообще?"


show kl smile
kl "Просто царапинка."
show kl neutral

x "Это не смешно. Это было важно для тебя."

show kl neutral2
kl "Хм..."

kl "Ну да."

show kl neutral
x "И ты спокоен?"

show kl neutral2
kl "Знаешь... На удивление да."

show kl smile
kl "Как будто груз с плеч."
show kl neutral2
kl "Я правда мечтал об этом, но..."
kl "Последние дни на меня всё так давило..."
kl "Я так боялся подвести ожидания всех..."
show kl neutral

x "Ты ни в чем не виноват."
x "Это всё дурацкая лошадь!"

show kl neutral2
kl "Не надо..."
show kl neutral
x "Ты столько к этому готовился..."
x "Если бы..."
x "Разве за это не должен отвечать твой механик?!"


kl "..."



show kl smile
"Друг оставался спокойным. Он покачал головой."

show kl neutral2
kl "У тебя же должен был быть отпуск?"
show kl neutral
x "А ты должен был просто выступить и погулять со мной!"
x "Посмотри на себя!"
show kl neutral2
kl "Пожалуйста, не делай глупостей."
kl "Я прекрасно провожу время."
show kl smile
kl "Отдыхаю... Провожу время с другом."
show kl neutral2
kl "Как твои дела?"

show kl neutral
"Его голос был мягким и ласковым, но я не мог смотреть на его забинтованное лицо без боли."

stop music fadeout 2.0

x "Прости..."
x "Но я сегодня собираюсь заниматься глупостями."

show kl smile
kl "Ничего."
"Друг вздохнул вслед уходящему мне так, будто бы и не сомневался, что я скажу это."


jump task










label sudoku_example:
     "Так... Ой..."
     call screen sudoku(sudoku_4x4)
     "Надо попробовать еще..."
     call screen sudoku(sudoku_6x6)
     "Господи..."
     call screen sudoku(sudoku_9x9)
