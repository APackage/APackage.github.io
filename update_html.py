import os

# apps.list dosyasını oku
apps_list_file = 'apps.list'

# Yeni öğeleri ekleyeceğimiz index.html dosyasının yolu
html_file = 'index.html'

# apps.list dosyasını oku
with open(apps_list_file, 'r') as f:
    apps = f.readlines()

# index.html dosyasını oku
with open(html_file, 'r') as f:
    html_content = f.readlines()

# HTML içeriğini kontrol et
print("index.html içeriği:")
print(''.join(html_content))

try:
    # <ul> etiketinin olduğu satırı bul
    ul_start = html_content.index('<ul>\n') + 1
    ul_end = html_content.index('</ul>\n')

    # <ul> arasındaki eski içeriği sil
    # Mevcut listeyi yeni öğelerle değiştiriyoruz
    new_apps = [f"<li>\n    <img src='{app.strip()}'>\n    <a href='/apps/{app.strip().lower()}/index.html' target='_blank'>{app.strip()}</a>\n    <a class='cat'>Game</a>\n    <a class='cat'>Emulator</a>\n</li>\n" for app in apps]

    # Güncellenmiş HTML içeriğini oluştur
    html_content = html_content[:ul_start] + new_apps + html_content[ul_end:]

    # Güncellenmiş HTML içeriğini dosyaya yaz
    with open(html_file, 'w') as f:
        f.writelines(html_content)

    print("index.html başarıyla güncellendi.")
except ValueError as e:
    print(f"Hata: <ul> etiketi bulunamadı. index.html dosyasındaki etiketler doğru değil veya beklenmedik bir biçim var. Hata: {e}")
