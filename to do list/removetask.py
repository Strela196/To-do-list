import Taskstorage, sys, time
#time.sleep is used to make everything not so rushed
def removingtasks():
    print("please write the task you want to remove")
    task = sys.stdin.readline()
    task = task.strip()

    Taskstorage.removetask(task)

    print("""you have succesfully removed the task
if you want to get the task back
well there is nothing you can do about that""")
    time.sleep(1)