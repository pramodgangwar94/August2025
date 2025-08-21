Question=[
    ["what is the capital of india", "Delhi","mumbai","Lucknow","Agra",1],
    ["what is the capital of UP", "Delhi","mumbai","Lucknow","Agra",3],
    ["what is the capital of Bihar", "Delhi","Patna","Lucknow","Agra",2],
    ["what is the capital of UK", "Delhi","mumbai","Dehradoon","Agra",3],
    ["what is the capital of Delhi", "Delhi","mumbai","Dehradoon","Agra",1],
    ["what is the capital of Haryana", "Delhi","mumbai","Dehradoon","Chandigarh",4],
    ["what is the capital of india", "Delhi","mumbai","Lucknow","Agra",1],
    ["what is the capital of UP", "Delhi","mumbai","Lucknow","Agra",3],
    ["what is the capital of Bihar", "Delhi","Patna","Lucknow","Agra",2],
    ["what is the capital of UK", "Delhi","mumbai","Dehradoon","Agra",3],
    ["what is the capital of Delhi", "Delhi","mumbai","Dehradoon","Agra",1],
    ["what is the capital of Haryana", "Delhi","mumbai","Dehradoon","Chandigarh",4],
    ["what is the capital of india", "Delhi","mumbai","Lucknow","Agra",1],
    ["what is the capital of UP", "Delhi","mumbai","Lucknow","Agra",3],
    ["what is the capital of Bihar", "Delhi","Patna","Lucknow","Agra",2],
    ["what is the capital of UK", "Delhi","mumbai","Dehradoon","Agra",3],
    ["what is the capital of Delhi", "Delhi","mumbai","Dehradoon","Agra",1],
    ["what is the capital of Haryana", "Delhi","mumbai","Dehradoon","Chandigarh",4]
    ]
Levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000]
Money=0
for i in range(0,len(Question)):
    Ques=Question[i]   
    print(f"\nQuestion{Question[i]}") 
    print(f"\nquestion{Levels[i]}")
    print(f"a.{Ques[1]}     b.{Ques[2]}")
    print(f"c.{Ques[3]}     d.{Ques[4]}")
    reply=int(input("enter your answer(1-4) or 0 to quit"))
    if (reply==0):
        Money=Levels[i-1]
        break
    if (reply==Ques[-1]):
        print(f"\ncorrect anser, you have won Rs. {Levels[i]}")
        if(i==4):
            Money=10000
        elif(i==9):
            Money=320000    
    else:
        print("wrong answer")  
        break  
print(f"your take home money is {Money}")