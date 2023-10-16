d={"alice":92,"bob":85,"charlie":78,"david":95,"eve":88}
highest=0
for k in d.values():
    if(highest<k):
        highest=k
print(d.key(),highest)
