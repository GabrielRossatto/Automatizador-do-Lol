import pyautogui 


def click(x, y): 
    """Move o mouse até o botão aceitar partida"""
    pyautogui.moveTo(x, y)
    pyautogui.click()

def check_screen(): 
    """Passa como parametro as coordenadas do botao aceitar partida"""  
    button_pos = pyautogui.locateOnScreen('aceitar.png', confidence = 0.7 )
    if button_pos != None: 
        click(button_pos.left, button_pos.top)
        return True
    return False