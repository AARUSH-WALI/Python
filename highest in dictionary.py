d={"alice":92,"bob":85,"charlie":78,"david":95,"eve":88}
highest=0
for k in d.keys():
    if(highest<d[k]):
        highest=d[k]
        ans=k
print(ans,highest)

    
    
