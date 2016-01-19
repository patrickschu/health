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


##sort according to source
sourcedict=defaultdict(tuple)

#this regex will allow us to extract the domain name only. it is truly un-elegant!
linkfinder=re.compile(
"://(.*?\.(?:com|co|net|org|org.uk|org.au|co.uk|com.au|co.nz|info|ca|me|ru|edu|nl|ie|us|gy|ch|tv|it|pl|com.sg|co.ke|com:8080|192))/")

#here be a loop
for item in cancerlist[1:len(cancerlist)]:
 	result=linkfinder.findall(item[3])[0]
 	# if len(result)==0:
#  	 	print item[3], result
 	if result in sourcedict:
 		sourcedict[result] = sourcedict[result] + (item[0], item[4])
 	else:
 		sourcedict[result] = (item[0], item[4])
#  
# 
# 
# 
for thing in sourcedict:
 	if len(sourcedict[thing]) > 199:
 		print thing, ",", len(sourcedict[thing])/2
# 	
	
print "length sourcedict", len(sourcedict)
# print sourcedict["www.forbes.com"]
#print result, item[3]
 

print "finish"
# 	
# 
# 
# 
# for item in cancerlist[1:len(cancerlist)]:
# 	if item[5] in authordict:
# 		authordict[item[5]] = authordict[item[5]] + (item[0], item[4])
# 	else:
# 		authordict[item[5]] = (item[0], item[4])
# 	

# for thing in authordict:
# 	if len(authordict[thing]) == 6:
# 		print len(authordict[thing])/2, ",", thing #, authordict[thing]
# 	
# print "number of authors", len(authordict)
# 
# print authordict['author']
##then what


#what do links tell us

