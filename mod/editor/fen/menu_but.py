# -*- coding: cp1252 -*-
from mod.__init__ import *
from menu import Menu
from mod.wgt.wgt_label import Wgt_label

briefing = \
"""\
Le but de ce jeu si vous le voulez (ou non), est de ramasser les petites
boules dor�e, en utilisant votre agilit� � la souris .

ATTENTION : Vous �tes en train de vous dire rien de plus facile, je vais
faire ca les doigts dans le nez, bah avant que vous vous salisiez vos
doigts ... d�trompez vous, cette mission est de loin plus dure que
ce que vous ne vous imaginez .
Car des murs traversant votre lieu de travail vous �craseront si vous
vous faites toucher, vous serez remplac�, et attention ! Le temps pour
r�ussir votre mission est limit� .

N'oubliez pas, toutes les boules sont positives pour vous, alors que,
tous les carr�s sont n�gatifs .
"""

class Menu_but(Menu):
	def __init__(__):
		Menu.__init__(__, ['Quitter'], "BUT")
	
	def boucle(__):
		__.font = 'data/fonts/VideoPhreak.ttf'
		__.label = Wgt_label(K.screen, 50, 280, w=__.size - 50, h=320, text=briefing, font=__.font, coul_font=(0, 0, 255), font_size=17)
		Menu.boucle(__)
		
	def draw(__):
		Menu.draw(__)
		__.label.blit()
		
	def draw_text(__):
		Menu.draw_text(__, y=600)
	
	def quit(__): pass
