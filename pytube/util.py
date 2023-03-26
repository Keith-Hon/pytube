import pytube as pt

def get_youtube_audio_stream(video_id):
    yt_url = f"https://www.youtube.com/watch?v={video_id}"
    yt = pt.YouTube(yt_url)
    audio_streams = yt.streams.filter(only_audio=True)
    if not audio_streams or len(audio_streams) == 0:
        return None
    stream = audio_streams[0]
    return stream

def get_youtube_video_stream(video_id):
    yt_url = f"https://www.youtube.com/watch?v={video_id}"
    yt = pt.YouTube(yt_url)
    video_streams = yt.streams.filter(progressive="True", file_extension='mp4')
    if not video_streams or len(video_streams) == 0:
        return None
    stream = video_streams.get_highest_resolution()
    return stream

def get_youtube_captions(video_id):
    yt_url = f"https://www.youtube.com/watch?v={video_id}"
    yt = pt.YouTube(yt_url)    
    return yt.captions
