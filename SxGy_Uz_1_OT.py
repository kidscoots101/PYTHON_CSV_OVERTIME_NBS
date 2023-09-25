"""
Recording link: xxxxxxxxxxxxxxx

1.	Staff Overtime Pay: 
You are given 1_OT.csv file by the Chief Technical Officer (CTO) in the department during an
 interview for an intern position in the Data Analytics department of a manufacturing company. 
 This file contains the working hours of 1200 staff in the company on a particular day. 
 Each record corresponds to one unique staff in the file. The file contains information on StaffID, 
 Department, Total Hours clocked for the day. The normal working hour for all staff is 8 hours, 
 any additional hours after the first 8 hours is considered as overtime (OT). The OT hours is capped 
 at 4 hours maximum. This is to ensure that the staff do not overwork themselves for additional pay. 
 This would mean that even a staff works for 20 hours, he/she will still be paid 8 hours normal rate 
 and 4 hours OT rate. The finance department uses this file for payroll computation.

Provide your solution based on the following requirements:
•	The company CEO would like to know the OT payments of the 1200 staff in the given file.
•	You are required to tabulate the result in the following format:
__________________________________________________
| Department Number |  Number of people working OT |
__________________________________________________
|                   |                              |
__________________________________________________
	
To value add to the analytics, your interviewer would like you to think of one additional analysis 
that the management of the company may be interested to find out. Present your suggested solution 
and explain how such analysis add values to the company.
"""
import csv
with open('1_OT.csv') as file:
    reader = csv.reader(file)
    count = 0
    ot_dict = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0
    }
    for i in reader:
        # i[2] is hours worked
        if i[2] == "Total Hours clocked":
            None
        elif int(i[2]) > 8:
            ot_dict[i[1]] += 1
with open("2_OT.csv", 'w') as final_dict:
    final_dict.write("Department Number,Number of OT(s)\n") 
    for department_number in sorted(ot_dict.keys()):
        ot_value = ot_dict[department_number]
        final_dict.write(f"{department_number},{ot_value}\n")
            
