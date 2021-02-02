# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:11:12 2021

@author: sumanthsetty
"""
from datetime import datetime, timedelta
from Job_scheduler import Node, BST_JobSchd

def add_Job():
    sched_time = input("Enter the start time of the Job in HH:MM format")
    while True:
        try:
            datetime.strptime(sched_time, '%H:%M')
        except ValueError:
            print("Incorrect format entry of time\nPlease try again")
            sched_time = input("Enter the start time of the Job in HH:MM format")
        else:
            break
    
    duration = input("Duration for the job")
    Job_name = input("Name of the Job")
    
    d = sched_time+","+duration+","+Job_name

    f = open("data.txt", "a")
    f.write(d)
    f.close()
    

f = open("data.txt", "r")
tree =  BST_JobSchd()
for x in f:
  tree.insert(x)
f.close()
  
tree.in_order()

add_Job()
tree.in_order()