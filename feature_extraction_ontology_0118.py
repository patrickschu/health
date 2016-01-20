import os
import re

print "start"
#read in each file
inputfiles=os.listdir("outputfiles_speakers")
#inputfiles=["usmessageboard.com_OnePercenter.txt", "060336_anwar.txt", "060336_earie.txt",
# "facebook.com_10206966179415036.txt"]
print "number of files", len(inputfiles)


# tagextracter takes the inputfile and any kind of tag that 
# encloses the text to be extracted
def tagextracter(inputtext, tag):
	regexstring="<"+tag+">(.*?)</"+tag+">"
	regexfinder=re.compile(regexstring, re.DOTALL)
	result=regexfinder.findall(inputtext)
	if len(result) > 1:
		print tag 
		print result[1]
		print "alarm!! extracter has found more than 1 result"
	if len(result) < 1: 
		print tag
		print "alarm"
		print "too short"
	else:
		return result[0]


#extract text only
for fili in inputfiles:
	try:
		#set up the inputfile
		inputfile=open("outputfiles_speakers/"+fili)
		inputtext=inputfile.read()
		#extract text&count words
		text=tagextracter(inputtext, "text")
		splittext=text.split()
		wordcount=len(splittext)
		#get the speaker name
		speaker=tagextracter(inputtext, "speaker")
	except: 
		print "Alarm", fili
		
print "finish\n---------\n\n\n"
#extracter takes the inputfile and any kind of tag that encloses the text to be extracted
#note how quoted text is a real issue for us
