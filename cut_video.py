import ffmpy3  # ffmpy3是一个用于FFmpeg的Python包装器

ff = ffmpy3.FFmpeg(
    inputs={'test.mp4': None},
    outputs={'output.avi': None}
)  # 这input.mp4会将当前目录中的文件作为输入，将视频容器从 MP4 更改为 AVI，而不更改任何其他视频参数，并output.avi在当前目录中创建一个新的输出文件。
ff.run()
# ffmpeg -ss 00:00:00 -i test.avi -t 00:00:10 -vf fps=30 out.avi
# python track.py --yolo-weights yolov8s.pt --reid-weights osnet_x0_25_msmt17.pt --source out.avi --save-vid
