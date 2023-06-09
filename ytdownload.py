import os
from pytube import YouTube
#User input about downloading

url = input("What is the URL of the video you are using?:  ")
path = input("Where should the file go?:")

#establish url
yt=YouTube(url)






print(yt.title)
print(yt.author)
print(yt.views)
print(yt.length)

#print all the available streams
print(yt.streams.filter(progressive=True))
#ask for streams
quality = input("What stream would you like to download from? (itag): ")
stream = yt.streams.get_by_itag(quality)
stream.download()
#download successful 
print("Download Complete... Enjoy your video!")

