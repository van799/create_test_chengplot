from matplotlib import pyplot as plt
import numpy as np




DUO_CH = 1
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
    arr_all_pic = np.zeros((Xsize*Ysize*count_test_pic), np.int32)
    threshold = gl_thesh * np.ones(greay.shape)
    greater = greay >= threshold
    binarized_image = greater * 1

    # plt.imshow(binarized_image, cmap='gray')
    # plt.show()

# create test vector
    greay_reshape = binarized_image.reshape(-1).astype(np.int32)
    (size_arr) = greay_reshape.shape

    arr_all_pic[Xsize*Ysize*(i - 1):Xsize*Ysize*i] = greay_reshape
    size_arr = Xsize*Ysize*i





text_saveCH1_odd = np.zeros((size_arr), np.int32)
text_saveCH2_even = np.zeros((size_arr), np.int32)

count_ij = 1
for i in range(0, (size_arr), 2):
    text_saveCH1_odd[0] = 0
    text_saveCH1_odd[count_ij] = arr_all_pic[i]
    count_ij = count_ij + 1

count_ij = 1
for i in range(1, (size_arr), 2):
    text_saveCH2_even[0] = 0
    text_saveCH2_even[count_ij] = arr_all_pic[i]
    count_ij = count_ij + 1

count_str = 1
str_st = np.zeros((size_arr+Xsize), np.int32)
kdr_st = np.zeros((size_arr+Xsize), np.int32)

num_pic = 1
for i in range(1, size_arr//DUO_CH+Xsize):
    kdr_st[0] = 1
    if i == ((Ysize * Xsize) // DUO_CH)*num_pic:
        kdr_st[i] = 1
        num_pic = num_pic + 1
count_size = 0

for j in range(0, Ysize*(count_test_pic-1), 1):
    for i in range(1, Xsize // DUO_CH + 1, 1):
        count_size = count_size + 1
        if i == Xsize // DUO_CH:
            str_st[count_size] = 1
            str_st[0] = 1

    # создание ТХТ файлов
with open("STR.txt", 'w') as file:
    for i in range((size_arr)):
        file.write(str(str_st[i]) + '\n')

with open("KDR.txt", 'w') as file:
    for i in range((size_arr)):
        file.write(str(kdr_st[i]) + '\n')

with open("DATA_READ1CH.txt", 'w') as file:
    for i in range((size_arr)):
        file.write(format(text_saveCH1_odd[i]) + '\n')
with open("DATA_READ2CH.txt", 'w') as file:
    for i in range((size_arr)):
        file.write(format(text_saveCH2_even[i]) + '\n')