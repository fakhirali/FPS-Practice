#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pygame
import random
import time
import math


# In[6]:


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
        pygame.display.flip()
    


# In[7]:


def makeTarget():
    t = Target(height,width,screen)
    t.draw()
    return t


# In[8]:


def DisplaySmth(thing, pos):
    font = pygame.font.SysFont(pygame.font.get_fonts()[0],32)
    text = font.render(thing, True, background_colour)
    screen.blit(text,(width/4,(height/4)+(32*pos)))
    pygame.display.flip()


# In[9]:


def DisplayAvg(avg):
    thing = "Average time: "+str(round(avg,3)) +" s"
    DisplaySmth(thing,0)


# In[10]:


def DisplayCount(count):
    thing = "Total dots: "+str(count)
    DisplaySmth(thing,1)


# In[11]:


def getDistance(p,q):
    x,y = p
    a,b = q
    return math.sqrt(pow((x-a),2)+pow((y-b),2))


# In[12]:


def DisplayDistance(distance):
    thing = "Total Distance: " + str(round(distance,3)) + " px"
    DisplaySmth(thing,2)


# In[13]:


def DisplayDistancePerSec(distancePerSec):
    thing = "Distance per second: " + str(round(distancePerSec,3)) + " per s"
    DisplaySmth(thing,3)


# In[14]:


pygame.init()


# In[15]:


background_colour = (255,255,255)
end_color = (0,0,255)
width = 600
height = 600


# In[16]:


screen = pygame.display.set_mode((width,height))
pygame.display.toggle_fullscreen()
pygame.display.set_caption("Shoot")
screen.fill(background_colour)

t = makeTarget()

timeTrack = 0
distance = 0
prevPos = (0,0)
count = 0
allTimes = []
running = True
end = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if abs(mpos[0] - t.pos[0]) <= t.scale and abs(mpos[1] - t.pos[1]) <= t.scale:
                count += 1
                if timeTrack == 0:
                    prevPos = t.pos
                    timeTrack = time.time()
                else:
                    distance += getDistance(t.pos,prevPos)
                    prevPos = t.pos
                    allTimes.append(time.time()-timeTrack)
                    timeTrack = time.time()
                screen.fill(background_colour)
                t = makeTarget()
            elif not end:
                end = True
                screen.fill(end_color)
                if len(allTimes) > 0:
                    DisplayAvg(sum(allTimes)/len(allTimes))
                    DisplayDistancePerSec(distance/sum(allTimes))
                DisplayCount(count)
                DisplayDistance(distance)
                distance = 0
                prevPos = (0,0)
                count = 0
                allTimes = []
                timeTrack = 0
                pygame.display.flip()
            else:
                end = False
                screen.fill(background_colour)
                t = Target(height,width,screen)
                t.draw()
                pygame.display.flip()
                
pygame.display.quit()


# In[ ]:




