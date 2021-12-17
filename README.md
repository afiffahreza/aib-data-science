# Tugas Besar Data Science II4042 Kecerdasan Buatan untuk Bisnis
18219006 - Marcelino Feihan  
18219014 - Zarfa Naida Pratista  
18219058 - Afif Fahreza  

**Deployment Link: https://prediksi-properti.herokuapp.com/**  

## Deskripsi Perusahan
Rumah123.com adalah sebuah situs pencarian properti di Indonesia. Situs ini juga menyediakan berita dan fitur pemberitahuan tentang properti. Ada juga beberapa perangkat yang dapat digunakan seperti Kalkulator KPR untuk melakukan kalkulasi sebelum membeli properti. Dengan lebih dari 900,000 listing, rumah123.com dapat membantu masyarakat Indonesia dalam menemukan rumah mereka dan investasi properti.

## Masalah
Orang-orang yang masih awam terhadap bidang properti masih kesulitan memilih properti yang berpeluang baik untuk investasi, sehingga tidak banyak menggunakan situs ini. Hal itu dikarenakan banyaknya masyarakat yang belum mengetahui cara melakukan perhitungan prediksi harga dari properti. Penggunaan situs rumah123.com tentu akan meningkat jika orang-orang yang tidak mengerti tentang bidang properti tetap bisa mengetahui peluang investasi tiap properti yang ada pada situs.  

**Pertanyaan:**  
Bagaimana agar orang yang awam properti tetap bisa rutin menggunakan situs untuk berinvestasi properti?  
**Pengukuran Keberhasilan:**  
Pengukuran akurasi model: R2 Score, MAE, MSE  
Pengukuran keberhasilan solusi: Kenaikan penggunaan website rumah123 untuk listing properti

## Solusi
Berdasarkan masalah yang ada, kami merumuskan solusi berupa pembuatan sistem yang dapat memberikan prediksi harga properti sesuai input pengguna yaitu luas bangunan, luas tanah, jumlah kamar, dan jumlah kamar mandi. Dengan website ini, diharapkan adanya kenaikan jumlah pembelian properti dari situs karena orang yang awam properti juga dapat mencoba untuk berinvestasi properti berdasarkan prediksi harga dari sistem kami.

## Data
Data didapat dari web scraping rumah123.com, dengan menggunakan web scraper pada link GitHub repository <a href="https://github.com/tugusav/Rumah123-Data-Analysis" target="_blank">berikut</a>. Data-data yang dipakai adalah harga properti, lokasi properti, luas tanah properti, dan banyaknya ruangan pada properti.

## Akses Website
Berikut merupakan hasil model yang telah kami deploy.
Link: https://prediksi-properti.herokuapp.com/

## Cara menjalankan web di lokal
```bash
git clone https://github.com/afiffahreza/aib-data-science.git
pip install -r requirements.txt
python app.py
```
Model bisa diupdate dengan menjalankan file [rumah123-predict.ipynb](https://github.com/afiffahreza/aib-data-science/blob/main/rumah123-predict.ipynb)
