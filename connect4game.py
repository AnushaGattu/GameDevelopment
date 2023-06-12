import pygame
import sys
pygame.init()
dis = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
info = pygame.display.Info()
x = info.current_w
y = info.current_h
pygame.display.set_caption("CONNECT 4 GAME")
pygame.font.init()
font_size = 200
font = pygame.font.SysFont("Arial", font_size)
letter1 = font.render("c", True, "purple")
letter2 = font.render("o", True, "red")
letter3 = font.render("n", True, "blue")
letter4 = font.render("n", True, "green")
letter5 = font.render("e", True, "blue")
letter6 = font.render("c", True, "orange")
letter7 = font.render("t", True, "purple")
letter8 = font.render("4", True, "black")
running = True

def start_game():
    window_width, window_height = 800, 600
    window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
    pygame.display.set_caption("Grid of Circles")
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 50)
    text = font.render("CONNECT-4", True, "black")
    font=pygame.font.SysFont("Arial",25)
    text1=font.render("Player-1",True,"black","lightpink")
    text2=font.render("Player-2",True,"black","lightpink")
    font = pygame.font.SysFont("Arial", 100)
    play = font.render("player-1 wins !", True, "red","black")
    play1= font.render("player-2 wins !", True, "red","black")
    
    
    grid_width, grid_height = 6, 7
    circle_radius = 15
    margin = 20
    circle_colors = ["red", "blue", "green"]
    occupied = 0

    def calculate_grid():
        available_width = window.get_width() - 2 * margin
        available_height = window.get_height() - 2 * margin
        grid_size_x = ((available_width - (grid_width - 1) * margin) // grid_width // 2)
        grid_size_y = ((available_height - (grid_height - 1) * margin) // grid_height // 2)
        grid_start_x = margin + (((available_width - grid_width * (grid_size_x + margin)) // 2))
        grid_start_y = margin + (((available_height - grid_height * (grid_size_y + margin)) // 2))

        return grid_size_x, grid_size_y, grid_start_x, grid_start_y

    def create_grid():
        grid = []

        for row in range(grid_height):
            grid.append([])
            for column in range(grid_width):
                grid[row].append(0)
        return grid

    def draw_circles(grid, grid_size_x, grid_size_y, grid_start_x, grid_start_y):
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                x = grid_start_x + j * (grid_size_x + margin)
                y = grid_start_y + i * (grid_size_y + margin)
                circle_color = circle_colors[value]
                pygame.draw.circle(window, circle_color, (x + grid_size_x // 2, y + grid_size_y // 2), circle_radius)
        if check_win(grid, 1):
            play_rect = play.get_rect(center=(window.get_width()//2, window.get_height()//2))
            window.blit(play, play_rect)
           
            button_rect,button_rect1 = draw_button()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        start_game()
                    if button_rect1.collidepoint(event.pos):
                        pygame.quit()


           
        elif check_win(grid, 2):
            play1_rect = play1.get_rect(center=(window.get_width()//2, window.get_height()//2))
            window.blit(play1, play1_rect)
            button_rect,button_rect1 = draw_button()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        start_game()
                    if button_rect1.collidepoint(event.pos):
                        pygame.quit()
            
                pygame.display.flip()
                pygame.display.update()
            
           
         

    grid = create_grid()
    
    def check_win(grid, player):
        # Check rows
        for row in grid:
            for i in range(grid_width - 3):
                if row[i] == row[i + 1] == row[i + 2] == row[i + 3] == player:
                    return True

        # Check columns
        for j in range(grid_width):
            for i in range(grid_height - 3):
                if grid[i][j] == grid[i + 1][j] == grid[i + 2][j] == grid[i + 3][j] == player:
                    return True

        # Check diagonals (top-left to bottom-right)
        for i in range(grid_height - 3):
            for j in range(grid_width - 3):
                if grid[i][j] == grid[i + 1][j + 1] == grid[i + 2][j + 2] == grid[i + 3][j + 3] == player:
                    return True

        # Check diagonals (top-right to bottom-left)
        for i in range(grid_height - 3):
            for j in range(3, grid_width):
                if grid[i][j] == grid[i + 1][j - 1] == grid[i + 2][j - 2] == grid[i + 3][j - 3] == player:
                    return True

        return False
    def draw_button():
        button_color = "red"
        button_rect = pygame.Rect(260, 535, 200, 100)
        button_rect1=pygame.Rect(800,535,200,100)
        pygame.draw.rect(window, button_color, button_rect)
        pygame.draw.rect(window, button_color, button_rect1)
        button_text = pygame.font.SysFont(None, 30).render("Start Game", True, (255, 255, 255))
        button_text2=pygame.font.SysFont(None,30).render("Exit",True,(225,225,225))
        text_rect = button_text.get_rect(center=button_rect.center)
        text_rect2=button_text2.get_rect(center=button_rect1.center)
        window.blit(button_text, text_rect)
        window.blit(button_text2,text_rect2)
        return button_rect,button_rect1
    
        
                

    running = True
    while running:
        window.fill(("violet"))
        pygame.draw.rect(window, ("lightyellow"), pygame.Rect(((window.get_width()-50)//2-400),40,830,600 ))
    
        window.blit(text, ( (window.get_width()-50)//2-120,50 ))
        window.blit(text1,( (window.get_width()-25)//2-120,550))
        window.blit(text2,( (window.get_width()-25)//2-120,600 ))
        pygame.draw.circle(window,"blue", ((window.get_width()+55)//2,565), circle_radius)
        pygame.draw.circle(window, "green", ((window.get_width()+55)//2,615), circle_radius)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                window_width, window_height = event.w, event.h
                window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    pos = pygame.mouse.get_pos()
                    col = (pos[0] - grid_start_x) // (grid_size_x + margin)
                    row = (pos[1] - grid_start_y) // (grid_size_y + margin)

                    if 0 <= row < grid_height and 0 <= col < grid_width and grid[row][col] == 0:
                        grid[row][col] = occupied % 2 + 1
                        occupied += 1
        grid_size_x, grid_size_y, grid_start_x, grid_start_y = calculate_grid()
        draw_circles(grid, grid_size_x, grid_size_y, grid_start_x, grid_start_y)
        pygame.display.update()
        pygame.display.flip()

while running:
    dis.fill("lightblue")
    x = info.current_w
    y = info.current_h
    dis.blit(letter1, (x - 200, y - 300))
    dis.blit(letter2, (x - 100, y - 300))
    dis.blit(letter3, (x, y - 300))
    dis.blit(letter4, (x + 100, y - 300))
    dis.blit(letter5, (x + 200, y - 300))
    dis.blit(letter6, (x + 300, y - 300))
    dis.blit(letter7, (x + 400, y - 300))
    dis.blit(letter8, (x + 500, y - 300))

    def draw_button():
        button_color = "red"
        button_rect = pygame.Rect(550, 500, 200, 100)
        pygame.draw.rect(dis, button_color, button_rect)
        button_text = pygame.font.SysFont(None, 30).render("Start Game", True, (255, 255, 255))
        text_rect = button_text.get_rect(center=button_rect.center)
        dis.blit(button_text, text_rect)
        return button_rect

    button_rect = draw_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                start_game()

    pygame.display.update()
    pygame.display.flip()

pygame.quit()
