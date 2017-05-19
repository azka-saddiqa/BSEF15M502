process= {}
waiting_list={}		#for process arrival and burst time
arrival_time_list=[]
burst_time_list=[]
num_of_process=0
start_time=0
#-------------------------------------------------------------------------------------
def getInput(iterations):
	for i in range (0,iterations):
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
#-----------------------------------------------------------------------------------------
def RR_technique(remaining_CPU_time,index,total_time,start,counter,next_index,quantum_time):
	if(remaining_CPU_time<0):
		total_time=total_time+process.get(index)[1]
		print start, "____________" , total_time, "P" , process.get(index)[2] , "Completed "
		counter=counter+1
	if(remaining_CPU_time==0):
		total_time=total_time+quantum_time
		print start, "____________" , total_time,"P" ,process.get(index)[2], "Completed "
		counter=counter+1
	if(remaining_CPU_time > 0):
		total_time=total_time + quantum_time
		print start, "____________" , total_time,"P" , process.get(index)[2]
	if(process.get(index)[1]>quantum_time):
		process[next_process_index]=[process.get(index)[0],remaining_CPU_time,process.get(index)[2]]
		next_index=next_index+1
	start=total_time
	return counter
#-----------------------------------------------------------------------------------------
def check_waiting_queue():
	if not bool(waiting_list):
		return 1
	if bool(waiting_list):
		if(total_time==waiting_list(i)[2]):
			print start, "____________" , total_time, "P" , process.get(index)[2] , "Completed "
			return 0
#-----------------------------------------------------------------------------------------
def displayGanttChart(itera,start,quantum_time,io_time):
	total_time=start
	count_num_of_processes=0
	index=1
	next_process_index=itera+1
	while(count_num_of_processes!=itera):
		remaining_CPU_time=process.get(index)[1]-quantum_time
		if(check_waiting_queue()==0):
			count_num_of_processes+=1
		if(index%2==0):
			total_time=total_time +io_time
			remaining_quantum_time=quantum_time-io_time
			time_to_auxilary_queue=total_time+io_time
			print start, "____________" , total_time,"P" , process.get(index)[2]
			waiting_list[process.get(index)[2]]=[remaining_quantum_time,remaining_CPU_time,time_to_auxilary_queue]
		elif(index%2==1):
			count_num_of_processes=RR_technique(remaining_CPU_time,index,total_time,start,count_num_of_processes,next,quantum_time)
	
		start=total_time
		index=index+1
	print "\n"	

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
num_of_process= input(" Enter the number of Processes : \n")
time_slice= input (" Enter quantum time for RR: ")
io_time=input(" Enter the time for the input waiting:")
process_type=input(" Enter the process nature for IO time i.e even no process(prress 1) , odd no process(press 0)")
start_time=getInput(num_of_process)
display_data(num_of_process)
check_Idle_Time(start_time)
#if(process_type==1):
displayGanttChart(num_of_process,start_time,time_slice,io_time)



