from Manager import Manager
import arcade

from moviepy.editor import *
import pygame

def main():
    # first screen
    pygame.display.set_caption('Redneck Rumble')

    clip = VideoFileClip("video/begin_cut.mp4")
    clip.preview()

    pygame.quit()

    # game
    manager = Manager()

    while True:
        manager.setup()
        arcade.run()

        # Dev trickshot
        while not manager.stop:
            pass

        if manager.end_game:
            if manager.win_state:
                clip = VideoFileClip("video/win_cut.mp4")
                clip.preview()
            else:
                clip = VideoFileClip("video/win_cut.mp4")
                clip.preview()

            manager.setup_retry()
            arcade.run()
        else:
            break

        if not manager.retry:
            break


if __name__ == "__main__":
    main()
