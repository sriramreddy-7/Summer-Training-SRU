details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
count=1
for i in details:
    s=str(i)
    age=""
    age=s[11]+s[12]
    age=int(age)
    if age>60:
        coun t+=1
print(count)