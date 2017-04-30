print (" Hello Azka!Welcome to python! ")
process= {}		#for the proceses and its A.t and B.t rspectively
turn_time={}		#for the turn-arround time of respective process
arrival=[]		#list for arrival time input from user
burst=[]		#list for burst time input from user
itera= input(" How many processes you want to enter : \n" )
quantum_t= input (" Enter quantum time for RR: \n")

for i in range (0,itera):
	num=input("Enter arrival time of the process")
	if(i==0):
		min1=num	
	elif(min1>num):
		min1=num	
	arrival.append(num)
	num1=input("Enter CPU time of the process")
	burst.append(num1)
	process[i+1]=[arrival[i],burst[i],i+1]

#-------------input data by user--------------------------	
print "\nProcesses     "," A.T"  ,"           " , " B.T"
for index in range (0,itera):
	print "P" , index+1, "             " , process.get(index+1)[0] ,"            " , process.get(index+1)[1]	
total=min1
#---------------for idle time exception------------------
if(total>0):
	print "\n0 ------", total , "idle time\n"
count=0
index=1
a=itera+1
#---------------scheduling the proceeses-----------------
while(count!=itera):
	rem=(process.get(index)[1])- quantum_t
	if(rem<0):
		total=total+process.get(index)[1]
		print min1, "____________" , total, "P" , process.get(index)[2] , "Completed "
		count=count+1
	if(rem==0):
		total=total+quantum_t
		print min1, "____________" , total,"P" ,process.get(index)[2], "Completed "
		count=count+1
	if(rem > 0):
		total=total+quantum_t
		print min1, "____________" , total,"P" , process.get(index)[2]
	if(process.get(index)[1]>quantum_t):
		process[a]=[process.get(index)[0],rem,process.get(index)[2]]
		a=a+1
	min1=total
	index=index+1
print "\n"
print " Total Running time = " , total, "\n"

 




