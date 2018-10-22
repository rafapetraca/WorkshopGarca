#-*- coding: utf-8 -*-
from lxml import html
import requests
from pymongo import MongoClient

# Paraa fazer a conexão
client = MongoClient()

conexao = MongoClient("localhost", 27017)
db = conexao["test"]
finding = db.dadosAllan.find()


#URL do site a coletar os dados
page = requests.get('http://celepar7.pr.gov.br/ceasa/hoje.asp')
tree = html.fromstring(page.content)
a =0
Linha = 3
produtos = []
precos_curitiba = []
precos_maringa = []
precos_londrina = []
precos_foz = []
precos_cascavel = []
result = []

while Linha < 201:
  produtos.append(str(tree.xpath('//html/body/div/center/table/tr[%d]/td[1]/font/text()' % Linha )))
  precos_curitiba.append(str(tree.xpath('//html/body/div/center/table/tr[%d]/td[2]/p/font/text()' % Linha )))
  precos_maringa.append(str(tree.xpath('//html/body/div/center/table/tr[%d]/td[3]/p/font/text()' % Linha)))
  precos_londrina.append(str(tree.xpath('//html/body/div/center/table/tr[%d]/td[4]/p/font/text()' % Linha)))
  precos_foz.append(str(tree.xpath('//html/body/div/center/table/tr[%d]/td[5]/p/font/text()' % Linha)))
  precos_cascavel.append(str(tree.xpath('//html/body/div/center/table/tr[%d]/td[6]/p/font/text()' % Linha)))
  #	if (str(tree.xpath('//html/body/div/center/table/tr[%d]/td[1]/font/text()' % Linha )) != (NULL)):
  aux = "Linha: "+str(Linha)+",Produto: " +str(produtos[a])+",Preco Curitiba: " +str(precos_curitiba[a])+",Preco Maringa: " +str(precos_maringa[a])+",Preco Londrina: " +str(precos_londrina[a])+",Preco Foz: " +str(precos_foz[a])+",Preco Cascavel: " +str(precos_cascavel[a])
  result.inserted_id()
  result = db.dadosAllan.insert({"result":"%s", %aux})
  print result
  Linha += 1
  a += 1


# MOSTRA
#for registro in collection:
#	print str(registro)
