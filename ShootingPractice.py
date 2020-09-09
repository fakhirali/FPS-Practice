#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pygame
import random


# In[3]:


pygame.init()


# In[4]:


background_colour = (255,255,255)
end_color = (0,0,255)
width = 600
height = 600


# In[5]:


class Target:
    def __init__(self, height, width,screen):
        self.height = height
        self.width = width
        self.screen = screen
        self.color = (255,0,0)
        self.scale = 20
        self.pos = None
    
    def getPos(self):
        x = random.randint(self.scale,self.width-self.scale)
        y = random.randint(self.scale,self.height-self.scale)
        return (x,y)

    def draw(self):
        self.pos = self.getPos()
        pygame.draw.circle(screen, self.color, self.pos, self.scale)
    


# In[6]:


screen = pygame.display.set_mode((width,height))
pygame.display.toggle_fullscreen()
pygame.display.set_caption("Shoot")
screen.fill(background_colour)


# In[7]:



def makeTarget():
    t = Target(height,width,screen)
    t.draw()
    pygame.display.flip()
    return t;


# In[8]:


t = makeTarget()

running = True
end = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if abs(mpos[0] - t.pos[0]) <= t.scale and abs(mpos[1] - t.pos[1]) <= t.scale:
                
                screen.fill(background_colour)
                t = makeTarget()
                
            elif not end:
                end = True
                screen.fill(end_color)
                pygame.display.flip()
            else:
                end = False
                screen.fill(background_colour)
                t = Target(height,width,screen)
                t.draw()
                pygame.display.flip()
                
pygame.display.quit()


# In[ ]:


pygame.display.quit()


# In[ ]:




