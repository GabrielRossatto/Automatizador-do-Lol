import champ
import ban
import accept

while True:
    if accept.check_screen():
        continue    
    if ban.check_ban():
        continue
    if champ.choose_champ(): 
        break

