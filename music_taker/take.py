import random
import sys

from pydub import AudioSegment


def take_music(x=10):
    # Apri il file della canzone
    song = AudioSegment.from_file('music.mp3')

    # Calcola la durata della canzone in secondi
    song_duration = len(song) / 1000

    # Genera un numero intero casuale compreso tra 0 e la durata della canzone in secondi
    start_index = random.randint(0, int(song_duration))

    # Prendi una porzione di x secondi a partire dall'indice di inizio casuale
    song_slice = song[start_index * 1000:start_index * 1000 + x * 1000]

    # Salva la porzione di canzone in un nuovo file
    song_slice.export('../combiner/music.mp3', format='mp3')


if __name__ == '__main__':
    time = sys.argv[1]
    time = time[:-2]
    time = int(time)
    if time < 1:
        time = 1
    take_music(time)
