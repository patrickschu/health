import codecs
import csv
import os


f=open("PCsample.csv", "r")
csvread=csv.reader(f)



#note the format: ['id', 'timestamp', 'url', 'content', 'author']


count=0

for row in csvread:
	print row
	count=count+1
	if count > 22:
		break
	


print "assi"


##how many posts, authors do we have






##sort according to source




##then what
