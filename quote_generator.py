import pygame
import pygame_gui
import sys
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel
from dataclasses import dataclass
import json
import random
class App:
  def __init__(self):
    pygame.init()
    self.size = (800, 600)
    self.screen = pygame.display.set_mode(self.size)
    self.manager = pygame_gui.UIManager(self.size)
    

    self.play_button = UIButton(
      relative_rect=pygame.Rect(350, 275, 150, 50),
      text='Play',
      manager=self.manager
    )

    self.display_label = UILabel(
      relative_rect=pygame.Rect(350, 50, 150, 50),
      text='',
      manager=self.manager
    )
  def random_quote(self):
                with open('quotes.json') as file:
                    content=file.read()
                    content=json.loads(content)
                    author=random.choice(list(content.keys()))
                    quote=content[author]
                    return (author, quote)
                    
  def process_events(self, event: pygame.event.Event):
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      if event.ui_element is self.play_button:
        quotes=self.random_quote()
        self.display_label.set_text(f'{quotes[1]}')

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

      pygame.display.flip()


App().run()