import pygame
import pygame_gui
import sys
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel
from dataclasses import dataclass
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
      relative_rect=pygame.Rect(350, 330, 150, 50),
      text='',
      manager=self.manager
    )


  def process_events(self, event: pygame.event.Event):
    pass

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