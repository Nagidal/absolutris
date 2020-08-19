#!/usr/bin/env python

from typing import Type
from typing import Iterable
import pygame
from absolutris import gui
from absolutris import errors
from absolutris import testhelper


def test_gui_classes() -> None:
    """
    Checks if a Gui class is usable.
    What makes a Gui class usable?
    """
    for _, GC in testhelper.find_gui_classes():
        # Check if it generates instances of Gui
        assert isinstance(GC(), gui.Gui)


def test_gui_instances() -> None:
    """
    Checks if every gui instance is usable.
    """
    # 8K resolution width, height, corresponding ranges
    res8Kw = 7680
    res8Kh = 4320
    rng8Kw = range(res8Kw + 1)
    rng8Kh = range(res8Kh + 1)
    window_pixel_width_modulus = 0
    window_pixel_height_modulus = 0
    min_playfield_width = 4
    min_playfield_height = 4
    min_pixel_width = 1
    min_pixel_height = 1
    min_mino_width = 1
    min_mino_height = 1
    for _, gi in testhelper.find_gui_instances():
        # Check types
        assert type(gi.game_window_x_pos) is int
        assert type(gi.game_window_y_pos) is int
        assert type(gi.game_window_title) is str
        assert type(gi.game_window_width) is int
        assert type(gi.game_window_height) is int
        assert type(gi.flags) is int
        assert type(gi.colors_window_bg) is pygame.Color
        assert type(gi.colors_window_fg) is pygame.Color
        assert type(gi.playfield_width) is int
        assert type(gi.playfield_height) is int
        assert type(gi.pixel_width) is int
        assert type(gi.pixel_height) is int
        assert type(gi.mino_width) is int
        assert type(gi.mino_height) is int
        # Check values
        assert gi.game_window_x_pos in rng8Kw
        assert gi.game_window_y_pos in rng8Kh
        assert "absolutris" in gi.game_window_title.lower(), "Game window title must contain 'absolutris'"
        assert gi.game_window_width in rng8Kw, f"Game window wider than {res8Kw} pixels"
        assert gi.game_window_height in rng8Kh, f"Game window higher than {res8Kh} pixels"
        assert gi.game_window_x_pos + gi.game_window_width in rng8Kw, "Game window partially off-screen"
        assert gi.game_window_y_pos + gi.game_window_height in rng8Kh, "Game window partially off-screen"
        assert testhelper.in_bitfield(gi.flags, 
                           pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.OPENGL | pygame.RESIZABLE | pygame.NOFRAME | pygame.SCALED)
        assert gi.game_window_width % gi.pixel_width == window_pixel_width_modulus
        assert gi.game_window_height % gi.pixel_height == window_pixel_height_modulus
        assert gi.playfield_height >= min_playfield_width, f"Playfield must be at least {min_playfield_width} wide"
        assert gi.playfield_width >= min_playfield_height, f"Playfield must be at least {min_playfield_width} high"
        assert (gi.playfield_width * gi.pixel_width * gi.mino_width) <= gi.game_window_width, "Playfield wider than game window"
        assert (gi.playfield_height * gi.pixel_height * gi.mino_height) <= gi.game_window_height, "Playfield higher than game window"
        assert gi.pixel_width >= min_pixel_width
        assert gi.pixel_height >= min_pixel_height
        assert gi.mino_width >= min_mino_width
        assert gi.mino_height >= min_mino_height


if __name__ == "__main__":
    pass