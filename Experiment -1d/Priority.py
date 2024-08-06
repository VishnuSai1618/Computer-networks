si = int(input("Enter the number of processes - "))
bt,tat,wt,bt1,pro = [],[],[],[],[]
pri = [0 for i in range(si)]
bt1 = [0 for i in range(si)]
pro = [0 for i in range(si)]
for i in range(si) :
    li =[]
    li = input("Enter the Burst Time & Priority of Process {} - ".format(i)).split(" ")
    bt.append(int(li[0]))
    pri[i] = int(li[1])
    bt1[pri[i]-1] = bt[i]
for i in range(si) :
    pro[i] = pri.index(i+1)
sum1 = 0
for i in range(si):
    wt.append(sum1)
    sum1=sum1+bt1[i]
    tat.append(sum1)
print("PROCESS\t\tPRIORITY\t\tBRUST TIME\tWAITING TIME\tTURNAROUND TIME")
for i in range(si) :
    print(pro[i],"\t\t",i+1,"\t\t",bt1[i],"\t\t",wt[i],"\t\t",tat[i],sep="")
avg1=sum(wt)/si
avg2=sum(tat)/si
print("Average Waiting Time --",avg1)
print("Average Turnaround Time --",avg2)
