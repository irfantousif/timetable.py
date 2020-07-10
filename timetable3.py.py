time_table = {'monday': {'1st-hour': 'physics', '2nd-hour': 'maths', '3rd-hour': 'social', '4th-hour': 'biology',
                         '5th-hour': 'computer', '6th-hour': 'chemistry'},
              'tuesday': {'1st-hour': 'maths', '2nd-hour': 'social', '3rd-hour': 'biology', '4th-hour': 'computer',
                          '5th-hour': 'chemistry', '6th-hour': 'physics'},
              'wednesday': {'1st-hour': 'social', '2nd-hour': 'biology', '3rd-hour': 'computer',
                            '4th-hour': 'chemistry', '5th-hour': 'physics', '6th-hour': 'maths'},
              'thursday': {'1st-hour': 'biology', '2nd-hour': 'computer', '3rd-hour': 'chemistry',
                           '4th-hour': 'physics', '5th-hour': 'maths', '6th-hour': 'social'},
              'friday': {'1st-hour': 'computer', '2nd-hour': 'chemistry', '3rd-hour': 'physics', '4th-hour': 'maths',
                         '5th-hour': 'social', '6th-hour': 'biology'}}
a = input("enter a day of time table:  ")
for k, v in time_table.items():
    if k == a:
        print(k)
        for hr,subj in v.items():
            print(hr,subj)

b = input("enter a subject from time table:  ")
for k, v in time_table.items():
   for hr,subj in v.items():
       if subj == b:
            print(k,hr)

nhrs=0
c = input("enter a subject from time table for number of hours in a week:  ")
for k, v in time_table.items():
   for hr,subj in v.items():
       if subj == c:
           nhrs+=1
print("Number of Hours: "+ str(nhrs))
d=input("enter a subject to delete: ")
for k,v in time_table.items():
    for h,s in v.items():
        if s==d:
            v[h]='--'
            break
print(time_table)
e=input("enter a subject to update: ")
f=input("enter which subject: ")
for k,v in time_table.items():
    for h,s in v.items():
        if s == e:
            v[h]= f
            break
print(time_table)