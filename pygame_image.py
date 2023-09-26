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
    ton10_img = pg.transform.rotate(ton_img, 10)
    lst = [ton_img, ton10_img]
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        for i in range(len(lst)):
            img_rct = lst[i].get_rect()
            img_rct.center = 300, 200
            screen.blit(lst[i], img_rct)
        
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()