#!/usr/bin/rscript

#treato data overview
setwd("/Users/ps22344/Documents")
treat=read.csv("LWIC_and_onto_merged_over50_0328.csv", header=T)

#rank by anaytical thinking, 1st per pl and 2nd pers sg, cognitive processes (cogproc), 
#insight (which is part of cogproc), certainty


colnames(treat1)
treat1=treat
treat1$analyticrank=rank(-treat1$Analytic, ties.method="min")
treat1$cogprocrank=rank(-treat1$cogproc, ties.method="min")
treat1$insightrank=rank(-treat1$insight, ties.method="min")
treat1$certaintyrank=rank(-treat1$certain, ties.method="min")
treat1$ontorank=rank(-treat1$ontofreq, ties.method="min")
treat1$werank=rank(-treat1$we, ties.method="min")
treat1$yourank=rank(-treat1$you, ties.method="min")


#treat1[1:100, c("Filename", "ontofreq", "ontorank")]
write.csv(treat1, "treato_with_rankings_ranksums_0328.csv")

listi=c('analyticrank','cogprocrank','insightrank','certaintyrank','ontorank',
'werank', 'yourank')

for (l in listi)
{
print (l);
print (summary(treat1[[l]]))
	
}
write.csv(cor(treat1[,c(107:113)]))



treat1$ranksum_no_pronouns=rowSums(treat1[,c(107:111)])
summary(treat1$ranksum)

treat1[1:20, c(listi, "ranksum")]

t=treat1[order(treat1$ranksum),]
write.csv(t, "treato_ranking_0328.csv")



# [1] "X"            "Filename"     "wordcount"    "think"        "believe"     
#   [6] "wonder"       "know"         "thinkfreq"    "believefreq"  "wonderfreq"  
#  [11] "knowfreq"     "ontofreq"     "Segment"      "WC"           "Analytic"    
#  [16] "Clout"        "Authentic"    "Tone"         "WPS"          "Sixltr"      
#  [21] "Dic"          "function."    "pronoun"      "ppron"        "i"           
#  [26] "we"           "you"          "shehe"        "they"         "ipron"       
#  [31] "article"      "prep"         "auxverb"      "adverb"       "conj"        
#  [36] "negate"       "verb"         "adj"          "compare"      "interrog"    
#  [41] "number"       "quant"        "affect"       "posemo"       "negemo"      
#  [46] "anx"          "anger"        "sad"          "social"       "family"      
#  [51] "friend"       "female"       "male"         "cogproc"      "insight"     
#  [56] "cause"        "discrep"      "tentat"       "certain"      "differ"      
#  [61] "percept"      "see"          "hear"         "feel"         "bio"         
#  [66] "body"         "health"       "sexual"       "ingest"       "drives"      
#  [71] "affiliation"  "achieve"      "power"        "reward"       "risk"        
#  [76] "focuspast"    "focuspresent" "focusfuture"  "relativ"      "motion"      
#  [81] "space"        "time"         "work"         "leisure"      "home"        
#  [86] "money"        "relig"        "death"        "informal"     "swear"       
#  [91] "netspeak"     "assent"       "nonflu"       "filler"       "AllPunc"     
#  [96] "Period"       "Comma"        "Colon"        "SemiC"        "QMark"       
# [101] "Exclam"       "Dash"         "Quote"        "Apostro"      "Parenth"     
# [106] "OtherP"