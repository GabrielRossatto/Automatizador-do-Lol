import champ
import accept 
import ban 

#PROGRAMA PRINCIPAL

while True:
    if accept.check_screen():
        continue    
    if champ.choose_champ():
        continue
    if ban.check_ban(): 
        break

