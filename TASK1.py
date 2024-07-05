def main():
    tasks = []
    while True:
        print("\n==== TO-DO LIST ====")
        print("1. ADD TASK")
        print("2. SHOW TASK STATUS")
        print("3. MARK TASK AS DONE")
        print("4. EXIT")
        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            try:
                n_tasks = int(input("How many tasks do you want to add: "))
                for i in range(n_tasks):
                    task = input("Enter the task: ")
                    tasks.append({"task": task, "done": False})
                    print("Task added!")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '2':
            print("\nTasks:")
            if not tasks:
                print("No tasks added.")
            else:
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")
        
        elif choice == '3':
            if not tasks:
                print("No tasks to mark as done.")
            else:
                try:
                    task_index = int(input("Enter the task number to mark as done: ")) - 1
                    if 0 <= task_index < len(tasks):
                        tasks[task_index]["done"] = True
                        print("Task marked as done!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        
        elif choice == '4':
            print("Exiting the TO-DO LIST.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
