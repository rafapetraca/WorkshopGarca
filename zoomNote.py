import requests
from lxml import html

page = requests.get('https://www.zoom.com.br/notebook/preco-2100-ou-mais/processador-intel-core-i7/processador-intel-core-i5/dedicada-off-board-/geforce-gtx-960m/radeon-r9-m370x/geforce-gtx-850m/geforce-gtx-860m/geforce-gtx-870m/geforce-gtx-880m/geforce-gtx-950m/geforce-gtx-970m/geforce-gtx-1050/geforce-gtx-1050-ti/geforce-gtx-1060/geforce-gtx-1070/geforce-gtx-1080/geforce-gtx-965m/geforce-gtx-980m/memoria-8-gb-ou-mais/16-gb-ou-mais/4k/2k/full-hd/qhd?resultsperpage=72')
tree = html.fromstring(page.text, 'lxml')

linha = 1
erro = 0

while True:

    nomeNotebook = list(tree.xpath('//*[@id="storeFrontList"]/li[%d]/div[2]/h2/a/text()' %linha))
    precoNotebook = list(tree.xpath('//*[@id="storeFrontList"]/li[%d]/div[3]/span[2]/a[1]/text()' %linha))

    if len(nomeNotebook) != 0 and len(precoNotebook) != 0:
        print(nomeNotebook[0])
        print(precoNotebook[0].replace(" ",""))

    else:
        erro+=1

    if erro == 3:
        print("To caindo fora meu irmão")
        break

    linha+=1
