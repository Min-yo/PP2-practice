from turtle import position
import math
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    baseLayer = pygame.Surface((640, 480))
    clock = pygame.time.Clock()
    R = (255, 0, 0)
    G = (0, 255, 0)
    B = (0, 0, 255)
    key_R = True
    key_G = False
    key_B = False

    prevX = 0
    prevY = 0

    currentX = -1
    currentY = -1

    screen.fill((0, 0, 0))

    isMouseDown = False
    rectan = True
    circle = False
    eraser = False
    square = False
    right_triangle = False
    equilateral_triangle = False
    rhombus = False

    while True:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: # 1 = rectangle
                    rectan = True
                    circle = False
                    eraser = False
                    square = False
                    right_triangle = False
                    equilateral_triangle = False
                    rhombus = False
                if event.key == pygame.K_2: # 2 = circle
                    rectan = False
                    circle = True
                    eraser = False
                    square = False
                    right_triangle = False
                    equilateral_triangle = False
                    rhombus = False
                if event.key == pygame.K_3: # 3 = eraser
                    rectan = False
                    circle = False
                    eraser = True
                    square = False
                    right_triangle = False
                    equilateral_triangle = False
                    rhombus = False
                if event.key == pygame.K_4: # 4 = square
                    rectan = False
                    circle = False
                    eraser = False
                    square = True
                    right_triangle = False
                    equilateral_triangle = False
                    rhombus = False
                if event.key == pygame.K_5: # 5 = right_triangle
                    rectan = False
                    circle = False
                    eraser = False
                    square = False
                    right_triangle = True
                    equilateral_triangle = False
                    rhombus = False
                if event.key == pygame.K_6: # 6 = equilateral_triangle
                    rectan = False
                    circle = False
                    eraser = False
                    square = False
                    right_triangle = False
                    equilateral_triangle = True
                    rhombus = False
                if event.key == pygame.K_7: # 7 = rhombus
                    rectan = False
                    circle = False
                    eraser = False
                    square = False
                    right_triangle = False
                    equilateral_triangle = False
                    rhombus = True
                if event.key == pygame.K_r:
                    key_R = True
                    key_G = False
                    key_B = False
                if event.key == pygame.K_g:
                    key_R = False
                    key_G = True
                    key_B = False
                if event.key == pygame.K_b:
                    key_R = False
                    key_G = False
                    key_B = True
                

        if eraser:
            if isMouseDown: #eraser
                    pygame.draw.line(screen, (0, 0, 0), (prevX, prevY), (currentX, currentY), 10)
                
            prevX = currentX
            prevY = currentY
        elif isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1: 
            screen.blit(baseLayer, (0, 0))

            if circle: #circle
                radius = math.sqrt((abs(prevX - currentX))**2+ (abs(prevY - currentY))**2)
                if key_R:
                    pygame.draw.circle(screen, R,(min(prevX, currentX), min(prevY, currentY)), radius, 1)
                elif key_G:
                    pygame.draw.circle(screen, G,(min(prevX, currentX), min(prevY, currentY)), radius, 1)
                elif key_B:    
                    pygame.draw.circle(screen, B,(min(prevX, currentX), min(prevY, currentY)), radius, 1)
            elif rectan: #rectangle
                r = calculateRect(prevX, prevY, currentX, currentY)
                if key_R:
                    pygame.draw.rect(screen, R,pygame.Rect(r), 1)
                elif key_G:
                    pygame.draw.rect(screen, G,pygame.Rect(r), 1)
                elif key_B:
                    pygame.draw.rect(screen, B,pygame.Rect(r), 1)
            elif square: #square
                r = calculateSqr(prevX, prevY, currentX, currentY)
                if key_R:
                    pygame.draw.rect(screen, R,pygame.Rect(r), 1)
                elif key_G:
                    pygame.draw.rect(screen, G,pygame.Rect(r), 1)
                elif key_B:
                    pygame.draw.rect(screen, B,pygame.Rect(r), 1)
            elif right_triangle: #right_triangle
                p1 = (min(prevX, currentX), max(prevY, currentY))
                p2 = (min(prevX, currentX), min(prevY, currentY))
                p3 = (max(prevX, currentX), max(prevY, currentY))
                if key_R:
                    pygame.draw.polygon(screen, R, (p1, p2, p3), 1)
                elif key_G:
                    pygame.draw.polygon(screen, G, (p1, p2, p3), 1)
                elif key_B:
                    pygame.draw.polygon(screen, B, (p1, p2, p3), 1)
            elif equilateral_triangle: #equilateral_triangle
                p1 = (min(prevX, currentX), max(prevY, currentY))
                
                least_side = min(abs(prevX - currentX), abs(prevY - currentY))
                if abs(prevX - currentX) == least_side:
                    p2 = ((prevX + currentX)/2, max(prevY, currentY) + least_side)
                    p3 = (max(prevX, currentX), max(prevY, currentY))
                elif abs(prevY - currentY) == least_side:
                    p2 = (min(prevX, currentX)+ least_side/2, min(prevY, currentY))
                    p3 = (min(prevX, currentX)+ least_side, max(prevY, currentY))
                
                #p2 = ((abs(prevX-currentX))/2+currentX, currentY)
                #p3 = (prevX, currentY)
                if key_R:
                    pygame.draw.polygon(screen, R, (p1, p2, p3), 1)
                elif key_G:
                    pygame.draw.polygon(screen, G, (p1, p2, p3), 1)
                elif key_B:
                    pygame.draw.polygon(screen, B, (p1, p2, p3), 1)
            elif rhombus: #rhombus
                p4 = ((prevX + currentX)/2, max(prevY, currentY))
                p2 = ((prevX + currentX)/2, min(prevY, currentY))
                p3 = (max(prevX, currentX), (prevY + currentY)/2)
                p1 = (min(prevX, currentX), (prevY + currentY)/2)
                if key_R:
                    pygame.draw.polygon(screen, R, (p1, p2, p3, p4), 1)
                elif key_G:
                    pygame.draw.polygon(screen, G, (p1, p2, p3, p4), 1)
                elif key_B:
                    pygame.draw.polygon(screen, B, (p1, p2, p3, p4), 1)

        pygame.display.flip()
        clock.tick(60)


def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
def calculateSqr(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), min(abs(x1 - x2), abs(y1 - y2)), min(abs(x1 - x2), abs(y1 - y2)))

# pygame.draw.polygone(surface=window, color=(255,0,0), points=[(50,100), (100,50), (150,100)])
main()

