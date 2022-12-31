import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import plotly.express as px
import tela as t


def valores_fii():
    link = 'https://valorinveste.globo.com/cotacoes/'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
    data = requests.get(link, headers=headers,timeout=5).text
    soup = BeautifulSoup(data,'html.parser')

    #procurando uma tabela na página
    #em html uma tabela é representada pela tag table
    table = soup.find_all('table')[2]
    dataframe = pd.DataFrame(columns=['Nome','Código','Última','Variação(%)','Fech. dia anteior(R$)'])

    #obtendo todas as linhas da tabela
    #em html uma linha da tabela é representada pela tag <tr>
    for row in table.tbody.find_all('tr'):
        #Obtendo todas as colunas em cada linha
        columns = row.find_all('td') #html cada coluna é <td>
        if(columns != []):
            nome = columns[0].text.strip(' ')
            codigo = columns[1].text.strip(' ')
            ultima = columns[2].text.strip(' ')
            variacao = columns[3].text.strip(' ')
            fech_dia_anterior = columns[4].text.strip(' ')
            dataframe = pd.concat([dataframe,pd.DataFrame.from_records([{
                'Nome':nome,
                'Código':codigo,
                'Última':ultima,
                'Variação(%)':variacao,
                'Fech. dia anterior(R$)':fech_dia_anterior
                }])])

    fundos = dataframe.set_index(dataframe['Código'])


    lista_interesses = ['MXRF11','KNRI11','HGLG11','BCFF11','ALZR11']
    interesses = pd.DataFrame()
    interesses.index = fundos['Código'][lista_interesses]
    interesses['Nome'] = fundos['Nome'][lista_interesses]
    interesses['Última'] = fundos['Última'][lista_interesses]
    interesses['Variação(%)'] = fundos['Variação(%)'][lista_interesses]
    interesses['Fech. dia anterior(R$)'] = fundos['Fech. dia anterior(R$)'][lista_interesses]

    codigo = pd.DataFrame()
    nome = pd.DataFrame()
    variacao = pd.DataFrame()
    fech_anterior = pd.DataFrame()
    codigo.index = interesses.index
    nome.index = interesses['Nome']
    variacao.index = interesses['Variação(%)']
    fech_anterior.index = interesses['Fech. dia anterior(R$)']



    t.retorno_interesses_0['text'] = codigo
    t.retorno_interesses_1['text'] = nome
    t.retorno_interesses_2['text'] = variacao
    t.retorno_interesses_3['text'] = fech_anterior
   
