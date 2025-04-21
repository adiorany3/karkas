"""
Modul informasi bangsa ternak Indonesia
=======================================
Modul ini berisi informasi tentang berbagai bangsa sapi, kambing, dan domba
yang ada di Indonesia beserta karakteristik spesifiknya.
"""

# Dictionary informasi bangsa sapi
SAPI = {
    "lokal": {
        "Sapi Bali": {
            "asal": "Domestikasi dari banteng (Bos javanicus)",
            "ciri_khas": "Warna merah bata, dengan warna hitam di kaki dan punggung (pada jantan dewasa)",
            "berat_jantan": "350-450 kg",
            "berat_betina": "250-350 kg",
            "persen_karkas": "52-58%",
            "keunggulan": "Adaptasi yang baik terhadap lingkungan tropis, daya tahan terhadap pakan berkualitas rendah",
            "search_url": "https://www.google.com/search?q=Sapi+Bali+Indonesia"
        },
        "Sapi Aceh": {
            "asal": "Aceh, turunan dari Bos indicus",
            "ciri_khas": "Tubuh kecil, warna coklat kemerahan hingga coklat tua",
            "berat_jantan": "250-300 kg",
            "berat_betina": "200-250 kg",
            "persen_karkas": "48-52%",
            "keunggulan": "Tahan terhadap iklim panas dan kekeringan",
            "search_url": "https://www.google.com/search?q=Sapi+Aceh+Indonesia"
        },
        "Sapi Madura": {
            "asal": "Madura, persilangan antara Bos indicus (zebu) dan Bos javanicus (banteng)",
            "ciri_khas": "Warna merah kecoklatan, punuk kecil, tanduk pendek",
            "berat_jantan": "300-400 kg",
            "berat_betina": "200-300 kg",
            "persen_karkas": "49-54%",
            "keunggulan": "Tahan cekaman panas, digunakan untuk karapan sapi",
            "search_url": "https://www.google.com/search?q=Sapi+Madura+karakteristik"
        },
        "Sapi Pesisir": {
            "asal": "Sumatera Barat, berasal dari keturunan banteng dan zebu",
            "ciri_khas": "Tubuh kecil kompak, warna bervariasi (hitam, coklat, merah)",
            "berat_jantan": "160-260 kg",
            "berat_betina": "140-210 kg",
            "persen_karkas": "47-50%",
            "keunggulan": "Mampu bertahan pada kondisi pakan minimal, adaptasi pada lahan pesisir",
            "search_url": "https://www.google.com/search?q=Sapi+Pesisir+Sumatera+Barat"
        },
        "Sapi Sumba Ongole (SO)": {
            "asal": "Pulau Sumba, keturunan sapi Ongole dari India",
            "ciri_khas": "Tubuh besar, warna putih keabu-abuan, bergelambir, berpunuk",
            "berat_jantan": "500-600 kg",
            "berat_betina": "350-450 kg",
            "persen_karkas": "52-56%",
            "keunggulan": "Tahan panas, kebal terhadap parasit, produktivitas tinggi di lahan kering",
            "search_url": "https://www.google.com/search?q=Sapi+Sumba+Ongole+Indonesia"
        }
    },
    "perah_afkir": {
        "Sapi Friesian Holstein (FH) Afkir": {
            "asal": "Belanda, diintroduksi ke Indonesia sebagai sapi perah",
            "ciri_khas": "Warna hitam-putih, tubuh besar, ukuran ambing besar",
            "berat_jantan": "700-800 kg",
            "berat_betina": "500-650 kg",
            "persen_karkas": "48-52%",
            "keunggulan": "Harga lebih terjangkau dibanding sapi potong, daging lebih tender pada usia tertentu",
            "keterangan_afkir": "Diafkir setelah 4-6 laktasi (5-8 tahun), kualitas daging sedang",
            "search_url": "https://www.google.com/search?q=Sapi+Friesian+Holstein+afkir+daging"
        }
    },
    "persilangan": {
        "Sapi Peranakan Ongole (PO)": {
            "asal": "Persilangan sapi lokal dengan sapi Ongole dari India",
            "ciri_khas": "Berwarna putih, bergelambir, dan berpunuk",
            "berat_jantan": "400-500 kg",
            "berat_betina": "300-400 kg",
            "persen_karkas": "51-55%",
            "keunggulan": "Pertumbuhan cepat, adaptasi baik dengan lingkungan tropis",
            "search_url": "https://www.google.com/search?q=Sapi+Peranakan+Ongole+PO+Indonesia"
        }
    }
}

# Dictionary informasi bangsa kambing
KAMBING = {
    "lokal": {
        "Kambing Kacang": {
            "asal": "Asli Indonesia, tersebar di seluruh nusantara",
            "ciri_khas": "Tubuh kecil, telinga pendek tegak, warna bervariasi (hitam, coklat, putih)",
            "berat_jantan": "20-30 kg",
            "berat_betina": "15-25 kg",
            "persen_karkas": "44-47%",
            "keunggulan": "Prolifikasi tinggi, adaptasi sangat baik, tahan penyakit",
            "search_url": "https://www.google.com/search?q=Kambing+Kacang+Indonesia"
        },
        "Kambing Peranakan Etawah (PE)": {
            "asal": "Persilangan kambing Etawah (India) dengan kambing Kacang",
            "ciri_khas": "Telinga panjang menggantung, hidung melengkung, bulu panjang",
            "berat_jantan": "50-80 kg",
            "berat_betina": "40-60 kg",
            "persen_karkas": "45-49%",
            "keunggulan": "Dual purpose (daging dan susu), produksi susu 1-3 liter/hari",
            "search_url": "https://www.google.com/search?q=Kambing+Peranakan+Etawah+PE+Indonesia"
        },
        "Kambing Jawarandu": {
            "asal": "Jawa Tengah, persilangan kambing Kacang dengan PE",
            "ciri_khas": "Ukuran sedang, telinga setengah menggantung",
            "berat_jantan": "35-60 kg",
            "berat_betina": "25-45 kg",
            "persen_karkas": "45-48%",
            "keunggulan": "Adaptasi baik, dual purpose, lebih mudah pemeliharaan",
            "search_url": "https://www.google.com/search?q=Kambing+Jawarandu+Indonesia"
        },
        "Kambing Marica": {
            "asal": "Sulawesi Selatan, asli Indonesia",
            "ciri_khas": "Tubuh sangat kecil, telinga tegak, tanduk pendek",
            "berat_jantan": "15-25 kg",
            "berat_betina": "10-20 kg",
            "persen_karkas": "43-46%",
            "keunggulan": "Tahan kondisi kering, efisien mencerna pakan kasar, rasa daging khas",
            "search_url": "https://www.google.com/search?q=Kambing+Marica+Sulawesi"
        },
        "Kambing Gembrong": {
            "asal": "Bali, kambing langka asli Indonesia",
            "ciri_khas": "Bulu panjang terutama di bagian leher dan pundak, warna putih",
            "berat_jantan": "30-45 kg",
            "berat_betina": "25-35 kg",
            "persen_karkas": "45-48%",
            "keunggulan": "Adaptasi pada daerah pegunungan, tahan kondisi kering",
            "search_url": "https://www.google.com/search?q=Kambing+Gembrong+Bali+Indonesia"
        }
    },
    "introduksi": {
        "Kambing Boer": {
            "asal": "Afrika Selatan, diintroduksi ke Indonesia",
            "ciri_khas": "Tubuh besar, telinga lebar menggantung, kepala coklat-merah dengan badan putih",
            "berat_jantan": "80-120 kg",
            "berat_betina": "60-90 kg",
            "persen_karkas": "48-52%",
            "keunggulan": "Pertumbuhan cepat, konformasi tubuh baik, efisiensi pakan tinggi",
            "search_url": "https://www.google.com/search?q=Kambing+Boer+Indonesia+ternak"
        },
        "Kambing Saanen": {
            "asal": "Swiss, diintroduksi untuk produksi susu",
            "ciri_khas": "Seluruh tubuh berwarna putih, telinga tegak",
            "berat_jantan": "70-100 kg",
            "berat_betina": "60-80 kg",
            "persen_karkas": "43-47%",
            "keunggulan": "Produksi susu tinggi (3-5 liter/hari)",
            "search_url": "https://www.google.com/search?q=Kambing+Saanen+Indonesia+peternakan"
        },
        "Kambing Anglo Nubian": {
            "asal": "Inggris, persilangan kambing dari Timur Tengah dan India",
            "ciri_khas": "Telinga panjang menggantung, hidung cembung, warna bervariasi",
            "berat_jantan": "80-110 kg",
            "berat_betina": "60-80 kg",
            "persen_karkas": "46-50%",
            "keunggulan": "Dual purpose, susu berkadar lemak tinggi (4-6%), adaptasi iklim panas",
            "search_url": "https://www.google.com/search?q=Kambing+Anglo+Nubian+Indonesia"
        },
        "Kambing Kalahari": {
            "asal": "Afrika Selatan, diintroduksi ke Indonesia",
            "ciri_khas": "Warna merah kecoklatan, telinga panjang ke bawah",
            "berat_jantan": "85-115 kg",
            "berat_betina": "60-85 kg",
            "persen_karkas": "48-52%",
            "keunggulan": "Pertumbuhan cepat, tahan cuaca panas, daya tahan terhadap penyakit",
            "search_url": "https://www.google.com/search?q=Kambing+Kalahari+Red+Indonesia"
        },
        "Kambing Jamnapari": {
            "asal": "India, diintroduksi ke Indonesia",
            "ciri_khas": "Tubuh besar, telinga panjang menggantung, hidung melengkung",
            "berat_jantan": "70-100 kg",
            "berat_betina": "50-70 kg",
            "persen_karkas": "46-49%",
            "keunggulan": "Produksi susu tinggi, adaptasi baik di daerah tropis",
            "search_url": "https://www.google.com/search?q=Kambing+Jamnapari+Indonesia"
        }
    },
    "persilangan": {
        "Kambing Sapera": {
            "asal": "Indonesia, persilangan Saanen dengan Peranakan Etawah",
            "ciri_khas": "Tubuh besar, warna dominan putih, telinga medium menggantung",
            "berat_jantan": "60-80 kg",
            "berat_betina": "50-65 kg",
            "persen_karkas": "45-48%",
            "keunggulan": "Produksi susu tinggi (3-4 liter/hari), adaptasi iklim tropis",
            "search_url": "https://www.google.com/search?q=Kambing+Sapera+Indonesia"
        },
        "Kambing Boerka": {
            "asal": "Indonesia, persilangan Boer dengan Kacang",
            "ciri_khas": "Ukuran medium, telinga semi-lop, warna bervariasi",
            "berat_jantan": "50-75 kg",
            "berat_betina": "35-55 kg",
            "persen_karkas": "47-50%",
            "keunggulan": "Pertumbuhan lebih cepat dari Kacang, konformasi tubuh lebih baik, adaptasi tinggi",
            "search_url": "https://www.google.com/search?q=Kambing+Boerka+Indonesia"
        }
    }
}

# Dictionary informasi bangsa domba
DOMBA = {
    "lokal": {
        "Domba Ekor Tipis (DET)": {
            "asal": "Asli Indonesia, tersebar di Jawa Barat dan Jawa Tengah",
            "ciri_khas": "Ekor kecil dan pendek, warna dominan putih",
            "berat_jantan": "20-35 kg",
            "berat_betina": "15-25 kg",
            "persen_karkas": "46-49%",
            "keunggulan": "Prolifikasi tinggi, adaptasi sangat baik",
            "search_url": "https://www.google.com/search?q=Domba+Ekor+Tipis+DET+Indonesia"
        },
        "Domba Ekor Gemuk (DEG)": {
            "asal": "Indonesia Timur (Sulawesi, Lombok, Madura)",
            "ciri_khas": "Ekor besar menyimpan lemak, warna dominan putih dengan bagian hitam di kepala",
            "berat_jantan": "30-45 kg",
            "berat_betina": "25-35 kg",
            "persen_karkas": "47-52%",
            "keunggulan": "Tahan kondisi kering, efisien dalam menyimpan energi",
            "search_url": "https://www.google.com/search?q=Domba+Ekor+Gemuk+DEG+Indonesia"
        },
        "Domba Garut": {
            "asal": "Garut, Jawa Barat, persilangan DET dengan domba Merino dan domba Cape",
            "ciri_khas": "Tubuh kompak, kepala tegap, tanduk melingkar pada jantan",
            "berat_jantan": "40-80 kg",
            "berat_betina": "30-50 kg",
            "persen_karkas": "48-52%",
            "keunggulan": "Konformasi tubuh baik, dikenal untuk domba aduan",
            "search_url": "https://www.google.com/search?q=Domba+Garut+aduan+karkas"
        },
        "Domba Batur": {
            "asal": "Banjarnegara, Jawa Tengah",
            "ciri_khas": "Tubuh kompak, bulu tebal, warna dominan putih",
            "berat_jantan": "40-65 kg",
            "berat_betina": "30-45 kg",
            "persen_karkas": "47-51%",
            "keunggulan": "Adaptasi di dataran tinggi, pertumbuhan cepat",
            "search_url": "https://www.google.com/search?q=Domba+Batur+Banjarnegara"
        },
        "Domba Kisar": {
            "asal": "Pulau Kisar, Maluku Barat Daya",
            "ciri_khas": "Ukuran kecil, ekor tipis, warna hitam putih",
            "berat_jantan": "20-30 kg",
            "berat_betina": "15-25 kg",
            "persen_karkas": "45-48%",
            "keunggulan": "Adaptasi pada lingkungan kering dan berbatu",
            "search_url": "https://www.google.com/search?q=Domba+Kisar+Maluku"
        }
    },
    "introduksi": {
        "Domba Merino": {
            "asal": "Spanyol/Australia, diintroduksi untuk wol",
            "ciri_khas": "Wol tebal dan halus, tubuh besar",
            "berat_jantan": "70-100 kg",
            "berat_betina": "50-70 kg",
            "persen_karkas": "48-52%",
            "keunggulan": "Produksi wol premium",
            "search_url": "https://www.google.com/search?q=Domba+Merino+Indonesia+wol"
        },
        "Domba Suffolk": {
            "asal": "Inggris, diintroduksi untuk daging",
            "ciri_khas": "Kepala dan kaki hitam, badan berisi dan berbulu putih",
            "berat_jantan": "90-130 kg",
            "berat_betina": "70-90 kg",
            "persen_karkas": "50-55%",
            "keunggulan": "Pertumbuhan cepat, konformasi tubuh superior",
            "search_url": "https://www.google.com/search?q=Domba+Suffolk+Indonesia+daging"
        },
        "Domba Dorper": {
            "asal": "Afrika Selatan, persilangan Dorset Horn dengan Blackhead Persian",
            "ciri_khas": "Kepala hitam, badan putih, tidak berbulu/self-shedding",
            "berat_jantan": "80-120 kg",
            "berat_betina": "60-90 kg",
            "persen_karkas": "51-56%",
            "keunggulan": "Pertumbuhan sangat cepat, adaptasi iklim panas, kualitas daging tinggi",
            "search_url": "https://www.google.com/search?q=Domba+Dorper+Indonesia"
        },
        "Domba Texel": {
            "asal": "Belanda, domba tipe daging",
            "ciri_khas": "Tubuh berotot, bulu pendek dan putih, kepala putih tanpa tanduk",
            "berat_jantan": "85-125 kg",
            "berat_betina": "65-85 kg",
            "persen_karkas": "52-56%",
            "keunggulan": "Persentase daging tinggi, rendah lemak, pertumbuhan cepat",
            "search_url": "https://www.google.com/search?q=Domba+Texel+Indonesia"
        }
    },
    "persilangan": {
        "Domba Compass Agrinak": {
            "asal": "Indonesia, persilangan terencana oleh Balitnak",
            "ciri_khas": "Variasi warna hitam dan putih, tubuh proporsional",
            "berat_jantan": "50-75 kg",
            "berat_betina": "40-55 kg",
            "persen_karkas": "49-53%",
            "keunggulan": "Pertumbuhan cepat, adaptasi baik, performa reproduksi tinggi",
            "search_url": "https://www.google.com/search?q=Domba+Compass+Agrinak+Indonesia"
        },
        "Domba St. Croix": {
            "asal": "Virgin Islands, disilangkan dengan domba lokal",
            "ciri_khas": "Tidak berbulu (hair sheep), warna dominan putih",
            "berat_jantan": "60-90 kg",
            "berat_betina": "45-65 kg",
            "persen_karkas": "48-52%",
            "keunggulan": "Tahan parasit, adaptasi iklim tropis, daya reproduksi tinggi",
            "search_url": "https://www.google.com/search?q=Domba+St+Croix+Indonesia"
        }
    }
}

def get_info_bangsa(jenis_ternak, kategori=None, nama_bangsa=None):
    """
    Mengambil informasi tentang bangsa ternak
    
    Parameters:
    jenis_ternak (str): 'sapi', 'kambing', atau 'domba'
    kategori (str, optional): 'lokal', 'persilangan', atau 'introduksi'
    nama_bangsa (str, optional): Nama spesifik bangsa
    
    Returns:
    dict: Informasi bangsa ternak yang diminta
    """
    jenis_ternak = jenis_ternak.lower()
    if jenis_ternak == 'sapi':
        data = SAPI
    elif jenis_ternak == 'kambing':
        data = KAMBING
    elif jenis_ternak == 'domba':
        data = DOMBA
    else:
        return None
    if kategori is None:
        return data
    if kategori not in data:
        return None
    if nama_bangsa is None:
        return data[kategori]
    if nama_bangsa not in data[kategori]:
        return None
    return data[kategori][nama_bangsa]

def get_all_breed_names(jenis_ternak):
    """
    Mengambil semua nama bangsa untuk jenis ternak tertentu
    
    Parameters:
    jenis_ternak (str): 'sapi', 'kambing', atau 'domba'
    
    Returns:
    list: Daftar nama bangsa
    """
    jenis_ternak = jenis_ternak.lower()
    if jenis_ternak == 'sapi':
        data = SAPI
    elif jenis_ternak == 'kambing':
        data = KAMBING
    elif jenis_ternak == 'domba':
        data = DOMBA
    else:
        return []
    nama_bangsa = []
    for kategori in data:
        nama_bangsa.extend(list(data[kategori].keys()))
    return nama_bangsa

def get_breed_categories(jenis_ternak):
    """
    Mengambil semua kategori bangsa untuk jenis ternak tertentu
    
    Parameters:
    jenis_ternak (str): 'sapi', 'kambing', atau 'domba'
    
    Returns:
    list: Daftar kategori bangsa
    """
    jenis_ternak = jenis_ternak.lower()
    if jenis_ternak == 'sapi':
        return list(SAPI.keys())
    elif jenis_ternak == 'kambing':
        return list(KAMBING.keys())
    elif jenis_ternak == 'domba':
        return list(DOMBA.keys())
    else:
        return []

def hitung_estimasi_karkas(jenis_ternak, nama_bangsa, berat_hidup, jenis_kelamin='jantan'):
    """
    Menghitung estimasi berat karkas berdasarkan informasi bangsa
    
    Parameters:
    jenis_ternak (str): 'sapi', 'kambing', atau 'domba'
    nama_bangsa (str): Nama spesifik bangsa
    berat_hidup (float): Berat hidup ternak dalam kg
    jenis_kelamin (str): 'jantan' atau 'betina'
    
    Returns:
    dict: Estimasi berat karkas dan persentase
    """
    jenis_ternak = jenis_ternak.lower()
    jenis_kelamin = jenis_kelamin.lower()
    data = None
    if jenis_ternak == 'sapi':
        for kategori in SAPI:
            if nama_bangsa in SAPI[kategori]:
                data = SAPI[kategori][nama_bangsa]
                break
    elif jenis_ternak == 'kambing':
        for kategori in KAMBING:
            if nama_bangsa in KAMBING[kategori]:
                data = KAMBING[kategori][nama_bangsa]
                break
    elif jenis_ternak == 'domba':
        for kategori in DOMBA:
            if nama_bangsa in DOMBA[kategori]:
                data = DOMBA[kategori][nama_bangsa]
                break
    if data is None:
        return None
    # Ambil persentase karkas
    persen_str = data['persen_karkas']
    persen_range = persen_str.replace('%', '').split('-')
    persen_min = float(persen_range[0])
    persen_max = float(persen_range[1])
    # Gunakan persentase maksimum untuk jantan dan minimum untuk betina
    if jenis_kelamin == 'jantan':
        persen_karkas = persen_max
    else:  # betina
        persen_karkas = persen_min
    # Hitung berat karkas
    berat_karkas = berat_hidup * persen_karkas / 100
    
    return {
        'berat_karkas': round(berat_karkas, 2),
        'persentase': persen_karkas,
        'bangsa': nama_bangsa,
        'jenis_ternak': jenis_ternak,
        'berat_hidup': berat_hidup,
        'jenis_kelamin': jenis_kelamin
    }

def filter_breed_by_weight(jenis_ternak, min_weight=None, max_weight=None, jenis_kelamin='jantan'):
    """
    Menyaring bangsa ternak berdasarkan berat
    
    Parameters:
    jenis_ternak (str): 'sapi', 'kambing', atau 'domba'
    min_weight (float, optional): Berat minimum dalam kg
    max_weight (float, optional): Berat maksimum dalam kg
    jenis_kelamin (str): 'jantan' atau 'betina'
    
    Returns:
    list: Daftar bangsa yang memenuhi kriteria
    """
    jenis_ternak = jenis_ternak.lower()
    jenis_kelamin = jenis_kelamin.lower()
    # Pilih dataset berdasarkan jenis ternak
    if jenis_ternak == 'sapi':
        data = SAPI
    elif jenis_ternak == 'kambing':
        data = KAMBING
    elif jenis_ternak == 'domba':
        data = DOMBA
    else:
        return []
    hasil = []
    for kategori in data:
        for nama_bangsa, info in data[kategori].items():
            # Ambil berat berdasarkan jenis kelamin
            if jenis_kelamin == 'jantan':
                berat_str = info['berat_jantan']
            else:  # betina
                berat_str = info['berat_betina']
            # Ekstrak nilai berat
            berat_range = berat_str.replace(' kg', '').split('-')
            berat_min = float(berat_range[0])
            berat_max = float(berat_range[1])
            # Gunakan rata-rata berat untuk perbandingan
            berat_avg = (berat_min + berat_max) / 2
            # Filter berdasarkan kriteria
            if min_weight is not None and berat_avg < min_weight:
                continue
            if max_weight is not None and berat_avg > max_weight:
                continue
            # Tambahkan ke hasil jika lolos filter
            hasil.append({
                'nama': nama_bangsa,
                'kategori': kategori,
                'berat_min': berat_min,
                'berat_max': berat_max,
                'berat_avg': berat_avg,
                'detail': info
            })
    # Urutkan hasil berdasarkan berat rata-rata (menurun)
    return sorted(hasil, key=lambda x: x['berat_avg'], reverse=True)

def compare_breeds(jenis_ternak, nama_bangsa_list):
    """
    Membandingkan beberapa bangsa ternak
    
    Parameters:
    jenis_ternak (str): 'sapi', 'kambing', atau 'domba'
    nama_bangsa_list (list): Daftar nama bangsa yang akan dibandingkan
    
    Returns:
    dict: Data perbandingan
    """
    jenis_ternak = jenis_ternak.lower()
    if jenis_ternak == 'sapi':
        data = SAPI
    elif jenis_ternak == 'kambing':
        data = KAMBING
    elif jenis_ternak == 'domba':
        data = DOMBA
    else:
        return None
    hasil = []
    for nama_bangsa in nama_bangsa_list:
        for kategori in data:
            if nama_bangsa in data[kategori]:
                info = data[kategori][nama_bangsa].copy()
                info['nama'] = nama_bangsa
                info['kategori'] = kategori
                # Ekstrak nilai persentase karkas untuk perbandingan
                persen_str = info['persen_karkas']
                persen_range = persen_str.replace('%', '').split('-')
                persen_min = float(persen_range[0])
                persen_max = float(persen_range[1])
                info['persen_karkas_min'] = persen_min
                info['persen_karkas_max'] = persen_max
                info['persen_karkas_avg'] = (persen_min + persen_max) / 2
                
                # Ekstrak nilai berat untuk perbandingan
                berat_jantan = info['berat_jantan']
                berat_jantan_range = berat_jantan.replace(' kg', '').split('-')
                info['berat_jantan_min'] = float(berat_jantan_range[0])
                info['berat_jantan_max'] = float(berat_jantan_range[1])
                info['berat_jantan_avg'] = (info['berat_jantan_min'] + info['berat_jantan_max']) / 2
                
                berat_betina = info['berat_betina']
                berat_betina_range = berat_betina.replace(' kg', '').split('-')
                info['berat_betina_min'] = float(berat_betina_range[0])
                info['berat_betina_max'] = float(berat_betina_range[1])
                info['berat_betina_avg'] = (info['berat_betina_min'] + info['berat_betina_max']) / 2
                
                hasil.append(info)
                break
    
    return hasil

def get_typical_weight(jenis_ternak, nama_bangsa, jenis_kelamin='jantan'):
    """
    Mendapatkan berat tipikal untuk bangsa ternak tertentu
    
    Parameters:
    jenis_ternak (str): 'sapi', 'kambing', atau 'domba'
    nama_bangsa (str): Nama spesifik bangsa
    jenis_kelamin (str): 'jantan' atau 'betina'
    
    Returns:
    float: Berat tipikal dalam kg (nilai tengah dari rentang)
    """
    info = None
    jenis_ternak = jenis_ternak.lower()
    jenis_kelamin = jenis_kelamin.lower()
    # Cari informasi bangsa
    if jenis_ternak == 'sapi':
        for kategori in SAPI:
            if nama_bangsa in SAPI[kategori]:
                info = SAPI[kategori][nama_bangsa]
                break
    elif jenis_ternak == 'kambing':
        for kategori in KAMBING:
            if nama_bangsa in KAMBING[kategori]:
                info = KAMBING[kategori][nama_bangsa]
                break
    elif jenis_ternak == 'domba':
        for kategori in DOMBA:
            if nama_bangsa in DOMBA[kategori]:
                info = DOMBA[kategori][nama_bangsa]
                break
    if info is None:
        return None
    # Ambil rentang berat sesuai jenis kelamin
    if jenis_kelamin == 'jantan':
        berat_str = info['berat_jantan']
    else:  # betina
        berat_str = info['berat_betina']
    
    # Ekstrak nilai berat
    berat_range = berat_str.replace(' kg', '').split('-')
    berat_min = float(berat_range[0])
    berat_max = float(berat_range[1])
    # Kembalikan nilai tengah
    return (berat_min + berat_max) / 2

def get_breed_image_url(jenis_ternak, nama_bangsa):
    """
    Mendapatkan URL gambar untuk bangsa ternak tertentu
    
    Parameters:
    jenis_ternak (str): 'sapi', 'kambing', atau 'domba'
    nama_bangsa (str): Nama spesifik bangsa
    
    Returns:
    str: URL gambar untuk bangsa ternak
    """
    jenis_ternak = jenis_ternak.lower()
    # Dictionary gambar untuk semua bangsa
    image_urls = {
        'sapi': {
            'Sapi Bali': 'https://iptp-fapet.ipb.ac.id/wp-content/uploads/2018/04/sapbal.jpg',
            'Sapi Aceh': 'https://disbun.acehprov.go.id/uploads/Sapi_Aceh.jpg',
            'Sapi Madura': 'https://disnak.jatimprov.go.id/storage/uploads/madura-1643073645.jpg',
            'Sapi Peranakan Ongole (PO)': 'https://disnak.jatimprov.go.id/storage/uploads/po-1643073580.jpg',
            'Sapi Brahman Cross': 'https://dispangtan.bulelengkab.go.id/information/2022061311121701-brahman-cross-bernilai-ekonomis-tinggi',
            'Sapi Limousin Cross': 'https://disnak.jatimprov.go.id/storage/uploads/limousin-1643073687.jpg',
            'Sapi Simmental Cross': 'https://disnak.jatimprov.go.id/storage/uploads/simental-1643073671.jpg',
            'Sapi Pesisir': 'https://disnak.sumbarprov.go.id/asset/img/artikel/sapi-pesisir.jpg',
            'Sapi Sumba Ongole (SO)': 'https://disnak.nttprov.go.id/img/artikel/sapi_sumba_ongole.jpg',
            'Sapi Friesian Holstein (FH) Afkir': 'https://cdn.antaranews.com/cache/800x533/2018/08/20180813120406sapi-perah.jpg',
            'Sapi Jersey Afkir': 'https://www.vetindo.com/images/easyblog_articles/88/Sapi-Jersey.jpg',
            'Sapi Brown Swiss Afkir': 'https://livestockinternational.my.id/wp-content/uploads/2022/05/Brown-Swiss.png',
            'Sapi Peranakan FH (PFH) Afkir': 'https://disbunnak.jatimprov.go.id/wp-content/uploads/2018/06/sapi-pfh.jpg'
        },
        'kambing': {
            'Kambing Kacang': 'https://i0.wp.com/www.ekor9.com/wp-content/uploads/2016/06/kambing-kacang-hitam-kambing-kacang-putih.jpg',
            'Kambing Peranakan Etawah (PE)': 'https://perumda-am.co.id/wp-content/uploads/2020/07/2.-Mengenal-Kambing-Etawa-beserta-Jenisnya-Sangat-banyak-Manfaatnya-edit.jpg',
            'Kambing Jawarandu': 'https://asset.kompas.com/crops/QS9rD1RhdNTpJl6CUbD3tLgpwQY=/0x0:938x625/750x500/data/photo/2022/01/31/61f6fe5c18f58.jpg',
            'Kambing Boer': 'https://i0.wp.com/petanindo.com/wp-content/uploads/2019/12/Kambing-Boer.jpg',
            'Kambing Saanen': 'https://ternakrumahan.com/wp-content/uploads/2020/12/Kambing-Saanen.jpg'
        },
        'domba': {
            'Domba Ekor Tipis (DET)': 'https://disnak.jatimprov.go.id/storage/uploads/det-1643093780.jpg',
            'Domba Ekor Gemuk (DEG)': 'https://blogpictures.99.co/domba-ekor-gemuk-2.png',
            'Domba Garut': 'https://disnak.jatimprov.go.id/storage/uploads/garut-1643093795.jpg',
            'Domba Merino': 'https://ternakrumahan.com/wp-content/uploads/2020/09/Domba-Merino.jpg',
            'Domba Suffolk': 'https://ternakrumahan.com/wp-content/uploads/2020/09/Domba-Suffolk.jpg'
        }
    }
    
    # Fallback images jika bangsa tidak ditemukan
    fallback_images = {
        'sapi': 'https://cdn-cms.pgimgs.com/static/2021/04/1.-JENIS-SAPI-PEDAGING.jpg',
        'kambing': 'https://i0.wp.com/www.ekor9.com/wp-content/uploads/2019/10/jenis-kambing-di-indonesia.jpg',
        'domba': 'https://asset.kompas.com/crops/a58L0xsYPQEPUaMTg_n3_kgnbAI=/0x0:739x493/750x500/data/photo/2020/06/19/5eecbbce72d31.jpg'
    }
    
    # Cari gambar untuk bangsa tertentu
    if jenis_ternak in image_urls and nama_bangsa in image_urls[jenis_ternak]:
        return image_urls[jenis_ternak][nama_bangsa]
    
    # Jika tidak ditemukan, kembalikan fallback image
    return fallback_images.get(jenis_ternak, fallback_images['sapi'])

def get_all_breeds_with_details(jenis_ternak):
    """
    Mengambil semua bangsa dengan detail lengkap untuk jenis ternak tertentu
    
    Parameters:
    jenis_ternak (str): 'sapi', 'kambing', atau 'domba'
    
    Returns:
    list: Daftar bangsa dengan semua detail
    """
    jenis_ternak = jenis_ternak.lower()
    if jenis_ternak == 'sapi':
        data = SAPI
    elif jenis_ternak == 'kambing':
        data = KAMBING
    elif jenis_ternak == 'domba':
        data = DOMBA
    else:
        return []
    
    hasil = []
    for kategori in data:
        for nama_bangsa, info in data[kategori].items():
            breed_info = info.copy()
            breed_info['nama'] = nama_bangsa
            breed_info['kategori'] = kategori
            breed_info['jenis_ternak'] = jenis_ternak
            hasil.append(breed_info)
    
    return hasil

def get_search_url(jenis_ternak, nama_bangsa):
    """
    Menghasilkan URL pencarian Google untuk bangsa ternak tertentu
    
    Parameters:
    jenis_ternak (str): 'sapi', 'kambing', atau 'domba'
    nama_bangsa (str): Nama spesifik bangsa
    
    Returns:
    str: URL pencarian Google
    """
    jenis_ternak = jenis_ternak.lower()
    
    # Coba ambil URL yang sudah ada di data
    if jenis_ternak == 'sapi':
        for kategori in SAPI:
            if nama_bangsa in SAPI[kategori]:
                if 'search_url' in SAPI[kategori][nama_bangsa]:
                    return SAPI[kategori][nama_bangsa]['search_url']
    elif jenis_ternak == 'kambing':
        for kategori in KAMBING:
            if nama_bangsa in KAMBING[kategori]:
                if 'search_url' in KAMBING[kategori][nama_bangsa]:
                    return KAMBING[kategori][nama_bangsa]['search_url']
    elif jenis_ternak == 'domba':
        for kategori in DOMBA:
            if nama_bangsa in DOMBA[kategori]:
                if 'search_url' in DOMBA[kategori][nama_bangsa]:
                    return DOMBA[kategori][nama_bangsa]['search_url']
    
    # Jika URL tidak ada, buat URL baru
    nama_ternak = jenis_ternak.capitalize()
    query = f"{nama_bangsa} {nama_ternak} Indonesia"
    return f"https://www.google.com/search?q={query.replace(' ', '+')}"
