import glob
import os
import sys
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

if len(sys.argv) != 2 :
    print("Usage: python cut_start.py path/")
    sys.exit (1)

path_in = str(sys.argv[1])
    
#path_in = '/home/user/Downloads/sem_6/NPTEL/'
path_out = path_in+'out/'

start_time = 9
arr = glob.glob(path_in + '*.mp4')
os.makedirs(path_out)

for i in range(1,len(arr)+1):
    print(arr[i-1])
    clip = VideoFileClip(str(arr[i-1]))
    print( clip.duration )
    end_in = clip.duration
    end_time = ((int)(end_in/60))*100 + ((end_in/60)-((int)(end_in/60)))*60
    print(end_time)
    ffmpeg_extract_subclip(str(arr[i-1]), start_time, end_time, targetname= path_out + (arr[i-1].split('/'))[len(arr[i-1].split('/'))-1])
    

