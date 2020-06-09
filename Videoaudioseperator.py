
#seprating audio from video 



import moviepy.editor
video=moviepy.editor.VideoFileClip("filename.mp4")
audio=video.audio
audio.write_audiofile("output.mp3")
video.close()