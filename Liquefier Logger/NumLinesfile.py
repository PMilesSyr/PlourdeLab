import os
os.chdir(r'C:\Users\Patrick\Documents\Plourde Lab\Liquefier Logger')
f = open("fulldata2.txt")


# get the number of lines in the file

with open("fulldata2.txt") as f:
	numlines1 = sum(1 for _ in f)
