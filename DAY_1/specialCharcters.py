ip="afrgRHAABDzxcv@#$%^&*()_+1234567890"
uv,uc,lv,lc,d,sc=0,0,0,0,0,0
for i in ip:
    if i.isupper():
        if i not in "AEIOU":
            uv+=1
        else:    
            uc+=1
    if i.islower():
        if i in 'aeiou':
            lv+=1
        else:
            lc+=1
    if i.isdigit():
        d+=1
    if not i.isalnum():
        sc+=1
        
print(f"Upper Vowels: {uv}\nUpper Consonants: {uc}\nLower Vowels: {lv}\nLower Consonants: {lc}\nDigits: {d}\nSpecial Characters: {sc}")