a=int(input("enter First number"));
b=int(input("enter Second number"));
c=int(input("enter third number"));
if((a>b) and (a>c)):
  largest=a
elif((b>a) and (b>c)):
  largest=b
else:
  largest=c
print("Largest of three is",largest)
