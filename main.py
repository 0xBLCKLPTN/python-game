import pygame as pg

pg.init()

class Game:
    def __init__(self) -> object:
        window_size: tuple = (300,300)
        pg.display.set_caption("Моя игра моя игра она же как и я")
        self.screen = pg.display.set_mode(window_size)
        background_color = (0, 0, 255)  # синий

 
        self.screen.fill(background_color)


        pg.display.flip()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

a = Game()