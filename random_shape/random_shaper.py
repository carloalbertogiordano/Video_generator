import sys

import pygame
import random

from Shape_generator import Forma

from pygame_recorder import ScreenRecorder

import os


def main():
    # Impostare così per rincoglionire il pc così pensa che ha un display
    os.environ["SDL_VIDEODRIVER"] = "dummy"

    # Inizializza pygame
    pygame.init()

    # Imposta le dimensioni dello schermo
    screen_width, screen_height = 108 * 10, 192 * 10
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Crea il clock di pygame per controllare la velocità di aggiornamento
    clock = pygame.time.Clock()

    # Scegli il refresh rate
    refresh_rate = random.randint(1, 30)

    # Imposta il titolo della finestra
    pygame.display.set_caption("Animazioni casuali, FPS:{}".format(str(refresh_rate)))

    # Cancella lo schermo
    screen.fill((0, 0, 0))

    # Create a screen recorder object
    recorder = ScreenRecorder(screen_width, screen_height, refresh_rate, out_file='../combiner/video.avi')

    # Salva il tempo d'inizio della animazione
    start_time = pygame.time.get_ticks()

    # Genera una durata casuale del video fra 5 e 20 secondi
    finish_time = random.randint(5, 20) * 1000

    print("time to wait: {} seconds".format(finish_time / 1000))

    # Ripeti l'animazione per x secondi
    while pygame.time.get_ticks() - start_time < finish_time:

        # Gestisci gli eventi in ingresso
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Crea una nuova forma
        forma = Forma(random.randint(0, screen_width),
                      random.randint(0, screen_height),
                      (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),),
                      screen_width,
                      screen_height
                      )

        # Aggiungi nuovi vertici alla forma
        forma.genera_vertici()

        # Disegna tutte le forme sullo schermo
        forma.disegna(screen)

        # Aggiorna lo schermo
        pygame.display.flip()

        # forma.make_pillow_image(screen)

        # Capture the frame
        recorder.capture_frame(screen)

        # Limita la velocità di aggiornamento a 30 FPS
        clock.tick(refresh_rate)

    # Stop the screen recording
    recorder.end_recording()

    #Save the video lenght to a file
    save_file = open("../combiner/video_length.txt", "w")
    save_file.write(str(finish_time/1000))
    save_file.close()


if __name__ == "__main__":
    main()


def generate_video():
    main()
