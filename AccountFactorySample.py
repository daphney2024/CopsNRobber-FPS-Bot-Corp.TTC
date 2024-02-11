#It's a OSS Sample Code
#The created account will increase the number of followers of the target ID
#This source code is based on my device, so the coordinates may not be compatible

import pyautogui as CNR
import time
#Terminal
UserA = input('Please input UserName')
print("UserName: "+ UserA)
PassB = input('Please input PassWord')
print("PassWord:" + PassB)
ID = input('Please input ID')
print("ID:" + ID)
numA = int(input()) 
resultA = str(UserA)
resultB = str(PassB)
UserB = resultA + resultB
num = 0
traffic = ".........."
Enter = 0.3
#Register
while int(num) <= numA:
 num = num + 1
 CNR.click(x=994, y=372)
 CNR.typewrite(traffic + resultA + str(num),interval=Enter)
 CNR.click(x=1675, y=355,duration=0)

 CNR.click(x=990, y=475,duration=0.5)
 CNR.typewrite(traffic + resultB,interval=Enter)
 CNR.click(x=1675, y=355,duration=0)

 CNR.click(x=991, y=575,duration=0.5)
 CNR.typewrite(traffic + resultB,interval=Enter)
 CNR.click(x=1675, y=355,duration=0)
#Exit
 CNR.click(x=1174, y=703, duration=1)
#Register Done
 CNR.click(x=1486, y=846, duration=15)#gift bonus
 CNR.click(x=1502, y=815, duration=0.5)#Accept
 CNR.click(x=1618, y=668, duration=0.5)#Game
 CNR.click(x=129, y=93, duration=6)#Exit
 CNR.click(x=1139, y=539, duration=2)#Exit Done
#Avoid Ads
 CNR.click(x=1021, y=973, duration=2)#※Home
 CNR.click(x=893, y=550, duration=1)#※Start CNR
 CNR.click(x=893, y=550, duration=1)#※Start CNR
 CNR.click(x=893, y=550, duration=1)#※Start CNR
 CNR.click(x=893, y=550, duration=1)#※Start CNR
 CNR.click(x=893, y=550, duration=1)#※Start CNR
 CNR.click(x=893, y=550, duration=1)#※Start CNR
#Lobby
 CNR.click(x=957, y=702, duration=25)#Accept
 CNR.click(x=1359, y=245, duration=0.5)#Avoid delays
 CNR.click(x=1359, y=245, duration=0.5)#Avoid delays
 CNR.click(x=1359, y=245, duration=0.5)#Avoid delays
 CNR.click(x=1502, y=744, duration=5)#Accept    
 CNR.click(x=1502, y=744, duration=0.5) 
 CNR.click(x=1253, y=97, duration=1)#Accept
 CNR.click(x=1253, y=97, duration=1)#Friend
 CNR.click(x=1253, y=97, duration=1)#Friend
 CNR.click(x=1253, y=97, duration=1)#Friend
#Friend
 CNR.click(x=138,y=277,duration=0.5)
 CNR.click(x=138,y=277,duration=0.5)
 CNR.click(x=1503, y=182, duration=1)#To Input
 CNR.press("backspace",presses=8)#Backspace
 CNR.typewrite(ID,interval=Enter)#Input
 CNR.click(x=1667, y=187,duration=0.5)#Search
 CNR.click(x=1667, y=187,duration=0.5)#Search
 CNR.click(x=1201, y=285,duration=1)#To Profile
#Profile
 CNR.click(x=737, y=581,duration=0.5)#Profile
 CNR.click(x=1761, y=102,duration=2)#Follow
 CNR.click(x=187, y=103,duration=0.5)#ToUndo
 CNR.click(x=187, y=103,duration=0.5)#Undo
 CNR.click(x=1412, y=100,  duration=0.5)#To Setting
#Setting
 CNR.click(x=216, y=695, duration=1)#Acc
 CNR.click(x=1686, y=849, duration=1)#To Logout
 CNR.click(x=1142, y=676, duration=1)#Logout Done
#Logout Done
 CNR.click(x=968, y=580, duration=7)#Login
 CNR.click(x=782, y=668, duration=0.5)#Register
 print(str(num) +"Done!")
 CNR.click(x=994, y=372, duration=0.5)
else:
 print("Complete!")
