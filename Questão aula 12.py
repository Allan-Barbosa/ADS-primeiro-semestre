salário=float(input("Digite seu salário:"))
if salário<500:
    nsalário=salário*1.15
else:
    if salário>=1000:
        nsalário=salário*1.1
    else:
        nsalário=salário*1.05
print("Seu novo salário é",nsalário)
    
