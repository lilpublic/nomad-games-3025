label mech:
     scene stadium with wipeleft
     play music scary fadein 1.0
     "Толпу распустили, никого нет."
     "Тихо..."
     "Только сломанный механический конь застрявший  в трибуне."
     "Я надеялся застать механика где-то поблизости."
     "Странно, что он вот так бросил своё детище."
     scene yurt with wipeleft

     "Кто-то выходит из юрты Калдыораза."

show mr neutral with dissolve

x "Прошу прощения..."

show mr neutral2
z "Я занят. Интервью и автографы не раздаю."
show mr neutral
stop music fadeout 1.0
x "Я веду расследование."
play music mech fadein 1.0
show mr neutral2
mr "Да чтобы Я!? Великий Маргулан!? И отвечал на твои вопросы!?"
mr "У МЕНЯ ТРАУР, ТЫ ЧТО НЕ ВИДИШЬ?" with Shake((0, 0, 0, 0), 3.0, dist=5)
"Как же истошно он кричит..."
show mr neutral
x "Что-то с Калдыоразом?"
show mr neutral2
mr "Чего? Он-то тут причем?"
show mr neutral2
mr "Бедняжка Кулын... Это был её дебют..."
mr "Я возлагал на неё столько надежд!"
mr "Моя лошадка..."


show mr neutral
x "Ничего, отремонтируешь."

show mr neutral2
mr "ДА ЧТО ТЫ ВООБЩЕ ПОНИМАЕШЬ!?" with Shake((0, 0, 0, 0), 3.0, dist=5)
"!?" with Shake((0, 0, 0, 0), 3.0, dist=5)

play music sudoku fadein 1.0
call screen sudoku(sudoku_6x6)
play music mech fadein 1.0

show mr neutral
x "Я хочу отыскать правду."
x "Ты - механик. Ты отвечал за лошадь Калдыораза и сейчас ты главный подозреваемый."


show mr neutral2

mr "Я!?" with Shake((0, 0, 0, 0), 3.0, dist=5)

mr "Ты вообще знаешь кто я?!"
mr "Я - гениальный изобретатель, молодое дарование!"
mr "Ты знаешь сколько у меня наград!?"
mr "УЙДИ С ДОРОГИ!" with Shake((0, 0, 0, 0), 3.0, dist=5)
stop music fadeout 1.0
"{cps=10}Господи...{/cps}"
"Тяжелый случай."
play music sudoku fadein 1.0

call screen sudoku(sudoku_2)

play music mech fadein 1.0
show mr neutral2
mr "Ты что, до сих пор не ушел?"

show mr neutral

x "Я собираю улики. Даже если ты что-то сделал, пока мне не в чем обвинить тебя."
x "Будет лучше, если ты окажешь помощь следствию."
x "Как механик, ты должен лучше всех знать, что произошло."

mr "{cps=10}...{/cps}"

show mr neutral2
mr "Кость."

show mr neutral
x "Что?"

show mr neutral2
mr "Всё проще некуда."
mr "Каким-то образом в моторном отсеке оказалась кость."
mr "Представляешь?!"
mr "Умом преступник явно не блещет."
show mr neutral

x "Как она могла там оказаться?"
x "Разве ты не должен был всё проверить?"

show mr neutral2
mr "Я всё проверил!!!"
show mr neutral
x "И?.."
mr "..."
x "Ты оставлял коня без присмотра?"
show mr neutral2

mr "Думаешь мне заняться нечем? Дел невпроворот!"
mr "Я оставил Калдыораза одного с конём."
mr "Я уже закончил калибровку и оставалась пара минут до его выхода."

show mr neutral
x "И куда ты отходил?"

show mr neutral2
mr "Встреча с потенциальным инвестором."

show mr neutral
x "И как прошло?"

show mr happy
mr "Отлично! Он очень хвалил моих механических лошадей и захотел приобрести себе сразу 50!"
show mr blush
x "...Рад, что хотя бы у тебя день удался."

show mr neutral2
mr "НЕТ." with Shake((0, 0, 0, 0), 3.0, dist=5)

mr "МОЯ СДЕЛКА ПОД УГРОЗОЙ!" with Shake((0, 0, 0, 0), 3.0, dist=5)

mr "СДЕЛАЙ ЧТО-НИБУДЬ. МОЯ РЕПУТАЦИЯ НЕ МОЖЕТ БЫТЬ ОПОРОЧЕНА." with Shake((0, 0, 0, 0), 3.0, dist=5)
mr "Я не хотел бы стать известным как “Создатель лошади-убийцы”."
show mr neutral
stop music fadeout 2.0
x "Ты хоть принёс свои соболезнования Калдыоразу?"

show mr neutral2
mr "Я рад, что он не погиб."
show mr neutral
x "..."

x "Что ж, удачи в начинаниях."


show mr neutral2
mr "Я НЕ НАЧИНАЮЩИЙ!!!" with Shake((0, 0, 0, 0), 3.0, dist=5)

play music basic fadein 1.0

hide mr with dissolve

play sound tada
show image "bone.png" with dissolve
"Получена: кость..?"
"Какой загадочный узор..."
hide image "bone.png" with dissolve
jump kenzh
