from __init__ import *
from mod.obj.joueur import Joueur
from mod.obj.mur import Mur

class Game:
	def __init__(__, joueurs=2):
		__.JOUEURS = []
		__.MURS = []
		__.BOMBS = []
		__.BONUS = []
		__.FIRES = []
		G.game = pygame.Surface((G.xmax, G.ymax))
		__.back = pygame.Surface((G.xmax, G.ymax))
		#pygame.draw.rect(G.screen, pygame.Color(0, 255, 0, 50), (0, 0, G.WIDTH, G.HEIGHT), 0)
		__.x = (G.WIDTH - G.xmax) / 2
		__.y = (G.HEIGHT - G.ymax) / 2
		G.screen.blit(G.game, (__.x, __.y))
		G.game.blit(__.back, (0, 0))
		__.place_mur(joueurs)
		__.quit = False
		__.boucle()

	def test_players_alive(__):
		nb_players = 0
		nb_teams = 0
		teams = []
		for i in G.JOUEURS:
			if not i.mort:
				nb_players += 1
				if not teams.count(i.team):
					nb_teams += 1
					teams.append(i.team)
		if nb_players <= 1 or (nb_teams == 1 and teams[0] != -1):
			return (0)
		return (1)

	def boucle(__):
		while not __.quit:
			if not pygame.mixer.music.get_busy(): pygame.mixer.music.play()
			G.screen.blit(G.game, (__.x, __.y))
			G.game.blit(__.back, (0, 0))
			for i in G.BOMBS: i.move()
			for i in G.MURS: G.game.blit(i.sprite, (i.x, i.y))
			for i in G.BONUS: i.move()
			for i in G.JOUEURS: i.move()
			for i in G.FIRES: i.move()

			pygame.display.update()

			for event in pygame.event.get():
				if event.type == QUIT or not __.test_players_alive():
					__.quit = True
				elif  event.type == KEYDOWN:
					print event.key
					for i in G.JOUEURS:
						if event.key == i.droite: i.direction_set(1)
						elif event.key == i.haut: i.direction_set(2)
						elif event.key == i.gauche: i.direction_set(3)
						elif event.key == i.bas: i.direction_set(4)
						elif event.key == i.activ_bomb: i.BOOM = True
						elif event.key == i.lache_bomb: i.bomb = True

				elif  event.type == KEYUP:
					for i in G.JOUEURS:
						if event.key == i.droite: i.direction_set(0)
						elif event.key == i.haut: i.direction_set(0)
						elif event.key == i.gauche: i.direction_set(0)
						elif event.key == i.bas: i.direction_set(0)
						elif event.key == i.activ_bomb: i.BOOM = False
			pygame.time.delay(40)


	def place_mur(__,nombre=2):
		w = int(G.xmax/(G.R*2)) + 1
		h = int(G.ymax/(G.R*2)) + 1
		for x in range(w):
			Mur(x * G.R * 2,  0)
			Mur(x * G.R * 2,  G.R * h * 2 - G.R * 2)
		for y in range(h-2):
			Mur(0,  G.R * 2 + y * G.R * 2)
			Mur(G.R * w * 2 - G.R * 2,  G.R * 2 + y * G.R * 2)

		for x in range(w-2):
			for y in range(h-2):
				if x != 0 and x!=1 or y!=0 and y!=1 or x==1 and y==1:
					if x != w-3 and x!=w-4 or y!=0 and y!=1 or x==w-4 and y==1:
						if x != w-3 and x!=w-4 or y!=h-3 and y!=h-4 or x==w-4 and y==h-4:
							if x != 0 and x!=1 or y!=h-3 and y!=h-4 or x==1 and y==h-4:
								if y % 2 and x % 2:
									Mur(G.R * 2 + x * G.R * 2,  G.R * 2 + y * G.R * 2)
								else:
									Mur(G.R * 2 + x * G.R * 2,  G.R * 2 + y * G.R * 2,  1)
							else:
								if x == 0 and y ==h-3:
									if nombre >= 4:
										Joueur(G.R * 2 + x * G.R * 2,  G.R * 2 + y * G.R * 2)
										G.JOUEURS[-1].team = 1
						else:
							if x == w-3 and y ==h-3:
								if nombre >= 2:
									Joueur(G.R * 2 + x * G.R * 2,  G.R * 2 + y * G.R * 2)
									G.JOUEURS[-1].team = 1

					else:
						if x == w-3 and y ==0:
							if nombre >= 3:
								Joueur(G.R * 2 + x * G.R * 2,  G.R * 2 + y * G.R * 2)
				else:
					if x == 0 and y ==0:
						Joueur(G.R * 2 + x * G.R * 2,  G.R * 2 + y * G.R * 2)
