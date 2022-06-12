import pyautogui
from time import sleep

champ = input('Digite o campeao que voce quer jogar: ')

def click_bar(a, b):  
    """Move o mouse até a barra de busca, digita o nome do campeão e escolhe
    """
    pyautogui.moveTo(a, b)
    pyautogui.click()
    pyautogui.write(champ)  
    sleep(2)  
    pyautogui.click(x = 439, y = 170) 
    sleep(2) 
    confirm = pyautogui.locateOnScreen('confirmar.png', confidence = 0.7) 
    while confirm != None:
        pyautogui.click(confirm.left, confirm.top)
        return True
    return False
        
def choose_champ(): 
    """Localiza a barra de pesquisa e o botão confirmar, passando as coordenadas
    como paramentro para a função click_bar"""
    button_bar_ban = pyautogui.locateOnScreen('barradepesquisa.png', confidence = 0.7)
    choose = pyautogui.locateOnScreen('escolha.png', confidence = 0.7)
    while choose != None: 
        click_bar(button_bar_ban.left, button_bar_ban.top)
        return True
    return False