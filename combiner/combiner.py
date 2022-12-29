from moviepy.editor import *


def combine_music_and_video():

    # Load the video
    video = VideoFileClip("video.avi")

    # Load the audio
    audio = AudioFileClip("music.mp3")

    # Merge audio and video
    result = video.set_audio(audio)

    # Save the result in a new file
    result.write_videofile("result.mp4")


if __name__ == '__main__':
    combine_music_and_video()
