import requests
from lxml import html
import datetime
import time
import pymongo

conexao = pymongo.MongoClient("mongodb://localhost")
mydb = conexao['cotacoes']

criptoMoedas = ['https://br.investing.com/indices/bovespa','https://br.investing.com/crypto/bitcoin/btc-usd','https://br.investing.com/crypto/ethereum/eth-usd','https://br.investing.com/crypto/ethereum-classic/etc-usd','https://br.investing.com/crypto/litecoin/ltc-usd','https://br.investing.com/currencies/usd-brl']

def crawler(site,hora,collection):
	r = requests.get(site,headers=header_html)
	tree = html.fromstring(r.content)

	nome = tree.xpath('//*[@id="leftColumn"]/div[1]/h1/text()')
	valor = tree.xpath('//*[@id="last_last"]/text()')
	porcentagem = tree.xpath('//*[@id="quotes_summary_current_data"]/div[1]/div[2]/div[1]/span[4]/text()')
	valor = str(valor).replace("['","").replace("']","").replace('.','').replace(',','.')
	porcentagem = str(porcentagem).replace("['","").replace("']","").replace('%','').replace(',','.')
	#hora = str(hora).replace("['","").replace("']","")
	nome = str(nome).replace("['","").replace("']","").replace('\\t','')
	inserir = (str(nome)+';'+str(hora)+';'+str(valor)+';'+str(porcentagem)+'\n')
	print (inserir)
	mydb[collection].insert({
		'nome':str(nome),
		'valor':float(valor),
		'porcentagem':float(porcentagem),
		'dataHora': hora,
	})

header_html = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
				'Accept-Encoding': 'gzip, deflate, br',
				'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
				'Cache-Control':'max-age=0',
				'Connection':'keep-alive',
				'Cookie':'SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%222103%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A32%3A%22D%C3%B3lar+Americano+Real+Brasileiro%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Fusd-brl%22%3B%7D%7D%7D%7D; adBlockerNewUserDomains=1524774691; optimizelyEndUserId=oeu1524774697481r0.8000480944372201; optimizelySegments=%7B%224225444387%22%3A%22gc%22%2C%224226973206%22%3A%22search%22%2C%224232593061%22%3A%22false%22%2C%225010352657%22%3A%22none%22%7D; optimizelyBuckets=%7B%7D; _ga=GA1.2.1063876129.1524774703; __qca=P0-1434760048-1524774704557; G_ENABLED_IDPS=google; r_p_s_n=1; geoC=BR; gtmFired=OK; _gid=GA1.2.1649450179.1525984783; PHPSESSID=i6broqfuj5j454r74mn9keech1; StickySession=id.68264849112.585.br.investing.com; __gads=ID=cd4e3089c79dbc92:T=1525985699:S=ALNI_MbbOetmzkOTtWKIfLdMTSKEoPFgTA; billboardCounter_30=2; nyxDorf=OT0yaWE%2BPnw3aD4ybiMxOmcxZiNjZmBmNTE%3D',
				'Host':'br.investing.com',
				'Referer':'https://www.google.com.br/',
				'Upgrade-Insecure-Requests': '1',
				'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36',
}
novo = open('criptoMoedas.csv','a+')
novo.write('nome;data;hora;valor;porcentagem\n')
novo.close()
while True:
	novo = open('criptoMoedas.csv','a+')
	for sites in criptoMoedas:
		today = datetime.datetime.today()
		if str(sites) == 'https://br.investing.com/crypto/bitcoin/btc-usd':
			crawler(sites,today,'btc-usd')
		elif str(sites) == 'https://br.investing.com/crypto/ethereum/eth-usd':
			crawler(sites,today,'eth-usd')
		elif str(sites) == 'https://br.investing.com/crypto/ethereum-classic/etc-usd':
			crawler(sites,today,'etc-usd')
		elif str(sites) == 'https://br.investing.com/crypto/litecoin/ltc-usd':
			crawler(sites,today,'ltc-usd')
		elif str(sites) == 'https://br.investing.com/currencies/usd-brl':
			crawler(sites,today,'usb-brl')
		elif str(sites) == 'https://br.investing.com/indices/bovespa':
			crawler(sites,today,'bovespa')
	novo.close()
	time.sleep(10)
