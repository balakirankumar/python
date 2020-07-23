
#seprating audio from video 



import moviepy.editor
video_name=input()
video=moviepy.editor.VideoFileClip(video_name)
audio=video.audio
audio_outname=input("Enter output file name :\t")
audio.write_audiofile(audio_outname+".mp3")
video.close()