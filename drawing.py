import matplotlib.pyplot as plt
import numpy as np

img=np.zeros((200,200),dtype='uint8')

plt.imshow(img)

x=int(np.random.randint(0,189,1))
y=int(np.random.randint(0,189,1))

for i in range(x,x+10):
    for j in range(y,y+10):
        img[i,j]=255
        
plt.imshow(img)


def check_dist(x1,y1,x2,y2):
    if (abs(x2-x1)<=1 and abs(y2-y1)<=1):
        return True
    else:
        if y2<y1:
            canvas[]
    

l=[1,2,3]
for a in l:
    pass
print(a)