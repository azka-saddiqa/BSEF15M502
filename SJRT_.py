print ("Welcome to python!!! ")
processes= {}		
time_of_scheduling=0				#for the proceses and its A.t and B.t rspectively
turn_around_time_of_processes={}		#for the turn-arround time of respective process
list_of_arrival_time=[]					#list for arrival time input from user
list_of_burst_time=[]					#list for burst time input from user


#Function Definitions
#-------------------------------input data from user--------------------------------------------------------------------------------------
def getInput(iterations):
	for i in range (0,iterations):
		arrival_time=input("Enter arrival time of the process")
		if(i==0):
			start_time=arrival_time	
		list_of_arrival_time.append(arrival_time)
		burst_time=input("Enter CPU time of the process")
		list_of_burst_time.append(burst_time)
		pId=i+1
		processes[i]=[list_of_arrival_time[i],list_of_burst_time[i],pId]
	return start_time

#------------------------------check idle time-------------------------------------------------------------------------------------------
def check_Idle_Time(starting_time):
	if(starting_time>0):
		print "\n0 ____________ ", starting_time , " CPU's Idle Time!!\n"

#-------------------------------display process info----------------------------------------------------------------------------------------
def display_process_info(iterations):
	print "\nProcesses     "," Arrival Time"  ,"           " , " Burst Time"
	for index in range (0,iterations):
		print "P" , processes.get(index)[2], "                " , processes.get(index)[0] ,"                        " , processes.get(index)[1]	
	
#-----------------------------------------check the remaining time0----------------------------------
def check_remaining_time(itera,current_dura,duration,index_,process_index):
	#arrival_next=processes.get(index_)[0]
	arrival_next=0	
	for i in range (0,duration):
 		current_dura+=1
		remaining_time= duration-current_dura
		if(index_<=itera):
			print processes
			arrival_next=processes.get(index_)[0]			
			if(current_dura==arrival_next):
				if(processes.get(index_)[1]<remaining_time):
					itera=itera+1
					processes[itera]=[processes.get(process_index+1)[0],remaining_time,process_index+1]	
					break
		index_+=1
	return itera
#-----------------------------------------display gannt chart -------------------------------------
def display_gantt_chart(current_dura,duration,start,i):
	if(current_dura==duration):
		print start, "____________" ,time_of_scheduling,"P" ,processes.get(i)[2], "Completed "
	elif(current_dura!=duration):
		print start, "____________" ,time_of_scheduling,"P" , processes.get(i)[2]
	return time_of_scheduling

#---------------------------------------sechule the process--------------------------------------------
def schedule_processes(iterations,start):
	index=1
	duration=0
	time_of_scheduling=start
	for i in range (0,iterations+1):
		duration=processes.get(i)[1]
		current_duration=0
		iterations=check_remaining_time(iterations,current_duration,duration,index,i)
		time_of_scheduling=time_of_scheduling+current_duration	
		start=display_gantt_chart(current_duration,duration,start,i)

# ***********************************************...Driving Program...*****************************************************

no_of_processes=input(" How many processes you want to enter : \n" )	
start_time_=getInput(no_of_processes)
display_process_info(no_of_processes)
check_Idle_Time(start_time_)
print processes
schedule_processes(no_of_processes,start_time_)









