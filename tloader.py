import os
import glob
import urllib.parse as urlparse

def uidget(uid):
    url_data = urlparse.urlparse(uid)
    query = urlparse.parse_qs(url_data.query)
    uid = query["v"][0]
    return uid

def transcriptDownloaderauto(uid):
    if "youtube" in uid:
            uid = uidget(uid)
    os.system(f'youtube-dl --write-auto-sub --skip-download https://www.youtube.com/watch?v={uid} -o ./transcripts/{uid}_auto')

def transcriptDownloaderfull(uid):
    if "youtube" in uid:
            uid = uidget(uid)
    os.system(f'youtube-dl --all-subs --skip-download https://www.youtube.com/watch?v={uid} -o ./transcripts/{uid}_man')

def audioDownloaderfull(uid):
    if "youtube" in uid:
            uid = uidget(uid)
    os.system(f'youtube-dl -i --extract-audio --audio-quality 0 https://www.youtube.com/watch?v={uid} -o "./audios/{uid}.%(ext)s"')

def AT_downloader(uids, audpath='audios', transpath='transcripts'):
    for uid in uids:
        if "youtube" in uid:
            uid = uidget(uid)
        transcriptDownloaderfull(uid)
        audioDownloaderfull(uid)

def main(video_id):
    video_id = uidget(video_id)
    trnxs = glob.glob(f'./transcripts/{video_id}*.vtt')
    if len(trnxs)>0:
        print(trnxs)
        print(video_id, "already downloaded")
        return None
    transcriptDownloaderfull(video_id)
    transcriptDownloaderauto(video_id)
    trnxs = glob.glob(f'./transcripts/{video_id}*.vtt')
    print(trnxs)
    if len(trnxs)==0:
        print(f"Leaving this as {video_id} has no subtitles to download")
        return None
    audioDownloaderfull(video_id)

def TAL(lst):
    for l in lst:
        main(l)

if __name__=="__main__":
    video_id = input("enter the video id you want to download: ")
    main(video_id)
