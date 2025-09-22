import numpy as np

"Q1"
week1_sleep = [6, 7, 8, 5, 9]
week2_sleep = [7, 6, 8, 7, 6]

"Q2"
days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]

"Q3"
daily_difference = np.array(week1_sleep) - np.array(week2_sleep)

"Q4"
"a"
total_week1 = sum(week1_sleep)

"b"
total_week2 = sum(week2_sleep)

"c"
average_week1 = total_week1 / len(week1_sleep)
average_week2 = total_week2 / len(week2_sleep)

"Q5"
slept_more_first_week = average_week1 > average_week2


if slept_more_first_week :
	print("Vous avez plus dormi la première semaine\n")
else:
	print("Vous avez plus dormi la deuxième semaine\n")

"Q6"
"a"	
sleep_wednesday_week1 = week1_sleep[2]

"b"
midweek_sleep_week2 = week2_sleep[1:4]

"Q7 et Q8"
sleep_enough_week1 = []
sleep_successful_days_week1 = []

for i in range(len(week1_sleep)):
	if week1_sleep[i] >= 8:
		sleep_enough_week1.append(days[i])
		sleep_successful_days_week1.append(week1_sleep[i])

	
