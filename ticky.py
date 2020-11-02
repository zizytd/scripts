#!/usr/bin/env python3

import re
import csv
import operator

error = {}
user = {}
user1 = {}
users = {}
error_list = []
user_list = []
user1_list = []
users_new = []

with open("sys.log") as sys: #the logfile used was gotten from the course Google IT Automation with Python
    for i in sys:
        i = i.strip()
        result = re.search(r"ticky: ERROR ([\w' ]*) \((.*)\)", i) #search for a pattern that matches ERROR messages lines
        if result != None:
            result1 = result[1]
            result2 = result[2]
            error_list.append(result1) # append the first capturing group that matches the error message of each line that contains *ERROR* to the error_list list
            user_list.append(result2) # append the second capturing group that matches the username of each line to the user_list list 
            for t in error_list:
                error[t] = error_list.count(t) # add to the error dictionary each unique error message as key and the count as value
            for c in user_list:
                user[c] = user_list.count(c) # add to the user dictionary each unique username as key and the count as value
        
        result = re.search(r"ticky: INFO ([\w' ]*) .*\((.*)\)", i) #search for a pattern that matches INFO messages lines
        if result != None:
            result2 = result[2] 
            user1_list.append(result2) #append the second capturing group that matches the username of each line that contains *INFO* to the user1_list list 
            for d in user1_list:
                user1[d] = user1_list.count(d) # add to the user1 dictionary each unique username as key and the count as value
print(error)
print(user)
print(user1)

# joining user and user1 dictionaries as one dictionary with one key and two values(inside a tuple).
# if keys in user not present in user1, add a new key to user1 and assign it a value of zero.
# joining two dictionaries, the two dictionaries must have the same set of keys.
for keys in user.keys(): 
    if keys not in user1.keys():
        user1[keys] = 0 
ds = [user1, user]
for k in user1.keys():
  users[k] = tuple(users[k] for users in ds)
print(users)
# sort the error dictionary by count(from the largest to the smallest
error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
error.insert(0,("Error", "Count")) # insert a new first index value to the sorted dictionary
# sort the users dictionary by username(a-z)
users = sorted(users.items(), key=operator.itemgetter(0)) 
users.insert(0,("Username", ("INFO", "ERROR"))) # insert a new first index value to the sorted dictionary
# joining a tuple that contains another tuple e.g ("ac",("3","4")) as one tuple e.g ("ac","3","4")
for i in users:
    t = (i[0] + ' ' + ' '.join([str(x) for x in i[1]])).split()
    t = tuple(t)
    users_new.append(t)

print(error)
print(users)
print(users_new)
# creating a new csv file  by parsing the error sorted dictionary
with open("error_message.csv", "w") as error_message:
    writer = csv.writer(error_message)
    writer.writerows(error)
# creating a new csv file by parsing the user_new list.
with open("user_statistics.csv", "w") as user_statistics:
    writer = csv.writer(user_statistics)
    writer.writerows(users_new)


                
            

            

