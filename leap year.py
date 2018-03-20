a=int(input("enter a year"));
if((a%4==0) and (a%100==0)):
  if(a%400==0):
    print("it is a leap year",a)
else:
  print("it is not a leap year",a)
