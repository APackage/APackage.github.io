import os

# Apps list dosyasını oku
apps_list_file = 'apps.list'

# Yeni öğeleri ekleyeceğimiz index.html dosyasının yolu
html_file = 'index.html'

# apps.list dosyasını oku
with open(apps_list_file, 'r') as f:
    apps = f.readlines()

# index.html dosyasını oku
with open(html_file, 'r') as f:
    html_content = f.readlines()

# <ul> etiketinin olduğu satırı bul
ul_start = html_content.index('<ul>\n') + 1
ul_end = html_content.index('</ul>\n')

# <ul> arasındaki eski içeriği sil
html_content = html_content[:ul_start] + [f"<li>{app.strip()}</li>\n" for app in apps] + html_content[ul_end:]

# Güncellenmiş html içeriğini dosyaya yaz
with open(html_file, 'w') as f:
    f.writelines(html_content)

print("index.html başarıyla güncellendi.")
