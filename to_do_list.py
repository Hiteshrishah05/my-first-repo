#To do list
tasks = []

while True:
    #giving choices to the user.
    print("To do list:")
    print("1.Add task")
    print("2.View task")
    print("3.Remove task")
    print("4.Exit")

    choice = input("enter your choice:")

    if choice == "1":
        task = input("Enter the task:")
        tasks.append(task)
        print(f" '{task}' added to your list.")

    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:
            print("Your tasks:")
            for i in range(len(tasks)):
                print(str(i + 1) + "." + tasks[i])

    elif choice == "3":
        if not tasks:
            print("No tasks to remove")
        else:
            for i in range(len(tasks)):
                print(str(i + 1) + "." + tasks[i])

            num = int(input("Enter task number to remove: "))

            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f" '{removed}' removed.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Good bye!")
        break

    else:
        print("Invalid choices , Try again.")