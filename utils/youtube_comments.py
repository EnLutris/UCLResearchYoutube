from itertools import islice
from youtube_comment_downloader import *
from datetime import datetime

def feriha(url):
    downloader = YoutubeCommentDownloader()
    comments = downloader.get_comments_from_url(url)
    comment_list = []
    for comment in comments:
        comment_datetime = datetime.fromtimestamp(comment['time_parsed'])
        comment_date = comment_datetime.strftime("%m/%d/%Y")
        comment_time = comment_datetime.strftime("%H:%M:%S")
        d = {'url': url, 'comment':comment['text'], 'date':comment_date, 'time': comment_time}
        comment_list.append(d)
    return comment_list
