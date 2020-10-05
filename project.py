import keyboard# ♫♂
import pyperclip#вот єта нада  ♫ ♂
import json#лоадинг████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

def logic():#ну вот єто та самая которая отвечает ну ♂ вIwEvEe ♂ поняли  ♂ ♫
   clip=pyperclip.paste()
   with open('letters.json',encoding="utf-8") as json_file:#ну єто жесон,вход віще /\nu tam ♫ ♂
      letters= json.load(json_file)
   out_str=[]#єто віход  ♫ ♂
   for i in clip:#тут месячніе  ♫ ♂
      if letters.get(i):
         out_str.append(letters.get(i)) 
   pyperclip.copy("".join(out_str))#тут копи ну типо копирование ♫ ♂
keyboard.add_hotkey("Alt + v",logic)#єто как конрл В но только альт В ♫ ♂
keyboard.wait()  #< тута вайт,с брітанского ждать   ♫ ♂     
# коменты написаны под травой