s=input()
h=float(input())
if s=="m" or s=="M":
    p=(72.7*h)-58
else:
    p=(62.1*h)-44.7
print("O seu peso ideal é",p)
