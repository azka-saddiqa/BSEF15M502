print (" Hello Azka!  welcome to python! ")
process= {}		#for the proceses and its A.t and B.t rspectively
turn_time={}		#for the turn-arround time of respective process
arrival=[]		#list for arrival time input from user
burst=[]		#list for burst time input from user
t_time=0
w_time=0		
sum1=0
sum2=0
itera=input("Enetr number of Proceeses you want to enter!:")
for i in range (0,itera):
	num=input("Enter arrival time of the process")
	if(i==0):
		min_stime=num	
	elif(min_stime>num):
		min_stime=num	
	arrival.append(num)
	num1=input("Enter CPU time of the process")
	burst.append(num1)
	process[i+1]=[arrival[i],burst[i]]
#-------------input data by user--------------------------	
print "\nProcesses     "," A.T"  ,"           " , " B.T"
for index in range (0,itera):
	print "P" , index+1, "             " , process.get(index+1)[0] ,"            " , process.get(index+1)[1]	
total=min_stime 
#---------------for idle time exception------------------
if(total>0):
	print "\n0 ------", total , "idle time\n"
#---------------scheduling the proceeses-----------------
for index in range (0,itera):
	b_time=process.get(index+1)[1]
	total= total+b_time
	t_time=total- process.get(index+1)[0]
	w_time=min_stime-process.get(index+1)[0]
	print min_stime , "_______" ,total,  " P", index+1 , " Completed "
	min_stime=total	
 	turn_time[index+1]=[t_time,w_time]
print "\n"
#-----------waiting time-------------
for i in range (0,itera):
	print "Waiting time of P" , i+1," = " , turn_time.get(i+1)[1]
	sum1=sum1+turn_time.get(i+1)[1]
print "\n Average Waiting time = " , (sum1/itera), "\n" 
#-----------turn around time----------
for i in range (0,itera):
	print "Turn-arround time of P" , i+1," = " , turn_time.get(i+1)[0]
	sum2=sum2+turn_time.get(i+1)[0]
print "\n Average Turn-around time = " , (sum2/itera), "\n" 
print " Total Running time = " , total, "\n"

 
