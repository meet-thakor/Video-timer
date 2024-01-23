import moviepy.editor as mpy
from moviepy.video.tools.segmenting import findObjects
import time

GREEN = (0, 255, 0)
SCREEN_SIZE = (1920, 1080)
VERTICAL_SPACE=100
HORIZONTAL_SPACE=100
ALL_CLIPS=[]
EPOCH=1705968000

for number in range(100):
    counter=time.strftime("%H:%M:%S", time.gmtime(EPOCH))
    txt_clip = ( mpy.TextClip( str(counter), fontsize=70, color='white')
                 .set_position('center')
                 .set_duration(1)
                 .set_start(number) )  # 1 second
    ALL_CLIPS.append(txt_clip)
    EPOCH+=1


final_clip = (
    mpy.CompositeVideoClip(ALL_CLIPS, size=SCREEN_SIZE)
    .on_color(color=GREEN, col_opacity=1)
)

final_clip.write_videofile("video_with_python.mp4", fps=1)