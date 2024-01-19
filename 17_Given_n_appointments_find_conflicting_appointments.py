appointments = [ [[1,5],[3,7],[2,6],[10,15],[5,6],[4,100]] , [[3,7],[2,6],[10,15],[5,6],[4,100]] ]
for a in appointments:
    print("finding conflicts for ", a)
    for i,appointment in enumerate(a):
        print("Appointments:", i, appointment)
        start,end = appointment  #current appointment
        for j in range (i+1,len(a)):
            print("Compare Appointments:", j, a[j])
            cond1 ,cond2 = False, False
            start_next_app,end_next_app = a[j]
            #Check if next appointment is before current appointment  
            if (start >= end_next_app): cond1 = True 
            #Check if the next appointment is after current appointment
            if  (end <= start_next_app): cond2 = True
            if (cond1 == False and cond2==False):      
                print("[%d,%d] conflicts with [%d,%d]" % (start_next_app,end_next_app,start,end))
