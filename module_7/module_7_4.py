class Team:
    def __init__(self, name, nmembers, score, time) -> None:
        self.name = name
        self.nmembers = nmembers
        self.score = score
        self.time = time


def challenge_result(team1, team2):
    if (
        team1.score > team2.score
        or team1.score == team2.score
        and team1.time > team2.time
    ):
        return "победа команды %s!" % team1.name
    elif (
        team1.score < team2.score
        or team1.score == team2.score
        and team1.time < team2.time
    ):
        return "победа команды %s!" % team2.name
    else:
        return "ничья!"


team1 = Team(name="Мастера кода", nmembers=5, score=40, time=1552.512)
team2 = Team(name="Волшебники данных", nmembers=6, score=42, time=2153.31451)

print("В команде %s участников: %s !" % (team1.name, team1.nmembers))
print(
    "Итого, сегодня в командах участников: %s и %s !" % (team1.nmembers, team2.nmembers)
)

print("Команда {} решила задач: {} !".format(team2.name, team2.score))
print("{} решили задачи за {} с !".format(team2.name, team2.time))

print(f"Команды решили {team1.score} и {team2.score} задач.")
print(f"Результат битвы: {challenge_result(team1, team2)}")
score_total = team1.score + team2.score
mean_time = round((team1.time + team2.time) / score_total, 1)
print(
    f"Сегодня было решено {score_total} задач, в среднем по {mean_time} секунды на задачу!"
)
