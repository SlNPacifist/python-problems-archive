import pygame
import sys
from axis_drawer import AxisDrawer
from button import Button
from input_box import InputBox
from solution import get_tile_number

# Инициализация Pygame
pygame.init()

# Размеры окна и цвета для визуального представления
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
GRID_COLOR = (0, 0, 0)  # Черный для контраста с плитками
TILE_COLOR = (200, 200, 200)  # Светло-серый для лучшей читаемости номеров
TEXT_COLOR = (0, 0, 0)  # Черный текст на светлом фоне
INPUT_BG_COLOR = (255, 255, 255)  # Белый фон для полей ввода
INPUT_BORDER_COLOR = (100, 100, 100)  # Серый для неактивных полей
BUTTON_COLOR = (100, 150, 255)  # Синий для кнопок
BUTTON_HOVER_COLOR = (150, 200, 255)  # Светло-синий для наведения
AXIS_COLOR = (0, 0, 255)  # Синий для осей

# Настройка дисплея
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Пронумерованные плитки")

# Настройка шрифтов
input_font = pygame.font.Font(None, 32)
button_font = pygame.font.Font(None, 32)
tile_font = pygame.font.Font(None, 36)
axis_font = pygame.font.Font(None, 24)

# Создание полей ввода
tile_size_input = InputBox(50, 50, 100, 30, '100', 'Размер плитки', font=input_font)
rows_input = InputBox(250, 50, 100, 30, '6', 'Количество строк', font=input_font)
cols_input = InputBox(450, 50, 100, 30, '8', 'Количество столбцов', font=input_font)

# Кнопки для масштабирования
zoom_factor = 1.0
zoom_step = 0.1
min_zoom = 0.5
max_zoom = 3.0

# Add these variables after other global variables
clicked_tile = None  # Хранит номер выбранной плитки
info_font = pygame.font.Font(None, 36)

def zoom_in():
    global zoom_factor
    zoom_factor = min(zoom_factor + zoom_step, max_zoom)

def zoom_out():
    global zoom_factor
    zoom_factor = max(zoom_factor - zoom_step, min_zoom)

# Создание кнопок для масштабирования
zoom_in_button = Button(650, 50, 40, 30, '+', zoom_in, font=button_font)
zoom_out_button = Button(700, 50, 40, 30, '-', zoom_out, font=button_font)

clock = pygame.time.Clock()
FPS = 30

mouse_x = 0
mouse_y = 0

# Основной игровой цикл
running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEWHEEL:
            # Обработка колесика мыши для масштабирования
            if event.y > 0:
                zoom_in()
            elif event.y < 0:
                zoom_out()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                clicked_tile = get_tile_number(mouse_x, mouse_y, tile_size, rows, cols)
        
        # Обработка событий для полей ввода
        tile_size_input.handle_event(event)
        rows_input.handle_event(event)
        cols_input.handle_event(event)
        
        # Обработка событий для кнопок
        zoom_in_button.handle_event(event)
        zoom_out_button.handle_event(event)


    # Заполнение экрана белым цветом
    screen.fill((255, 255, 255))

    # Отрисовка полей ввода
    tile_size_input.draw(screen)
    rows_input.draw(screen)
    cols_input.draw(screen)

    # Отрисовка кнопок
    zoom_in_button.draw(screen)
    zoom_out_button.draw(screen)

    # Преобразование текстовых значений в числа с обработкой ошибок
    try:
        tile_size = int(tile_size_input.text)
        rows = int(rows_input.text)
        cols = int(cols_input.text)
    except ValueError:
        tile_size = 100
        rows = 6
        cols = 8

    # Расчет общего количества плиток
    total_tiles = rows * cols

    # Начальная позиция сетки (с учетом отступа для полей ввода и места для осей)
    grid_start_x = 50  # Сдвиг вправо для размещения Y-оси и подписей
    grid_start_y = 150  # Сдвиг вниз на 50 пикселей (было 100)

    # Создание объекта для отрисовки осей
    # Вычисляем размеры области осей на основе размера плитки и количества строк/столбцов
    axis_width = cols * tile_size
    axis_height = rows * tile_size
    
    # Создаем вектор для точки начала осей
    origin = pygame.math.Vector2(grid_start_x, grid_start_y)
    
    axis_drawer = AxisDrawer(
        origin=origin,
        width=axis_width,
        height=axis_height,
        zoom_factor=zoom_factor,
        font=axis_font
    )

    # Отрисовка сетки и номеров с учетом масштаба
    tile_number = 0
    for row in range(rows):
        for col in range(cols):
            if tile_number > total_tiles:
                break
                
            # Вычисление позиции плитки с учетом масштаба
            x = grid_start_x + col * tile_size * zoom_factor
            y = grid_start_y + row * tile_size * zoom_factor

            # Отрисовка прямоугольника плитки с учетом масштаба
            pygame.draw.rect(screen, TILE_COLOR, (x, y, tile_size * zoom_factor, tile_size * zoom_factor))
            pygame.draw.rect(screen, GRID_COLOR, (x, y, tile_size * zoom_factor, tile_size * zoom_factor), 1)

            # Создание и позиционирование текста номера с учетом масштаба
            text = tile_font.render(str(tile_number), True, TEXT_COLOR)
            text_rect = text.get_rect(center=(x + (tile_size * zoom_factor) // 2, y + (tile_size * zoom_factor) // 2))
            screen.blit(text, text_rect)

            tile_number += 1
    
    # Отрисовка осей с делениями и подписями
    axis_drawer.draw_axes(screen)

    # Получение текущей позиции мыши
    mouse_pos = pygame.mouse.get_pos()
    
    # Проверка, находится ли мышь в пределах области плиток
    if (grid_start_x <= mouse_pos[0] <= grid_start_x + axis_width * zoom_factor and 
        grid_start_y <= mouse_pos[1] <= grid_start_y + axis_height * zoom_factor):
        
        # Преобразование координат мыши в координаты сетки с учетом масштаба
        mouse_x = int((mouse_pos[0] - grid_start_x) / zoom_factor)
        mouse_y = int((mouse_pos[1] - grid_start_y) / zoom_factor)
        
        # Отрисовка координат мыши
        coord_text_surface = input_font.render("Координаты мыши", True, TEXT_COLOR)
        screen.blit(coord_text_surface, (800, 20))
        coord_surface = input_font.render(f"x={mouse_x}, y={mouse_y}", True, TEXT_COLOR)
        screen.blit(coord_surface, (800, 50))

    # Отображение информации о выбранной плитке
    if clicked_tile is not None:
        info_text = f"Выбрана плитка: {clicked_tile}"
        info_surface = info_font.render(info_text, True, (0, 0, 0))
        screen.blit(info_surface, (10, WINDOW_HEIGHT - 40))

    # Обновление дисплея
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
