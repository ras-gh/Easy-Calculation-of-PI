#A program to calculate the value of PI using an easy approximation formula

#start with the integer 3
#calculcate the value of sin(3)
#add this on to 3
#now truncate the result to 4 decimal places
#keep iterating the above step but starting with 
#the result of the previous calculation

import math
start=3
roundamount=3
extravalue= math.sin(start)
approxpi=start+extravalue
print("Program to calculate PI using an approximation method")
print(f"Initial approximation is {approxpi}")
for i in range(1,20):

    approxpi+=math.sin(approxpi)
    approxpi=round(approxpi,roundamount)
    print(f"{approxpi} to {roundamount} decimal places")
    roundamount+=1

#The maximum number of decimal places displayed in the terminal seems to be 15




