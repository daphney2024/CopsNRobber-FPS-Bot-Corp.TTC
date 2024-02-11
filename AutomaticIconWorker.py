#It's a OSS Sample Code
#Get color code from 160*160px image and automate CNR painting
#This source code is based on my device, so the coordinates may not be compatible

import cv2
import numpy as np
import pyautogui as CNR
import time
import pyperclip

bgr_array = cv2.imread('Test.PNG') #file
traffic = "..."
num = 0
SubA = 0
SubB = 0
AddX = 0
AddY = 0
CNRY = 212
for i in range(256):
 num = num + 1
 AddX = AddX + 1
 AddY = AddY + 1
 Tg1 = 0+SubA
 Tg2 = 0+SubB
 result = (bgr_array[Tg1, Tg2, :])
 B = (result[0])
 G = (result[1])
 R = (result[2])
 color = (R,G,B)
 html_color = '#%02X%02X%02X' % (color[0],color[1],color[2])
 print(html_color)

 CNR.click(x=294, y=258, duration=0.5)#Palette
 CNR.click(x=865, y=812, duration=0.5)#To Keyboard
 CNR.press("backspace",presses=15)#Empty the keyboard
 CNR.typewrite(traffic+html_color,interval=0.1)#Input the Color code
 def Undo():
  CNR.click(x=1361, y=166, duration=0.5)#Undo
 Undo()
 Undo()
 CNRX = 626 + 40*AddX
 def Paint():
  CNR.click(x=CNRX, y=CNRY, duration=0.5)#Paint
 Paint()
 Paint()
 Paint()
 SubA = SubA + 10
 if  num == 16*1:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*2:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*3:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*4:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*5:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*6:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*7:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*8:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*9:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*10:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*11:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*12:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*13:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*14:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*15:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 if  num == 16*16:
   AddX = 0
   CNRX = 0
   CNRY = CNRY + 40
   SubA = 0
   SubB = SubB + 10
   Tg1 = 0
 else:
   print("Done!")
