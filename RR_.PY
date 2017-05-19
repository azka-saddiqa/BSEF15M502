process= {}		#for process arrival and burst time
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
		process[i+1]=[arrival_time_list[i],burst_time_list[i],i+1]
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
def displayGanttChart(itera,start,quantum_time):
	total_time=start
	count_num_of_processes=0
	index=1
	next_process_index=itera+1
	while(count_num_of_processes!=itera):
		remaining_CPU_time=(process.get(index)[1])- quantum_time
		if(remaining_CPU_time<0):
			total_time=total_time+process.get(index)[1]
			print start, "____________" , total_time, "P" , process.get(index)[2] , "Completed "
			count_num_of_processes=count_num_of_processes+1
		if(remaining_CPU_time==0):
			total_time=total_time+quantum_time
			print start, "____________" , total_time,"P" ,process.get(index)[2], "Completed "
			count_num_of_processes=count_num_of_processes+1
		if(remaining_CPU_time > 0):
			total_time=total_time + quantum_time
			print start, "____________" , total_time,"P" , process.get(index)[2]
		if(process.get(index)[1]>quantum_time):
			process[next_process_index]=[process.get(index)[0],remaining_CPU_time,process.get(index)[2]]
			next_process_index=next_process_index+1
		start=total_time
		index=index+1
	print "\n"	
#-------------------------------------------------------------------------------------------------------
num_of_process= input(" Enter the number of Processes : \n")
time_slice= input (" Enter quantum time for RR: ")
start_time=getInput(num_of_process)
display_data(num_of_process)
check_Idle_Time(start_time)
displayGanttChart(num_of_process,start_time,time_slice)




