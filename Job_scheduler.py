# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:33:00 2021

@author: sumanthsetty
"""


from datetime import datetime, timedelta
from JOB_Organiser_classes import Node, BST_JobSchd

def add_Job():
    sched_time = input("Enter the start time of the Job in HH:MM format (ex:12:30,1:25..) :-")
    while True:
        try:
            datetime.strptime(sched_time, '%H:%M')
        except ValueError:
            print("Incorrect format entry of time\nPlease try again")
            sched_time = input("Enter the start time of the Job in HH:MM format")
        else:
            break
    while True:
        duration = input("Duration for the job in minutes (ex:25,30..) :-")
        try:
            int(duration)
        except ValueError:
            print("Incorrect format of duration\nPlease enter in minutes(integers)")
            duration = input("Duration for the job in minutes (ex:25,30..) :-")
        else:
            break
            
    Job_name = input("Name of the Job:-")
    print("_"*40)
    
    d = sched_time+","+duration+","+Job_name
    
    return d

    

tree =  BST_JobSchd()

with open("data.txt") as f:
    for line in f:
        tree.insert(line)

while True:
    print("Please choose an option from the list below:")
    print("Press 1 to view today's scheduled jobs")
    print("Press 2 to add a job to today's schedule")
    print("Press 3 to remove a job from the schedule")
    print("Press 4 to quit")

    req = int(input("Enter here:-"))
    
    if req == 1:
        tree.in_order()    
    elif req == 2:
        NewJob = add_Job()
        tree.insert(NewJob)
    elif req == 3:
        print("Enter the Job details ")
        job_info =  add_Job()
        Time,dur,nam = job_info.split(",")
        #key = datetime.strptime(Time, '%H:%M').time()
        result = tree.search(job_info)
        print(result)
        if result:
            if result.name_of_job == nam and result.duration == dur:
                print(f"Deleting {key}\nSuccessfully deleted")
                tree.delete(result)
                
                with open("data.txt","r") as f:
                    lines = f.readlines()
                    
                with open("data.txt","w") as f:
                    for line in lines:
                        if line.strip("\n") != job_info:
                            f.write(line)
                
                print("Press any key to continue...........")
            else:
                print("Sorry the job mentioned is not found in the file")
                print("Press any key to continue...........")
                
        else:
            print("Sorry the job mentioned is not found in the file")
            print("Press any key to continue...........\n")
        
    else:
        print("Quiting..........")
        break
  
