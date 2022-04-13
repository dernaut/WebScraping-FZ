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





listaCuentas=["Antonella_Emecatorce",
              "camilo123",
              "Juls_Kawasaki",
              "bletAIRWitia",
              "Frederic_Chopin",
              "juan123",
              "Elizabeth_Vangogh",
              "juan123",
              "KehrseiteSchlch_Kenh",
              "juan123",
              "Selina_Cat",
              "juan123",
              "Vioiet_Harmon",
              "juan123",
              "Tomas_Ruiz",
              "chupalagato",
              "Toma_Ruiz",
              "nahuel2017",
              "Arturo_Anderson",
              "gildemierda",
              "Gabriei_Ruiz",
              "jhonaputo",
              "Ignacio_Haze",
              "infinito@8888",
              "Gnzjakzy_Whzkan",
              "Tuptaabuel@r21",
              "Shannezka_Haze",
              "perroperro",
              "Hanae_Mckenna",
              "tsukinose666samp",
              "Mentiroso_Elinfiel",
              "santino2016",
              "Kadok_Carrasco",
              "trei789987",
              "Jhony_Mora",
              "trei789987",
              "Nuh_Bukele",
              "trei789987",
              "Samay_Bennett",
              "nahuel2017",
              "Yakov_Leze",
              "emily123",
              "Larrick_Bolton",
              "chino123"]


listaLinks=["Treizy_Butterls",
            "https://rol4.fenixzone.com/foro/index.php?topic=299799.msg5555235",
            "Gabriei_Vasseur",
            "https://rol4.fenixzone.com/foro/index.php?topic=315724.msg5820176",
            "Fabrica_Blueberry",
            "https://rol4.fenixzone.com/foro/index.php?topic=316652.0",
            "Method_Wutang",
            "https://rol4.fenixzone.com/foro/index.php?topic=315003.msg5806152",
            "Giovanni_Rios",
            "https://rol4.fenixzone.com/foro/index.php?topic=306178.msg5598081",
            "Brian_Lobo",
            "https://rol4.fenixzone.com/foro/index.php?topic=220768.0",
            "Dimitri_Kramerz",
            "https://rol4.fenixzone.com/foro/index.php?topic=316654.0",
            "Julian_Kawasaki",
            "https://rol4.fenixzone.com/foro/index.php?topic=257986.msg4559551",
            "Beleen_Bouffard",
            "https://rol4.fenixzone.com/foro/index.php?topic=315077.msg5807287",
            "Dimitri_Tryggxz",
            "https://rol4.fenixzone.com/foro/index.php?topic=316454.msg5835936",
            "Tyss_Tryggxz",
            "https://rol4.fenixzone.com/foro/index.php?topic=318135.msg5871789",
            "Helena_Harper",
            "https://rol4.fenixzone.com/foro/index.php?topic=316314.msg5832794",
            "Mary_Blackesley",
            "https://rol4.fenixzone.com/foro/index.php?topic=261862.msg4640123",
            "Jules_Wieczorek",
            "https://rol4.fenixzone.com/foro/index.php?topic=289649.msg5329761",
            "Sheng_Kramerz",
            "https://rol4.fenixzone.com/foro/index.php?topic=308723"
            ]
            
                         


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
    
              
