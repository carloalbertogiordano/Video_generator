import random
import sys

from pydub import AudioSegment


def take_music(x=10):
    # Open the song file
    song = AudioSegment.from_file('music.mp3')

    # Calculate the length of the song in seconds
    song_duration = len(song) / 1000

    # Generate a random number between 0 and the song length
    start_index = random.randint(0, int(song_duration))

    # Take a portion of x seconds starting from the start_index
    song_slice = song[start_index * 1000:start_index * 1000 + x * 1000]

    # Save the portion of the song in a new file
    song_slice.export('../combiner/music.mp3', format='mp3')


if __name__ == '__main__':
    time = sys.argv[1]
    time = time[:-2]
    time = int(time)
    if time < 1:
        time = 1
    take_music(time)
