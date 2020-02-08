import pytube
import os
import subprocess #터미널, 콘솔 명령어 실행하고 리턴값 받아주는 녀석

yt = pytube.YouTube("https://www.youtube.com/watch?v=HWRVveKx_u4") #다운받을 동영상 URL 지정
videos = yt.streams.all()

print('videos', videos)

for i in range(len(videos)):
    print(i, ',', vides[i])

cNum = int(input("다운 받을 화질은?(0~21 입력)"))

downdir = "D:/study/인프런/06.web/004.python/section2/youtube"

videos[cNum],download(downdir)

newFileName = input("변환 할 mp 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg', '-i',
    os.path.join(downdir,oriFileName),
    os.path.join(downdir,newFileName)
])

print("동영상 다운로드 및 mp 변환 완료!")

#ffmpeg -i "원본동영상 파일이름" new.mp3

# 숙제는 URL만 입력받아 다운로드 및 변환하기.
# 동영상 두세개 다운로드 변환,
# 동영상 다운 후 mp로 변환하시겠습니까? y -> 변환 할 mp 이름 입력하게, n -> 동영상 다운만 받고 끝
