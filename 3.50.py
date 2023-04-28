h=int(input())
m=int(input())
hd = 0.5 * 60 * h + 0.5 * m
md= 6 * m
count=0
while hd!=md:
    count+=1
    hd+=0.5
    md+=6
    if hd==360:
        hd=0
    if md==360:
        md=0
        
        
print(count)

    
h=int(input())
m=int(input())
hd = 0.5 * 60 * h + 0.5 * m
md= 6 * m
count=0
while abs(hd-md)!=90 or abs(hd-md)!=270 or abs(md-hd)!=90 or abs(md-hd)!=270:
    count+=1
    hd+=0.5
    md+=6
    if abs(hd-md)==90:
        break
    if hd>=360:
        hd=hd-360
    if md>=360:
        md=md-360
        
        
print(count)

    
