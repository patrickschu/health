###Health 2. py, Extracting ontological verbs

import codecs
import csv
import os
from collections import defaultdict
import re

## we need to organize dataset by author

f=open("PCsample_2.csv", "r")
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
authordict=defaultdict(list)

for item in cancerlist[1:len(cancerlist)]:
	if item[5] in authordict:
		authordict[item[5]].append((item[0], item[4]))
	else:
		authordict[item[5]] = [(item[0], item[4])]
	

for thing in authordict:
	print thing
	uniqlist=[]
	output=open("outputfiles_speakers/"+thing+".txt", "a")
	output.write("<file> <speaker>"+thing+"</speaker> <text> ")
	for x in authordict[thing]:
		output.write(x[1])
		uniqlist.append(x[0])
	output.write(" </text> <uniques>"+",".join(uniqlist)+"</uniques> </file>")
	output.close()
	
print "number of authors", len(authordict)
