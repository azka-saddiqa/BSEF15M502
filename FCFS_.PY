
process= {}		#for process arrival and burst time
time={}			#for the turn-arround time and waiting time of respective process
arrival_time_list=[]
burst_time_list=[]
num_of_process=0
start_time=0
#-----------------------------------------------------------------------------------------
def getInput(itera):
	for i in range (0,itera):
		arrival=input("Enter arrival time of the process")
		if(i==0):
			start_time=arrival	
		arrival_time_list.append(arrival)
		burst=input("Enter Burst time of the process")
		burst_time_list.append(burst)
		process[i+1]=[arrival_time_list[i],burst_time_list[i]]
	return start_time
#--------------------------------------------------------------------------------------------------
def display_data(itera):
	print "\nArrival.Time"  ,"        " , "Burst.Time"
	for index in range (0,itera):
		print "   ", process.get(index+1)[0] ,"                " , process.get(index+1)[1]	
#---------------------------------------------------------------------------------------------------
def check_Idle_Time(starting_point):
	if(starting_point>0):
		print "\n0 ------", starting_point , " CPU's Idle Time\n"
#---------------------------------------------------------------------------------------------------
def displayGanttChart(itera,start):
	total_time=start
	for index in range (1,itera+1):
		b_time=process.get(index)[1]
		total_time= total_time+b_time;
		turn_around_time=total_time- process.get(index)[0]
		wait_time=start-process.get(index)[0]
		print start , "_______" ,total_time,  "P",index , " Completed "	
		start=total_time
		time[index]=[turn_around_time,wait_time]
	print "\n"	
#-------------------------------------------------------------------------------------------------------
def display_average_waiting_time(itera):
	sum1=0
	for i in range (0,itera):
		print "Waiting time of P" , i+1," = " , time.get(i+1)[1]
		sum1=sum1+time.get(i+1)[1]
	print "\n Average Waiting time = " , (sum1/itera), "\n" 
#-------------------------------------------------------------------------------------------------------------
def display_average_turnAround_time(itera):
	sum2=0
	for i in range (0,itera):
		print "Turn-arround time of P" , i+1," = " , time.get(i+1)[0]
		sum2=sum2+time.get(i+1)[0]
	print "\n Average Turn-around time = " , (sum2/itera), "\n" 
#--------------------------------------------------------------------------------------------------------
num_of_process= input(" Enter the number of Processes : \n")
start_time=getInput(num_of_process)
display_data(num_of_process)
check_Idle_Time(start_time)
total=displayGanttChart(num_of_process,start_time)
display_average_turnAround_time(num_of_process)
display_average_waiting_time(num_of_process)


