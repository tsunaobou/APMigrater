import os
import re

b = os.getcwd()
idx = 0
s = ""
with open(b+'/apmusic.txt','r',encoding="utf-8_sig") as f:
	for line in f:
		a = line.split('\t')
		#print(a)
		print(a[0],a[3])
		s+=a[3] + '---' + a[0] + "\n"

with open(b+"/songs.txt","w",encoding="utf-8_sig") as o:
	o.write(s)