import pygame
import pygame_gui
import sys
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel
from dataclasses import dataclass
import json
import random
def afficher(text,position,taille,police,couleur):
    """cette fonction affiche à l'ecran un texte. 
     exemple d'utilisation:
     self.menu_label=afficher('Bienvenue\nby Lesno',(550,100),60)
     self.screen.blit(self.menu_label[0], self.menu_label[1])# Un autre appel dans le run avant le flip
       """
    pygame.init()
    font=pygame.font.SysFont(police, taille, bold=True)
    text_surface=font.render(text,True,couleur) #couleur blanche
    text_rect=text_surface.get_rect(center=position)#position en x et y
    clock = pygame.time.Clock()
    return (text_surface, text_rect)

class App:
  def __init__(self):
    pygame.init()
    self.size = (800, 600)
    self.screen = pygame.display.set_mode(self.size)
    self.manager = pygame_gui.UIManager(self.size)
    self.citation=''
    self.display_position=(400,120)

    self.play_button = UIButton(
      relative_rect=pygame.Rect(350, 275, 150, 50),
      text='Play',
      manager=self.manager
    )

    self.display_label=afficher(f'{self.citation}',self.display_position,10,'arial',(255,255,255))#couleur blanche
    self.screen.blit(self.display_label[0], self.display_label[1])

    self.welcome_label=afficher('Quote Generator by Lesno',(400,50),40,'time new roman',(255,0,0))#couleur rouge
    self.screen.blit(self.welcome_label[0], self.welcome_label[1])

  def random_quote(self):
                with open('quotes.json', encoding='utf8') as file:
                    content=file.read()
                    content=json.loads(content)
                    author=random.choice(list(content.keys()))
                    quote=content[author]
                    return (author, quote)
                    
  def process_events(self, event: pygame.event.Event):
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      if event.ui_element is self.play_button:
        quotes=self.random_quote()
        self.citation=f'{quotes[1]}\n {quotes[0]}'
        self.display_label=afficher(f'{self.citation}',self.display_position,40,'arial',(255,255,255))#couleur blanche
        self.screen.blit(self.display_label[0], self.display_label[1])

  def run(self):
    clock = pygame.time.Clock()
    while True:
      time_delta = clock.tick(60)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if not self.manager.process_events(event):
          self.process_events(event)

      self.manager.update(time_delta/1000)

      pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect((0, 0), self.size))

      self.manager.draw_ui(self.screen)

      self.screen.blit(self.display_label[0], self.display_label[1])

      self.screen.blit(self.welcome_label[0], self.welcome_label[1])

      pygame.display.flip()


App().run()