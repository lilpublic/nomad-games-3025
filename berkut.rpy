label berkut:

     "Ты проходишь чуть дальше к указанной Кенжетаем юрте."
     "Позади юрты стоит экипировка для охоты с беркутом."
     "Ты осматриваешь насесты с сидящими на них птицами."
     "Какие беркуты... Большие вблизи..."
     "Птицы осматривают тебя умными глазами и начинают хлопать крыльями."
     stop music fadeout 2.0
     z "Кто здесь!?"
     z "Покажись!!!"


     show zh neutral2 with dissolve
     z "Что ты делаешь с моими птицами!!!"
     show zh neutral
     "Какой и впрямь внушающий ужас молодой человек..."
     "Ты вспоминаешь слова Кенжетая и решаешь быть осторожным."
     x "...Я просто смотрю."
     z "{cps=10}...{/cps}"
     play music zhen fadein 1.0
     show zh neutral2
     z "Так ты еще один любитель птиц!"

     z "Кто тебе нравится? Этого вот зовут Абиль..."
     z "Это значит ВОИН на арабском. Скажи, ультра крутое имя?!" with Shake((0, 0, 0, 0), 3.0, dist=5)
     show zh neutral
     "Ты неловко киваешь в ответ."
     show zh neutral2
     z "А этого зовут Улан..."
     z "Знаешь, что означает имя Улан?!"
     "{cps=10}Ты отрицательно качаешь головой.{/cps}"
     z "МОЛОДОЙ ВОИН... Крутое, пышущее молодостью имя..."
     z "А этого! Этого зовут Арынгазы!!!"
     z "Знаешь, что значит?!!"
     z "СМЕЛЫЙ ВОИН!!!" with Shake((0, 0, 0, 0), 3.0, dist=5)
     show zh neutral
     "{cps=10}?..{/cps}"
     show zh neutral2
     z "А вот это Нариман! Означает ОГНЕННЫЙ ВОИН..." with Shake((0, 0, 0, 0), 3.0, dist=5)
     show zh neutral
     "{cps=10}......{/cps}"
     show zh neutral2
     zh "И Жантай..."
     zh "А вот Жантай означает МОЙ МИЛЫЙ, моя жизнь..."
     show zh neutral
     "Вау... Этот молодой человек правда любит своих беркутов..."
     "Может, он даже не такой страшный?.."
     "Просто взрослый мужчина... Горячо любящий своих пернатых товарищей."
     "Так поэтично..."
     x "Кх-кхм."
     "Ты собираешься с мыслями, чтобы допросить молодого человека, но кажется ему совершенно нет до тебя дела."
     "Точно, он ведь даже не назвал свое имя..."

     x "Меня зовут [povname]... Я детектив."
     show zh neutral2
     zh "Очень приятно, [povname]! Меня зовут Женiс!"
     zh "Я участвую в турнире по охоте с беркутом!"
     show zh neutral
     x "Я хотел бы задать пару вопросов про произошедшее..."
     show zh neutral2
     zh "ПРО ЛОШАДЬ, ДА?!" with Shake((0, 0, 0, 0), 3.0, dist=5)
     show zh neutral
     "Ты не успеваешь договорить когда Женic перебивает тебя и трясет тебя за плечи."
     show zh neutral2
     zh "Ох уж эта Шайтан машина..."

     "Точно, теперь ты замечаешь, что на насестах нет ни одного механического беркута."
     zh "Терпеть не могу эти механические электрические шайтан-машины..."
     zh "Я приехал чтобы защищать свою ЧЕСТЬ!" with Shake((0, 0, 0, 0), 3.0, dist=5)
     zh "Честь своего родного АУЛА!!!"
     zh "Использовать машины в таком древнем обычае просто возмутимо!!!"
     "Возможно, он прав?.."
     "Ты достаешь костяные бусины, полученные у механика."
     show zh neutral
     x "Вы знаете что-нибудь об этом?.."
     show zh neutral2
     zh "Жантай недавно принес мне в клюве вторую половину этого костяного браслета."
     zh "Я постоянно видел эти бусины у организатора на руке... И в его юрте."
     "?!"
     zh "Откуда они?.."
     show zh neutral
     x "Они были найдены в механическом коне пострадавшего."
     x "Возможно, кто-то пытался вывести коня из строя перед началом соревнований."
     show zh neutral2
     zh "Тц..."
     zh "Эти проклятые машины..."

     "Странно..."
     "Что-то не сходится..."
     zh "Я готовился к началу соревнований вместе со всеми, здесь, в своей юрте."
     zh "Я точно слышал этого... Кричащего молодого человека."
     "Маргулан и правда готовил коня к скачкам."
     zh "Еще была целая толпа людей с камерами."
     "Должно быть, пресса вместе с инвесторами."
     "Маргулан говорил и о них тоже."
     zh "Был кто-то еще..."
     "Хм?"
     show zh neutral
     x "Кто-то еще?.."
     show zh neutral2
     zh "Да. Определенно был кто-то еще."
     show zh neutral
     x "Спасибо за помощь."
     show zh neutral2
     zh "Вот бы механическим зверям запретили участвовать в следующем году..."
     show zh neutral

     stop music fadeout 2.0

     "Ты благодаришь Женiса и собираешься возвращаться к Калдыоразу."
     hide zh with dissolve
     "Теперь нужно распросить Калдыораза!"
     play music drama


     show tl neutral2 with easeinleft
     play sound punch
     tl "[povname] мырза!"
     tl "Я вас совсем обыскался!!"
     tl "Вам нужно пройти в юрту Батырхан мырзы!"
     show tl neutral



jump finale
