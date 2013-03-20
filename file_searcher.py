import os
import sys
import fnmatch
import glob
matches=[]
data=sys.argv[2]
path=sys.argv[1]
ind=0
f=open(data,"r")
f1=open("list1","w")
for query in f:
	flag=0
	str0=""
	str1=''
	matches[:]=[]
	for ch in query:
		if(flag==0):
			if(ch!='\t'):
				str0=str0+ch
			else:
				flag=1
		else:
			if(ch!='\n'):
				str1=str1+ch
	for root, dirnames, filenames in os.walk(path):
		for filename in  fnmatch.filter(filenames, str1):
				#print f
	                matches.append(os.path.join(root,filename))
	#for match in matches:
	#	print match		
	words=[]
	result=[]
	length=len(str0)
	'''if(length==0):
		for match in matches:
			result.append(match)
	'''
	for i in range(0,length+1):
		for j in "abcdefghijklmnopqrstuvwxyz0123456789":
			str2=str0[:i]+j+str0[i:]
			words.append(str2)
	for i in range(0,length):
	        for j in "abcdefghijklmnopqrstuvwxyz0123456789":
	                str2=str0[:i]+j+str0[(i+1):]
	                words.append(str2)
	if(length!=1):
		for i in range(0,length):
			str2=str0[:(i)]+str0[(i+1):]
			words.append(str2)
	#for word in words:
	#	print word
	for r,d,f in os.walk(path):
	    for files in f:
	        for word in words:
			#if word in files:
				#print files
			if files.startswith(word+".") or (files==word):
				str3=os.path.join(r,files)
				#if(str3 in result):
				#	str3=str3
				#else:
				if(str3 in matches):
	             			if(str3 in result):
						str3=str3
					else:
						f1.write(str0+"\t\t"+str1+"\t\t"+r+"\t\t"+files+"\n")
						result.append(str3)
f1.close()
str0=""
str1=""
f1=open("list1","r")
f2=open("list2","w")

with open("list1") as f:
    content = f.readlines()
dirc=[]
for line in content:
	words=line.split()
	count=0
	for an_line in content:
		an_words=an_line.split()
		if(an_words[2]==words[2]):
			count=count+1
	str3=words[2]+"\t"+str(count)
	if str3 in dirc:
		str3=str3
	else:
		dirc.append(str3)	
for i in dirc:
	f2.write(i+"\n")

