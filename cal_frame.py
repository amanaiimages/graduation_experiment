import cv2
import numpy as np
import csv
 
def calc_black_whiteArea(canny_image):
    image_size = canny_image.size
    whitePixels = cv2.countNonZero(canny_image)
    blackPixels = canny_image.size - whitePixels
 
    whiteAreaRatio = (whitePixels/image_size)*100#[%]
    blackAreaRatio = (blackPixels/image_size)*100#[%]
 
    print("White Area [%] : ", whiteAreaRatio)
    print("Black Area [%] : ", blackAreaRatio)
    
    with open('guru-pu2_1123.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        writer.writerow([second,whiteAreaRatio])
 
    
if __name__ == "__main__":
    multi_n = 5 #何秒ごとに区切った画像ファイルの分析か
    second = 0
    while second <= 6050:  #総合時間
    # イメージの読み込み
        frame_path = "/Users/wadashuto/EXPERIMENT/frame_group2_1123/image_"+ str(second).zfill(8) + ".png"
        image = cv2.imread("image_"+ str(second).zfill(8) + ".png")
    
        # キャニー法で画像を二値化処理（白と黒で分ける）
        canny_image = cv2.Canny(image, 50, 150)
 
        # 画像として保存
        cv2.imwrite("black_white" + second +".jpg", canny_image)
    
        # calculation black and white area
        calc_black_whiteArea(canny_image)
        second += multi_n
