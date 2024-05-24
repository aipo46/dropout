# Submission Akhir: Menyelesaikan Permasalahan Institusi Pendidikan Jaya Jaya Institut

## ***Business Understanding***

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.


## **Permasalahan Bisnis**

Jumlah *dropout* yang tinggi menjadi salah satu masalah yang besar untuk Jaya Jaya Institut. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan *dropout* sehingga dapat diberi bimbingan khusus.

## **Cakupan Proyek**

Untuk mengatasi permasalahan *dropout* siswa dalam pendidikannya, akan digunakan pendekatan dan metode/teknik berikut:

### Pemahaman Data (*Data Understanding*)
- Mengumpulkan data historis mengenai informasi profil siswa, performa belajar siswa dan faktor-faktor lain yang terkait.
- Mempelajari tipe dan karakteristik *dataset*.

### Persiapan Data (*Data Preparation*)
- Membersihkan dan mengolah data untuk mengatasi *missing values*, data duplikat, dan masalah lain yang mungkin mempengaruhi kualitas analisis.
- Melakukan proses transformasi data seperti *encoding* kategori, normalisasi, dan pemilihan fitur yang relevan untuk analisis.
- Menjelajahi korelasi antar variabel untuk memahami hubungan di antara variabel-variabel tersebut.

### *Machine Learning Modeling*
- Memisahkan data menjadi *training set* dan *testing set*.
- Melatih beberapa model menggunakan *training set*, dengan variabel target *status* dan variabel fitur yang relevan.
- Menyesuaikan *hyperparameter* model dan melakukan validasi model.

### *Evaluation*
- Menggunakan *testing set* untuk mengevaluasi kinerja model dengan metrik yang sesuai seperti *accuracy*, *precision*, *recall* dan *F1-score*.

### *Deployment*
- Menjalankan model *Logistic Regression* yang telah dibuat ke dalam lingkup produksi sehingga *user* dapat berinteraksi dengan model.

## **Persiapan**

Sumber data: 
Dicoding Repository https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

*Setup environment*:

1. Pastikan sudah menginstall Visual Studio Code  di komputer Anda.
2. Install Aplikasi addoun Python.
3. Install Apliaksi addon Jupyter Notebook.
3. Buat environment virtual dengan Visual Studio Code.
5. Install library yang dibutuhkan dengan perintah dalam file requirements.txt (Auto install sat create virtaul environment).
6. Buka Jupyter Notebook dengan perintah create file .ipynb.
7. Siap mengerjakan proyek.

## ***Business Dashboard***

*Dashboard* dibuat dengan menggunakan *Tableau* untuk menampilkan distribusi data dan pengaruh variabel-variabel data terhadap *Dropout*. *Dashboard* dapat diakses pada *link* berikut ini:

https://public.tableau.com/views/Dropout_Analytic/Dashboard1?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link

## ***Prototype Solusi Machine Learning***

*Prototype* dibuat dengan menggunakan *Streamlit* untuk menampilkan prediksi data dari variabel-variabel data terhadap *Dropout*. *Prototype* dapat diakses pada *link* berikut ini:

https://jayainstitute.streamlit.app/

## ***Conclusion***

- Tingkat ketidaklulusan (*Dropout Rate*) sebesar 39,15% dari 3.630 siswa.
- Tingkat ketidaklulusan cukup seimbang antara siswa Laki-laki 720 siswa dan siswa Perempuan 701 siswa.
- Dari 1.421 siswa yang *dropout* sebanyak 1287 siswa tidak menerima beasiswa.
- Dari 1.421 siswa yang *dropout* terdapat 1.214 siswa yang mengikuti kelas pagi dan 207 siswa yang mengikuti kelas malam.



### **Rekomendasi *Action Items***

Beberapa rekomendasi *action items* yang harus dilakukan institusi guna menyelesaikan permasalahan atau mencapai target mereka.

- Mengembangkan program pendidikan / kelas alternatif yang dapat menjangkau siswa yang mungkin kesulitan menghadiri kelas pada waktu reguler, seperti program jarak jauh.
- Gencar memberikan program beasiswa pada murid baru atau yang existing.
- Menjalin kerjasama industri agar lulusan Jaya Jaya Institut dapat terserap langsung ke industri setelah lulus.
- Menyediakan tutor atau mentor, kelas remedial, bimbingan akademik, dan dukungan psikologis bagi siswa yang membutuhkannya.

