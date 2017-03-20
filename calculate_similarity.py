#!/usr/bin/python
# -*- coding: UTF-8 -*-
from math import *
filename=raw_input('input file.csv:')
rfile=open('./data/'+filename.replace('.csv','')+'.csv','r')
firstRow= rfile.readline()
newstr=firstRow
firstRow=firstRow.replace('\n','')
firstRowArr=firstRow.split(',')
firstCol1=float(firstRowArr[3])
firstCol2=float(firstRowArr[4])
firstCol3=float(firstRowArr[5])
firstCol4=float(firstRowArr[6])
firstCol5=0.0
if(not (firstRowArr[7]=='')):
  firstCol5=float(firstRowArr[7])

for Row in rfile:
  Row=Row.replace('\n','')
  rowArr=Row.split(',')
  col1=float(rowArr[3])
  col2=float(rowArr[4])
  col3=float(rowArr[5])
  col4=float(rowArr[6])
  col5=0.0
  if(not (rowArr[7]=='')):
    col5=float(rowArr[7])
  similarity=sqrt( (firstCol1 - col1)**2 + (firstCol2 - col2)**2 + (firstCol3 - col3)**2 +(firstCol4 - col4 )**2 + (firstCol5 - col5)**2 )
  newstr+=Row+','+str(round(similarity,2))+'\n'
rfile.close()
print newstr

wfile=open(filename.replace('.csv','')+'.csv','w')
wfile.write(newstr)
wfile.close()
