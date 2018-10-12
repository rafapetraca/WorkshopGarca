#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from lxml import html

page = requests.get("https://www.dolarhoje.net.br/dolar-comercial/")
tree = html.fromstring(page.content)
Linha = 0
contador = 2

while Linha < 30:
    dolar = str(tree.xpath('//*[@id="mainContent"]/div/div[2]/div/div[2]/div[5]/div[3]/p[%d]/text()[1]' % contador))
    
    inserir = dolar
    print (inserir)
    Linha = Linha+1
    contador = contador + 1
