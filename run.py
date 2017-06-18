import time, os

if __name__ == '__main__':
  f = open('play.txt', 'r')
  frame_raw = f.read()
  frame_raw = frame_raw.replace('.', ' ')
  f.close()
  frames = frame_raw.split('SPLIT')
  os.system('mplayer -vo null -vc null video.mp4 > /dev/null 2>&1 &')
  #os.system('mplayer test.mp4 &')
  init_time = time.time()

  import cv2
  vidcap = cv2.VideoCapture('video.mp4')
  total_frames = int(vidcap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
  fps = vidcap.get(cv2.cv.CV_CAP_PROP_FPS)
  video_length = total_frames / fps

  while time.time() <= init_time + video_length:
    os.system('clear')
    print(frames[int((time.time()-init_time)*10)])
    time.sleep(0.05)

