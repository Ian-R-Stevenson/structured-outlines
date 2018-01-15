#csv2dot.py
#12-12-2017 14:38
#read in CSV file wityh unit data and output a dot file, csv or text for graphing
#ver 1: Unit Learning Outcomes

###
#CSV structure
#Unit Number	Unit Name	Type	ULO Text	Assessment Item	Criterion	Standard	Standard Text


import datetime
import sys
import os
import subprocess
import csv

if len(sys.argv) < 2: #no infile specified
	print 'usage: Python csv2dot.py infile [outfile (optional)]'
	exit()

if len(sys.argv)<3: #only infile specified
	outfile=sys.argv[1].split('.',1)[0]+'.dot'
	outfile=outfile.replace (" ", "_")
else:
	outfile=sys.argv[2]
	outfile=outfile.replace (" ", "_")

#with open(sys.argv[1], 'r') as infile: # Open the file for reading.
#	data = infile.read()  # Read the contents of the file into memory.

with open(sys.argv[1]) as csvfile:
	reader=csv.DictReader(csvfile)
	out_list=[] #prepare list for output
	unitname=" "



#use this for CSV output
#use this for csv style output
	for row in reader: #select ULOs
		 #outfile.write('URL: ' + row['url'] + '\n' + 'username: ' + row['username']  + '\n' + 'password: ' + row['password'] + '\n' + '\n'  )
		 if row['UnitName']!=unitname :
  		   unitname=row['UnitName']
  		   out_list.append('"'+'Bachelor of Music'+'","'+row['UnitName']+'"') #append each new item to list

		 if row['Type']=='ULO':
			 out_list.append('"'+row['UnitName']+'","'+row['ULOText']+'"') #append each new item to list
outfile=outfile.split('.',1)[0]+'EDIT.csv'
with open (outfile, 'w') as outfileHandle:
	for line in out_list:
		outfileHandle.write (line+'\n')
	print "successfully output" + outfile


#use this for graph style output
	# for row in reader: #select ULOs
	# 	 #outfile.write('URL: ' + row['url'] + '\n' + 'username: ' + row['username']  + '\n' + 'password: ' + row['password'] + '\n' + '\n'  )
	# 	 if row['UnitName']!=unitname :
  	# 	   unitname=row['UnitName']
  	# 	   out_list.append('"'+'Bachelor of Music'+'"->"'+row['UnitName']+'"') #append each new item to list
    #
	# 	 if row['Type']=='ULO':
	# 		 out_list.append('"'+row['UnitName']+'"->"'+row['ULOText']+'"') #append each new item to list
	# d=datetime.datetime.now() #timestamp curent datetime into output

#use this for output to .dot
#note outfile already .dot
# with open (outfile, 'w') as outfileHandle:
# 	outfileHandle.write ('digraph "LearningOutcomes" \n { \n //generated '+ str(d) +'\n \n graph [rankdir="TB", splines="true"];\n\n')
# 	for line in out_list:
# 		outfileHandle.write (line+';\n')
# 	outfileHandle.write ('}')
# print "successfully output" + outfile

#use this for output to draw.io
# outfile=outfile.split('.',1)[0]+'.txt'
# with open (outfile, 'w') as outfileHandle:
	# for line in out_list:
	# 	outfileHandle.write (line+'\n')
	# print "successfully output" + outfile
