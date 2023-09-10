import time
h=0
m=0
s=0
while True:
    for i in range(13):
        if i>= 0:
            if h==13:
                h=1

            for i in range(60):
                if i >= 0:
                    if m==60:
                        m=0
                    for i in range(60):
                        if s==60:
                            s=0
                        print("%02d:%02d:%02d"%(h,m,s))
                        time.sleep(1)
                        s+=1
                    m+=1
            h+=1


