import pyautogui
from time import sleep

ban = input('Digite o campeao que vc quer banir: ')

def ban_champ(c, d):  
    """Move o mouse até o campeão a ser banido e bane"""
    pyautogui.moveTo(c, d)
    pyautogui.click()
    pyautogui.write(ban)
    sleep(2)  
    pyautogui.click(x = 439, y = 170) 
    sleep(2) 
    banir_champ = pyautogui.locateOnScreen('banir.png', confidence = 0.7)
    while banir_champ != None:
        pyautogui.click(banir_champ.left, banir_champ.top)
        return True
    return False
    

def check_ban(): 
    """Localiza a barra de busca e o campeão que vc quiser banir, passando
    as coordenadas para a função ban_champ escrever e clicar"""
    button_bar = pyautogui.locateOnScreen('barradepesquisa.png', confidence = 0.7)
    banimento = pyautogui.locateOnScreen('banimento.png', confidence = 0.7) 
    while banimento != None:   
        ban_champ(button_bar.left, button_bar.top)
        return True
    return False