'''
Created on Nov 10, 2016

@author: jose
'''
import webbrowser
import time


print ("hola")

x=7
y=9

print (x>y)

total_breaks=3
break_count=0



print("clock starting"+time.ctime())
while (break_count < total_breaks):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=oTfgfoVb6io", new=0, autoraise=True)
    break_count = break_count+1
