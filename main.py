import pygame, random, copy

def draw(passed_in_board):
    for i, row in enumerate(passed_in_board):
        for j, col in enumerate(row):                
            if not col:
                continue
            pygame.draw.rect(window, col, pygame.Rect(sand_size * j, sand_size * i, sand_size, sand_size))


pygame.init()
width, height = 800, 800
window = pygame.display.set_mode((width, height))
sand_size = 10
running = True
clock = pygame.time.Clock()
board = [[0] * (width//sand_size) for i in range(width//sand_size)]
color_index = random.randint(0, 255)
red_amount = random.randint(0, 255)
blue_amount = random.randint(0, 255)
color_index_increment = random.randint(0, 10)/10
wind_amount = 1
screen_color = 0
font = pygame.font.Font(None, 36)  # You can also specify a font file path instead of 'None'

all_boards = []

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen_color+=.01


    mx, my = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        row, col = my//sand_size, mx//sand_size
        board[row][col] = (red_amount, color_index%255, blue_amount)
        color_index += color_index_increment
    else:
        row, col = my//sand_size, mx//sand_size
        board[row][col] = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_c]:
        board = [[0] * (width//sand_size) for i in range(width//sand_size)]
    if keys[pygame.K_r]:
        color_index = random.randint(0, 255)
        red_amount = random.randint(0, 255)
        blue_amount = random.randint(0, 255)
        color_index_increment = random.randint(2, 10)/10
    if keys[pygame.K_q]:
        running = False

    que = []

    for i in range(len(board)-1):
        for j in range(len(board[i])):
            if board[i][j] and not board[i+1][j]:
                ri = random.randint(2, 3)
                rj = random.randint(-wind_amount, +wind_amount)
                if i+ri >= len(board) or not (1 < j+rj < len(board[0])) or board[i+ri][j+rj]:
                    que.append((i+1, j, board[i][j]))
                    board[i][j] = 0
                else:
                    que.append((i+ri, j+rj, board[i][j]))
                    board[i][j] = 0
                    continue

    for i, j, color in que:
        board[i][j] = color

    if not all_boards or board != all_boards[-1]:
        all_boards.append(copy.deepcopy(board))
                
    window.fill((screen_color, screen_color, screen_color))
    draw(board)
    pygame.display.update()


for board in all_boards:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    screen_color+=.01
    window.fill('black')
    for i, row in enumerate(board):
        for j, col in enumerate(row):                
            if not col:
                continue
            pygame.draw.rect(window, col, pygame.Rect(sand_size * j, sand_size * i, sand_size, sand_size))

    pygame.display.update()