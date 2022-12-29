from moviepy.editor import *


def combine_music_and_video():

    # Carica il video
    video = VideoFileClip("video.avi")

    # Carica l'audio
    audio = AudioFileClip("music.mp3")

    # Unisci il video e l'audio
    result = video.set_audio(audio)

    # Salva il risultato in un nuovo file
    result.write_videofile("result.mp4")


if __name__ == '__main__':
    combine_music_and_video()
