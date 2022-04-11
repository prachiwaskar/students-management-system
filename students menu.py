#Menu driven prg using dictionary,list for students
#1 Add 2 Update  3 Delete  4 Select All records  5 Select specific record
stList={}
stdict={}
flag=1
while flag==1:
     print("1: Add Record 2: Update  3: Delete  4: Select all records 5: Select specific 6: Exit")
     ch=int(input("Enter choice : "))
     if ch==1:
         rn=int(input(f"Enter value for rn"))
         name=input(f"Enter value for name")
         m1 = int(input(f"Enter value for m1"))
         m2=int(input(f"Enter value for m2"))
         tot=m1+m2
         per=tot/2
         stdict.update({rn:{"rn":rn, "name" : name,"m1":m1,"m2":m2,"total":tot,"per":per}})
     elif ch==2:
         r_up=int(input("enter rno to update : "))
         print(f"Original data = {stdict[r_up]}")
         n_up=input("Enter name to update : ")
         m1_up=int(input("Enter m1 to update : "))
         m2_up = int(input("Enter m2 to update : "))
         tot_up=m1_up+m2_up
         per_up=tot_up/2
         st_up={"rn":r_up,"name" : n_up,"m1":m1_up,"m2":m2_up,"total":tot_up,"per":per_up}
         stdict[r_up]=st_up
         print("Student details updated")
         print(f"Updated data = {stdict[r_up]}")
     elif ch == 3:
         r_up = int(input("enter rno to delete : "))
         print(f"Original data = {stdict[r_up]}")
         stdict.pop(r_up)
         print("Student details deleted")
     elif ch==4:
         print("RN   Name   M1   M2    Total    Per")
         for s,sts in stdict.items():
             #print(s,end="  ")
             for x in sts:
                print(sts[x], end="    ")
             print("")
     elif ch==5:
         choice1=int(input("Enter search key to get data : 1:rn, 2:name 3: per"))
         if choice1==1:
            r_view=int(input("Enter rn to see details "))
            flagr = 0
            for s, sts in stdict.items():
                if sts['rn'] == r_view:
                    flagr += 1
                    if flagr == 1:
                        print("Rn    name    m1   m2   Total   Per")
                        print(f"{sts['rn']}   {sts['name']}   {sts['m1']}   {sts['m2']}   {sts['total']}   {sts['per']}")
                    else:
                        print(f"{sts['rn']}   {sts['name']}   {sts['m1']}   {sts['m2']}   {sts['total']}   {sts['per']}")
            if flagr == 0:
                print(f"Student having rno {r_view} is not found")

         elif choice1==2:
            n_view=input("Enter name to see details ")
            flagn=0
            for s, sts in stdict.items():
                if sts['name']==n_view:
                    flagn+=1
                    if flagn==1:
                        print("Rn    name    m1   m2   Total   Per")
                        print(f"{sts['rn'][]}   {sts['name']}   {sts['m1']}   {sts['m2']}   {sts['total']}   {sts['per']}")
                    else:
                        print(f"{sts['rn']}   {sts['name']}   {sts['m1']}   {sts['m2']}   {sts['total']}   {sts['per']}")
            if flagn==0:
                print(f"Student having name {n_view} is not found")
            else:
                print(f"{flagn} students have name = {n_view}")
         elif choice1==3:
            p_view=float(input("Enter per to see student details "))
            flagp=0
            for s, sts in stdict.items():
                if sts['per']==p_view:
                    flagp+=1
                    if flagp==1:
                        print("Rn    name    m1   m2   Total   Per")
                        print(f"{sts['rn']}   {sts['name']}   {sts['m1']}   {sts['m2']}   {sts['total']}   {sts['per']}")
                    else:
                        print(f"{sts['rn']}   {sts['name']}   {sts['m1']}   {sts['m2']}   {sts['total']}   {sts['per']}")
            if flagp==0:
                print(f"Student having per {p_view} is not found")
            else:
                print(f"{flagp} students have per = {p_view}")
     elif ch==6:
         flag=0
         break


