team1_num = int(input())
team2_num = int(input())
score_1 = int(input())
score_2 = int(input())
team1_time = float(input())
team2_time = float(input())
print('"В команде Мастера кода участников: %d!"' % team1_num)
print('"Итого сегодня в командах участников: %s и %d!"' % (team1_num, team2_num))
print('"Команда Волшебники данных решила задач: {}!"'.format(score_2))
print('"Волшебники данных решили задачи за {} c!"'.format(team2_time))
print(f'"Команды решили {score_1} и {score_2} задач"')
print(
    f'"Сегодня было решено {score_2 + score_1} задач, в среднем по '
    f'{(score_2 + score_1) / (team1_time + team2_time)} секунды на задачу"')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print('"Победа команды мастера кода!"')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print('"Победа команды Волшебники данных!"')
else:
    print('"Ничья!"')

