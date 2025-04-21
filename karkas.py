"""
Kalkulator Komponen Karkas dan Non-Karkas Ternak Indonesia
===================================================
Program ini menghitung perkiraan berat komponen karkas dan non-karkas
untuk sapi, kambing, dan domba berdasarkan berat hidup.

Referensi persentase komponen karkas dan non-karkas diadaptasi
dari literatur peternakan Indonesia.
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

current_year = datetime.datetime.now().year

# Handle potential import error with a more informative message
try:
    import info_bangsa_ternak as ibt
except ImportError:
    st.error("""
    Error: Tidak dapat mengimpor modul 'info_bangsa_ternak'.
    
    Pastikan file 'info_bangsa_ternak.py' berada di direktori yang sama dengan 'karkas.py'.
    Jika sudah ada, pastikan nama file telah ditulis dengan benar (info_bangsa_ternak.py).
    
    Anda juga bisa menjalankan aplikasi dengan cara:
    ```
    cd /Users/macbookpro/Desktop/karkas
    streamlit run karkas.py
    ```
    """)
    st.stop()

def hitung_komponen_sapi(berat_hidup, bangsa=None, jenis_kelamin='jantan'):
    """Menghitung komponen karkas dan non-karkas untuk sapi."""
    persentase = {
        'karkas': 52.5,
        'daging': 40.5,
        'tulang': 9.0,
        'lemak': 3.0,
        'kulit': 8.0,
        'kepala': 4.5,
        'kaki': 2.5,
        'ekor': 0.5,
        'darah': 3.5,
        'jeroan_merah': 4.0,
        'jeroan_hijau': 8.0,
        'lemak_internal': 4.0,
    }
    
    if bangsa:
        try:
            for kategori in ibt.SAPI:
                if bangsa in ibt.SAPI[kategori]:
                    data_bangsa = ibt.SAPI[kategori][bangsa]
                    persen_str = data_bangsa['persen_karkas']
                    persen_range = persen_str.replace('%', '').split('-')
                    if jenis_kelamin == 'jantan':
                        persentase['karkas'] = float(persen_range[1])
                    else:
                        persentase['karkas'] = float(persen_range[0])
                    
                    faktor = persentase['karkas'] / 52.5
                    persentase['daging'] *= faktor
                    persentase['tulang'] *= faktor
                    persentase['lemak'] *= faktor
                    break
        except Exception as e:
            st.warning(f"Gagal menyesuaikan persentase karkas: {str(e)}")
    
    hasil = {}
    for komponen, persen in persentase.items():
        hasil[komponen] = round(berat_hidup * persen / 100, 2)
    
    return hasil

def hitung_komponen_kambing(berat_hidup, bangsa=None, jenis_kelamin='jantan'):
    """Menghitung komponen karkas dan non-karkas untuk kambing."""
    persentase = {
        'karkas': 45.0,
        'daging': 34.0,
        'tulang': 8.0,
        'lemak': 3.0,
        'kulit': 8.5,
        'kepala': 6.0,
        'kaki': 2.5,
        'ekor': 0.3,
        'darah': 4.0,
        'jeroan_merah': 3.0,
        'jeroan_hijau': 9.0,
        'lemak_internal': 3.0,
    }
    
    if bangsa:
        try:
            for kategori in ibt.KAMBING:
                if bangsa in ibt.KAMBING[kategori]:
                    data_bangsa = ibt.KAMBING[kategori][bangsa]
                    persen_str = data_bangsa['persen_karkas']
                    persen_range = persen_str.replace('%', '').split('-')
                    if jenis_kelamin == 'jantan':
                        persentase['karkas'] = float(persen_range[1])
                    else:
                        persentase['karkas'] = float(persen_range[0])
                    
                    faktor = persentase['karkas'] / 45.0
                    persentase['daging'] *= faktor
                    persentase['tulang'] *= faktor
                    persentase['lemak'] *= faktor
                    break
        except Exception as e:
            st.warning(f"Gagal menyesuaikan persentase karkas: {str(e)}")
    
    hasil = {}
    for komponen, persen in persentase.items():
        hasil[komponen] = round(berat_hidup * persen / 100, 2)
    
    return hasil

def hitung_komponen_domba(berat_hidup, bangsa=None, jenis_kelamin='jantan'):
    """Menghitung komponen karkas dan non-karkas untuk domba."""
    persentase = {
        'karkas': 47.0,
        'daging': 35.0,
        'tulang': 8.5,
        'lemak': 3.5,
        'kulit': 9.0,
        'wol': 4.0,
        'kepala': 5.5,
        'kaki': 2.5,
        'ekor': 1.0,
        'darah': 3.5,
        'jeroan_merah': 3.0,
        'jeroan_hijau': 8.5,
        'lemak_internal': 3.5,
    }
    
    if bangsa:
        try:
            for kategori in ibt.DOMBA:
                if bangsa in ibt.DOMBA[kategori]:
                    data_bangsa = ibt.DOMBA[kategori][bangsa]
                    persen_str = data_bangsa['persen_karkas']
                    persen_range = persen_str.replace('%', '').split('-')
                    if jenis_kelamin == 'jantan':
                        persentase['karkas'] = float(persen_range[1])
                    else:
                        persentase['karkas'] = float(persen_range[0])
                    
                    faktor = persentase['karkas'] / 47.0
                    persentase['daging'] *= faktor
                    persentase['tulang'] *= faktor
                    persentase['lemak'] *= faktor
                    break
        except Exception as e:
            st.warning(f"Gagal menyesuaikan persentase karkas: {str(e)}")
    
    hasil = {}
    for komponen, persen in persentase.items():
        hasil[komponen] = round(berat_hidup * persen / 100, 2)
    
    return hasil

def tampilkan_hasil_streamlit(jenis_ternak, berat_hidup, hasil, bangsa=None, jenis_kelamin=None):
    """Menampilkan hasil perhitungan dalam format Streamlit."""
    st.header(f"Hasil Perhitungan Komponen {jenis_ternak.capitalize()}")
    
    if bangsa:
        st.subheader(f"Bangsa: {bangsa}")
    
    st.subheader(f"Berat Hidup: {berat_hidup} kg")
    
    if jenis_kelamin:
        st.subheader(f"Jenis Kelamin: {jenis_kelamin.capitalize()}")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Tabel Hasil", "Visualisasi", "Info Bangsa", "Referensi"])
    
    komponen_karkas = ['karkas', 'daging', 'tulang', 'lemak']
    data_karkas = []
    data_non_karkas = []
    
    for komponen in komponen_karkas:
        if komponen in hasil:
            persen = hasil[komponen] / berat_hidup * 100
            data_karkas.append({
                'Komponen': komponen.capitalize(),
                'Berat (kg)': f"{hasil[komponen]:.2f}",
                'Persentase (%)': f"{persen:.2f}"
            })
    
    for komponen, nilai in hasil.items():
        if komponen not in komponen_karkas:
            persen = nilai / berat_hidup * 100
            nama_komponen = komponen.replace('_', ' ').capitalize()
            data_non_karkas.append({
                'Komponen': nama_komponen,
                'Berat (kg)': f"{nilai:.2f}",
                'Persentase (%)': f"{persen:.2f}"
            })
    
    with tab1:
        st.subheader("Komponen Karkas")
        df_karkas = pd.DataFrame(data_karkas)
        st.dataframe(df_karkas.style.highlight_max(axis=0, subset=['Berat (kg)']), use_container_width=True)
        
        st.subheader("Komponen Non-Karkas")
        df_non_karkas = pd.DataFrame(data_non_karkas)
        st.dataframe(df_non_karkas.style.highlight_max(axis=0, subset=['Berat (kg)']), use_container_width=True)
        
        total_berat_karkas = sum(float(row['Berat (kg)']) for row in data_karkas if row['Komponen'] != 'Karkas')
        total_berat_non_karkas = sum(float(row['Berat (kg)']) for row in data_non_karkas)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Berat Karkas", f"{hasil['karkas']:.2f} kg", f"{hasil['karkas']/berat_hidup*100:.1f}%")
        with col2:
            st.metric("Total Berat Non-Karkas", f"{total_berat_non_karkas:.2f} kg", f"{total_berat_non_karkas/berat_hidup*100:.1f}%")
    
    with tab2:
        st.subheader("Visualisasi Komponen Utama")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            fig_pie, ax_pie = plt.subplots(figsize=(10, 8))
            
            labels_pie = ['Karkas']
            sizes_pie = [hasil['karkas']]
            colors_pie = ['#ff9999']
            
            non_karkas_labels = []
            non_karkas_sizes = []
            
            for komponen, nilai in hasil.items():
                if komponen != 'karkas' and komponen not in ['daging', 'tulang', 'lemak'] and nilai > 0.5:
                    non_karkas_labels.append(komponen.replace('_', ' ').capitalize())
                    non_karkas_sizes.append(nilai)
            
            labels_pie.extend(non_karkas_labels)
            sizes_pie.extend(non_karkas_sizes)
            colors_pie.extend(plt.cm.Paired(range(len(non_karkas_labels))))
            
            explode = [0.1] + [0] * len(non_karkas_labels)
            
            ax_pie.pie(sizes_pie, explode=explode, labels=labels_pie, autopct='%1.1f%%', 
                   startangle=90, colors=colors_pie, shadow=True)
            ax_pie.axis('equal')
            plt.title(f'Distribusi Komponen Utama {jenis_ternak.capitalize()}', fontsize=16)
            st.pyplot(fig_pie)
        
        with col2:
            st.write("##### Komposisi Utama")
            for i, (label, size) in enumerate(zip(labels_pie, sizes_pie)):
                st.write(f"{label}: {size:.2f} kg ({size/berat_hidup*100:.1f}%)")
        
        st.subheader("Detail Komponen Karkas vs Non-Karkas")
        
        detail_labels = []
        detail_sizes = []
        detail_colors = []
        
        for komponen in ['daging', 'tulang', 'lemak']:
            if komponen in hasil:
                detail_labels.append(komponen.capitalize())
                detail_sizes.append(hasil[komponen])
                detail_colors.append('#ff9999')
        
        for komponen, nilai in sorted(hasil.items(), key=lambda x: x[1], reverse=True):
            if komponen not in ['karkas', 'daging', 'tulang', 'lemak'] and nilai > 0.2:
                detail_labels.append(komponen.replace('_', ' ').capitalize())
                detail_sizes.append(nilai)
                detail_colors.append('#66b3ff')
        
        fig_bar, ax_bar = plt.subplots(figsize=(12, 8))
        bars = ax_bar.bar(detail_labels, detail_sizes, color=detail_colors)
        
        for bar in bars:
            height = bar.get_height()
            ax_bar.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{height:.1f}', ha='center', va='bottom', fontsize=9)
        
        plt.xticks(rotation=45, ha='right')
        plt.ylabel('Berat (kg)')
        plt.title(f'Berat Komponen Detail {jenis_ternak.capitalize()} ({berat_hidup} kg)', fontsize=16)
        plt.tight_layout()
        st.pyplot(fig_bar)
    
    with tab3:
        if bangsa:
            st.subheader(f"Informasi Bangsa {bangsa}")
            
            data_bangsa = None
            kategori_bangsa = None
            
            if jenis_ternak.lower() == "sapi":
                for kategori in ibt.SAPI:
                    if bangsa in ibt.SAPI[kategori]:
                        data_bangsa = ibt.SAPI[kategori][bangsa]
                        kategori_bangsa = kategori
                        break
            elif jenis_ternak.lower() == "kambing":
                for kategori in ibt.KAMBING:
                    if bangsa in ibt.KAMBING[kategori]:
                        data_bangsa = ibt.KAMBING[kategori][bangsa]
                        kategori_bangsa = kategori
                        break
            elif jenis_ternak.lower() == "domba":
                for kategori in ibt.DOMBA:
                    if bangsa in ibt.DOMBA[kategori]:
                        data_bangsa = ibt.DOMBA[kategori][bangsa]
                        kategori_bangsa = kategori
                        break
            
            if data_bangsa:
                col1, col2 = st.columns([2, 3])
                
                with col1:
                    # Get image URL from the function instead of the data dictionary
                    image_url = ibt.get_breed_image_url(jenis_ternak, bangsa)
                    st.image(image_url, caption=bangsa, use_container_width=True)
                
                with col2:
                    st.markdown(f"#### Kategori: {kategori_bangsa.capitalize()}")
                    st.markdown(f"**Asal:** {data_bangsa['asal']}")
                    st.markdown(f"**Ciri Khas:** {data_bangsa['ciri_khas']}")
                    st.markdown(f"**Berat Jantan:** {data_bangsa['berat_jantan']}")
                    st.markdown(f"**Berat Betina:** {data_bangsa['berat_betina']}")
                    st.markdown(f"**Persentase Karkas:** {data_bangsa['persen_karkas']}")
                    st.markdown(f"**Keunggulan:** {data_bangsa['keunggulan']}")
                    
                    # Display culling information if available (for dairy cattle)
                    if 'keterangan_afkir' in data_bangsa:
                        st.markdown(f"**Keterangan Afkir:** {data_bangsa['keterangan_afkir']}")
                    
                    # Tambahkan link pencarian Google
                    search_url = data_bangsa.get('search_url', ibt.get_search_url(jenis_ternak, bangsa))
                    st.markdown(f"[🔍 Cari info lebih lanjut tentang {bangsa} di Google]({search_url})")
                
                # Add special notes for dairy cattle culls
                if kategori_bangsa == 'perah_afkir':
                    st.info("""
                    **Catatan untuk Sapi Perah Afkir:**
                    Sapi perah afkir memiliki karakteristik daging yang berbeda dari sapi potong. 
                    Umumnya memiliki tekstur daging yang lebih keras namun dapat diolah dengan 
                    teknik masak yang tepat seperti slow cooking atau braising.
                    """)
                
                st.subheader("Perbandingan dengan Standar")
                
                persen_str = data_bangsa['persen_karkas']
                persen_range = persen_str.replace('%', '').split('-')
                persen_min = float(persen_range[0])
                persen_max = float(persen_range[1])
                persen_avg = (persen_min + persen_max) / 2
                
                default_persen = 0
                if jenis_ternak.lower() == "sapi":
                    default_persen = 52.5
                elif jenis_ternak.lower() == "kambing":
                    default_persen = 45.0
                elif jenis_ternak.lower() == "domba":
                    default_persen = 47.0
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Persentase Karkas Bangsa Ini", f"{persen_avg:.1f}%", 
                             f"{persen_avg - default_persen:.1f}%" if persen_avg != default_persen else "0%")
                
                with col2:
                    berat_jantan = data_bangsa['berat_jantan'].replace(' kg', '').split('-')
                    berat_jantan_avg = (float(berat_jantan[0]) + float(berat_jantan[1])) / 2
                    
                    berat_betina = data_bangsa['berat_betina'].replace(' kg', '').split('-')
                    berat_betina_avg = (float(berat_betina[0]) + float(berat_betina[1])) / 2
                    
                    if jenis_kelamin and jenis_kelamin.lower() == 'betina':
                        st.metric("Berat Hidup Rata-rata", f"{berat_betina_avg:.1f} kg", 
                                 f"{berat_hidup - berat_betina_avg:.1f} kg")
                    else:
                        st.metric("Berat Hidup Rata-rata", f"{berat_jantan_avg:.1f} kg", 
                                 f"{berat_hidup - berat_jantan_avg:.1f} kg")
                
                with col3:
                    if jenis_kelamin and jenis_kelamin.lower() == 'betina':
                        karkas_ideal = berat_hidup * persen_min / 100
                    else:
                        karkas_ideal = berat_hidup * persen_max / 100
                    
                    st.metric("Karkas Ideal", f"{karkas_ideal:.1f} kg", 
                             f"{karkas_ideal - hasil['karkas']:.1f} kg")
            else:
                st.warning(f"Data detail untuk bangsa {bangsa} tidak ditemukan")
        else:
            st.info("Silakan pilih bangsa ternak untuk melihat informasi detail")
    
    with tab4:
        st.subheader("Referensi dan Sumber Data")
        st.markdown("""
        #### Sumber Data Persentase Komponen Karkas:
        
        1. **Sapi:**
           - Soeparno. (2015). *Ilmu dan Teknologi Daging*. Gadjah Mada University Press.
           - Sutaryo, B., et al. (2018). "Karakteristik Karkas Sapi Potong di Indonesia." *Jurnal Ilmu dan Teknologi Peternakan*, 6(2), 54-63.
           
        2. **Sapi Perah Afkir:**
           - Usmiati, S., & Setiyanto, H. (2019). "Karakteristik Daging Sapi Friesian Holstein Afkir dari Berbagai Umur Kronologis." *Jurnal Ilmu Produksi dan Teknologi Hasil Peternakan*, 7(1), 29-34.
           - Setyono, D.J., et al. (2017). "Kualitas Karkas Sapi Perah Afkir yang Diberi Suplementasi Konsentrat Selama Periode Adaptasi." *Buletin Peternakan*, 41(2), 142-149.
        
        3. **Kambing:**
           - Sunarlim, R., & Usmiati, S. (2016). "Karakteristik Daging Kambing dengan Perendaman Enzim Papain." *Jurnal Ilmu Ternak dan Veteriner*, 11(2), 105-111.
           - Ginting, S. P., & Mahmilia, F. (2014). "Kualitas Karkas Kambing Kacang Jantan yang Diberi Pakan dengan Level Protein Berbeda." *Jurnal Ilmu-Ilmu Peternakan*, 24(1), 8-17.
        
        4. **Domba:**
           - Budisatria, I. G. S., et al. (2017). "Pengaruh Jenis Kelamin terhadap Kinerja Produksi dan Kualitas Fisik Daging Ternak Domba." *Buletin Peternakan*, 41(4), 455-466.
           - Tiesnamurti, B. (2019). *Pengembangan Teknologi Produksi Domba di Indonesia*. IAARD Press.
        
        #### Catatan Metodologi:
        Persentase yang digunakan dalam kalkulator ini merupakan rata-rata dari berbagai penelitian pada ternak Indonesia 
        dengan mempertimbangkan faktor breed, pakan, dan sistem produksi yang umum di Indonesia.
        
        Perhitungan ini bersifat estimasi dan hasil aktual dapat bervariasi berdasarkan genetik, pakan, umur, 
        jenis kelamin, dan kondisi pemeliharaan ternak.
        
        #### Catatan untuk Sapi Perah Afkir:
        Sapi perah afkir adalah sapi perah yang sudah tidak produktif lagi untuk produksi susu. Karakteristik daging sapi 
        perah afkir berbeda dengan sapi potong, umumnya memiliki persentase karkas lebih rendah, kandungan lemak yang berbeda,
        dan tekstur daging yang lebih keras. Namun, dengan penanganan pasca panen yang tepat, daging sapi perah afkir tetap 
        dapat dimanfaatkan dengan baik terutama untuk produk olahan daging.
        """)

def main():
    st.set_page_config(
        page_title="Kalkulator Komponen Karkas",
        page_icon="🐄",
        layout="wide",
    )
    
    st.title("Kalkulator Komponen Karkas dan Non-Karkas Ternak Indonesia")
    st.write("""
    Program ini menghitung perkiraan berat komponen karkas dan non-karkas
    untuk sapi, kambing, dan domba berdasarkan berat hidup dan bangsa ternak.
    
    Referensi persentase diadaptasi dari literatur peternakan Indonesia.
    """)
    
    with st.sidebar:
        st.header("Input Data Ternak")
        jenis_ternak = st.selectbox(
            "Pilih jenis ternak:",
            ["Sapi", "Kambing", "Domba"]
        )
        
        # Get breed categories for filtering
        categories = []
        if jenis_ternak == "Sapi":
            categories = ibt.get_breed_categories("sapi")
        elif jenis_ternak == "Kambing":
            categories = ibt.get_breed_categories("kambing")
        elif jenis_ternak == "Domba":
            categories = ibt.get_breed_categories("domba")
        
        # Category filter
        selected_category = "Semua Kategori"
        if categories:
            category_options = ["Semua Kategori"] + [cat.capitalize() for cat in categories]
            selected_category = st.selectbox(
                f"Filter Kategori {jenis_ternak}:",
                category_options
            )
        
        # Get filtered breed list
        daftar_bangsa = []
        if jenis_ternak == "Sapi":
            if selected_category == "Semua Kategori":
                daftar_bangsa = ibt.get_all_breed_names("sapi")
            else:
                # Get breeds only from the selected category
                category = selected_category.lower()
                daftar_bangsa = list(ibt.SAPI.get(category, {}).keys())
        elif jenis_ternak == "Kambing":
            if selected_category == "Semua Kategori":
                daftar_bangsa = ibt.get_all_breed_names("kambing")
            else:
                category = selected_category.lower()
                daftar_bangsa = list(ibt.KAMBING.get(category, {}).keys())
        elif jenis_ternak == "Domba":
            if selected_category == "Semua Kategori":
                daftar_bangsa = ibt.get_all_breed_names("domba")
            else:
                category = selected_category.lower()
                daftar_bangsa = list(ibt.DOMBA.get(category, {}).keys())
        
        daftar_bangsa = ["Default/Umum"] + daftar_bangsa
        
        bangsa = st.selectbox(
            f"Pilih bangsa {jenis_ternak.lower()}:",
            daftar_bangsa
        )
        
        jenis_kelamin = st.radio(
            "Jenis Kelamin:",
            ["Jantan", "Betina"]
        )
        
        default_weight = 100.0
        if bangsa != "Default/Umum":
            try:
                default_weight = ibt.get_typical_weight(
                    jenis_ternak.lower(), 
                    bangsa, 
                    jenis_kelamin.lower()
                ) or 100.0
            except:
                pass
        
        berat_hidup = st.number_input(
            "Masukkan berat hidup (kg):",
            min_value=0.1,
            max_value=2000.0,
            value=float(default_weight),
            step=0.5
        )
        
        hitung = st.button("Hitung Komponen")
    
    if hitung:
        bangsa_param = None if bangsa == "Default/Umum" else bangsa
        
        if jenis_ternak == "Sapi":
            hasil = hitung_komponen_sapi(berat_hidup, bangsa_param, jenis_kelamin.lower())
            tampilkan_hasil_streamlit("sapi", berat_hidup, hasil, bangsa_param, jenis_kelamin)
        elif jenis_ternak == "Kambing":
            hasil = hitung_komponen_kambing(berat_hidup, bangsa_param, jenis_kelamin.lower())
            tampilkan_hasil_streamlit("kambing", berat_hidup, hasil, bangsa_param, jenis_kelamin)
        elif jenis_ternak == "Domba":
            hasil = hitung_komponen_domba(berat_hidup, bangsa_param, jenis_kelamin.lower())
            tampilkan_hasil_streamlit("domba", berat_hidup, hasil, bangsa_param, jenis_kelamin)

if __name__ == "__main__":
    main()

# Footer with LinkedIn profile link and improved styling
st.markdown("""
<hr style="height:1px;border:none;color:#333;background-color:#333;margin-top:30px;margin-bottom:20px">
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align:center; padding:15px; margin-top:10px; margin-bottom:20px">
    <p style="font-size:16px; color:#555">
        © {current_year} Developed by: 
        <a href="https://www.linkedin.com/in/galuh-adi-insani-1aa0a5105/" target="_blank" 
           style="text-decoration:none; color:#0077B5; font-weight:bold">
            <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" 
                 width="16" height="16" style="vertical-align:middle; margin-right:5px">
            Galuh Adi Insani
        </a> 
        with <span style="color:#e25555">❤️</span>
    </p>
    <p style="font-size:12px; color:#777">All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
