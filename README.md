# GreenPath
## Sistem Rekomendasi Tanaman Menggunakan Deep Learning

Sistem Rekomendasi Tanaman adalah aplikasi berbasis deep learning yang memberikan rekomendasi tanaman yang cocok berdasarkan berbagai kondisi lingkungan dan tanah. Sistem ini bertujuan untuk membantu petani dan profesional pertanian dalam mengambil keputusan yang lebih tepat mengenai pemilihan tanaman, mengoptimalkan hasil panen, dan memaksimalkan keuntungan. Sistem ini memperhitungkan beberapa faktor seperti jenis tanah, iklim, curah hujan, suhu, kelembapan, pH tanah, dan kandungan nitrogen, fosfor, serta kalium untuk menentukan tanaman yang paling sesuai untuk suatu wilayah. Dengan menganalisis data historis dan menggunakan model prediktif, sistem ini memberikan rekomendasi yang dipersonalisasi sesuai dengan kondisi spesifik lahan atau area pertanian.

## Fitur Utama
- Pengumpulan Data Input: Sistem memungkinkan pengguna untuk memasukkan data yang relevan seperti parameter tanah, informasi iklim, dan lokasi geografis.
- Praproses Data: Data input diproses untuk menangani nilai yang hilang, menormalkan atau menskalakan fitur, dan mengubah variabel kategorikal.
- Model Deep Learning: Model deep learning digunakan untuk membangun model prediktif yang dapat menangkap hubungan non-linear antara parameter lingkungan dan tanaman.
- Pelatihan dan Evaluasi Model: Model dilatih menggunakan data historis dan dievaluasi dengan metrik kinerja yang tepat untuk memastikan akurasi dan keandalan.
- Rekomendasi Tanaman: Berdasarkan model yang telah dilatih, sistem merekomendasikan tanaman yang paling cocok untuk parameter input yang diberikan.
- Antarmuka Pengguna yang Ramah: Sistem menyediakan antarmuka pengguna yang mudah digunakan di mana pengguna dapat dengan mudah memasukkan data mereka, melihat rekomendasi, dan mengeksplorasi informasi tambahan.

## Teknologi yang Digunakan
- Python: Bahasa pemrograman yang digunakan untuk pengembangan model, praproses data, dan pengembangan aplikasi web.
- TensorFlow/Keras: Framework deep learning yang digunakan untuk pelatihan model, evaluasi, dan prediksi.
- Pandas: Pustaka manipulasi data yang digunakan untuk praproses data dan analisis.
- NumPy: Pustaka komputasi numerik yang digunakan untuk menangani array dan operasi matematika.
- Streamlit: Framework open-source yang digunakan untuk membangun antarmuka pengguna (UI) interaktif untuk aplikasi data science. Framework ini dirancang khusus untuk mempermudah pengembangan aplikasi web dengan menggunakan Python.
- HTML/CSS: Bahasa markup dan styling yang digunakan untuk merancang antarmuka web.
- JavaScript: Bahasa scripting yang digunakan untuk interaksi sisi klien dan meningkatkan antarmuka pengguna.

## Pengembangan di Masa Depan
- Integrasi data cuaca real-time untuk meningkatkan akurasi rekomendasi.
- Incorporasi harga pasar tanaman dan analisis profitabilitas untuk membantu petani dalam membuat keputusan ekonomi yang layak.
- Pengembangan aplikasi mobile untuk akses yang lebih mudah di smartphone dan tablet.
- Integrasi umpan balik pengguna dan pengumpulan data untuk terus meningkatkan kinerja sistem rekomendasi.

## Akses Program
Streamlit : https://greenpath.streamlit.app/
