
import nltk
import re
import os
import csv
import sys

normal = {'it\'s':'it is','i':'I','I\'m':'I am','im':'I am','ua':'you are','ur':'your','i\'m':'I am','that\'s':'that is','would\'ve':'would have','could\'ve':'could have','did\'nt':'did not','does\'nt':'does not','he\'s':'he is','i\'ve':'I have','wasn\'t':'was not','you\'re':'you are','she\'s':'she is','we\'re':'we are','they\'re':'they are','that\'s':'that is','who\'s':'who is','what\'s':'what is','what\'re':'what are','where\'s':'where is','when\'s':'when is','why\'s':'why is','how\'s':'how is','i\'ll':'I will','you\'ll':'you will','he\'ll':'he will','she\'ll':'she will','it\'ll':'it will','we\'ll':'we will','they\'d':'they would','they\'ll':'they will','that\'ll':'that will','who\'ll':'who will','I\'d':'I would','you\'d':'you would','he\'d':'he would','she\'d':'she would','we\'d':'we would','they\'d':'they would','i\'d':'I had','isn\'t':'is not','aren\'t':'are not','haven\'t':'have not','hasn\'t':'has not','can\'t':'cannot','sd':'sweet dream','fn':'fine','lol':'laughing out loud'}

f1 = open("D:\\code\\test.csv","r") #input file- training file/test file
outfile1 = open("tagging.txt","w")
outfile = open("senttag.txt","w")
outf1 = open("processedtext_withcomma.txt",'w')
csv_f1 = csv.reader(f1)
for r in csv_f1:
    s = r[5]
    r1 = s.lower()
    temp = ""
    token = []
    #wds=nltk.word_tokenize(r1)
    r1=re.sub(r'^"','',r1)
    r1=re.sub(r'"$','',r1)
    #print(r1)
    wds=r1.split( )
    for w in wds:
	#print (w)
	#print ("\n")
        w1 = w.strip('\``')
        w = w1.strip('.!?,')
        if re.search(r"^@([A-Za-z])+", w):
            pass
        elif re.search("^http://", w):
            pass
            #temp=temp+" "+tg
        elif re.search("^\d+", w):
            pass
        elif re.search("www.//([a-zA-z])+",w):
            pass
        elif re.search("#([A-Za-z])+",w):
            pass
            #tg="("+w+",<SYB>)"
            #temp=temp+" "+tg
        elif w == "":
            pass
        elif w in normal:
            nwd =normal[w]
            nwds = nwd.split( )
            for w1 in nwds:
                token.append(w1)
        else:
            token.append(w)
    #print(token)
    outf1.write("%s" %token)
    tg = nltk.pos_tag(token)
    #print(tg)
    outfile1.write("%s" % tg )
    outfile1.write("\n")
    outfile.write("%s" % s )
    outfile.write("::" )
    outfile.write("%s" % tg )
    outfile.write("\n")
print("tag end")
f1.close()
outfile1.close()
outfile.close()
outf1.close()

noun_hash = {}
adj_hash = {}
noun_noun_hash = {}
adj_noun_hash = {}
verb_hash = {}
adverb_hash = {}
nns_hash = {}
vbp_hash = {}
c_adj_hash = {}
c_verb_hash = {}
c_adverb_hash = {}

outfile2 = open("noun.txt","w")                                     
outfile3 = open("adj.txt","w")                                                   
outfile4 = open("adj_noun.txt","w")                     
outfile5 = open("noun_noun.txt","w")
outfile6 = open("verb.txt","w")
outfile7 = open("adverb.txt","w")
outfile8 = open("NNS.txt","w")
outfile9 = open("VBP.txt","w")
outfile10 = open("vb_rb_vbp_adj.txt","w")                                     
outfile11 = open("vb_rb_vbp_verb.txt","w")                                                   
outfile12 = open("vb_rb_vbp_adverb.txt","w")  

f2 = open("D:\\code\\tagging","r")#input file
for r1 in f2:    
    a1 = r1.split("),")
    #print(a1)
    prev_tag = ""
    prev_wd = ""
    for t1 in a1:
        w1 = t1.split(",")
        ln = len(w1)
        if ln<2:
            pass
        else:
            wd1 = w1[0]
            ps1 = w1[1]
            wd2 = re.sub("\'","",wd1)
            wd3 = re.sub("\(","",wd2)
            wd4 = re.sub("\[","",wd3)
            wd5 = re.sub("\"","",wd4)
            wd6 = re.sub("\.","",wd5)
            wd7 = re.sub("\;","",wd6)
            wd8 = re.sub("\*","",wd7)
            wd9= re.sub("\:","",wd8)
            wd10 = re.sub("\/","",wd9)
            wd11 = re.sub("^\s+","",wd10)
            wd12= re.sub("\s+$","",wd11)
            wd13 = re.sub("@","",wd12)
            wd14 = re.sub("#","",wd13)
            wd15 = re.sub("-","",wd14)
            wd16 = re.sub("=","",wd15)
            wd = re.sub("~","",wd16)
            #print(wd)
            ps2 = re.sub("\\'","",ps1)
            ps3 = re.sub("\)","",ps2)
            ps = re.sub("\]","",ps3)
            ps4 = re.sub("^\s+","",ps)
            ps = re.sub("\s+$","",ps4)
            t = wd+' '+ps
            
            #print(wd,ps)       
            present_tag = ps
            if re.search(r'(^&(.+))',wd):
                pass
            elif prev_tag == '' and present_tag == "NN": 
                noun_hash[wd] = noun_hash.get(wd,0)+1
                #print(wd,present_tag)
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag == '' and present_tag == "JJ": 
                adj_hash[wd] = adj_hash.get(wd,0)+1
                #print(wd,present_tag)
                prev_tag = present_tag
                prev_wd = wd
            elif  prev_tag == '' and present_tag == "RB": 
                adverb_hash[wd] = adverb_hash.get(wd,0)+1
                #print(wd,present_tag)
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag == '' and present_tag == "VB": 
                verb_hash[wd] = verb_hash.get(wd,0)+1
                #print(wd,present_tag)
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag == '' and present_tag == "NNS": 
                nns_hash[wd] = nns_hash.get(wd,0)+1
                #print(wd,present_tag)
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag == '' and present_tag == "VBP": 
                vbp_hash[wd] = vbp_hash.get(wd,0)+1
                #print(wd,present_tag)
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag == 'JJ' and present_tag == 'NN': 
                wrd=prev_wd+" "+wd
                adj_noun_hash[wrd] = adj_noun_hash.get(wrd,0)+1
                #print(wd,present_tag)
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag == 'NN' and present_tag == 'NN':
                wrd=prev_wd+" "+wd
                noun_noun_hash[wrd] = noun_noun_hash.get(wrd,0)+1
                #print(wd,present_tag)
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag != '' and present_tag == "NN":
                noun_hash[wd] = noun_hash.get(wd,0)+1
                #print(wd,present_tag)
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag != '' and present_tag == "JJ":
                adj_hash[wd] = adj_hash.get(wd,0)+1
                #print(wd,present_tag)
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag == 'VB' or 'RB' or 'VBP' and present_tag == 'JJ': 
                wrd=prev_wd+" "+wd
                c_adj_hash[wrd] = c_adj_hash.get(wrd,0)+1
                #print(wd,present_tag)
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag == 'VB' or 'RB' or 'VBP' and present_tag == 'VB': 
                wrd=prev_wd+" "+wd
                c_verb_hash[wrd] = c_verb_hash.get(wrd,0)+1
                #print(wd,present_tag)
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag == 'VB' or 'RB' or 'VBP' and present_tag == 'RB': 
                wrd=prev_wd+" "+wd
                c_adverb_hash[wrd] = c_adverb_hash.get(wrd,0)+1
                #print(wd,present_tag)
                prev_tag = present_tag
                prev_wd = wd
            else:
                prev_tag = present_tag
                prev_wd = wd
                #print(wd,present_tag)

#print("pos end")
f2.close()
totnnfq = 0
cumnnfq = 0
for k in noun_hash.keys():
    v=noun_hash[k]
    totnnfq=totnnfq+v
    sys.stdout.write("noun     %s %d \n" %(k,v))
items = [(v, k) for k, v in noun_hash.items()]
items.sort()
items.reverse()
items=[(k,v) for v, k in items]
for k, v in items:
    #print("%s: %s" % (k, v))
    cumnnfq=cumnnfq+v
    tp = float(v/totnnfq)
    cumtp = float(cumnnfq/totnnfq)*100
    temp = k+' '+ str(v) +'   '+ str(tp) +'  '+ str(cumnnfq) +'   '+str(cumtp)
    outfile2.write(temp)
    outfile2.write("\n")

totjjfq = 0
cumjjfq = 0
for k in adj_hash.keys():
    v=adj_hash[k]
    totjjfq=totjjfq+v
    sys.stdout.write("adj     %s %d \n" %(k,v))
items = [(v, k) for k, v in adj_hash.items()]
items.sort()
items.reverse()
items=[(k,v) for v, k in items]
for k, v in items:
    #print("%s: %s" % (k, v))
    cumjjfq=cumjjfq+v
    tp = float(v/totjjfq)
    cumtp = float(cumjjfq/totjjfq)*100
    temp = k+' '+ str(v) +'   '+ str(tp) +'  '+ str(cumjjfq) +'   '+str(cumtp)
    outfile3.write(temp)
    outfile3.write("\n")

totvbfq = 0
cumvbfq = 0
for k in verb_hash.keys():
    v=verb_hash[k]
    totvbfq=totvbfq+v
    sys.stdout.write("verb     %s %d \n" %(k,v))
items = [(v, k) for k, v in verb_hash.items()]
items.sort()
items.reverse()
items=[(k,v) for v, k in items]
for k, v in items:
    #print("%s: %s" % (k, v))
    cumvbfq=cumvbfq+v
    tp = float(v/totvbfq)
    cumtp = float(cumvbfq/totvbfq)*100
    temp = k+' '+ str(v) +'   '+ str(tp) +'  '+ str(cumvbfq) +'   '+str(cumtp)
    outfile6.write(temp)
    outfile6.write("\n")

totrbfq = 0
cumrbfq = 0
for k in adverb_hash.keys():
    v=adverb_hash[k]
    totrbfq=totrbfq+v
    sys.stdout.write("adverb     %s %d \n" %(k,v))
items = [(v, k) for k, v in adverb_hash.items()]
items.sort()
items.reverse()
items=[(k,v) for v, k in items]
for k, v in items:
    #print("%s: %s" % (k, v))
    cumrbfq=cumrbfq+v
    tp = float(v/totrbfq)
    cumtp = float(cumrbfq/totrbfq)*100
    temp = k+' '+ str(v) +'   '+ str(tp) +'  '+ str(cumrbfq) +'   '+str(cumtp)
    outfile7.write(temp)
    outfile7.write("\n")


totnnsfq = 0
cumnnsfq = 0
for k in nns_hash.keys():
    v=nns_hash[k]
    totnnsfq=totnnsfq+v
    sys.stdout.write("nns     %s %d \n" %(k,v))
items = [(v, k) for k, v in nns_hash.items()]
items.sort()
items.reverse()
items=[(k,v) for v, k in items]
for k, v in items:
    #print("%s: %s" % (k, v))
    cumnnsfq=cumnnsfq+v
    tp = float(v/totnnsfq)
    cumtp = float(cumnnsfq/totnnsfq)*100
    temp = k+' '+ str(v) +'   '+ str(tp) +'  '+ str(cumnnsfq) +'   '+str(cumtp)
    outfile8.write(temp)
    outfile8.write("\n")

totvbpfq = 0
cumvbpfq = 0
for k in vbp_hash.keys():
    v=vbp_hash[k]
    totvbpfq=totvbpfq+v
    sys.stdout.write("vbp     %s %d \n" %(k,v))
items = [(v, k) for k, v in vbp_hash.items()]
items.sort()
items.reverse()
items=[(k,v) for v, k in items]
for k, v in items:
    #print("%s: %s" % (k, v))
    cumvbpfq=cumvbpfq+v
    tp = float(v/totvbpfq)
    cumtp = float(cumvbpfq/totvbpfq)*100
    temp = k+' '+ str(v) +'   '+ str(tp) +'  '+ str(cumvbpfq) +'   '+str(cumtp)
    outfile9.write(temp)
    outfile9.write("\n")

totjjnnfq = 0
cumjjnnfq = 0
for k in adj_noun_hash.keys():
    v=adj_noun_hash[k]
    totjjnnfq=totjjnnfq+v
    sys.stdout.write("adj-nn   %s %d \n" %(k,v))
items = [(v, k) for k, v in adj_noun_hash.items()]
items.sort()
items.reverse()
items=[(k,v) for v, k in items]
for k, v in items:
    #print("%s: %s" % (k, v))
    cumjjnnfq=cumjjnnfq+v
    tp = float(v/totjjnnfq)
    cumtp = float(cumjjnnfq/totjjnnfq)*100
    temp = k+' '+ str(v) +'   '+ str(tp) +'  '+ str(cumjjnnfq) +'   '+str(cumtp)
    outfile4.write(temp)
    outfile4.write("\n")

totnnnnfq = 0
cumnnnnfq = 0
for k in noun_noun_hash.keys():
    v=noun_noun_hash[k]
    totnnnnfq=totnnnnfq+v
    sys.stdout.write("nn-nn   %s %d \n" %(k,v))
items = [(v, k) for k, v in noun_noun_hash.items()]
items.sort()
items.reverse()
items=[(k,v) for v, k in items]
for k, v in items:
    #print("%s: %s" % (k, v))
    cumnnnnfq=cumnnnnfq+v
    tp = float(v/totnnnnfq)
    cumtp = float(cumnnnnfq/totnnnnfq)*1100
    temp = k+' '+ str(v) +'   '+ str(tp) +'  '+ str(cumnnnnfq) +'   '+str(cumtp)
    outfile5.write(temp)
    outfile5.write("\n")

totcnnfq = 0
cumcnnfq = 0
for k in c_adj_hash.keys():
    v=c_adj_hash[k]
    totcnnfq=totcnnfq+v
    sys.stdout.write("c_noun     %s %d \n" %(k,v))
items = [(v, k) for k, v in c_adj_hash.items()]
items.sort()
items.reverse()
items=[(k,v) for v, k in items]
for k, v in items:
    #print("%s: %s" % (k, v))
    cumcnnfq=cumcnnfq+v
    tp = float(v/totcnnfq)
    cumtp = float(cumcnnfq/totcnnfq)
    temp = k+' '+ str(v) +'   '+ str(tp) +'  '+ str(cumcnnfq) +'   '+str(cumtp)
    outfile10.write(temp)
    outfile10.write("\n")

totcjjfq = 0
cumcjjfq = 0
for k in c_verb_hash.keys():
    v=c_verb_hash[k]
    totcjjfq=totcjjfq+v
    sys.stdout.write("c_adj     %s %d \n" %(k,v))
items = [(v, k) for k, v in c_verb_hash.items()]
items.sort()
items.reverse()
items=[(k,v) for v, k in items]
for k, v in items:
    #print("%s: %s" % (k, v))
    cumcjjfq=cumcjjfq+v
    tp = float(v/totcjjfq)
    cumtp = float(cumcjjfq/totcjjfq)
    temp = k+' '+ str(v) +'   '+ str(tp) +'  '+ str(cumcjjfq) +'   '+str(cumtp)
    outfile11.write(temp)
    outfile11.write("\n")

totcvbfq = 0
cumcvbfq = 0
for k in c_adverb_hash.keys():
    v=c_adverb_hash[k]
    totcvbfq=totcvbfq+v
    sys.stdout.write("c_verb     %s %d \n" %(k,v))
items = [(v, k) for k, v in c_adverb_hash.items()]
items.sort()
items.reverse()
items=[(k,v) for v, k in items]
for k, v in items:
    #print("%s: %s" % (k, v))
    cumcvbfq=cumcvbfq+v
    tp = float(v/totcvbfq)
    cumtp = float(cumcvbfq/totcvbfq)*100
    temp = k+' '+ str(v) +'   '+ str(tp) +'  '+ str(cumcvbfq) +'   '+str(cumtp)
    outfile12.write(temp)
    outfile12.write("\n")
            
outfile2.close()
outfile3.close()
outfile4.close()
outfile5.close()
outfile6.close()
outfile7.close()
outfile8.close()
outfile9.close()
outfile10.close()
outfile11.close()
outfile12.close()


