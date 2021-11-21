from Bin import func_bin
from matplotlib import pyplot as plt
import numpy as np
import cv2





count_test_pic = 3
gl_thesh = 127




for i in range(1, count_test_pic):
    rgb_img = plt.imread('(' + str(i) + ').bmp')


# color pic -> gray pic
    red     = rgb_img[:, :, 0].astype(np.int32)
    green   = rgb_img[:, :, 1].astype(np.int32)
    blue    = rgb_img[:, :, 2].astype(np.int32)

    red_coef   = 306;
    green_coef = 601;
    blue_coef  = 116;

    img_R = (red_coef * red) // 1024;
    img_G = (green_coef * green) // 1024;
    img_B = (blue_coef * blue) // 1024;

    greay = img_R + img_G + img_B
# gray pic -> bin pic
    (Xsize, Ysize) = greay.shape
    arr_all_pic = np.zeros((Xsize*Ysize, count_test_pic), np.int32)
    threshold = gl_thesh * np.ones(greay.shape)
    greater = greay >= threshold
    binarized_image = greater * 1

    # plt.imshow(binarized_image, cmap='gray')
    # plt.show()

# create test vector
    greay_reshape = binarized_image.reshape(-1).astype(np.int32)
    (size_arr) = greay_reshape.shape

    arr_all_pic[:, i] = greay_reshape




for i in range(1, count_test_pic-1):
    arr_all_pic_concatente = np.concatenate(arr_all_pic[1, i], arr_all_pic[1, i+1])

(size_arr) = arr_all_pic_concatente.shape
text_saveCH1_odd = np.zeros((size_arr), np.int32)
text_saveCH2_even = np.zeros((size_arr), np.int32)

count_ij = 1
for i in range(0, (size_arr), 2):
    text_saveCH1_odd[0] = 0
    text_saveCH1_odd[count_ij] = greay_reshape[i]
    count_ij = count_ij + 1

count_ij = 1
for i in range(1, (size_arr), 2):
    text_saveCH2_even[0] = 0
    text_saveCH2_even[count_ij] = greay_reshape[i]
    count_ij = count_ij + 1

count_str = 1
str_st = np.zeros((size_arr), np.int32)
kdr_st = np.zeros((size_arr), np.int32)

for i in range(1, size_arr + 1):
    kdr_st[0] = 1
    if i == ((Ysize * Xsize) // 2):
        kdr_st[i] = 1

count_size = 0
for j in range(0, size_arr, 1):
    for i in range(1, Xsize // 2 + 1, 1):
        count_size = count_size + 1
        if i == Xsize // 2:
            str_st[count_size] = 1
            str_st[0] = 1

    # создание ТХТ файлов
with open("STR.txt", 'w') as file:
    while i > size_arr*count_test_pic:
        file.write(str(str_st[i]) + '\n')

with open("KDR.txt", 'w') as file:
    for i in range((size_arr)*i):
        file.write(str(kdr_st[i]) + '\n')

with open("DATA_READ1CH.txt", 'w') as file:
    for i in range((size_arr)*i):
        file.write(format(text_saveCH1_odd[i]) + '\n')
with open("DATA_READ2CH.txt", 'w') as file:
    for i in range((size_arr)*i):
        file.write(format(text_saveCH2_even[i]) + '\n')