import random
clean=0
action=["l","r","s"]
floor=["dirty", "dirty"]
for fl in floor:
    pos = random.randint(0, 2)
    if(action[pos]=="l"):
        if(fl==floor.length-1):
            print("on last")
            continue
        else:
            print("moving right")
            fl=fl+1
    else if(action[pos]=='r'):
        
        if(fl==0):
            print("on first")
            continue
        else:
            print("moving left")
            fl=fl-1
    else if(action[pos]=='s'):
        if(fl=="dirty"):
            print("cleaning")
            clean=clean+1
if(clean==len(my_array)):
    print("Cleaned")
        
