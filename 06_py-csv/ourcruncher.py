#Talia Daniel
#SoftDev
#06
#2022-09-28
#Time Spent: 0.8 Hour

"""
DISCO:
atom adds a new line upon save (extra time to debug because i edited csv)
intro usage of .replace() and .strip()
how to include weights in random selection
typecasting converts the entire list value not just contents meaning the list syntax remains

QCC:

OPS SUMMARY:
- opens file and reads content into a string variable
- splits the string by \n using .split()
- splits each entry differently based on whether it has a quotation mark or a comma
- created dictionary using percentages as keys and names of jobs as values
- created tuple using the dict keys (percentages)
- created job list based on the dict values (jobs)
- chose a job using random.choices() with the weights attribute
- turned selection into a string removing list syntax and printed in an fstring

"""
import random

dict = {}

file1 = open("occupations.csv")
string = file1.read()
each_entry = string.split("\n")
for i in each_entry:
    if '"' in i:
        parsed_arr = i.strip('"').split('"')
    else:
        parsed_arr = i.split(",")
    #print(parsed_arr)
    #print(parsed_arr[1])
    occupation = parsed_arr[0]
    percentage = float(parsed_arr[1].replace(",",""))
    dict[percentage] = []
    dict[percentage].append(occupation)

    
#print(dict)

all_percents = tuple(dict.keys())
all_occupations_arr = list(dict.values())
randomWeightedPercent = random.choices(all_occupations_arr,weights=(all_percents))
stringV = str(randomWeightedPercent).strip("[").strip("]").strip("'")
print(f"{stringV}")

#print(dict[all_percents[random.randrange(len(all_percents))]])