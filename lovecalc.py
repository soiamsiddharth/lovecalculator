name1=input("whats your name:")
name2=input("your partners name:")

combine_name=name1+name2
namein_lowercase=combine_name.lower()




T=namein_lowercase.count("t")
R=namein_lowercase.count("r")
U=namein_lowercase.count("u")
E=namein_lowercase.count("e")

total=T+R+U+E

L=namein_lowercase.count("l")
O=namein_lowercase.count("o")
V=namein_lowercase.count("v")
E=namein_lowercase.count("e")

score=L+O+V+E


lovecalculator=int(str(total)+str(score))



if (lovecalculator>20) and (lovecalculator<50) :
 print("you are made for each other")

elif (lovecalculator<10) and (lovecalculator<60) :
 print(f"you go together like coke and mentos")

else:
 print("u dont deserve him or her")