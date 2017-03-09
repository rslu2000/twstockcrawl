import math;
csv=raw_input('choose csv file:')
print csv
rfile = open("./data/"+csv.replace('.csv','')+'.csv','r')
first=rfile.readline();
newstr=first
newdata = first.replace('\n','').split(',');
col1=float(newdata[3])
col2=float(newdata[4])
col3=float(newdata[5])
col4=float(newdata[6])
min_val=99999999999999.0
min_date=''
for line in rfile:
  olddata=line.replace('\n','')
  newstr+=olddata
  olddata=olddata.split(',');

  oldcol1=float(olddata[3])
  oldcol2=float(olddata[4])
  oldcol3=float(olddata[5])
  oldcol4=float(olddata[6])
  sqrt_val = math.sqrt((col1-oldcol1)**2+(col2-oldcol2)**2+(col3-oldcol3)**2+(col4-oldcol4)**2)
  if( min_val > sqrt_val ):
    min_val=sqrt_val
    min_date=olddata[0]
  newstr+=','+str(round(sqrt_val,2))+'\n'
rfile.close()
print newstr
print 'yesterday most like ' + min_date + ',it value:' + str(min_val)
#wfile=open(csv.replace('.csv','')+'.csv','w')
#wfile.write(newstr)
#wfile.close()
