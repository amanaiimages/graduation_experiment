import cv2
from os import makedirs
from os.path import splitext, dirname, basename, join
 
def save_frames(video_path: str, frame_dir: str, 
                name="image", ext="jpg"):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return
    v_name = splitext(basename(video_path))[0]
    if frame_dir[-1:] == "\\" or frame_dir[-1:] == "/":
        frame_dir = dirname(frame_dir)
    frame_dir_ = join(frame_dir, v_name)
 
    makedirs(frame_dir_, exist_ok=True)
    base_path = join(frame_dir_, name)
    
    multi_n = 5 #何秒ごとに区切るか
    idx = 0
    while cap.isOpened():
        idx += 1
        ret, frame = cap.read()
        if ret:
            if cap.get(cv2.CAP_PROP_POS_FRAMES) == 1:  # 0秒目のフレームを保存する
                cv2.imwrite("{}_{}.{}".format(base_path, "00000000", ext),frame)
            elif idx < cap.get(cv2.CAP_PROP_FPS):
                continue
            else:  # muti_n秒ずつフレームを保存する
                second = int(cap.get(cv2.CAP_PROP_POS_FRAMES)/(idx * multi_n))
                secondmulti = second * multi_n
                filled_second = str (secondmulti).zfill(8)
                cv2.imwrite("{}_{}.{}".format(base_path, filled_second, ext),
                            frame)
                idx = 0
        else:
            break
 #動画データと作成したいディレクトリのパスを指定し、関数の実行。
save_frames("guru-pu2_1123.mp4", "/Users/wadashuto/EXPERIMENT/frame_group2_1123")
