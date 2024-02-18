import requests
from bs4 import BeautifulSoup
import os

# Bağlantıya istek gönder
url = "https://s3.cloud.ngn.com.tr/level300/indir.html"
response = requests.get(url)

# HTML içeriğini analiz etmek için BeautifulSoup kullan
soup = BeautifulSoup(response.text, 'html.parser')

# Tüm zip dosyalarının bulunduğu bağlantıları topla
zip_links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href.endswith('.zip'):
        zip_links.append(href)

# İndirme klasörü oluştur
download_dir = "downloads"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Dosyaları indir
for zip_link in zip_links:
    zip_filename = os.path.basename(zip_link)
    zip_path = os.path.join(download_dir, zip_filename)
    with open(zip_path, 'wb') as f:
        print(f"İndiriliyor: {zip_filename}")
        zip_response = requests.get(zip_link)
        f.write(zip_response.content)
        print(f"{zip_filename} indirildi.")
