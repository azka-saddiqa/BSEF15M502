print (" Hello Azka!Welcome to python! ")
process= {}		#for the proceses and its A.t and B.t rspectively
turn_time={}		#for the turn-arround time of respective process
arrival=[]		#list for arrival time input from user
burst=[]		#list for burst time input from user
itera= input(" How many processes you want to enter : \n" )

for i in range (0,itera):
	num=input("Enter arrival time of the process")	
	arrival.append(num)
	num1=input("Enter CPU time of the process")
	burst.append(num1)
	process[i+1]=[arrival[i],burst[i],i+1]

#-------------input data by user--------------------------	
print "\nProcesses     "," A.T"  ,"           " , " B.T"
for index in range (0,itera):
	print "P" , index+1, "             " , process.get(index+1)[0] ,"            " , process.get(index+1)[1]	
j=1
min1=0
total=0
for index in range (0,itera+1):
	duration=process.get(index+1)[1]
	temp=0
	for i in range (0,duration):
 		temp=temp+1
		remaining= duration-temp
		if(j<=itera):
			arrival_next_process=process.get(j)[0]			
			if(temp==arrival_next_process):
				if(process.get(j)[1]<remaining):
					itera=itera+1
					process[itera]=[process.get(index+1)[0],remaining,index+1]	
					break
		j+=1
	total=total+temp
	if(temp==duration):
		print min1, "____________" , total,"P" ,process.get(index+1)[2], "Completed "
	elif(temp!=duration):
		print min1, "____________" , total,"P" , process.get(index+1)[2]
	min1=total
	
	



