import datetime

user_goal = input("Enter your goal, separated by a colon \n:")
input_list = user_goal.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()

# calculate now till the deadline
time_till = deadline_date - today_date



print(f"Hello! Time remaining for your goal: {goal} is {time_till.days} days Good Luck")