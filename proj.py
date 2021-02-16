from pygame_functions import *
import pygame, sys
import string

screenSize(800,800)

label1 = makeLabel("""Find the speed and acceleration of a small""", 30, 10, 10, "blue", "Times New Roman", "yellow")
label4 = makeLabel("""stone lodged in the tread of the tire (on its outer edge).""", 30, 10, 40, "blue", "Times New Roman", "yellow")
showLabel(label1)
showLabel(label4)


label2 = makeLabel("Enter radius and constant rate here", 30, 10, 150, "blue", "Times New Roman", "yellow")
showLabel(label2)


wordBox1= makeTextBox(10, 200, 300, 0, "Enter number here", 10, 24)
showTextBox(wordBox1)
entry1 = textBoxInput(wordBox1)

output = makeLabel(entry1, 30, 10, 250, "blue", "Times New Roman", "yellow")
showLabel(output)

x = entry1.split()
v = (2*3.14*(float(x[0])))/ (60/(int(x[1])))
a = pow(float(v), 2)/(float(x[0]))
anglee = ((int(x[1]))/60*360)/5
print(str(v), type(str(v)))

output3 = makeLabel('The speed of the stone on its outer edge is', 25, 10, 310, "blue", "Times New Roman", "yellow")
showLabel(output3)
output2 = makeLabel(str(v), 30, 10, 350, "blue", "Times New Roman", "yellow")
showLabel(output2)


output4 = makeLabel('and its acceleration is', 25, 10, 410, "blue", "Times New Roman", "yellow")
showLabel(output4)
output5 = makeLabel(str(a), 30, 10, 450, "blue", "Times New Roman", "yellow")
showLabel(output5)
pause(5000)

if entry1 != '':
    def rotate(surface,angle):
        rotated_surface = pygame.transform.rotozoom(surface,-angle,1)
        rotated_rect = rotated_surface.get_rect(center= (300,300))
        return rotated_surface,rotated_rect

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([600,600])
    tire = pygame.image.load("C:/Users/aksau/Desktop/3(2) курс/Game Physics/ppn5.png")
    tire_rect = tire.get_rect(center= (300,300))
    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        angle += anglee  #float(entry1)
        screen.fill((0,0,0))
        tire_rotated,tire_rotated_rect = rotate(tire,angle)


        screen.blit(tire_rotated, tire_rotated_rect)
        pygame.display.flip()
        clock.tick(5)

        


endWait()