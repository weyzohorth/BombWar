import pygame
from pygame.locals import *
pygame.init()

class Global:
	def __init__(__):
		__.version = "1.0"
		__.JOUEURS = []
		__.MURS = []
		__.BOMBS = []
		__.BONUS = []
		__.FIRES = []
		__.R = 23
		__.WIDTH = __.HEIGHT = 640
		w = int(__.WIDTH/(__.R*2)) + 1
		h = int(__.HEIGHT/(__.R*2)) + 1
		__.xmax = __.WIDTH - (not w % 2) * __.R * 2
		__.ymax = __.HEIGHT - (not h % 2) * __.R * 2
		__.son_mort = pygame.mixer.Sound("datas/son/mort.ogg")
		__.son_explo = pygame.mixer.Sound("datas/son/boom.ogg")
		__.son_bonus = pygame.mixer.Sound("datas/son/bonus.ogg")
		__.son_bomb = pygame.mixer.Sound("datas/son/bomb.ogg")
		__.son_bomb_tel = pygame.mixer.Sound("datas/son/bomb_tel.ogg")
		pygame.mixer.music.load("datas/son/02 - Sleepwalker.ogg")
		__.screen = pygame.display.set_mode((__.WIDTH, __.HEIGHT))
		pygame.display.set_icon(pygame.image.load('datas/img/joueurs/joueur0.gif').convert())
		pygame.display.set_caption("BombWar 1.0 by W3YZOH0RTH", "BombWar")

G = Global()
