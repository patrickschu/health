import os, re, nltk, string, codecs, csv
#from n

print "start"
#read in each file

inputfiles=os.listdir("outputfiles_speakers")
#inputfiles=["usmessageboard.com_OnePercenter.txt", "facebook.com_10206966179415036.txt", "061006_*guest.txt"]
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
		print "alarm!! tag extracter has found more than 1 result\n----\n\n"
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
	return result
	

#set up csv file
filename="healthoutput_0328"
outputfile=open(filename+".csv", "a")
logfile=open(filename+"_log.csv", "a")
writer=csv.writer(outputfile, dialect="excel")
header=['Filename','wordcount', 'think', 'believe', 'wonder', 'know', 'thinkfreq', 'believefreq', 'wonderfreq', 'knowfreq', 'ontofreq']
writer.writerow(header)

#extract text and speakers for csv file
for fili in inputfiles:
	try:
		#set up the inputfile
		inputfile=open("outputfiles_speakers/"+fili, "r")
		inputtext=inputfile.read()
	
		#get the speaker name
		speaker=tagextracter(inputtext, "speaker", fili)
		speakertext=speaker+".txt"
		#extract text&count words
		text=tagextracter(inputtext, "text", fili)
		#splittext=nltk.wordpunct_tokenize(text)
		splittext=[i for i in nltk.wordpunct_tokenize(text)  if i not in string.punctuation]
		wordcount=float(len(splittext))
		#we;re not worrying about punctuation as in this context we don't expect any
	
		# #get the variables
# 		#note that we can add e.g. third person forms
# 		#or e.g. exclude negation and focus on 1st person only
 		think=featureextracter(text, "(think|thought)", fili)
		believe=featureextracter(text, "(believe|believed)", fili)
		wonder=featureextracter(text, "(wonder|wondered)", fili)
		know=featureextracter(text, "(know|knew|known)", fili)
		outputvalues=[len(think), len(believe), len(wonder), len(know)]
		outputfloats=[float(i) for i in outputvalues]
		outputfreqs=[i / wordcount for i in outputfloats]
		overallfreq=sum(outputfloats)/wordcount
		final=[speakertext]+[wordcount]+outputfloats+outputfreqs+[overallfreq]
	
		# #write up the csv file
# 		outputfile.write(speaker+","+
# 		str(wordcount)+","+
# 		",".join([str(i) for i in outputfloats])+","+
# 		",".join([str(i) for i in outputfreqs])+","+
# 		str(overallfreq)+"\n")
		
# 		#write up the csv file
# 		outputfile.write(speaker+"\t"+
# 		str(wordcount)+"\t"+
# 		"\t".join([str(i) for i in outputfloats])+"\t"+
# 		"\t".join([str(i) for i in outputfreqs])+"\t"+
# 		str(overallfreq)+"\n")
		
		
#write up the csv file
 		
 		writer.writerow(final)
 		
	
		#and the log
		logfile.write(speaker+".txt,"+
		" ".join(think)+","+
		" ".join(believe)+","+
		" ".join(wonder)+","+
		" ".join(know)+"\n")
		
	except Exception, e: 
		print "Alarm", fili, e

outputfile.close()
logfile.close()
print "finish\n---------\n\n\n"
# from Pennebaker 2005: ontological verbs: think, believe, wonder, know
#Excluded files for strange formatting
#
#/Users/ps22344/Downloads/outputfiles_speakers/060336_earie.txt
#/Users/ps22344/Downloads/outputfiles_speakers/060336_anwar.txt	

#what about users posting links

#note issues with quoted text

#some "speakers" are collections of unregistered posters
	
	


