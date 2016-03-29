import csv
inputi=open("LWIC_and_onto_merged_0328.csv", "r")
outputi=open("LWIC_and_onto_merged_over50_0328.csv", "w")


outputrows=[]
reader=csv.reader(inputi, dialect="excel")

#get header out of the way
header=reader.next()
print header[2]

#item[2] is the wordcount
for line in reader:
 	if float(line[2]) > 49:
 		outputrows.append(line)
 
print "the outputfile has {} rows".format(len(outputrows))
# 
print "writing"
writer=csv.writer(outputi, dialect="excel")
writer.writerow(header)
writer.writerows(outputrows)

inputi.close()
outputi.close()

print "finish"