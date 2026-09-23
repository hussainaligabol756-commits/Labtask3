sum=0
even=0
odd=0
numbers=[]

for i in range(1,11):
    num=int(input("Enter the num "+str(i)+" :"))
    numbers.append(num)
    sum+=num
    average=sum/10
    if(num%2==0):
        even+=1
    else:
        odd+=1 
            
print("The sum of all nums: ",sum)   
print("The average: ",average)
print("The smallest number: ",min(numbers))
print("The largest number: ",max(numbers))
print("The even numbers: ",even)
print("The odd numbers: ",odd)
