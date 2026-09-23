total_obt=0
for i in range(1,6):
    sub=int(input("Enter the subject " +str(i)+ " marks: "))
    total_obt+=sub
    percent=total_obt/500*100;
    if(percent >= 80 and percent <=100):
        grade="A-1"
        result="Pass"
    elif(percent >=70 and percent < 80):
        grade="A"
        result="Pass"
    elif(percent >=60 and percent < 70):
        grade="B"
        result="Pass"    
    elif(percent >=50 and percent < 60):
        grade="c"
        result="Pass" 
    elif(percent >=40 and percent < 50):
        grade="D"
        result="Pass"               
    elif(percent < 40):
        grade="E"
        result="Fail"  
                  
print("*****The Student's Result*****")                 
print(f"The Total Marks: ",total_obt)
print(f"The Percentage: ",percent)
print(f"The Grade: ",grade)
print(f"The result: ",result)                   
