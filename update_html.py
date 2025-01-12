import json
import os

# apps.list dosyasını oku
with open('apps.list', 'r') as file:
    apps = json.load(file)

# HTML içeriğini oluştur
html_content = """
<ul>
"""

for app in apps:
    html_content += f'''
    <li>
        <img src="{app['image']}" alt="{app['name']}">
        <a href="{app['url']}" target="_blank">{app['name']}</a>
        {"".join([f'<a class="cat">{category}</a>' for category in app['categories']])}
    </li>
    '''

html_content += """
</ul>
"""

# HTML dosyasını kaydet
with open('index.html', 'w') as file:
    file.write(html_content)
