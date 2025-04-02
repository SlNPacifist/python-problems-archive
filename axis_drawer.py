import pygame

class AxisDrawer:
    def __init__(self, origin, width, height, zoom_factor=1.0, font=None):
        """
        Инициализация компонента для отрисовки осей координат
        
        Args:
            origin: Точка начала осей как pygame.math.Vector2
            width: Ширина области осей в пикселях
            height: Высота области осей в пикселях
            zoom_factor: Коэффициент масштабирования (по умолчанию 1.0)
            font: Шрифт для подписей осей (по умолчанию None, используется стандартный)
        """
        self.origin = origin
        self.width = width
        self.height = height
        self.zoom_factor = zoom_factor
        self.axis_color = (0, 0, 255)  # Синий для осей
        self.axis_font = font if font else pygame.font.Font(None, 24)
        self.tick_length = 5  # Длина делений на осях
        self.label_interval = 100  # Интервал для подписей (каждые 100 пикселей)
        self.arrow_size = 10  # Размер стрелок на концах осей
    
    def draw_axes(self, screen):
        """
        Отрисовка осей X и Y с делениями и подписями
        
        Args:
            screen: Поверхность Pygame для отрисовки
        """
        # Ось Y (вертикальная)
        pygame.draw.line(screen, self.axis_color, 
                        (self.origin.x, self.origin.y), 
                        (self.origin.x, self.origin.y + self.height * self.zoom_factor), 
                        2)
        
        # Ось X (горизонтальная)
        pygame.draw.line(screen, self.axis_color, 
                        (self.origin.x, self.origin.y), 
                        (self.origin.x + self.width * self.zoom_factor, self.origin.y), 
                        2)
        
        # Отрисовка стрелок на концах осей
        self._draw_arrows(screen)
        
        # Подписи осей
        self._draw_axis_labels(screen)
        
        # Отрисовка делений и подписей
        self._draw_x_ticks(screen)
        self._draw_y_ticks(screen)
    
    def _draw_arrows(self, screen):
        """
        Отрисовка стрелок на концах осей X и Y
        
        Args:
            screen: Поверхность Pygame для отрисовки
        """
        # Стрелка на конце оси X
        x_end = (self.origin.x + self.width * self.zoom_factor, self.origin.y)
        x_arrow_left = (x_end[0] - self.arrow_size, x_end[1] - self.arrow_size)
        x_arrow_right = (x_end[0] - self.arrow_size, x_end[1] + self.arrow_size)
        pygame.draw.polygon(screen, self.axis_color, [x_end, x_arrow_left, x_arrow_right])
        
        # Стрелка на конце оси Y
        y_end = (self.origin.x, self.origin.y + self.height * self.zoom_factor)
        y_arrow_left = (y_end[0] - self.arrow_size, y_end[1] - self.arrow_size)
        y_arrow_right = (y_end[0] + self.arrow_size, y_end[1] - self.arrow_size)
        pygame.draw.polygon(screen, self.axis_color, [y_end, y_arrow_left, y_arrow_right])
    
    def _draw_axis_labels(self, screen):
        """
        Отрисовка подписей осей X и Y
        
        Args:
            screen: Поверхность Pygame для отрисовки
        """
        # Подпись оси Y (в конце оси)
        y_label = self.axis_font.render("Y", True, self.axis_color)
        screen.blit(y_label, (self.origin.x - 20, self.origin.y + self.height * self.zoom_factor + 10))
        
        # Подпись оси X
        x_label = self.axis_font.render("X", True, self.axis_color)
        screen.blit(x_label, (self.origin.x + self.width * self.zoom_factor + 10, self.origin.y - 20))
    
    def _draw_x_ticks(self, screen):
        """
        Отрисовка делений и подписей на оси X
        
        Args:
            screen: Поверхность Pygame для отрисовки
        """
        # Определяем количество делений на основе ширины и интервала
        num_ticks = int(self.width / self.label_interval) + 1
        
        for i in range(num_ticks + 1):
            # Позиция деления в пикселях
            pixel_pos = i * self.label_interval
            # Позиция деления с учетом масштаба
            x_pos = self.origin.x + pixel_pos * self.zoom_factor
            
            # Отрисовка деления
            pygame.draw.line(screen, self.axis_color, 
                            (x_pos, self.origin.y - self.tick_length), 
                            (x_pos, self.origin.y + self.tick_length), 
                            1)
            
            # Подпись значения
            x_text = self.axis_font.render(str(pixel_pos), True, self.axis_color)
            screen.blit(x_text, (x_pos - 10, self.origin.y - 20))
    
    def _draw_y_ticks(self, screen):
        """
        Отрисовка делений и подписей на оси Y
        
        Args:
            screen: Поверхность Pygame для отрисовки
        """
        # Определяем количество делений на основе высоты и интервала
        num_ticks = int(self.height / self.label_interval) + 1
        
        for i in range(num_ticks + 1):
            # Позиция деления в пикселях
            pixel_pos = i * self.label_interval
            # Позиция деления с учетом масштаба
            y_pos = self.origin.y + pixel_pos * self.zoom_factor
            
            # Отрисовка деления
            pygame.draw.line(screen, self.axis_color, 
                            (self.origin.x - self.tick_length, y_pos), 
                            (self.origin.x + self.tick_length, y_pos), 
                            1)
            
            # Подпись значения
            y_text = self.axis_font.render(str(pixel_pos), True, self.axis_color)
            screen.blit(y_text, (self.origin.x - 30, y_pos - 10))
    
    def set_zoom_factor(self, zoom_factor):
        """Установка коэффициента масштабирования"""
        self.zoom_factor = zoom_factor 