#treato data overview
setwd("/Users/ps22344/Documents")
treat=read.csv("LWIC_and_onto_merged_over50_0328.csv", header=T)

summarizer=function(column) 
{
	print (c('length:', length(column)));
	print (c('mean:', mean(column)));
	print (c('median:', median(column)));
	print (c('standard deviation:', sd(column)));
	print (c('range', range(column)));
		
}





for (item in colnames(treat)[3:length(colnames(treat))])
{
	
	print ("--------");
	print (c("VARIABLE NAME:", item));
	summarizer(treat[[item]]);
	print ("--------");
	writeLines("\n\n***************\n\n");

}




for (item in colnames(treat)[3:length(colnames(treat))])
{
	
	print ("--------");
	print (c("VARIABLE NAME:", item));
	print (cor(treat[[item]], treat$ontofreq));
	print ("--------");
	writeLines("\n\n***************\n\n");

}


# a couple plots
png("certain.png")
boxplot(treat$certain, main="Certainty")
dev.off()

#
t=treat[order(-treat$ontofreq),]
t[1:20,c(2, 12)]


g=treat[order(-treat$certain),]
g[1:20,c(2, 59)]




  # [1] "X"            "Filename"     "wordcount"    "think"        "believe"      "wonder"       "know"         "thinkfreq"   
  # [9] "believefreq"  "wonderfreq"   "knowfreq"     "ontofreq"     "Segment"      "WC"           "Analytic"     "Clout"       
 # [17] "Authentic"    "Tone"         "WPS"          "Sixltr"       "Dic"          "function."    "pronoun"      "ppron"       
 # [25] "i"            "we"           "you"          "shehe"        "they"         "ipron"        "article"      "prep"        
 # [33] "auxverb"      "adverb"       "conj"         "negate"       "verb"         "adj"          "compare"      "interrog"    
 # [41] "number"       "quant"        "affect"       "posemo"       "negemo"       "anx"          "anger"        "sad"         
 # [49] "social"       "family"       "friend"       "female"       "male"         "cogproc"      "insight"      "cause"       
 # [57] "discrep"      "tentat"       "certain"      "differ"       "percept"      "see"          "hear"         "feel"        
 # [65] "bio"          "body"         "health"       "sexual"       "ingest"       "drives"       "affiliation"  "achieve"     
 # [73] "power"        "reward"       "risk"         "focuspast"    "focuspresent" "focusfuture"  "relativ"      "motion"      
 # [81] "space"        "time"         "work"         "leisure"      "home"         "money"        "relig"        "death"       
 # [89] "informal"     "swear"        "netspeak"     "assent"       "nonflu"       "filler"       "AllPunc"      "Period"      
 # [97] "Comma"        "Colon"        "SemiC"        "QMark"        "Exclam"       "Dash"         "Quote"        "Apostro"     
# [105] "Parenth"      "OtherP" 
