
print (" Hello Azka!Welcome to python! ")
process= {}             #for the proceses and its A.t and B.t rspectively
turn_time={}		#for the turn-arround time of respective process
arrival=[]		#list for arrival time input from user
burst=[]		#list for burst time input from user
t_time=0
w_time=0		
sum1=0
sum2=0
itera= input(" How many processes you want to enter : \n" )
for i in range (0,itera):
	num=input("Enter arrival time of the process")
	if(i==0):
		min1=num	
	elif(min1>num):
		min1=num	
	arrival.append(num)
	num1=input("Enter CPU time of the process")
	burst.append(num1)
	process[burst[i]]=[arrival[i],i+1]
#-------------input data by user--------------------------
print "\nProcesses     "," A.T"  ,"           " , " B.T"
for index in range (0,itera):
	print "P" , index+1, "             " , arrival[i] ,"            " , burst[i]	

burst.sort()	#sort the burst time in asecending order
total=min1
#---------------for idle time exception------------------
if(total>0):
	print "\n0 ------", total , "idle time\n"
#---------------scheduling the proceeses-----------------
for i in range (0,itera):
	index=process.get(burst[i])[1]
	total=total+burst[i]
	t_time=total- process.get(burst[i])[0]
	w_time=min1-process.get(burst[i])[0]
	print min1, "____________" , total, " P",index , "Completed "
	min1=total	
 	turn_time[burst[i]]=[t_time,w_time]
print "\n"
#-----------waiting time-------------
for i in range (0,itera):
	print "Waiting time of P" , i+1," = " , turn_time.get(burst[i])[1]
	sum1=sum1+turn_time.get(burst[i])[1]
print "\n Average Waiting time = " , (sum1/itera), "\n" 
#-----------turn around time----------
for i in range (0,itera):
	print "Turn-arround time of P" , i+1," = " , turn_time.get(burst[i])[0]
	sum2=sum2+turn_time.get(burst[i])[0]
print "\n Average Turn-around time = " , (sum2/itera), "\n" 
print " Total Running time = " , total, "\n" 

