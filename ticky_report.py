#!/usr/bin/env python3

import re
import csv
import operator
import pandas as pd
import subprocess

error = {}
user = {}
user1 = {}
error_list = []
user_list = []
user1_list = []

with open("sys.log") as sys:
    for i in sys:
        i = i.strip()
        result = re.search(r"ticky: ERROR ([\w ]*) \((.*)\)", i)
        if result != None:
            result1 = result[1]
            result2 = result[2]
            error_list.append(result1)
            user_list.append(result2)
            for t in error_list:
                error[t] = error_list.count(t)
            for c in user_list:
                user[c] = user_list.count(c)
        
        result = re.search(r"ticky: INFO ([\w ]*) .*\((.*)\)", i)
        if result != None:
            result2 = result[2]
            user1_list.append(result2)
            for d in user1_list:
                user1[d] = user1_list.count(d)
print(error)
print(user)
print(user1)

for keys in user.keys():
    if keys not in user1.keys():
        user1[keys] = 0
ds = [user1, user]
users = {}
for k in user1.keys():
  users[k] = ",".join([str(i) for i in (list(users[k] for users in ds))])
print(users)
error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
error.insert(0,("Error", "Count"))
users = sorted(users.items(), key=operator.itemgetter(0))
users.insert(0,("Username", "INFO", "ERROR"))

print(error)
print(users)
with open("error_message.csv", "w") as error_message:
    writer = csv.writer(error_message)
    writer.writerows(error)
with open("user_statistics1.csv", "w") as user_statistics:
    writer = csv.writer(user_statistics)
    writer.writerows(users)
with open("user_statistics1.csv") as user_statistics:
    with open("user_statistics.csv", "w") as statistics:
        statistics.write("Username,INFO,ERROR\n")

    with open("user_statistics.csv", "a") as statistics:
        for i in user_statistics:
            i = i.strip()
            if '"' in i:
                t = i.replace('"', '')
                print(t)
                statistics.write(t+"\n")

subprocess.run(["rm", "user_statistics1.csv"])



                
            

            

