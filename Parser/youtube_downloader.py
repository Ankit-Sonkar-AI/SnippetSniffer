'''
Collect artists I like.
Find all their songs - lastfm api?
Mark whether I like each - listen once
Download ones I like - via youtube url
Pay artist - ???
Get notified of new albums
Get notified of UK dates
'''

from __future__ import unicode_literals
import youtube_dl
from datetime import datetime

file_of_url_list = 'youtube_list.txt'
file_of_downloaded_urls = 'downloaded.txt'
download_path = '~/Music/downloads/'

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    'noplaylist' : True,
    'outtmpl': download_path + '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        #'preferredquality': '192',
    }]
}

with open(file_of_url_list) as f:
    urls = f.readlines()

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)

with open(file_of_downloaded_urls, 'a') as f:
    f.write('\n' + datetime.now().strftime('%y-%m-%d-%H:%M') + '\n')
    f.writelines(urls)

with open(file_of_url_list, 'w') as f:
    f.write('')

