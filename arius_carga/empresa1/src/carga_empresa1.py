from unicodedata import name
import pyautogui
from datetime import date, timedelta, datetime
import time
import yaml

def gerar_carga():
    
    with open('c:\\arius_carga\\empresa1\\config\\config.yaml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config)     
    #abrir arius    
    pyautogui.keyDown('win')
    pyautogui.press(['r'])
    pyautogui.keyUp('win')
    time.sleep(3)
    pyautogui.write(cfg["erp_arius"])
    time.sleep(3)
    pyautogui.press(['return'])    
    time.sleep(5)#15

    #user
    pyautogui.write(cfg["login_erp"])
    time.sleep(2)
    pyautogui.press(['return']) 

    #password
    pyautogui.write(cfg["senha_erp"])
    time.sleep(2)
    pyautogui.press(['return'])
    pyautogui.press(['return'])
    pyautogui.press(['return'])
    time.sleep(5)    
    pyautogui.press(['return'])
    time.sleep(3)
    pyautogui.press(['return'])
    time.sleep(1)
    pyautogui.press(['return'])
    pyautogui.press(['return'])
    time.sleep(5)#15

    
    #click cadastro de produtos    
    pyautogui.doubleClick(cfg["cadastro_de_produtos"])
    time.sleep(1)

    #pressiona sim
    pyautogui.press(['tab'])
    pyautogui.press(['return'])
    time.sleep(1)

    #pressiona sim
    pyautogui.press(['tab'])
    pyautogui.press(['return'])
    """"
    este processo pode demorar de 30 a 120s recomendo
    esperar 120s para executar a proxima acao isso aumenta 
    a taxa de sucesso da execução do programa
    """
    time.sleep(120)
    pyautogui.press(['return','return'])  

    #exit erp
    pyautogui.keyDown('alt')
    pyautogui.press(['f4'])
    pyautogui.keyUp('alt')
    time.sleep(5)                
    #open kw
    pyautogui.keyDown('win')
    pyautogui.press(['r'])
    pyautogui.keyUp('win')
    time.sleep(3)
    pyautogui.write(cfg["kw"])
    pyautogui.press(['return'])
    time.sleep(5)#20
    pyautogui.write(cfg["login"])
    pyautogui.press(['tab'])
    pyautogui.write(cfg["senha"])
    time.sleep(1)
    pyautogui.press(['return'])
    
    #import files 
    time.sleep(5)#10
    pyautogui.click(cfg["processos"])
    time.sleep(2)
    pyautogui.click(cfg["importacao"])
    time.sleep(2)
    pyautogui.click(cfg["importar"])
    """"
    este processo pode demorar de 20 a 90s recomendo
    esperar 90s para executar a proxima acao isso aumenta 
    a taxa de sucesso da execução do programa
    """
    time.sleep(90)         
    
    #gerar tabelas no pdv
    pyautogui.click(cfg["gerar_tabelas"])
    time.sleep(3)
    pyautogui.click(cfg["todos"])    
    pyautogui.click(cfg["gerar"])
    """"
    este processo pode demorar de 20 a 70s recomendo
    esperar 70s para executar a proxima acao isso aumenta 
    a taxa de sucesso da execução do programa
    """
    time.sleep(70)
    pyautogui.keyDown('alt')
    pyautogui.press(['f4'])
    pyautogui.keyUp('alt')
    time.sleep(2)
    
def log_carga():
    with open('C:\\arius_carga\\empresa1\\config\\config.yaml','r', encoding="utf-8") as config:
            cfg = yaml.safe_load(config) 

    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')         
    file = open(cfg["log_carga"], 'a')
    file.write(f'CARGA NA EMPRESA1 [OK] - {data}\n\n')
    file.close()
    pyautogui.alert('CARGA NA EMPRESA1 EFETUADA')
                    
gerar_carga()
log_carga()
