a=int(input("請一個輸入三位數:"))
b=a//100
c=(a-b*100)//10
d=a-c*10-b*100
print("每位數字的總和",(b+c+d))