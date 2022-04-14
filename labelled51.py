import sys
import csv
import os
import re

file1 = open("D:\\code\\test.csv","r")#input file
file2 = open("D:\\code\\seed.txt","r")#input file
file3 = open("D:\\code\\senttag.txt","r")#input file
file4 = open("D:\\code\\special.txt","r")#input file
outf1 = open("tweet_class.txt","w")
outf2 = open("class_tweet.txt","w")


labelhash = {}
arr1 = []
arr2 = []
i = 0
cnt = 0
seedhash = {}
specialhash = {}
csv_f1 = csv.reader(file1)
for r in csv_f1:
    s1 = r[5]
    #print(s1)
    ss = input("press enter key")
    #r1 = s1.lower()
    arr1.append(s1)
    i=i+1
    #print(i)
for f2 in file2:
    l1 = f2.split(":")
    pp = l1[0]
    c = l1[1]
    p = pp.split(" ")
    pl = len(p)
    if pl>1:
        p1 = p[0]
        p2 = p[1]
        ss1 = p1+"-"+p2
        #seesdhash = ss1
        seedhash[ss1] = c
    else:
        p1 = p[0]
        seedhash[p1] = c

for f4 in file4:
    l11 = f4.split(":")
    pp1 = l11[0]
    c1 = l11[1]
    specialhash[pp1] = c1
    
    
for f3 in file3:
    sp = f3.split("::")
    rs = sp[0]
    f4 = sp[1]
    #cnt = cnt+1
    #print(f3)
    #ss=input("press enter key")
    arr2 = f4.split("),")
    for temp1 in arr2:
        prev_tag = ""
        prev_wd = ""
        #temp1 = arr2[i]
        w1 = temp1.split(",")
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
            wd = re.sub("-","",wd14)
            #print(wd)
            ps2 = re.sub("\\'","",ps1)
            ps3 = re.sub("\)","",ps2)
            ps = re.sub("\]","",ps3)
            ps4 = re.sub("^\s+","",ps)
            ps = re.sub("\s+$","",ps4)
            present_tag = ps
            if prev_tag == '' and present_tag == "NN":
                if wd in seedhash:
                    c = seedhash[wd]
                    labelhash[c] = labelhash.get(c,0)+1
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag == '' and present_tag == "JJ": 
                if wd in seedhash:
                    c = seedhash[wd]
                    labelhash[c] = labelhash.get(c,0)+1
                    #print("uni",c)
                prev_tag = present_tag
                prev_wd = wd
            elif  prev_tag != '' and present_tag == "RB": 
                if wd in seedhash:
                    c = seedhash[wd]
                    labelhash[c] = labelhash.get(c,0)+1
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag != '' and present_tag == "VB": 
                if wd in seedhash:
                    c = seedhash[wd]
                    labelhash[c] = labelhash.get(c,0)+1
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag != '' and present_tag == "VBP": 
                if wd in seedhash:
                    c = seedhash[wd]
                    labelhash[c] = labelhash.get(c,0)+1
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag != '' and present_tag == "NNP": 
                if wd in seedhash:
                    c = seedhash[wd]
                    labelhash[c] = labelhash.get(c,0)+1
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag == 'JJ' and present_tag == 'NN': 
                wrd=prev_wd+"-"+wd
                if wrd in seedhash:
                    c = seedhash[wrd] 
                    labelhash[c] = labelhash.get(c,0)+1
                    #print("bi",c)
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag == 'NN' and present_tag == 'NN':
                wrd=prev_wd+"-"+wd
                if wrd in seedhash:
                    c = seedhash[wrd]
                    labelhash[c] = labelhash.get(c,0)+1
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag != '' and present_tag == "NN":
                if wd in seedhash:
                    c = seedhash[wrd] 
                    labelhash[c] = labelhash.get(c,0)+1
                prev_tag = present_tag
                prev_wd = wd
            elif prev_tag != '' and present_tag == "JJ":
                if wd in seedhash:
                    c = seedhash[wd] 
                    labelhash[c] = labelhash.get(c,0)+1
                    #print("not equal to uni",c)
                prev_tag = present_tag
                prev_wd = wd
            if wd in seedhash:
                    c = seedhash[wd] 
                    labelhash[c] = labelhash.get(c,0)+1
            elif wd in specialhash:
                c1 = specialhash[wd]
                labelhash[c1] = labelhash.get(c1,0)+1
            else:
                prev_tag = present_tag
                prev_wd = wd
                
    
    sys.stdout.write("noun     %s %d \n" %(k,v))
    items = [(v, k) for k, v in labelhash.items()]
    items.sort()
    items.reverse()
    items=[(k,v) for v, k in items]
    for k, v in items:
        print("%s: %s" % (k, v))         
        temp2 = arr1[cnt]
        temp3 = k.strip()
        print(labelhash)
        
        break
   
    #print(temp3+"  "+rs)
    outf1.write(rs)
    outf1.write("   ")
    outf1.write(temp3)
    outf1.write("\n")
    
    outf2.write(temp3)
    outf2.write("   ")
    outf2.write(rs)
    outf2.write("\n")
    cnt=cnt+1
    #print(cnt)
    temp3 = ""
    #ss=input("press enter key")
    #print("\n")

    labelhash = {}
print("end")
    

file1.close()
file2.close()
file3.close()
file4.close()
outf1.close()    
outf2.close()
