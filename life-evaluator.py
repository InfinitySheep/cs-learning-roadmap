#Instructions
#Ask the user:
#Name
#Number of AP classes they’re taking
#Do they procrastinate? (yes / no)
#Do they work a part-time job? (yes / no)


#Print a blunt summary:
#Sleep status
#Workload status
#Habit assessment
#Final prediction (burnout / survival / thriving)

#User Inputs
name = input("What is your name: ")
ap_num = int(input("How many AP classes are you taking "))
proc_num = int(input("Rate your level of procrastination from 1 to 10 "))
job = input("Do you work a part-time job ")
if (job == 'yes' or job == "Yes"):
    job = True
elif (job == "no" or job == "No"):
    job = False

#Summary Calculator
user_rating = 0

#Number of AP Classes influence
if ap_num >= 6:
    user_rating += 65
elif(ap_num == 4 or ap_num == 5):
    user_rating += 55
elif(ap_num == 2 or ap_num == 3):
    user_rating += 35
elif (ap_num == 1):
    user_rating += 25
    
#Level of Procrastination influnce
if (proc_num == 9 or proc_num == 10):
    user_rating *= 1.5
elif (proc_num == 7 or proc_num == 8):
    user_rating *= 1.4
elif (proc_num == 5 or proc_num == 6):
    user_rating *= 1.3
elif (proc_num == 3 or proc_num == 4):
    user_rating *= 1.2

if (user_rating >= 80):
    print(f'{name} Ur completely screwed ngl.')
    if (job):
        print('However, you at least making some money!')
    else:
        print("And no job?? I wish you luck!")
elif (user_rating >= 60 and user_rating < 80):
    print(f"{name}, u need to lock in bruh.")
    if (job):
        print('However, you making that money though!')
elif (user_rating >= 40 and user_rating < 60):
    print(f'{name}, ur managing.')
    if (job):
        print("and you making dough.")
else:
    print(f'{name}, ur thriving like a king!')
    if (job):
        print("Brother is locked in for-real.")
    else:
        print("Mind as well get a job to top it off!")

