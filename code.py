import random
for i in range(10):
    print(i)
print("10...Лотерея!!!")

prizes = ["А-а-а-втомобиль!", "Банка с огурцами", "Орущая кошка, покормите ее уже!",
          "Чирик", "Путевка в Крым, но кажется далеко от моря", "Вьетнамские флешбэк"]

people = ["Дед Макар", "Путин", "Шмель", "Твоя собака"]

for participant in people:
    prize = random.choice(prizes)
    print("{0} получает лот '{1}'! Поздравляем!"
          .format(participant, prize))