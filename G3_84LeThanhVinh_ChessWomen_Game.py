'''
NGười viết: Lê THành VInh
MSSV: 2110940
Ngày viết: 19/04/2023
Mô tả: Báo cáo cuối kì: EDA Chess - phần Game
'''


import pygame, sys, random
from pygame.locals import *

#PHẦN 1: ĐỊNH NGHĨA CÁC THAM SỐ
WINDOWWIDTH = 400
WINDOWHEIGHT = 600

# B2: khởi tạo thư viện pygame
pygame.init()

#B3: Lập cửa sổ game (400, 300). DISPLAYSURF là 1 biến kiểu surface (khung đen đen)
FPS = 60
fpsClockVinh = pygame.time.Clock()

#PHẦN 2: NỀN GAME 
#TỐC ĐỘ CUỘN NỀN
BGSPEED = 1.5
BGIMG = pygame.image.load('G3_84_LeThanhVinh_ChessWomen/background.png')

# LAYER (SURFACE) NỀN
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('84 - Lê Thành Vinh - 7.5 Game Xe Đua')

# LỚP HÌNH NỀN = CUỘN NỀN
class Background():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = BGSPEED
        self.img = BGIMG
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    def draw(self):
        DISPLAYSURF.blit(self.img, (self.x, self.y))
        DISPLAYSURF.blit(self.img, (self.x, self.y - self.height))
    def update(self):
        self.y += self.speed
        if self.y >= self.height:
            self.y = 0

#PHẦN 3: XE TRONG GAME

#KÍCH THƯỚC XE
X_MARGIN = 80
CARWIDTH = 40
CARHEIGHT = 80
CARSPEED = 10
CARIMG = pygame.image.load('G3_84_LeThanhVinh_ChessWomen/car.png')
#LỚP XE TRONG GAME
class Car84():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.x = (WINDOWWIDTH - self.width) / 2
        self.y = (WINDOWHEIGHT - self.height) / 2
        self.speed = CARSPEED
        self.surfaceVinh = pygame.Surface((self.width, self.height))
        self.surfaceVinh.fill((255, 255, 255))        
    def draw(self):
        DISPLAYSURF.blit(CARIMG, (int(self.x), int(self.y)))
    def update(self, moveLeft, moveRight, moveUp, moveDown):
        if moveLeft == True:
            self.x -= self.speed
        if moveRight == True:
            self.x += self.speed
        if moveUp == True:
            self.y -= self.speed
        if moveDown == True:
            self.y += self.speed

        if self.x < X_MARGIN:
            self.x = X_MARGIN
        if self.x + self.width > WINDOWWIDTH - X_MARGIN:
            self.x = WINDOWWIDTH - X_MARGIN - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > WINDOWHEIGHT:
            self.y = WINDOWHEIGHT - self.height
        

#PHẦN 4: XE CHƯỚNG NGẠI VẬT = XE NGƯỢC CHIỀU:obstacles ##
LANEWIDTH = 60
DISTANCE = 200
OBSTACLESSPEED = 10
CHANGESPEED = 0.001
OBSTACLESIMG = pygame.image.load('G3_84_LeThanhVinh_ChessWomen/obstacles.png')

class Obstacles():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.distance = DISTANCE
        self.speed = OBSTACLESSPEED
        self.changeSpeed = CHANGESPEED
        self.ls = []
        for i in range(5):
            y = -CARHEIGHT-i*self.distance
            lane = random.randint(0, 3)
            self.ls.append([lane, y])

    def draw(self):
        for i in range(5):
            x = int(X_MARGIN + self.ls[i][0]*LANEWIDTH + (LANEWIDTH-self.width)/2)
            y = int(self.ls[i][1])
            DISPLAYSURF.blit(OBSTACLESIMG, (x, y))

    def update(self):
        for i in range(5):
            self.ls[i][1] += self.speed
        self.speed += self.changeSpeed
        if self.ls[0][1] > WINDOWHEIGHT:
            self.ls.pop(0)
            y = self.ls[3][1] - self.distance
            lane = random.randint(0, 3)
            self.ls.append([lane, y])


#PHẦN 5: TÍNH ĐIỂM
class Score():
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('sans', 20)
    def draw(self):
        font = pygame.font.SysFont('consolas', 30)
        scoreSuface = font.render('Score: '+str(int(self.score)), True, (0, 0, 0))
        DISPLAYSURF.blit(scoreSuface, (10, 10))
    def update(self):
        self.score += 0.02
# PHẦN 6: XỬ LÝ VA CHẠM: Collision
def rectCollision(rect1, rect2):
    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
        return True
    return False
def isGameover(car84, obstacles):
    carRect = [car84.x, car84.y, car84.width, car84.height]
    for i in range(5):
        x = int(X_MARGIN + obstacles.ls[i][0]*LANEWIDTH + (LANEWIDTH-obstacles.width)/2)
        y = int(obstacles.ls[i][1])
        obstaclesRect = [x, y, obstacles.width, obstacles.height]
        if rectCollision(carRect, obstaclesRect) == True:
            return True
    return False
    
    #PHẦN 7: CÁC THỦ TỤC CHƠI GAME
def gameOver(bg, car84, obstacles, score):
    font = pygame.font.SysFont('consolas', 60)
    headingSuface = font.render('GAMEOVER', True, (255, 0, 0))
    headingSize = headingSuface.get_size()

    font = pygame.font.SysFont('consolas', 20)
    commentSuface = font.render('Press "space" to replay', True, (0, 0, 0))
    commentSize = commentSuface.get_size()

    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == K_SPACE:
                        return
            bg.draw()
            car84.draw()
            obstacles.draw()
            score.draw()
            DISPLAYSURF.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0])/2), 100))
            DISPLAYSURF.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0])/2), 400))
            pygame.display.update()
            fpsClockVinh.tick(FPS)

def gameStart(bg):
        bg.__init__()
        font = pygame.font.SysFont('consolas', 60)
        headingSuface = font.render('RACING', True, (255, 0, 0))
        headingSize = headingSuface.get_size()

        font = pygame.font.SysFont('consolas', 20)
        commentSuface = font.render('Press "space" to play', True, (0, 0, 0))
        commentSize = commentSuface.get_size()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    return
            bg.draw()
            DISPLAYSURF.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0])/2), 100))
            DISPLAYSURF.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0])/2), 400))
            pygame.display.update()
            fpsClockVinh.tick(FPS)

def gamePlay(bg, car84, obstacles, score):
        car84.__init__()
        obstacles.__init__()
        bg.__init__()
        score.__init__()
        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        moveLeft = True
                    if event.key == K_RIGHT:
                        moveRight = True
                    if event.key == K_UP:
                        moveUp = True
                    if event.key == K_DOWN:
                        moveDown = True
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        moveLeft = False
                    if event.key == K_RIGHT:
                        moveRight = False
                    if event.key == K_UP:
                        moveUp = False
                    if event.key == K_DOWN:
                        moveDown = False
            if isGameover(car84, obstacles):
                return 
            bg.draw()
            bg.update()
            car84.draw()
            car84.update(moveLeft, moveRight, moveUp, moveDown)
            obstacles.draw()
            obstacles.update()
            score.draw()
            score.update()
            pygame.display.update()
            fpsClockVinh.tick(FPS)

def main():
    bg = Background()
    car84 = Car84()
    obstacles = Obstacles()
    score = Score()
    gameStart(bg)
    while True:
        gamePlay(bg, car84, obstacles, score)
        gameOver(bg, car84, obstacles, score)



if __name__ == '__main__':
    main()



