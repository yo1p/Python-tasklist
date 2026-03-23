
import time

import json



def add_task(tasks):
   while True:
                     new_task = input("Add a new task: ")
                     if new_task.isdigit():
                       print("Invalid input. Please enter a string")
                       continue
                     else:
                       tasks.append(new_task)
                       print(tasks)
                       print("Adding new task..")
                       time.sleep(1)
                       print("Task successfully added!")
                       break 
                     
def view_task(tasks):
    print("\n---Current tasks---")
    if not tasks:
         print("This tasklist is currently empty!")
         return     
    for index,task in enumerate(tasks,start=1):
           print(f"{index}. {task}")



def delete_task(tasks):
     for index,task in enumerate(tasks,start=1):
               print(f"{index}. {task}")
     while True:
                   try:
                       if len(tasks)==0:
                         print("The list is empty")
                         break
                       choice = int(input("Select a task you would like to delete by entering its corresponding number: "))
                       if 1 <= choice <= len(tasks):
                         removed = tasks.pop(choice-1)
                         print(f"Removing '{removed}'...")
                         time.sleep(1)
                         print(f"{removed} has been successfully removed!")
                         break
                      
                       else:
                         print("Invalid number")
                   except ValueError:
                     print("Invalid Input! Please only enter Integers")
                     continue             
                         

def save_tasks(tasks): # save tasks into a json file
     with open("tasklist.json","w") as file:
          json.dump(tasks,file,indent=4)

def load_tasks():
    try: 
     with open("tasklist.json","r") as file: # load tasks and replace the hardcoded tasklist
          data = json.load(file)
          return data 
    except FileNotFoundError:
      return []
      
          
def main():
    is_Running = True

    print("*---Checklist App---*")

    tasks = load_tasks()



    # tasks = [   # task list
    #      "Study python",
    #     "Finish project",
    # ]

    print("What do you want to do")

    while is_Running:
        print("\n1. Add a task\n"
        "2. View current tasks\n"
        "3. Delete a task\n"
        "4. Exit")
        
        try:
            select = int(input("Select from this list by entering its corresponding number: "))
            if select>4:
             print("Please only enter a number between 1-4!")
             continue
            elif select==4:
                print("Exiting..")
                time.sleep(1)
                print("Goodbye!")
                break
            elif select==1: # Add a task
                add_task(tasks)
                save_tasks(tasks)
                
            elif select==2: # View tasks
                view_task(tasks)
               

            elif select==3: # Delete task
                 delete_task(tasks)
                 save_tasks(tasks)
               
        except ValueError:
            print("Invalid Input. Please only enter numbers!") 
       

if __name__ == '__main__':
    main()