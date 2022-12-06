#coded by Bisno Das

import pytube
from pytube import YouTube

link = input(" Enter Your Video URL ==> ")
link = str(link)
youtube = pytube.YouTube(link)
youtube.streams.first().download()

print("Video Has Been Downloaded", link)