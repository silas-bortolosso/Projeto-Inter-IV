# -*- coding: utf-8 -*-

from numpy import append
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sqlalchemy import create_engine, false, text
import pymysql

##engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/')

hostname="127.0.0.1"
dbname="artistas"
uname="root"
pwd="1505Qtds"



engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                .format(host=hostname, db=dbname, user=uname, pw=pwd))

class Indeed:
    def __init__(self,driver):
        self.driver=driver
    def navegate(self,url):
        self.driver.get(url)
        
chrome=webdriver.Chrome()
v=Indeed(chrome)

v.navegate("https://www.last.fm/pt/tag/sertanejo/artists")


colunas=v.driver.find_element_by_class_name('grid-items-section')
artistas=[]
ouvintes=[]
for i in range (0,len(colunas.text.split('\n'))):
    if 'ouvintes' in colunas.text.split('\n')[i]:
        artistas.append(colunas.text.split('\n')[i-1])
        ouvintes.append(colunas.text.split('\n')[i].replace("ouvintes" , ""))
   
infos_artistas=[]
l_bibliografia=[]
for i in artistas:
    s=''
    for j in range (0,len(i.split(' '))):
        if j == len(i.split(' '))-1:
            s+=i.split(' ')[j]
        else:
            s+=i.split(' ')[j]+'+'
       
    print(s)
    v.navegate("https://www.last.fm/pt/music/"+s+"/+wiki")
    try:
        infos=v.driver.find_element_by_class_name("factbox")
        infos_artistas.append(infos.text.split("\n"))
    except:
        infos_artistas.append("nao ha")
    bibliografia=v.driver.find_element_by_class_name("wiki-content")
    l_bibliografia.append(bibliografia.text)
    
Anos_de_atividade=[]
Local_de_fundacao=[]
Membros=[]
for i in infos_artistas:
    if not 'Anos de atividade' in i:
        Anos_de_atividade.append('nao informado')
    if not 'Local de fundação' in i:
        Local_de_fundacao.append('Brasil')
    if not 'Membros' in i:
        Membros.append('nao informado')
    else:
        pass
    for j in range (0,len(i)):
        if i[j] == 'Anos de atividade':
            Anos_de_atividade.append(i[j+1])
        elif i[j]  == 'Local de fundação':
            Local_de_fundacao.append(i[j+1])
        elif i[j]  == 'Membros':
            ss=""
            for k in range(j,len(i) - 1):
                if k == len(i):
                    ss+=i[k]
                else:
                    ss+=" "+i[k]+", "
            Membros.append(ss)    
                

dic={"artista":artistas, "ouvintes" : ouvintes, "bibliografia": l_bibliografia,"anos_atv":Anos_de_atividade,"local_fund" : Local_de_fundacao,"membros" : Membros}

df = pd.DataFrame(dic)


df.to_sql("artistas",engine,if_exists='append',index=False)







       

    