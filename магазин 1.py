predmet = []
cis = [10, 5, 40, 15, 20, 25, 10, 10, 5, 20, 15]

mon = 175
predmet.append("игрушечный нож за 10 монет,")
predmet.append("паучий пончик за 5 монет,")
predmet.append("медальён в форме сердца за 40 монет,")
predmet.append("шляпа кафбоя за 15 монет,")
predmet.append("балетная пачка за 20 монет,")
predmet.append("грубые перчатки за 25 монет,")
predmet.append("мутные очки за 10 монет,")
predmet.append("крабовое яблоко за 10 монет,")
predmet.append("морской чай за 5 монет,")
predmet.append("легендарный герой за 20 монет,")
predmet.append("фартук за 15 монет,")
input("Привет!")
input("*кто-то говорит сзади*")
input("*вы обернулись*")
input("*вы увидели стойку с табличкой где написано МАГАЗИН*")
input("хочешь чтонибуть купить?*говорит ...некто?*")
a = input("*что вы ответите?*")
if a == "да" or a == "конечно" or a == "давай":
    input("*вы говорите "+a+" ведь у вас много монет и некуда деть*")
    input("хорошо.*сказал ...некто?*")
    for i in range(len(predmet)):
        print(i + 1, ") ", predmet[i])
    input()
    
    for step in range(7):
        if mon < 5:
                print("у тебя нету денег!!")
        shop = int(input("что купишь?(номер предмета)"))
        if mon < 5:
                print("у тебя нету денег!!")
                
        elif shop >= 1 and shop <= 11 and mon > 5:
            if mon > 5:
                input("у вас было " + str(mon))
                mon = mon - cis[shop-1]
                input("у вас сейчас " + str(mon))
                
else:
    b = input("*но у вас много монет может всё таки купить что-то?*")
    if b == "да" or a == "конечно" or a == "давай":
        print("*вы говорите "+b+" ведь у вас много монет и некуда деть но продавец пропал!!*")
    else:
        print("вы пошли дальше и споткнулись и уранили все монеты которые все украли*")