import pandas,os
os.chdir(os.path.join("/Users","ps22344","Documents"))
one=pandas.read_csv("healthoutput_0328.csv")
print one.columns
two=pandas.read_csv("treato_LIWC2015.csv")
print two.columns
merged=one.merge(two,on="Filename")
print len(merged)
merged.to_csv('LWIC_and_onto_merged_0328.csv')
