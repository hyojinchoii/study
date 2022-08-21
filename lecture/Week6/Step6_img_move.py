import os
from glob import glob

path = 'meta-data/imagers/'
copy_path = './images_copy'

if os.path.exists(path) :
    if not os.path.exists(copy_path):
        os.mkdir(copy_path)

    img_list = glob(path + '*.png')

    for each_img_path in img_list:
        print(each_img_path)
        with open('C:\최효진\lecture\Week6\meta-data\images\103.png','rb') as f:
            img = f.read()

        with open('C:\최효진\lecture\Week6\102.png','wb') as f:
            f.write(img)

