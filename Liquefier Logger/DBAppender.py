import pymongo
from pymongo import MongoClient
import time
import datetime
from bson.objectid import ObjectId

client = MongoClient()
db = client.test
liqLog = db.liqLog

print("Running DBAppender")

numEntries = db.liqLog.count()
print("Log file contained ", numEntries, "entries")

import os
os.chdir(r'C:\Users\Patrick\Documents\Plourde Lab\Liquefier Logger')
f = open("2015_06(Jun).txt")
linelist = f.readlines()


with open("2015_06(Jun).txt") as f:
	numlines1 = sum(1 for _ in f)
	print(numlines1)

if numlines1 > numEntries:

	dif = numlines1 - numEntries

	for b in range(dif, 0, -1):

		# prepare line of file for becoming a document
		
		s = numlines1 - b

		length = len(linelist[s])

		# index all tabs in the string

		n = 0
		tablist = []
		for i in range(0, length):
			#print("i = ", i)

			if linelist[s][i] == "	":
				tablist.append(i)
				n += 1
				#print("n = ", n)

		# index all slashes in string

		m = 0
		slashlist = []
		for i in range(0, length):

			if linelist[s][i] == "/":
				slashlist.append(i)
				m += 1

		# index all colons in string

		p = 0
		colonlist = []
		for i in range(0, length):
			
			if linelist[s][i] == ":":
				colonlist.append(i)
				p += 1


		# Now assign values to all variables (this is done in a very spaghetti way)

		num1 = int(tablist[0]) - 4
		num2 = int(slashlist[0])
		num3 = num2 + 1
		num4 = int(slashlist[1])

		yearchar = linelist[s][num1:tablist[0]]
		monthchar = linelist[s][0:num2]
		daychar = linelist[s][num3:num4]

		num5 = int(tablist[0]) + 1
		num6 = int(colonlist[0])
		num7 = num6 + 1
		num8 = int(colonlist[1])
		num9 = num8 + 1
		num10 = num9 + 2
		num11 = num10 + 1
		num12 = num11 + 2

		hourchar = linelist[s][num5:num6]
		minutechar = linelist[s][num7:num8]
		secondchar = linelist[s][num9:num10]
		ampmchar = linelist[s][num11:num12]

		pres = float(linelist[s][int(tablist[1])+1:tablist[2]])

		heat = float(linelist[s][int(tablist[2])+1:tablist[3]])

		temp = float(linelist[s][int(tablist[3])+1:tablist[4]])

		level_cm = float(linelist[s][int(tablist[4])+1:tablist[5]])

		placehold = linelist[s][int(tablist[5])+1:tablist[6]]
		if placehold == "< 1":
			level_L = "< 1"
		elif placehold == "> 150":
			level_L = "> 150"
		else:
			level_L = float(placehold)

		water_in = float(linelist[s][int(tablist[8])+1:tablist[9]])

		water_out = float(linelist[s][int(tablist[9])+1:tablist[10]])

		oil_T = float(linelist[s][int(tablist[10])+1:tablist[11]])

		he_gas_T = float(linelist[s][int(tablist[11])+1:tablist[12]])

		lo_pres = float(linelist[s][int(tablist[13])+1:tablist[14]])

		hi_pres = float(linelist[s][int(tablist[14])+1:tablist[15]])

		ln2 = float(linelist[s][int(tablist[15])+1:tablist[16]])

		cyl_p = float(linelist[s][int(tablist[16])+1:tablist[17]])

		he_purity = float(linelist[s][int(tablist[17])+1:int(tablist[17])+5])

		xdate = datetime.datetime(int(yearchar), int(monthchar), int(daychar), int(hourchar), int(minutechar), int(secondchar), 00)
		print(xdate)

		# Make the document

		newdata = {"xid": s,
				   "date": xdate,
				   "month": monthchar,
				   "day": daychar,
				   "year": yearchar,
				   "hour": hourchar,
				   "minute": minutechar,
				   "second": secondchar,
				   "ampm": ampmchar,
				   "pres": pres,
				   "heat": heat,
				   "temp": temp,
				   "level_cm": level_cm,
				   "level_L": level_L,
				   "water_in": water_in,
				   "water_out": water_out,
				   "oil_T": oil_T,
				   "he_gas_T": he_gas_T,
				   "lo_pres": lo_pres,
				   "hi_pres": hi_pres,
				   "ln2": ln2,
				   "cyl_p": cyl_p,
				   "he_purity": he_purity,
				   }

		db.liqLog.insert(newdata)

newcount = db.liqLog.count()

if newcount == numEntries:
	print("liqLog collection appended successfully")
else:
	print("liqLog collection append failed. Missing ", newcount - numEntries, " entries")

print("Log file now contains ", numlines1, " entries")