# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:06:07 2021

@author: dell
"""

import pandas as pd
import matplotlib.pyplot as plt

print("\t\t\tWELCOME TO EXAMINATION MANAGEMENT SYSTEM\n\n")
print("Student Database Registration\n")

choice=int(input("Enter 0 to exit\nEnter 1 to proceed\n"))
if choice==0:
    print("OK Thanks")
elif choice==1:
    print("-"*42)
    workday=int(input("Enter the number of working days:"))
    nos=int(input("Enter the number of students:"))
    print("-"*30)
    
    e=0
    namelist=[]
    rollist=[]
    feelist=[]
    attendlist=[]
    indlist=[]
    for i in range(nos):
        e+=1
        
        print("Student",e)
        name=str(input("Enter the name of student:"))
        roll=int(input("Enter the roll number:"))
        fee=str(input("Enter the fee status ('P' for paid & 'N' for not paid):"))
        presday=int(input("Enter the number of days the student was present:"))
        attend=(presday/workday)*100
        
        namelist.append(name)
        rollist.append(roll)
        feelist.append(fee)
        attendlist.append(attend)
        indlist.append(e)
        print("*"*30)
        
        reqfee="P"
        reqattend=75.00
        
    while True:
        print("Enter the serial number to choose the option:-")
        print("1.) To show Eligible students")
        print("2.) To change the eligibility criteria")
        print("3.) Reset the eligibility criteria")
        print("4.) View the fee status and attendance status")
        print("5.) To delete the student record")
        print("6.) Print the list of all students")
        print("\tEnter 0 to exit")
        
        choice2=int(input("Enter your choice:"))
        
        namelist2=[]
        rollist2=[]
        feelist2=[]
        attendlist2=[]
        
        if choice2==1:
            liista=[]
            liistb=[]
            liistc=[]
            z=-1
            
            if reqfee=="B":
                for a in feelist:
                    z+=1
                    if a=="P" or "N":
                        liista.append(z)
            elif reqfee=="P":
                for a in feelist:
                    z+=1
                    if a=="P":
                        liista.append(z)
            elif reqfee=="N":
                for a in feelist:
                    z+=1
                    if a=="N":
                        liista.append(z)
                    
            y=-1
            for b in attendlist:
                y+=1
                if b>=reqattend:
                    liistb.append(y)
            
            x=0
            for c in liista:
                for d in liistb:
                    if c==d:
                        x+=1
                        liistc.append(c)
            
            e2=0
            indlist2=[]
            for f in liistc:
                e2+=1
                namelist2.append(namelist[f])
                rollist2.append(rollist[f])
                feelist2.append(feelist[f])
                attendlist2.append(attendlist[f])
                indlist2.append(e2)
                
            dict2={"Student":namelist2,
                       "Roll Number":rollist2,
                       "Fee Status":feelist2,
                       "Attendance":attendlist2}
            dtf2=pd.DataFrame(dict2,index=indlist2)
            print("-"*25)
            
            x1=0
            for a in feelist:
                x1+=1
            
            print("\n")
            eliglist1=["Eligible","Ineligible"]
            eliglist2=[x,x1-x]
            
            plt.title("Eligibility")
            plt.bar(eliglist1,eliglist2,color=["b","red"],width=0.3)
            plt.xlabel("Criteria")
            plt.ylabel("No. of students")
            plt.show()
            print("\n")
            
            print("The eligible students are:\n",dtf2)
            print("-"*30)
            continue
    
        elif choice2==2:
            reqfee=str(input("Enter the new fee criteria ('P' for paid,'N' for not paid & 'B' for both):"))
            reqattend=float(input("Enter the least attendance required (updated):"))
            print("Eligibility criteria updated.\n")
            print("-"*30)
            continue
        
        elif choice2==3:
            reqfee="P"
            reqattend=75.00
            print("Eligibility criteria reset.")
            print("-"*30)
            continue
        
        elif choice2==4:
            x2=0
            x3=0
            for a in feelist:
                if a=="P":
                    x2+=1
                elif a=="N":
                    x3+=1
            x4=0
            x5=0
            for a in attendlist:
                if a>=75.00:
                    x4+=1
                else:
                    x5+=1
            
            paidlist1=["Paid","Not paid"]
            paidlist2=[x2,x3]
            preslist1=["75 % and above","below 75 %"]
            preslist2=[x4,x5]
            
            plt.title("Fee Status")
            plt.bar(paidlist1,paidlist2,color=["b","red"],width=0.3)
            plt.xlabel("Criteria")
            plt.ylabel("No. of students")
            plt.show()
            print("\n")
            
            plt.title("Attendance status")
            plt.bar(preslist1,preslist2,color=["b","red"],width=0.3)
            plt.xlabel("Criteria")
            plt.ylabel("No. of students")
            plt.show()
            print("-"*30)
            
        elif choice2==5:
            delroll=int(input("Enter the roll number of the student (whose record is to be deleted):"))
            y=-1
            for k in rollist:
                y+=1
                if k==delroll:
                    rollist.pop(y)
                    namelist.pop(y)
                    feelist.pop(y)
                    attendlist.pop(y)
            print("Student record deleted.")
            print("-"*30)
            continue
        
        elif choice2==6:
            e3=0
            indlist3=[]
            for a in rollist:
                e3+=1
                indlist3.append(e3)
            dict3={"Student":namelist,
                   "Roll Number":rollist,
                   "Fee Status":feelist,
                   "Attendance (%)":attendlist}
            dtf3=pd.DataFrame(dict3,index=indlist3)
            print("The list of all students -\n",dtf3)
            print("-"*30)
            continue
        
        elif choice2==0:
            print("OK Thanks.")
            break
        
        else:
            print("Please enter correct serial number.")
            continue
        
else:
    print("OK Thanks.")
