from bs4 import BeautifulSoup
import os
import json

# HTML dosyasını oku
with open('index.html', 'r') as file:
    html_content = file.read()

# BeautifulSoup ile HTML'yi parçalara ayır
soup = BeautifulSoup(html_content, 'html.parser')

# <ul> etiketini bul
ul_tag = soup.find('ul')

# Eğer <ul> etiketi bulunamazsa hata ver
if not ul_tag:
    raise ValueError("<ul> etiketi bulunamadı.")

# apps.list dosyasını oku
with open('apps.list', 'r') as f:
    apps = json.load(f)

# Yeni app'leri <ul> içerisine ekle
for app in apps:
    li_tag = soup.new_tag('li')

    img_tag = soup.new_tag('img', src=app['image'])
    a_tag = soup.new_tag('a', href=app['url'], target="_blank")
    a_tag.string = app['name']
    
    # Kategorileri de ekle
    for category in app['categories']:
        cat_tag = soup.new_tag('a', class='cat') 
        cat_tag.string = category
        li_tag.append(cat_tag)

    # img ve a taglerini li içine ekle
    li_tag.insert(0, img_tag)
    li_tag.insert(1, a_tag)

    # Yeni li'yi <ul> içine ekle
    ul_tag.append(li_tag)

# Güncellenmiş içeriği dosyaya kaydet
with open('index.html', 'w') as file:
    file.write(str(soup))

print("index.html başarıyla güncellendi.")
