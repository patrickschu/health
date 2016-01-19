import codecs
import csv
import os
from collections import defaultdict
import re


f=open("PCsample.csv", "r")
csvread=csv.reader(f)



#note the format: ['uniq', 'id', 'timestamp', 'url', 'content', 'author']
#150001 lines

#we're saving this as a Windows comma-separated spreadsheet

#put the whole thing into a list
cancerlist=[]

for row in csvread:
	cancerlist.append(row)

print "start"
##how many authors do we have
print "number of posts", len(cancerlist) - 1
authordict=defaultdict(tuple)

for item in cancerlist[1:len(cancerlist)]:
	if item[5] in authordict:
		authordict[item[5]] = authordict[item[5]] + (item[0], item[4])
	else:
		authordict[item[5]] = (item[0], item[4])
	

# for thing in authordict:
# 	if len(authordict[thing]) == 6:
# 		print len(authordict[thing])/2, ",", thing #, authordict[thing]
	
print "number of authors", len(authordict)
