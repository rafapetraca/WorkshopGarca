import requests
from lxml import html 

page = requests.get("https://www.zoom.com.br/notebook/notebook-dell-i15-7572-a30c-intel-core-i7-8550u-15-6-16gb-hd-1-tb-geforce-mx150-ssd-128-gb?__zaf_=preco-2100-ou-mais%7C%7C_o%3A11")
tree = html.fromstring(page.text, "lxml")

preco = list(tree.xpath('//*[@id="mobile-container"]/div[1]/section/header/div/div[2]/div[1]/div[2]/div/div[2]/p/span[2]/a/strong/text()'))
nome = list(tree.xpath('//*[@id="mobile-container"]/div[1]/section/header/div/div[2]/div[1]/div[2]/h1/span/text()'))

print(nome)
