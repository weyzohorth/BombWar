from mod.__init__ import *
from random import randrange
from mod.obj.bonus import Bonus

class Mur:
	def __init__(__,x,y,des=0):
		G.MURS.append(__)
		__.x, __.y = x, y
		__.r = G.R
		__.des = des
		__.sprite = pygame.image.load('datas/img/autres/mur'+str(des)+'.gif').convert()
		G.game.blit(__.sprite, (x, y))

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	def boom(__):
		if __.des:
			if not randrange(3):
				Bonus(__.x,__.y)
			try:
				G.MURS.remove(__)
			except:
				pass
