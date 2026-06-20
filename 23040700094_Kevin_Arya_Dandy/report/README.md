# Tugas Praktikum: Akuisisi Bukti Jaringan (PCAP), Hashing SHA-256, dan Simulasi Blockchain Menggunakan Python

## 1. Identitas Mahasiswa
* **Nama** : Kevin Arya Dandy
* **NIM** : 23040700094

---

## 2. Deskripsi Tugas
Tugas ini mengimplementasikan simulasi blockchain sederhana menggunakan bahasa pemrograman Python untuk menyimpan metadata dan menjaga integritas bukti digital (data forensik jaringan). Sistem membaca file rekaman lalu lintas jaringan (*packet capture*), menghitung nilai identitas digitalnya, dan mengikatnya ke dalam rantai blok yang saling terhubung guna memastikan prinsip *chain of custody* terjaga dengan aman.

---

## 3. Tools yang Digunakan
* **Wireshark**: Digunakan untuk melakukan akuisisi lalu lintas data jaringan dan menghasilkan dataset file PCAP.
* **Python 3.11**: Bahasa pemrograman utama untuk membangun struktur blockchain dan memproses file jaringan.
* **Scapy Library**: Pustaka Python untuk membaca file PCAP dan menghitung jumlah paket jaringan di dalamnya.
* **Hashlib**: Pustaka bawaan Python untuk menghitung nilai kriptografi algoritma SHA-256.

---

## 4. Cara Menjalankan Program
1. Pastikan folder repositori memiliki struktur standar (`evidence/`, `sourcecode/`, `screenshot/`, dan `report/`).
2. Memasukan 5 file PCAP hasil akuisisi Wireshark ke dalam folder `evidence/`.
3. Membuka **Command Prompt (CMD)** dan arahkan direktori aktif ke dalam folder `sourcecode/`.
4. Menjalankan perintah berikut untuk mengeksekusi program:
   ```bash
   python blockchain_pcap .py


## 5. Screenshot Hasil Eksekusi & Validasi Blockchain
Berikut adalah dokumentasi bukti eksekusi program yang file gambarnya tersimpan di dalam folder `screenshot/`:

### A. Hasil Perhitungan Awal Hash PCAP (`hashing_result.png`)
![Hasil Hashing](screenshot/hashing_result.png)

### B. Struktur Rantai Blok yang Terbentuk (`blockchain_result.png`)
![Struktur Blockchain](screenshot/blockchain_result.png)

### C. Pembuktian Status Akhir Keabsahan Sistem (`validation_result.png`)
![Hasil Validasi](screenshot/validation_result.png)

---

## 6. Hasil Output & Validasi Eksekusi Program (Teks Log)
Berikut adalah salinan teks log output asli dari Command Prompt saat program berhasil memvalidasi seluruh rangkaian block data:

```text
=== TAHAP 1: Perhitungan Hash Bukti Digital (PCAP) ===
[Sukses] PCAP01_23040700094.pcap -> Hash: b048c53314939bb436a8ee35444a375abb45c614b96abed42bcbcdf07a253d0c
[Sukses] PCAP02_23040700094.pcap -> Hash: 60631e7ca761f91aa97d524bca402cdea68e499769f22788e0544c3f0f2069a9
[Sukses] PCAP03_23040700094.pcap -> Hash: 57b5878e737fc645c3b29242c269dc3f944897d914185b50659f4267020f28ab
[Sukses] PCAP04_23040700094.pcap -> Hash: e837ed466e7bbea95fc6da177971269e8de809391f117dd4ad47220013a72e1e
[Sukses] PCAP05_23040700094.pcap -> Hash: b772693354bd95d8339f46f42935ec05e82a4b371065562c557ba2bc45df69d8

=== TAHAP 2: Simulasi Masukkan Metadata PCAP ke Blockchain ===
==================================================
Index         : 0
Timestamp     : 2026-06-20 17:49:36.402243
Evidence File : Genesis Block
Packet Count  : 0
Evidence Hash : 0
Previous Hash : 0
Block Hash    : c8e351b044ff9095839af7b424013220a3ade6d637400bf785ba1a210c1ec07
----------------------------------------

Index         : 1
Timestamp     : 2026-06-20 17:49:36.402243
Evidence File : PCAP01_23040700094.pcap
Packet Count  : 30
Evidence Hash : b048c53314939bb436a8ee35444a375abb45c614b96abed42bcbcdf07a253d0c
Previous Hash : c8e351b044ff9095839af7b424013220a3ade6d637400bf785ba1a210c1ec07
Block Hash    : 235fdbfda3d3f85134ee03efed7d6641d38e746ff9599920328880106204f1fa
----------------------------------------

Index         : 2
Timestamp     : 2026-06-20 17:49:36.402243
Evidence File : PCAP02_23040700094.pcap
Packet Count  : 50
Evidence Hash : 60631e7ca761f91aa97d524bca402cdea68e499769f22788e0544c3f0f2069a9
Previous Hash : 235fdbfda3d3f85134ee03efed7d6641d38e746ff9599920328880106204f1fa
Block Hash    : 66adfd6be838480d1f55df4d9129c4d814fec9f7ff8bdb46b13e116bf44a41af
----------------------------------------

Index         : 3
Timestamp     : 2026-06-20 17:49:36.402243
Evidence File : PCAP03_23040700094.pcap
Packet Count  : 70
Evidence Hash : 57b5878e737fc645c3b29242c269dc3f944897d914185b50659f4267020f28ab
Previous Hash : 66adfd6be838480d1f55df4d9129c4d814fec9f7ff8bdb46b13e116bf44a41af
Block Hash    : 289fcd6d4db180983bdd697721e764ffeb3de7245cafcf7bdd3e67a28d0f1947
----------------------------------------

Index         : 4
Timestamp     : 2026-06-20 17:49:36.402243
Evidence File : PCAP04_23040700094.pcap
Packet Count  : 90
Evidence Hash : e837ed466e7bbea95fc6da177971269e8de809391f117dd4ad47220013a72e1e
Previous Hash : 289fcd6d4db180983bdd697721e764ffeb3de7245cafcf7bdd3e67a28d0f1947
Block Hash    : 6216db328af6ac72aac89fa90d46812984e3ccfa5675627e8ba34456171ce8c3
----------------------------------------

Index         : 5
Timestamp     : 2026-06-20 17:49:36.402243
Evidence File : PCAP05_23040700094.pcap
Packet Count  : 100
Evidence Hash : b772693354bd95d8339f46f42935ec05e82a4b371065562c557ba2bc45df69d8
Previous Hash : 6216db328af6ac72aac89fa90d46812984e3ccfa5675627e8ba34456171ce8c3
Block Hash    : 10e5d620cbaaed99d199b48f0dfaf65e24cde67c0467aa41e1f79afe7f706450
==================================================

=== TAHAP 3: Validasi Blockchain ===
Blockchain Validation : VALID