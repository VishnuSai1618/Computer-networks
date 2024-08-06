si = int(input("Enter the no of processes - "))
bt,tat,wt,bt1 = [],[],[],[]
rem,tot_time,time,co = 0,0,0,0
for i in range(si):
    bt.append(int(input("Enter Burst Time for process {} -".format(i+1))))
    tat.append(0)
    tot_time = tot_time+bt[i]
    bt1.append(bt[i])
sli = int(input("Enter the size of time slice - "))
while time<tot_time :
    rem = co%si
    if bt[rem]>=sli:
        bt[rem] = bt[rem]-sli
        time = time+sli
        if bt[rem] == 0:
            tat[rem] = time
    elif bt[rem] == 0 :
        bt[rem] = 0
    else :
        time = time + bt[rem]
        bt[rem] = 0
        tat[rem] = time
    co = co + 1
for i in range(si) :
    wt.append(tat[i]-bt1[i])
print("PROCESS\t\tBRUST TIME\tWAITING TIME\tTURNAROUND TIME")
for i in range(si) :
    print("P",i,"\t\t",bt1[i],"\t\t",wt[i],"\t\t",tat[i],sep="")
avg1=sum(wt)/si
avg2=sum(tat)/si
print("Average Waiting Time --",avg1)
print("Average Turnaround Time --",avg2)
