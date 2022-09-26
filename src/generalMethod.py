import pygame, sys
from pygame.locals import *
from pygame import mixer


def playMusic(isDisable: bool, musicAddr = None) -> None:
    mixer.music.load(musicAddr)
    if not isDisable:
        mixer.music.play()


def stopMusic() -> None:
    mixer.music.stop()


def switchMusic(isDisable: bool) -> bool:
    if isDisable:
        mixer.music.play()
    else:
        mixer.music.pause()
    return not isDisable