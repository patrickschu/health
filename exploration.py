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
sourcedict=defaultdict(list)

#this regex will allow us to extract the domain name only. it is truly un-elegant!
linkfinder=re.compile(
"://(.*?\.(?:com|co|net|org|org.uk|org.au|co.uk|com.au|co.nz|info|ca|me|ru|edu|nl|ie|us|gy|ch|tv|it|pl|com.sg|co.ke|com:8080|192))/")

#here be a loop to fill the dictionary
for item in cancerlist[1:len(cancerlist)]:
 	result=linkfinder.findall(item[3])[0]
 	# if len(result)==0:
#  	 	print item[3], result
 	if result in sourcedict:
 		sourcedict[result].append((item[0], item[5], item[4]))
 	else:
 		sourcedict[result] = [(item[0], item[5], item[4])]
#  
# 
# 
# let's look at the dictionary
# write a text file for each venue
# this is commented out just so we don't write the freaking thing every single time
for thing in sourcedict:
	print thing
	output=open("outputfiles/"+thing+".txt", "a")
	for x in sourcedict[thing]:
			output.write(x[0]+" , "+x[1]+":\n"+x[2]+ "\n\n------------\n\n")
	output.close()
	

	
print "length sourcedict", len(sourcedict)
# print sourcedict["www.forbes.com"]
#print result, item[3]
 
#ontological verbs: think, believe, wonder, know
#according to PB 2005: 166
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
#we're looking for experts, "projected expert identity"
#onthological verbs
#links?
#anton, goering is not in works cited


