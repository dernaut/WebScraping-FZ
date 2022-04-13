import selenium
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import requests
from datetime import datetime
from datetime import timedelta
import pytz
import time
import json 










options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument('headless')
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")





listaCuentas=["name",
              "password",
              "name",
              "password",
              "...",
              "..."]


listaLinks=["name",
            "link",
            "name",
            "link",
            "...",
            "..."]
            
                         


e=0
listaCuentasCompletadas=[]
listaFiltradaCuentas=[]

while -1:
    f= open("cuentas.txt", "r")
    while(True):
        linea = f.readline()
        listaCuentasCompletadas.append(linea.strip("\n"))
        if not linea:
            break
    f.close()
    
    print("FILTRANDO CUENTAS")

    for cuenta in listaLinks:
        if cuenta not in listaCuentasCompletadas:
            listaFiltradaCuentas.append(cuenta)
    print("-- Comenzando tarea --")
    timeZ_Colombia = pytz.timezone('America/Bogota')
    dateZ_Colombia = datetime.now (timeZ_Colombia)
    fechaInicio_Co= dateZ_Colombia.strftime("%Y-%m-%d %H:%M:%S")
    fechaInicioCorreo= dateZ_Colombia.strftime("%d/%m/%Y %I:%M %p") 
    url = 'https://api-enviar-correo.herokuapp.com/terminado'
    mensaje = {
            "detalle": "Comenzando Tarea, Cuentas restantes: "+str(len(listaFiltradaCuentas)/2),
            "proxfecha": "-",
            "inicio": fechaInicioCorreo,
            "fin": "-",
            "transcurrido": "-"
            }
    x = requests.post(url, json=mensaje)
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
    fechaInicio=datetime.strptime(fechaInicio_Co, "%Y-%m-%d %H:%M:%S")
    while e < (len(listaFiltradaCuentas)):
        o=0
        print("Cuenta que recibe +1: "+listaFiltradaCuentas[e])
        print("Link: "+listaFiltradaCuentas[e+1])
        driver.get("https://rol4.fenixzone.com/foro/index.php?action=login")
            
        while o < (len(listaCuentas)):
            try:
                boton=driver.find_element_by_class_name("button_submit")
                icono=driver.find_element_by_id("dropdownMenuLink")
                casilla_usuario=driver.find_element_by_name("user")
                casilla_contra=driver.find_element_by_name("passwrd")
                icono.click()
                casilla_usuario.send_keys(listaCuentas[o])
                casilla_contra.send_keys(listaCuentas[o+1])
                time.sleep(4)
                try:
                    boton.submit()
                except:
                    print("Error al iniciar sesión")
                o=o-2
            except:
                print("Usario logeado: "+listaCuentas[o])
                driver.get(listaFiltradaCuentas[e+1])
                time.sleep(4)
                respeto=driver.find_element_by_link_text('[+Respeto]')
                time.sleep(4)
                respeto.click()
                driver.implicitly_wait(10)
                print("Se ha dado +1")
                try:
                    print("Cerrando sesión")
                    driver.close()
                    driver.quit()

                except:
                    print("ERROR No se puede continuar")
                driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
                driver.get("https://rol4.fenixzone.com/foro/index.php?action=login")
                time.sleep(4)

                    
            o=o+2

        f=open("cuentas.txt", "a")
        f.write(listaFiltradaCuentas[e].lstrip()+"\n")
        f.write(listaFiltradaCuentas[e+1].lstrip()+"\n")
        f.close()
        e=e+2

            
    timeZ_Colombia = pytz.timezone('America/Bogota')
    dateZ_Colombia = datetime.now (timeZ_Colombia)
    fechaFin_Co= dateZ_Colombia.strftime("%Y-%m-%d %H:%M:%S")
    fechaFin=datetime.strptime(fechaFin_Co, "%Y-%m-%d %H:%M:%S")
    fechaFinCorreo=dateZ_Colombia.strftime("%d/%m/%Y %I:%M %p")
    f=open("cuentas.txt", "r+")
    f.truncate(0)
    f.close()    
        
    driver.close()
    driver.quit()
    print("-- Se ha completado la tarea --")
    url = 'https://api-enviar-correo.herokuapp.com/terminado'
    mensaje = {
            "detalle": "Se ha completado la tarea satisfactoriamente",
            "proxfecha": "En 26 horas aproximadamente",
            "inicio": fechaInicioCorreo,
            "fin": fechaFinCorreo,
            "transcurrido": str(fechaFin - fechaInicio)+" Horas"
            }
    x = requests.post(url, json=mensaje)
        
    time.sleep(93600)
    
              
