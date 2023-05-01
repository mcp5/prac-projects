import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

# calculate how many days to the deadline

todaydate = datetime.datetime.today()

goaldate = deadline_date - todaydate

print(f"Dear user! Time remaining for your goal:  {goal} is {goaldate.days} days")

