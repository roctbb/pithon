print('Walk Adviser v0.1 by RoctBB')
print("Добро пожаловать!")
temperature = int(input('Сколько там градусов? '))
is_raining = input('Идет дождь (да/нет)? ').lower()

if is_raining == "нет" and temperature >= 20:
    print("Иди гуляй, че как сыч сидишь!")
elif is_raining == "нет" or temperature >= 23:
    print("Ну вообще и прогуляться можно...")
else:
    print("Го в КС, я создал!")
