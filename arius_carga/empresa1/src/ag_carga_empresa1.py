import pyautogui
import time
import schedule
import yaml

def start():
    with open('C:\\arius_carga\\loja\\config\\config_ag_carga_empresa1.yaml','r', encoding="utf-8") as config:
        cfg = yaml.safe_load(config) 

    pyautogui.keyDown('win')
    pyautogui.press(['r'])
    pyautogui.keyUp('win')
    time.sleep(3)
    pyautogui.write(cfg["arius_carga_empresa1"])
    time.sleep(3)
    pyautogui.press(['return'])

with open('C:\\arius_carga\\loja\\config\\config_ag_carga_empresa1.yaml','r', encoding="utf-8") as config:
        cfg = yaml.safe_load(config) 

schedule.every().day.at(cfg["agenda_carga"]).do(start)

while 1:
    schedule.run_pending()
    time.sleep(1)
