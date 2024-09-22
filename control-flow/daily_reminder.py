# prompt for a singe task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
# Use a Match Case statement to react differently based on the task’s priority.
# Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
match priority:
    case "high":
        reminder = f"{task} is a high priority task "
        if time_bound == "yes":
            reminder += "and it requires immediate attention."
        else:
            reminder += "."
    case "medium":
        reminder = f"{task} is a medium priority task "
        if time_bound == "yes":
            reminder += "you should consinder addressing it soon."
        else:
            reminder += "."
    case "low":
        reminder = f"{task} is a low priority task"
        if time_bound == "yes":
            reminder = "and you should consinder doing it when free."
        else:
            reminder += "."
    case _:
        reminder = "you have entered an invalid priority!"
print(f"reminder: {reminder} ")
