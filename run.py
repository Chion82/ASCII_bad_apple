import time
import os

if __name__ == '__main__':
	with open('play.txt', 'r') as f
		frame_raw = f.read()
		frame_raw = frame_raw.replace('.', ' ')
		f.close()
	try:
		f.close()
	frames = frame_raw.split('SPLIT')
	os.system('mplayer -vo null -vc null video.mp4 &')
	#os.system('mplayer test.mp4 &')
	init_time = time.time()
	while time.time() <= init_time + 218:
		os.system('clear')
		print(frames[int((time.time()-init_time)*10)])
		time.sleep(0.05)

