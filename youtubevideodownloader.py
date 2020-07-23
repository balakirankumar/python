
# import pytube

# yt = pytube.YouTube('http://youtube.com/watch?v=9bZkp7q19f0')

# yt.streams.filter(progressive=True)
# stream=yt.streams.first()
# stream.download("Tesing")
# print("completed")




#FOR PLAYLIS

# import pytube
# from pytube import Playlist
# playlist = Playlist("playlistlink")
# for i in playlist:
	# yt=pytube.YouTube(i)
	# stream=yt.streams.first()
	# stream.download('foldername')


#FOR SINGLE DOWNLOADS


	
import pytube
link = input("Enter the link :\t")
yt = pytube.YouTube(link)
stream = yt.streams
for i in stream :
	print(i)
n=int(input("Enter stream no :\t"))
stream[n].download()
print("Completed")