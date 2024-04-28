import time,rotatescreen
p=rotatescreen.get_primary_display()
l=[90,180,270,0]
for i in range(5):
    for j in l:
        p.rotate_to(j)
        time.sleep(0.5)