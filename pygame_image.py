import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    tmr = 0
    img = pg.image.load("ex01/fig/3.png")
    ton_img = pg.transform.flip(img, True, False)
    ton10_img = pg.transform.rotozoom(ton_img, 10, 1.0)
    lst = [ton_img, ton10_img]
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
        x = tmr%1600
        if 0 <= tmr%20 < 10:
            i = 0
        else:
            i = 1
        screen.blit(bg_img, [-x, 0])
        screen.blit(pg.transform.flip(bg_img, True, False), [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(lst[i], [300, 200])
        
        pg.display.update()
        tmr += 1        
        clock.tick(20)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()