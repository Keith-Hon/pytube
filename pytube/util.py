import pytube as pt
import time

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

def get_youtube_captions(video_id, retries=3, retry_delay=3):
    yt_url = f"https://www.youtube.com/watch?v={video_id}"
    
    for attempt in range(retries):
        try:
            print('trying to get captions the ' + str(attempt + 1) + ' time')            
            yt = pt.YouTube(yt_url)
            captions = yt.captions
            
            if captions is not None and len(keys(captions)) > 0:
                return captions
            else:
                raise ValueError("Captions not found")
        except (pt.exceptions.PytubeError, ValueError) as e:
            if attempt < retries - 1:  # Retry until the last attempt
                time.sleep(retry_delay)  # Wait for retry_delay seconds before the next attempt
            else:
                return None