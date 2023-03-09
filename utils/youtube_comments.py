from itertools import islice
from youtube_comment_downloader import *
from datetime import datetime
from deep_translator import GoogleTranslator

def get_youtube_comments(url):
    downloader = YoutubeCommentDownloader()
    comments = downloader.get_comments_from_url(url)
    comment_list = []
    for comment in comments:
        comment_datetime = datetime.fromtimestamp(comment['time_parsed'])
        comment_date = comment_datetime.strftime("%m/%d/%Y")
        comment_time = comment_datetime.strftime("%H:%M:%S")
        comment_en = GoogleTranslator(source='auto', target='en').translate(comment['text'])
        comment_details = {'url': url, 'comment':comment['text'], 'comment_en':comment_en, 'date':comment_date, 'time': comment_time}
        comment_list.append(comment_details)
    return comment_list
