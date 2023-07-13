from pytube import YouTube

def youtube_down(url):
    DOWNLOAD_FOLDER = '.\\' # 유튜브 동영상 저장할 디렉토리
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(DOWNLOAD_FOLDER)
    print("다운로드 완료")