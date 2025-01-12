import json
import os

# apps.list JSON dosyasının yolu
apps_list_file = 'apps.list'

# index.html dosyasının yolu
html_file = 'index.html'

# apps.list dosyasını oku
with open(apps_list_file, 'r') as f:
    apps = json.load(f)

# index.html dosyasını oku
with open(html_file, 'r') as f:
    html_content = f.readlines()

try:
    # <ul> etiketinin olduğu satırı bul
    ul_start = html_content.index('<ul>\n') + 1
    ul_end = html_content.index('</ul>\n')

    # Yeni uygulamaları oluştur
    new_apps = []
    for app in apps:
        app_html = f"""
        <li>
            <img src="{app['image']}">
            <a href="{app['url']}" target="_blank">{app['name']}</a>
        """
        # Kategorileri ekle
        for category in app['categories']:
            app_html += f'<a class="cat">{category}</a>'
        app_html += "</li>\n"
        new_apps.append(app_html)

    # Güncellenmiş HTML içeriğini oluştur
    html_content = html_content[:ul_start] + new_apps + html_content[ul_end:]

    # Güncellenmiş HTML içeriğini dosyaya yaz
    with open(html_file, 'w') as f:
        f.writelines(html_content)

    print("index.html başarıyla güncellendi.")
except ValueError as e:
    print(f"Hata: <ul> etiketi bulunamadı. index.html dosyasındaki etiketler doğru değil veya beklenmedik bir biçim var. Hata: {e}")
