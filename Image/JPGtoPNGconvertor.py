import sys
import os
from PIL import Image

fol1 = input('Enter 1st folder to enter : ')
fol2 = input('Enter 2st folder to Save : ')

#fol1 = sys.argv[1]
#fol2 = sys.argv[2]

#path = os.path.join('Scripting',fol1)
#if os.path.isdir(path+'\\'+fol2) == False:
    #os.mkdir(path+'\\'+fol2)
    
#if not os.path.exists(fol2):
    #os.makedirs(path+'\\'+fol2)
    
if not os.path.exists(fol2):
    os.makedirs(fol2)
    
for fname in os.listdir(fol1):
    img = Image.open(f'{fol1}\\{fname}')
    cutname = os.path.splitext(fname)[0]
    img.save(f'{fol2}\\{cutname}.png', 'png')
    print('Successsfully converted')
