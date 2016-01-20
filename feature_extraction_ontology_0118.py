import os
import re

print "start"
#read in each file
#inputfiles=os.listdir("outputfiles_speakers")
inputfiles=["usmessageboard.com_OnePercenter.txt", "facebook.com_10206966179415036.txt", "061006_*guest.txt"]
print "number of files", len(inputfiles)


# tagextracter takes the inputfile and any kind of tag that 
# encloses the text to be extracted
def tagextracter(inputtext, tag, fili):
	regexstring="<"+tag+">(.*?)</"+tag+">"
	regexfinder=re.compile(regexstring, re.DOTALL)
	result=regexfinder.findall(inputtext)
	if len(result) > 1:
		print tag 
		print result[1]
		print "alarm!! extracter has found more than 1 result"
	if len(result) < 1: 
		print fili
		print tag
		print "alarm"
		print "too short"
	else:
		return result[0]
		
#featureextracter takes the inputstring and the search term; in this case an ontological
#verb
def featureextracter(inputtext, search_term, fili):
	regexstring=" "+search_term+" "
	regexfinder=re.compile(regexstring)
	result=regexfinder.findall(inputtext)
	print len(result)
	print result
	return result
	

#set up csv file
outputfile=open("healthoutput.csv", "a")


#extract text and speakers for csv file
for fili in inputfiles:
	try:
		#set up the inputfile
		inputfile=open("outputfiles_speakers/"+fili)
		inputtext=inputfile.read()
		
		#get the speaker name
		speaker=tagextracter(inputtext, "speaker", fili)
		#extract text&count words
		text=tagextracter(inputtext, "text", fili)
		splittext=text.split()
		wordcount=len(splittext)
		
		#get the variables
		#note that we can add e.g. third person forms
		#or e.g. exclude negation and focus on 1st person only
		think=featureextracter(text, "(think|thought)", fili)
		believe=featureextracter(text, "(believe|believed)", fili)
		wonder=featureextracter(text, "(wonder|wondered)", fili)
		know=featureextracter(text, "(know|knew|known)", fili)
		
		#write up the csv file
		outputfile.write(
		speaker+","+
		wordcount+","+
		len(think)+","+
		len(believe)+","+
		len(wonder)+","+
		len(know)+"\n"
		)
	except: 
		print "Alarm", fili

outputfile.close()
print "finish\n---------\n\n\n"
# from Pennebaker 2005: ontological verbs: think, believe, wonder, know
		
	
	


