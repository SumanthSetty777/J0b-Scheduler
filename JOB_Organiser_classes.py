# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:04:34 2021

@author: sumanthsetty
"""
from datetime import datetime, timedelta

#Creating a node which stores time, duration and job name 
class Node:
    def __init__(self,key):
        sched_time, duration, name_of_job = key.split(",")
        raw_sched_time = datetime.strptime(sched_time, '%H:%M')
        key = raw_sched_time.time()
        end_time = (raw_sched_time + timedelta(minutes=int(duration))).time()
        self.data = key
        self.scheduled_end = end_time
        self.duration = duration
        self.name_of_job = name_of_job.rstrip()
        self.left_child = None
        self.right_child = None
        
    def __str__(self):
        return(f"{self.data},{self.duration},{self.name_of_job}")
        pass
        
        
class BST_JobSchd:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root, key)
    
    def _insert(self, curr, key):
        if key.data > curr.data and key.data >= (curr.scheduled_end):
            if curr.right_child == None:
                curr.right_child = key
                self.to_print(key, True)
            else:
                self._insert(curr.right_child, key)
        elif key.data < curr.data and key.scheduled_end <= curr.data:
           
            if curr.left_child == None:
                    curr.left_child = key
                    self.to_print(key, True)
            else:
                self._insert(curr.left_child, key)
                
        else:
            self.to_print(key, False)
            
    def to_print(self, key, bool):
        if bool:
            print(f"successfully added\n")
            print(f"Scheduled Time:-{key.data}\nDuration:-{key.duration}\nEnd Time:-{key.scheduled_end}\nJob Name:-{key.name_of_job}")
            print("_"*40)
        else:
            print(f"Did not add the job\n")
            print(f"Scheduled Time:-{key.data}\nDuration:-{key.duration}\nEnd Time:-{key.scheduled_end}\nJob Name:-{key.name_of_job}")
            print("The scheduled time maybe overlaping\ncheck it properly")
            print("_"*40)
    def in_order(self):
        self._in_order(self.root)
        print("")
        
    def _in_order(self,curr):
        if curr:

            self._in_order(curr.left_child)
            print(curr)
            self._in_order(curr.right_child)
            
     
    def pre_order(self):
        self._pre_order(self.root)
        print("")
        
    def _pre_order(self, curr):
        if curr:
            print(curr.data, end=" ")
            self._pre_order(curr.left_child)
            #print(curr.data, end =" ")
            self._pre_order(curr.right_child)
     
     
    def post_order(self):
        self._post_order(self.root)
        print("")
        
    def _post_order(self, curr):
        if curr:
            
            self._post_order(curr.left_child)
            #print(curr.data, end =" ")
            self._post_order(curr.right_child)
            print(curr.data, end=" ")
        
    def search(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        key = key.data 
        return self._search(self.root,key)
        
    def _search(self,curr,key):
        if curr:
            if curr.data == key:
                return curr
            elif key < curr.data:
                return self._search(curr.left_child, key)
            else:
                return self._search(curr.right_child, key)
        else:
            return None
        
    def min_right_subtree(self, curr):
        if curr.left_child == None:
            return curr
        else:
            return self.min_right_subtree(curr.left_child)
                 
    def delete(self,key):
        if not isinstance(key, Node):
            key = Node(key)
        key = key.data        
        print(key)
        self._delete(self.root, None, None, key)
    
    def _delete(self, curr, prev, isleft, key):
        if curr:
            if curr.data == key:
                print("yes")
                if curr.left_child and curr.right_child:
                    min_child = self.min_right_subtree(curr.right_child)
                    curr.data = min_child.data
                    self._delete(curr.right_child, curr, False, min_child.data)
                elif curr.left_child == None and curr.right_child == None:
                    if prev:
                        if isleft:
                            return prev.left_child
                            prev.left_child = None
                        else:
                            return prev.right_child
                            prev.right_child = None
                    else:
                        return self.root
                        self.root = None
                elif curr.left_child == None:
                    if prev:
                        if isleft:
                            return prev.left_child
                            prev.left_child = curr.right_child
                        else:
                            return prev.right_child
                            prev.right_child = curr.right_child
                    else:
                        return self.root
                        self.root = curr.right_child
                else:
                    if prev:
                        if isleft:
                            return prev.left_child
                            prev.left_child = curr.left_child
                        else:
                            return prev.right_child
                            prev.right_child = curr.left_child
                    else:
                        return self.root
                        self.root = curr.left_child
            elif key < curr.data:
                self._delete(curr.left_child, curr, True, key)
            else:
                self._delete(curr.right_child, curr, False, key)
        else:
            print(f"Element not found")
            
            
            
