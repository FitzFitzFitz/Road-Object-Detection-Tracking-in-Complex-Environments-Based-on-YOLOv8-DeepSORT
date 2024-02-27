from moviepy.editor import *
input_file = "test.avi"
output_file = "test.mp4"
video = VideoFileClip(input_file)
video.write_videofile(output_file, codec="libx264")
