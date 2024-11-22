#"Форматирование строк".

# Использование %:
print("В команде Мастера кода участников: %s " % 5)
print("В команде Волшебники данных участников: %s " % 6)
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s" % {'team1_num': 5, 'team2_num': 6})

#Использование format():

print( "Команда Волшебники данных решила задач: {score_2} !".format(score_2 = 42))
print("Волшебники данных решили задачи за {team2_time} с !".format(team2_time =18015.2))
print( "Команда Мастера кода решила задач: {score_1} !".format(score_1 = 40))
print("Мастера кода решили задачи за {team1_time} с !".format(team1_time =10717.6))

#Использование f-строк:
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
     result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
     result = "Победа команды Волшебники Данных!"
else:
     result = "Ничья!"
print(f'Результат битвы: {result}')



print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")





