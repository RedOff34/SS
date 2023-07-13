from asyncio.windows_events import NULL
import os
import sys
import module.anyang_video.anyang_videoUrl
import module.video2pdfslides.video2pdfslides
import module.Tesseract_ocr.convert
import module.youtube_download.youtube_download
import module.FlashCards.FlashCards
if __name__=='__main__':

        
        while(True):
            print("---------사용하고자 하는 메뉴 선택-----------")
            print("1. 안양대 사이버강의 영상 다운")
            print("2. 유튜브 강의 영상 다운")
            print("3. PDF 추출")
            print("4. OCR 변환")
            print("5. 단어장 만들기!")
            print("0을 누르면 프로그램 종료\n\n")

    
            Menu_Num=int(input("☞사용하고자 하는 메뉴 선택: " ))

            video_path=NULL

            if(Menu_Num==1): # 안양대 사이버
                try:
                    video_path= module.anyang_video.anyang_videoUrl.anyang_url()
                    os.system('cls') # 화면 청소
                except:
                    print("동영상 주소 에러!! 다시 입력")
            
            elif(Menu_Num==2): # 유튜브 다운
                try:
                    module.youtube_download.youtube_download.youtube_down()
                    os.system('cls')
                except:
                    print("URL주소를 잘못 입력하셧습니다.\n\n")
                    continue
            elif(Menu_Num==3): #PDF 추출 #video_path="데이터표시.mp4"
                if(video_path==NULL):
                    print("추출하고자 하는 파일명을 입력. ex) 캡스톤디자인.mp4 ")
                    video_path=input()
                    module.video2pdfslides.video2pdfslides.video2pdfslides(video_path)
                    os.system('cls')
                else:
                    module.video2pdfslides.video2pdfslides.video2pdfslides(video_path) 
                    os.system('cls')
            elif(Menu_Num==4): #OCR 변환
                module.Tesseract_ocr.convert.pdf_to_ocr()
                os.system('cls')
            elif(Menu_Num==5): #단어장 만들기
                module.FlashCards.FlashCards.flashcard()
                os.system('cls')
            elif(Menu_Num==0):
                sys.exit(0)
            break