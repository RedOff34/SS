import os
import time
import cv2
import imutils
import shutil
import img2pdf
import glob
import argparse

############# 상수정의

OUTPUT_SLIDES_DIR = f"./output"

FRAME_RATE = 3                   # 초당 프레임수 처리, 카운트가 적을수록 속도가 빠름.
WARMUP = FRAME_RATE              # 스킵이 될 프레임 수 초기화
FGBG_HISTORY = FRAME_RATE * 15   
VAR_THRESHOLD = 16               
DETECT_SHADOWS = False           
MIN_PERCENT = 0.1               
MAX_PERCENT = 3                  


def get_frames(video_path):
    '''비디오 패스에 있는 영상의 프레임을 반환하는 기능으로
    Frame_rate에서 정의한 값으로 영상의 프레임을 건너뜀'''
    
    
    # 열린 영상에 대한 비디오의 프레임 너비와 높이 초기화
    vs = cv2.VideoCapture(video_path)
    if not vs.isOpened():
        raise Exception(f'unable to open file {video_path}')


    total_frames = vs.get(cv2.CAP_PROP_FRAME_COUNT)
    frame_time = 0
    frame_count = 0
    print("total_frames: ", total_frames)
    print("FRAME_RATE", FRAME_RATE)

   
   
    while True:
        
        #프레임 재생시간 단위로 동영상 설정
        vs.set(cv2.CAP_PROP_POS_MSEC, frame_time * 1000)   
        frame_time += 1/FRAME_RATE

        (_, frame) = vs.read()
        
        if frame is None:
            break

        frame_count += 1
        yield frame_count, frame_time, frame

    vs.release()
 

#영상프레임에서 png파일 추출 함수
def detect_unique_screenshots(video_path, output_folder_screenshot_path):
 
    fgbg = cv2.createBackgroundSubtractorMOG2(history=FGBG_HISTORY, varThreshold=VAR_THRESHOLD,detectShadows=DETECT_SHADOWS)

    
    captured = False
    start_time = time.time()
    (W, H) = (None, None)

    screenshoots_count = 0
    for frame_count, frame_time, frame in get_frames(video_path):
        orig = frame.copy() 
        frame = imutils.resize(frame, width=600) 
        mask = fgbg.apply(frame) 

   
        if W is None or H is None:
            (H, W) = mask.shape[:2]

     
        p_diff = (cv2.countNonZero(mask) / float(W * H)) * 100

 

        if p_diff < MIN_PERCENT and not captured and frame_count > WARMUP:
            captured = True
            filename = f"{screenshoots_count:03}_{round(frame_time/60, 2)}.png"

            path = os.path.join(output_folder_screenshot_path, filename)
            print("saving {}".format(path))
            cv2.imwrite(path, orig)
            screenshoots_count += 1

       
        elif captured and p_diff >= MAX_PERCENT:
            captured = False
    print(f'{screenshoots_count} screenshots Captured!')
    print(f'Time taken {time.time()-start_time}s')
    return 

#디렉토리 초기화
def initialize_output_folder(video_path):
    '''Clean the output folder if already exists'''
    output_folder_screenshot_path = f"{OUTPUT_SLIDES_DIR}/{video_path.rsplit('/')[-1].split('.')[0]}"

    if os.path.exists(output_folder_screenshot_path):
        shutil.rmtree(output_folder_screenshot_path)

    os.makedirs(output_folder_screenshot_path, exist_ok=True)
    print('initialized output folder', output_folder_screenshot_path) #./ouput/ #./ouput/디렉토리명
    return output_folder_screenshot_path


 #pdf 변환 함수
def convert_screenshots_to_pdf(output_folder_screenshot_path, video_path):
    output_pdf_path = f"{OUTPUT_SLIDES_DIR}/{video_path.rsplit('/')[-1].split('.')[0]}" + video_path[2:-4] + '.pdf'
    print('output_folder_screenshot_path', output_folder_screenshot_path)
    print('output_pdf_path', output_pdf_path)
    print('converting images to pdf..')
    with open(output_pdf_path, "wb") as f:
        f.write(img2pdf.convert(sorted(glob.glob(f"{output_folder_screenshot_path}/*.png"))))
    print('Pdf Created!')
    print('pdf saved at', output_pdf_path)



#함수 실행부분
def video2pdfslides(video_path2):
    
    #main의 매개변수에서 인자 전달
    video_path=".\\"+video_path2
    #!!윈도우는 \ 역슬래쉬!!

    print('video_path', video_path)
    output_folder_screenshot_path = initialize_output_folder(video_path)
    detect_unique_screenshots(video_path, output_folder_screenshot_path)   
   
    convert_screenshots_to_pdf(output_folder_screenshot_path, video_path)