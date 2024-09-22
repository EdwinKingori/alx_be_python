# prompt for a singe task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time_bound? (yes/no): ")

# process task based on priority

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
