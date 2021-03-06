from matplotlib import pyplot as plt
import numpy as np

Ysize = 1080
Xsize = 1920
DUO_CH = 1

if DUO_CH == 0:
    with open("DATA_READ1CH.txt", 'r') as file:
        read_1ch = file.read().splitlines()
    read_1ch = list(map(int, read_1ch))

else:
    with open("DATA_READ1CH.txt", 'r') as file:
        read_1ch = file.read().splitlines()
    with open("DATA_READ2CH.txt", 'r') as file:
        read_2ch = file.read().splitlines()
    read_1ch = list(map(int, read_1ch))
    read_2ch = list(map(int, read_2ch))




open_pic = np.zeros((Ysize, Xsize))

size_arr = len(read_1ch)
size_pic = Ysize*Xsize

if DUO_CH == 0:
    call_pic = size_arr // size_pic
    count_arr = 0
    while call_pic > 0:
        for j in range(Ysize):
            for i in range(Xsize):
                count_arr = count_arr + 1
                open_pic[j,i] = read_1ch[count_arr]
        plt.imshow(open_pic, cmap = "gray")
        plt.show()
        call_pic = call_pic - 1
else:
    call_pic = size_arr // (size_pic // 2)
    count_arr = 0
    while call_pic > 0:
        for j in range(Ysize):
            for i in range(1, Xsize, 2):
                count_arr = count_arr + 1
                open_pic[j,i-1] = read_1ch[count_arr]
                open_pic[j,i]   = read_2ch[count_arr]
        plt.imshow(open_pic, cmap = "gray")
        plt.show()
        call_pic = call_pic - 1