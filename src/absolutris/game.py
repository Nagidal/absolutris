#!/usr/bin/env python

import pygame
import os
import logging
# Necessary for Typing
from absolutris import config_loader
# Own modules
from absolutris import errors


# setup logging
logger = logging.getLogger(__name__)


class Game:
    """
    Main Game class.
    """
    def __init__(self, config: config_loader.Config) -> None:
        self.config = config
        if self.config.cli.gui == "default":
            logger.debug("using default gui")
            from absolutris.gui import default as gui
        elif self.config.cli.gui == "debug":
            logger.debug("using DEBUG gui")
            from absolutris.gui import debug as gui
        elif self.config.cli.gui == "m":
            logger.debug("using DEBUG gui")
            from absolutris.gui import m as gui
        else:
            raise errors.GuiNotImplemented(f"Cannot find any instance of \"{self.config.cli.gui}\" in gui.py")
        self.gui = gui
    def setup_game_window(self) -> None:
        # Set initial game window position
        os.environ["SDL_VIDEO_WINDOW_POS"] = f"{self.gui.game_window_x_pos},{self.gui.game_window_y_pos}"
        pygame.display.set_caption(self.gui.game_window_title)
        self.game_window = pygame.display.set_mode(
                size=(self.gui.game_window_width, self.gui.game_window_height), 
                flags=self.gui.flags
            )
        self.game_window.fill(self.gui.colors_window_bg)
    def run_gui(self) -> None:
        logger.debug(f"Running game with {self.config.cli.gui} gui")
        pygame.init()
        self.setup_game_window()
        self.pygame_running = True
        logger.info(f"Entering main game loop")
        while self.pygame_running:
            for event in pygame.event.get():
                # React to quitting pygame, e.g. by closing the game window
                if event.type == pygame.QUIT:
                    logger.debug("User closed pygame window")
                    self.pygame_running = False
                    break
                # React to keypresses:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        # distinguish between Q and Ctrl-Q
                        mods = pygame.key.get_mods()
                        # End main loop if Ctrl-Q was pressed
                        if mods & pygame.KMOD_CTRL:
                            logger.debug("User pressed Ctrl-Q to quit the game")
                            self.pygame_running = False
                            break
        logger.info(f"Left main game loop")
        pygame.quit()
        logger.debug("Finished running game with {self.config.cli.gui} gui")


def run(config: config_loader.Config) -> None:
    if config.cli.gui is not None:
        game = Game(config)
        game.run_gui()
    else:
        logger.debug("Runing game with no gui")
        logger.debug("Finished runing game with no gui")



if __name__ == "__main__":
    logger.debug(f"GUI started from __main__")
    logger.debug(f"GUI ended from __main__")
