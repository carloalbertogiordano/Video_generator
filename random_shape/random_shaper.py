import sys

import pygame
import random

from Shape_generator import Shape

from pygame_recorder import ScreenRecorder

import os


def main():
    # Set this so that no window is shown
    os.environ["SDL_VIDEODRIVER"] = "dummy"

    pygame.init()

    # Set screen dimensions
    screen_width, screen_height = 108 * 10, 192 * 10
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Create a clock to regulate loading speed
    clock = pygame.time.Clock()

    # Set the refresh rate
    refresh_rate = random.randint(1, 30)

    # Set the window tite
    pygame.display.set_caption("Random animations, FPS:{}".format(str(refresh_rate)))

    # Clean the screen
    screen.fill((0, 0, 0))

    # Create a screen recorder object
    recorder = ScreenRecorder(screen_width, screen_height, refresh_rate, out_file='../combiner/video.avi')

    # Save the start time, used to save the length of the video
    start_time = pygame.time.get_ticks()

    # Generate a random time length fot the video
    finish_time = random.randint(5, 20) * 1000

    print("time to wait: {} seconds".format(finish_time / 1000))

    # Repeat the animation for set time
    while pygame.time.get_ticks() - start_time < finish_time:

        # Handle incoming events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Generate a new shape
        shape = Shape(random.randint(0, screen_width),
                      random.randint(0, screen_height),
                      (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),),
                      screen_width,
                      screen_height
                      )

        # Add vertex to the shape
        shape.generate_vertices()

        # Draw the shape on the screen
        shape.draw(screen)

        # Update the screen
        pygame.display.flip()

        # Capture the frame
        recorder.capture_frame(screen)

        # Limit the refresh rate to 30 FPS
        clock.tick(refresh_rate)

    # Stop the screen recording
    recorder.end_recording()

    # Save the video lenght to a file
    save_file = open("../combiner/video_length.txt", "w")
    save_file.write(str(finish_time / 1000))
    save_file.close()


if __name__ == "__main__":
    main()


def generate_video():
    main()
