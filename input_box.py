import pygame

class InputBox:
    def __init__(self, x, y, width, height, text='', label='', font=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (100, 100, 100)  # Серый для неактивных полей
        self.text = text
        self.label = label
        self.font = font if font else pygame.font.Font(None, 32)
        self.txt_surface = self.font.render(text, True, (0, 0, 0))
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = (0, 0, 255) if self.active else (100, 100, 100)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                    self.color = (100, 100, 100)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode.isnumeric():
                        self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, (0, 0, 0))

    def draw(self, screen):
        # Отрисовка метки
        label_surface = self.font.render(self.label, True, (0, 0, 0))
        screen.blit(label_surface, (self.rect.x, self.rect.y - 25))
        
        # Отрисовка поля ввода
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5)) 