import sys
import subprocess
import os

try:
    import pygame
except ImportError:
    print("Installing pygame...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    import pygame
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class Game():
    def __init__(self,W,fps,bg):
        pygame.init()
        pygame.display.set_caption('TIC TAC TOE')
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.W = W
        self.bg = bg
        self.H = 100
        self.sc = pygame.display.set_mode((W,W+self.H))
        self.sc.fill(bg)
        self.over = 0
        self.x_point = 0
        self.o_point = 0
        self.draws = 0
        self.turn = 'X'
        self.res = [[0]*3,[0]*3,[0]*3]
        self.font = pygame.font.SysFont(resource_path("fonts/Boldonse-Regular.ttf"),40)
        self.x_img = pygame.transform.scale(pygame.image.load(resource_path("X.png")), (self.W//4,self.W//4))
        self.o_img = pygame.transform.scale(pygame.image.load(resource_path("O.png")), (self.W//4,self.W//4))
        x_text = self.font.render(f'X: {self.x_point}', True, 'black')
        o_text = self.font.render(f'O: {self.o_point}', True, 'black')
        d_text = self.font.render(f'Draw: {self.draws}', True, 'black')
        xo_text = self.font.render(f'Turn: {"X" if self.turn == "O" else "X"}',True,'black') 
        self.sc.blit(x_text,(5,5))
        self.sc.blit(o_text,(100,5))
        self.sc.blit(d_text,(5,35))
        self.sc.blit(xo_text,(5,65))
        pygame.draw.line(self.sc,'white',(0,self.H-2),(W,self.H-2),5)
        for i in range(1,3):
            pygame.draw.line(self.sc,'white',((W//3)*i,self.H),((W//3)*i,self.H+W),5)
            pygame.draw.line(self.sc,'white',(0,((W//3)*i)+self.H),(W,((W//3)*i)+self.H),5)
        pygame.display.update()
    
    def points(self):
        self.res = [[0]*3, [0]*3, [0]*3]
        self.sc.fill(self.bg)
        pygame.draw.line(self.sc, 'white', (0, self.H - 2), (self.W, self.H - 2), 5)
        for i in range(1, 3):
            pygame.draw.line(self.sc, 'white', ((self.W//3)*i, self.H), ((self.W//3)*i, self.H + self.W), 5)
            pygame.draw.line(self.sc, 'white', (0, ((self.W//3)*i) + self.H), (self.W, ((self.W//3)*i) + self.H), 5)
        pygame.draw.rect(self.sc, self.bg, (0, 0, self.W, self.H - 5))
        pygame.draw.line(self.sc, 'white', (0, self.H - 2), (self.W, self.H - 2), 5)
        x_text = self.font.render(f'X: {self.x_point}', True, 'black')
        o_text = self.font.render(f'O: {self.o_point}', True, 'black')
        d_text = self.font.render(f'Draw: {self.draws}', True, 'black')
        xo_text = self.font.render(f'Turn: {"X" if self.turn == "O" else "X"}',True,'black') 
        self.sc.blit(xo_text,(5,65))
        self.sc.blit(x_text,(5,5))
        self.sc.blit(o_text,(100,5))
        self.sc.blit(d_text,(5,35))
        
        self.over = 0
        pygame.display.update()
    def reset(self):
        self.turn = 'X'
        self.over = 0
        self.x_point = 0
        self.o_point = 0
        self.draws = 0
        self.points()
    def draw(self,x,y,turn):
        image = self.x_img if turn == 'X' else self.o_img
        size = self.W//3
        offset = (size - (self.W//4))//2
        pox = x* size + offset
        poy = y* size + offset + self.H
        xo_text = self.font.render(f'Turn: {"X" if turn == "O" else "O"}',True,'black') 
        pygame.draw.rect(self.sc,self.bg,(0,65,self.W,25))
        self.sc.blit(xo_text,(5,65))
        self.sc.blit(image,(pox,poy))
        pygame.display.update()
    def winner(self):
        for i in self.res:
            if i[0] == i[1] == i[2] != 0:
                return i[0]
        for i in range(3):
            if self.res[0][i] == self.res[1][i] == self.res[2][i] != 0:
                return self.res[0][i]
        if (self.res[0][0] == self.res[1][1] == self.res[2][2] != 0 or self.res[0][2] == self.res[1][1] == self.res[2][0] != 0):
            return self.res[1][1]
        if all(self.res[i][j] != 0 for i in range(3) for j in range(3)):
            return 'draw'    
        return 0
    def show_winer(self,res):
        font = pygame.font.SysFont(None,35)
        win = font.render(f"{res} won",True,'white')
        if res == 'draw':
            win = font.render(f"{res}",True,'white')
        self.sc.blit(win,(120,35))
        pygame.display.update()
        
    def run(self):
        while True:
            self.clock.tick(self.fps)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(),sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_r:
                        self.reset()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if self.over:
                        self.points()
                        continue
                    if e.pos[1] < self.H:
                        continue
                    x = e.pos[0]//(self.W//3)
                    y = (e.pos[1]-self.H)//(self.W//3)
                    if self.res[y][x] == 0:
                        self.res[y][x] = self.turn
                        self.draw(x,y,self.turn)
                        res = self.winner()
                        if res != 0:
                            self.over = 1
                            if res == 'X':
                                self.x_point += 1
                            elif res == 'O':
                                self.o_point += 1
                            else:
                                self.draws += 1
                            self.show_winer(res)
                        if self.turn == 'X':
                            self.turn = 'O'
                        else:
                            self.turn = 'X'
                        

ttt = Game(300,60,"#FFAE00")
ttt.run()
     