tasks = []
while True:
  print("\nTo-Do List")
  print("1.Add Task")
  print("2.View Tasks")
  print("3.Exit")

  choice = input("Choose an option (1/2/3):")

  if choice =="1":
    task = input("Enter a task:")
    tasks.apend(task)
    print("Added:",task)

  elif choice =="2":
    if not tasks:
      print("No tasks yet.")
    else:
      print("\nYour tasks:")
      for i, task in enumerate(tasks, start=1):
        print(f"{i}.{tasks}")

  elif choice =="3":
    print("Goodbye!")
    break
 else:
    print("Invalid choice")
