#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 12:59:21 2017

@author: HomeFolder
"""

import Tkinter as Tk
import random

def floodit(n,numColors):
    
    colorList = ['white','red','green','blue','cyan','yellow','magenta']
    
    if numColors > len(colorList):
        numColors = len(colorList)
    
    root = Tk.Tk()
    
    width = 500
    height = 600

    game_width = 500
    game_height = 500
    
    square_w = game_width/n
    square_h = game_height/n
    
    w = Tk.Canvas(root,width=width,height=height)
    
    w.pack()
    
    w.create_rectangle(0,game_height,width/2,game_height + (height-game_height)/3,fill = "white",width=5)
    w.create_rectangle(0,game_height+(height-game_height)/3,width/2,game_height+2*(height-game_height)/3,fill = "white",width=5)
    w.create_rectangle(0,game_height+2*(height-game_height)/3,width/2,game_height+3*(height-game_height)/3,fill = "white",width=5)

    w.create_rectangle(width/2,game_height,width,game_height + (height-game_height)/3,fill = "white",width=5)
    w.create_rectangle(width/2,game_height+(height-game_height)/3,width,game_height+2*(height-game_height)/3,fill = "white",width=5)
    w.create_rectangle(width/2,game_height+2*(height-game_height)/3,width,game_height+3*(height-game_height)/3,fill = "white",width=5)

    w.create_text(width/4,game_height+(height-game_height)/6,text="6x6")
    w.create_text(width/4,game_height+3*(height-game_height)/6,text="10x10")
    w.create_text(width/4,game_height+5*(height-game_height)/6,text="14x14")
    
    w.create_text(3*width/4,game_height+(height-game_height)/6,text="4 Colors")
    w.create_text(3*width/4,game_height+3*(height-game_height)/6,text="5 Colors")
    w.create_text(3*width/4,game_height+5*(height-game_height)/6,text="6 Colors")

    grid = []
    
    for i in range(n):
        
        grid.append([])
        
        for j in range(n):
            
            color = random.randint(0,numColors-1)
            
            grid[i].append(w.create_rectangle(i * square_w,j * square_h,(i+1) * square_w,(j+1) * square_h,fill=colorList[color],width=0))
          
    flooded = [[0,0]]
   
    def click_square(event):
        
        if event.y <= 500:

            i = event.x / square_w
            j = event.y / square_h

            pickedColor = w.itemcget(grid[i][j],'fill')
        
            while True:
            
                current = len(flooded)
        
                for k in range(len(flooded)):
                    
                    index1 = flooded[k][0]
                    index2 = flooded[k][1]
                    
                    w.itemconfig(grid[index1][index2],fill = pickedColor)
                
                    if (index1 - 1) >= 0:
                
                        if w.itemcget(grid[index1-1][index2],'fill') == pickedColor:
                    
                            if [index1-1,index2] not in flooded:
                                flooded.append([index1-1,index2])
                    
                    if (index1 + 1) < n:
                        
                        if w.itemcget(grid[index1+1][index2],'fill') == pickedColor:
                    
                            if [index1+1,index2] not in flooded:
                                flooded.append([index1+1,index2])
                    
                    if (index2 - 1) >= 0:
                            
                        if w.itemcget(grid[index1][index2-1],'fill') == pickedColor:
                            if [index1,index2-1] not in flooded:
                                flooded.append([index1,index2-1])
                
                    if (index2 + 1) < n:
                        
                        if w.itemcget(grid[index1][index2+1],'fill') == pickedColor:
                            
                            if [index1,index2+1] not in flooded:
                        
                                flooded.append([index1,index2+1])
                                
                if current == len(flooded):
                    break
                                
        else:
            
            if event.x < width/2:
                if event.y < game_height+(height-game_height)/3:
                    
                    print "6x6"
                    floodit(6,numColors)
                    
                elif event.y < game_height+2*(height-game_height)/3:
                    
                    print "10x10"
                    floodit(10,numColors)
                    
                elif event.y < game_height+3*(height-game_height)/3:
                    
                    print "14x14"
                    floodit(14,numColors)
            else: 
                if event.y < game_height+(height-game_height)/3:
                    
                    print "4 Colors"
                    floodit(n,4)
                    
                elif event.y < game_height+2*(height-game_height)/3:
                    
                    print "5 Colors"
                    floodit(n,5)
                    
                elif event.y < game_height+3*(height-game_height)/3:
                    
                    print "6 Colors"
                    floodit(n,6)
                
    w.bind("<Button-1>",click_square)
    root.mainloop()
    
floodit(6,8)
