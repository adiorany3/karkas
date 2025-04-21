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
import numpy as np  # Add NumPy import for visualization functions

# Set page config at the beginning of the script
st.set_page_config(
    page_title="Kalkulator Komponen Karkas",
    page_icon="🐄",
    layout="wide",
)

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

# Hide default Streamlit elements
hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_st_style, unsafe_allow_html=True)

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
        st.info("""
        **Komponen Karkas:** Bagian dari tubuh ternak yang telah disembelih dan dikuliti, 
        tanpa kepala, kaki, ekor, dan organ dalam. Karkas terdiri dari daging, tulang, dan lemak yang 
        merupakan bagian utama yang dikonsumsi.
        """)
        
        st.success("""
        **Karkas:** Bagian tubuh hasil pemotongan ternak setelah dikurangi darah, kepala, kaki, kulit, 
        organ dalam, dan ekor. Karkas umumnya terdiri dari daging, tulang, dan lemak dalam perbandingan 
        bervariasi tergantung jenis ternak, umur, dan kondisi ternak.
        """)
        
        st.success("""
        **Daging:** Merupakan komponen utama karkas yang terdiri dari otot dan jaringan ikat seperti 
        tendon dan ligamen. Daging menyumbang sekitar 70-80% dari berat karkas. Komponen ini memiliki 
        nilai ekonomis dan nutrisi tertinggi dalam karkas, mengandung protein berkualitas tinggi, 
        vitamin B kompleks, zat besi, dan mineral penting lainnya.
        """)
        
        st.success("""
        **Tulang:** Merupakan struktur keras yang menyusun kerangka karkas ternak. Tulang 
        berkontribusi sekitar 15-20% dari total karkas. Komponen ini memiliki nilai ekonomis 
        yang signifikan sebagai sumber kalsium, kolagen, dan bahan dasar produk seperti kaldu, soup stock, 
        dan gelatin. Tulang juga bisa diolah menjadi tepung tulang sebagai pakan ternak atau pupuk.
        """)
        
        st.success("""
        **Lemak:** Jaringan adiposa yang terdistribusi di berbagai lokasi karkas seperti lemak 
        subkutan (di bawah kulit), lemak intermuskular (di antara otot), dan lemak intramuskular (marbling). 
        Lemak memengaruhi cita rasa, juiciness, dan keempukan daging. Persentase lemak karkas bervariasi 
        tergantung jenis ternak, umur, pakan, dan genetik, berkisar antara 5-30% dari berat karkas.
        """)
        
        df_karkas = pd.DataFrame(data_karkas)
        df_karkas['Berat (kg)'] = df_karkas['Berat (kg)'].astype(float)
        df_karkas['Persentase (%)'] = df_karkas['Persentase (%)'].astype(float)
        df_karkas['Berat (kg)'] = df_karkas['Berat (kg)'].map(lambda x: f"{x:.2f}")
        df_karkas['Persentase (%)'] = df_karkas['Persentase (%)'].map(lambda x: f"{x:.2f}")
        max_berat_idx = pd.to_numeric(df_karkas['Berat (kg)']).idxmax()
        df_karkas['Komponen'] = df_karkas.apply(
            lambda row: f"**{row['Komponen']}** 🔴" if row.name == max_berat_idx else row['Komponen'], 
            axis=1
        )
        
        st.write("Tabel di bawah ini menunjukkan berat dan persentase dari setiap komponen karkas. Nilai tertinggi ditandai dengan 🔴.")
        st.table(df_karkas)
        
        st.subheader("Komponen Non-Karkas")
        st.info("""
        **Komponen Non-Karkas:** Bagian ternak yang tidak termasuk dalam karkas, seperti kulit, 
        kepala, kaki, ekor, darah, dan organ dalam. Meskipun bukan karkas, komponen ini tetap memiliki 
        nilai ekonomis dan dapat dimanfaatkan (edible dan non-edible offal).
        """)
        
        df_non_karkas = pd.DataFrame(data_non_karkas)
        df_non_karkas['Berat (kg)'] = df_non_karkas['Berat (kg)'].astype(float)
        df_non_karkas['Persentase (%)'] = df_non_karkas['Persentase (%)'].astype(float)
        df_non_karkas = df_non_karkas.sort_values('Berat (kg)', ascending=False)
        df_non_karkas['Berat (kg)'] = df_non_karkas['Berat (kg)'].map(lambda x: f"{x:.2f}")
        df_non_karkas['Persentase (%)'] = df_non_karkas['Persentase (%)'].map(lambda x: f"{x:.2f}")
        max_berat_non_karkas_idx = pd.to_numeric(df_non_karkas['Berat (kg)']).idxmax()
        df_non_karkas['Komponen'] = df_non_karkas.apply(
            lambda row: f"**{row['Komponen']}** 🔵" if row.name == max_berat_non_karkas_idx else row['Komponen'], 
            axis=1
        )
        
        st.write("Tabel di bawah ini menunjukkan berat dan persentase dari setiap komponen non-karkas, diurutkan dari yang terberat. Nilai tertinggi ditandai dengan 🔵.")
        st.table(df_non_karkas)
        
        total_berat_karkas = sum(float(row['Berat (kg)']) for row in data_karkas if row['Komponen'] != 'Karkas')
        total_berat_non_karkas = sum(float(row['Berat (kg)']) for row in data_non_karkas)
        
        summary_data = {
            'Kategori': ['Total Karkas', 'Total Non-Karkas', 'Total Keseluruhan'],
            'Berat (kg)': [
                f"{hasil['karkas']:.2f}",
                f"{total_berat_non_karkas:.2f}",
                f"{hasil['karkas'] + total_berat_non_karkas:.2f}"
            ],
            'Persentase (%)': [
                f"{hasil['karkas']/berat_hidup*100:.2f}",
                f"{total_berat_non_karkas/berat_hidup*100:.2f}",
                f"{(hasil['karkas'] + total_berat_non_karkas)/berat_hidup*100:.2f}"
            ]
        }
        
        df_summary = pd.DataFrame(summary_data)
        st.subheader("Ringkasan Hasil")
        st.table(df_summary)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Berat Karkas", f"{hasil['karkas']:.2f} kg", f"{hasil['karkas']/berat_hidup*100:.1f}%")
        with col2:
            st.metric("Total Berat Non-Karkas", f"{total_berat_non_karkas:.2f} kg", f"{total_berat_non_karkas/berat_hidup*100:.1f}%")
    
    with tab2:
        st.subheader("Visualisasi Komponen Utama")
        st.info("""
        Visualisasi berikut menunjukkan distribusi komponen karkas dan non-karkas dari ternak.
        Chart bagian atas menampilkan proporsi utama (karkas vs non-karkas), 
        sementara chart bagian bawah menampilkan detail komponen-komponen spesifik.
        """)
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            # Improved pie chart with better colors and organization
            fig_pie, ax_pie = plt.subplots(figsize=(10, 7))
            
            # Prepare data for two-level pie chart
            karkas_data = []
            karkas_labels = []
            karkas_colors = plt.cm.Reds(np.linspace(0.4, 0.7, 3))
            
            for komponen in ['daging', 'tulang', 'lemak']:
                if komponen in hasil:
                    karkas_data.append(hasil[komponen])
                    karkas_labels.append(komponen.capitalize())
            
            non_karkas_data = []
            non_karkas_labels = []
            
            # Sort non-karkas components by weight for better visualization
            sorted_non_karkas = sorted(
                [(k, v) for k, v in hasil.items() 
                 if k not in ['karkas', 'daging', 'tulang', 'lemak']],
                key=lambda x: x[1], reverse=True
            )
            
            # Select top 6 non-karkas components for better readability
            top_non_karkas = sorted_non_karkas[:6]
            other_non_karkas_total = sum(v for k, v in sorted_non_karkas[6:])
            
            if other_non_karkas_total > 0:
                for k, v in top_non_karkas:
                    non_karkas_data.append(v)
                    non_karkas_labels.append(k.replace('_', ' ').capitalize())
                non_karkas_data.append(other_non_karkas_total)
                non_karkas_labels.append('Lainnya')
            else:
                for k, v in sorted_non_karkas:
                    non_karkas_data.append(v)
                    non_karkas_labels.append(k.replace('_', ' ').capitalize())
            
            # Improved color palettes
            non_karkas_colors = plt.cm.Blues(np.linspace(0.3, 0.8, len(non_karkas_data)))
            
            # Create two groups for the legend
            karkas_group = {'Data': karkas_data, 'Labels': karkas_labels, 'Colors': karkas_colors}
            non_karkas_group = {'Data': non_karkas_data, 'Labels': non_karkas_labels, 'Colors': non_karkas_colors}
            
            # Draw the pie chart
            def func(pct, allvals):
                absolute = round(pct/100.*sum(allvals), 1)
                return f"{pct:.1f}%\n({absolute:.1f} kg)"
            
            wedges, texts, autotexts = ax_pie.pie(
                karkas_data + non_karkas_data,
                autopct=lambda pct: func(pct, karkas_data + non_karkas_data),
                startangle=90,
                colors=np.concatenate([karkas_colors, non_karkas_colors]),
                wedgeprops=dict(width=0.5, edgecolor='w'),
                pctdistance=0.85
            )
            
            # Create a circle at the center to turn it into a donut chart
            centre_circle = plt.Circle((0, 0), 0.25, fc='white')
            fig_pie.gca().add_artist(centre_circle)
            
            # Equal aspect ratio ensures the pie chart is circular
            ax_pie.axis('equal')
            
            # Add title with total weight
            plt.title(f'Distribusi Komponen {jenis_ternak.capitalize()} ({berat_hidup} kg)', fontsize=14, pad=20)
            
            # Create legend with custom colors
            legend_elements = []
            
            # Karkas components for legend
            for i, label in enumerate(karkas_group['Labels']):
                legend_elements.append(
                    plt.Line2D([0], [0], marker='o', color='w', 
                              label=f"{label} ({karkas_group['Data'][i]:.1f} kg)",
                              markerfacecolor=karkas_group['Colors'][i], markersize=10)
                )
            
            # Non-karkas components for legend
            for i, label in enumerate(non_karkas_group['Labels']):
                legend_elements.append(
                    plt.Line2D([0], [0], marker='o', color='w', 
                              label=f"{label} ({non_karkas_group['Data'][i]:.1f} kg)",
                              markerfacecolor=non_karkas_group['Colors'][i], markersize=10)
                )
            
            # Place legend outside the pie chart
            ax_pie.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5), 
                       fontsize=9, frameon=True, title="Komponen (kg)")
            
            plt.tight_layout()
            st.pyplot(fig_pie)
        
        with col2:
            st.write("#### Ringkasan Komposisi")
            
            # Create a summary table with percentages
            total_karkas = sum(karkas_data)
            total_non_karkas = sum(non_karkas_data)
            
            st.metric(
                "Total Karkas", 
                f"{total_karkas:.2f} kg", 
                f"{total_karkas/berat_hidup*100:.1f}% dari berat hidup"
            )
            
            st.metric(
                "Total Non-Karkas",
                f"{total_non_karkas:.2f} kg",
                f"{total_non_karkas/berat_hidup*100:.1f}% dari berat hidup"
            )
            
            # Add a small horizontal bar chart showing karkas vs non-karkas proportion
            fig_bar_summary, ax_bar_summary = plt.subplots(figsize=(5, 2))
            bar_data = [total_karkas, total_non_karkas]
            bar_labels = ['Karkas', 'Non-Karkas']
            
            bars = ax_bar_summary.barh(
                bar_labels, 
                bar_data, 
                color=['#ff9999', '#66b3ff'], 
                height=0.5
            )
            
            # Add data labels to the bars
            for i, bar in enumerate(bars):
                width = bar.get_width()
                ax_bar_summary.text(
                    width/2, 
                    bar.get_y() + bar.get_height()/2, 
                    f'{width:.1f} kg ({width/berat_hidup*100:.1f}%)', 
                    ha='center', 
                    va='center', 
                    color='black', 
                    fontweight='bold'
                )
            
            ax_bar_summary.set_xlim(0, berat_hidup)
            ax_bar_summary.set_xlabel('Berat (kg)', fontsize=8)
            ax_bar_summary.set_title('Proporsi Karkas vs Non-Karkas', fontsize=10)
            ax_bar_summary.grid(axis='x', linestyle='--', alpha=0.7)
            plt.tight_layout()
            st.pyplot(fig_bar_summary)
            
            # Display key ratio information
            st.write("#### Rasio Komponen Karkas")
            
            if 'daging' in hasil and 'tulang' in hasil and hasil['tulang'] > 0:
                rasio_daging_tulang = hasil['daging'] / hasil['tulang']
                st.metric(
                    "Rasio Daging : Tulang", 
                    f"{rasio_daging_tulang:.2f} : 1",
                    f"{rasio_daging_tulang - 4.5:.2f}" if rasio_daging_tulang != 4.5 else "0",
                    help="Rasio ideal adalah sekitar 4.5:1. Nilai lebih tinggi menunjukkan proporsi daging yang lebih besar."
                )
    
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
                
                # Add explanation for the comparison section
                st.info("""
                **Perbandingan dengan Standar:** 
                Bagian ini menunjukkan perbandingan antara parameter ternak yang dipilih dengan nilai standar atau ideal. 
                Angka positif menunjukkan nilai di atas standar, sedangkan angka negatif menunjukkan nilai di bawah standar.
                Perbedaan ini dapat disebabkan oleh faktor genetik, manajemen pemeliharaan, 
                atau kondisi lingkungan yang berbeda.
                """)
                
                persen_str = data_bangsa['persen_karkas']
                persen_range = persen_str.replace('%', '').split('-')
                persen_min = float(persen_range[0])
                persen_max = float(persen_range[1])
                persen_avg = (persen_min + persen_max) / 2
                
                # Use the same default percentage values as defined in the calculation functions
                default_persen = 0
                if jenis_ternak.lower() == "sapi":
                    default_persen = 52.5  # Matches the value in hitung_komponen_sapi
                elif jenis_ternak.lower() == "kambing":
                    default_persen = 45.0  # Matches the value in hitung_komponen_kambing
                elif jenis_ternak.lower() == "domba":
                    default_persen = 47.0  # Matches the value in hitung_komponen_domba
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    # Add tooltip explanation for persentase karkas metric
                    karkas_diff = persen_avg - default_persen
                    karkas_help = f"""
                    Perbandingan persentase karkas bangsa {bangsa} ({persen_avg:.1f}%) 
                    dengan nilai standar untuk {jenis_ternak} ({default_persen:.1f}%).
                    Nilai positif menunjukkan bangsa ini memiliki persentase karkas lebih tinggi dari standar,
                    yang berarti efisiensi produksi daging lebih tinggi.
                    """
                    
                    st.metric(
                        "Persentase Karkas Bangsa Ini", 
                        f"{persen_avg:.1f}%", 
                        f"{karkas_diff:.1f}%" if karkas_diff != 0 else "0%",
                        help=karkas_help
                    )
                    
                    # Add additional explanation below the metric
                    if karkas_diff > 1:
                        st.caption(f"👍 Bangsa ini memiliki persentase karkas {karkas_diff:.1f}% lebih tinggi dari standar {jenis_ternak}.")
                    elif karkas_diff < -1:
                        st.caption(f"👎 Bangsa ini memiliki persentase karkas {abs(karkas_diff):.1f}% lebih rendah dari standar {jenis_ternak}.")
                    else:
                        st.caption("✓ Persentase karkas bangsa ini sesuai dengan standar.")
                
                with col2:
                    berat_jantan = data_bangsa['berat_jantan'].replace(' kg', '').split('-')
                    berat_jantan_avg = (float(berat_jantan[0]) + float(berat_jantan[1])) / 2
                    
                    berat_betina = data_bangsa['berat_betina'].replace(' kg', '').split('-')
                    berat_betina_avg = (float(berat_betina[0]) + float(berat_betina[1])) / 2
                    
                    if jenis_kelamin and jenis_kelamin.lower() == 'betina':
                        berat_diff = berat_hidup - berat_betina_avg
                        berat_help = f"""
                        Perbandingan berat hidup ternak yang diinput ({berat_hidup:.1f} kg) 
                        dengan berat rata-rata {jenis_ternak} betina bangsa {bangsa} ({berat_betina_avg:.1f} kg).
                        Nilai positif menunjukkan ternak lebih berat dari rata-rata bangsa ini,
                        yang dapat mengindikasikan manajemen pemeliharaan yang baik atau umur yang lebih dewasa.
                        """
                        
                        st.metric(
                            "Berat Hidup Rata-rata", 
                            f"{berat_betina_avg:.1f} kg", 
                            f"{berat_diff:.1f} kg",
                            help=berat_help
                        )
                        
                        # Add additional explanation
                        pct_diff = (berat_diff / berat_betina_avg) * 100
                        if pct_diff > 10:
                            st.caption(f"⭐ Ternak ini {pct_diff:.1f}% lebih berat dari rata-rata bangsa ini (betina).")
                        elif pct_diff < -10:
                            st.caption(f"⚠️ Ternak ini {abs(pct_diff):.1f}% lebih ringan dari rata-rata bangsa ini (betina).")
                        else:
                            st.caption("✓ Berat ternak ini sesuai dengan rata-rata bangsa.")
                    else:
                        berat_diff = berat_hidup - berat_jantan_avg
                        berat_help = f"""
                        Perbandingan berat hidup ternak yang diinput ({berat_hidup:.1f} kg) 
                        dengan berat rata-rata {jenis_ternak} jantan bangsa {bangsa} ({berat_jantan_avg:.1f} kg).
                        Nilai positif menunjukkan ternak lebih berat dari rata-rata bangsa ini,
                        yang dapat mengindikasikan manajemen pemeliharaan yang baik atau umur yang lebih dewasa.
                        """
                        
                        st.metric(
                            "Berat Hidup Rata-rata", 
                            f"{berat_jantan_avg:.1f} kg", 
                            f"{berat_diff:.1f} kg",
                            help=berat_help
                        )
                        
                        # Add additional explanation
                        pct_diff = (berat_diff / berat_jantan_avg) * 100
                        if pct_diff > 10:
                            st.caption(f"⭐ Ternak ini {pct_diff:.1f}% lebih berat dari rata-rata bangsa ini (jantan).")
                        elif pct_diff < -10:
                            st.caption(f"⚠️ Ternak ini {abs(pct_diff):.1f}% lebih ringan dari rata-rata bangsa ini (jantan).")
                        else:
                            st.caption("✓ Berat ternak ini sesuai dengan rata-rata bangsa.")
                
                # Add recommendations based on the comparison
                st.subheader("Rekomendasi")
                
                recommendations = []
                
                # Persentase karkas recommendations
                if karkas_diff > 2:
                    recommendations.append(
                        "🔹 **Perbaikan Persentase Karkas:** Ternak ini memiliki persentase karkas di bawah ideal. "
                        "Pertimbangkan untuk memperbaiki manajemen pakan dengan meningkatkan rasio konsentrat "
                        "pada fase penggemukan dan evaluasi ulang program nutrisi."
                    )
                elif karkas_diff < -2:
                    recommendations.append(
                        "🔹 **Persentase Karkas Optimal:** Ternak ini memiliki persentase karkas di atas ideal. "
                        "Ini menunjukkan efisiensi produksi daging yang sangat baik. Pertahankan manajemen pemeliharaan saat ini."
                    )
                
                # Berat hidup recommendations
                if jenis_kelamin.lower() == 'betina':
                    if berat_diff < -10:
                        recommendations.append(
                            "🔹 **Berat Hidup Sub-optimal:** Ternak betina ini lebih ringan dari rata-rata bangsa. "
                            "Evaluasi sistem pemeliharaan, kualitas pakan, dan jadwal pemberian pakan. "
                            "Pertimbangkan untuk menambah asupan nutrisi atau memeriksa kesehatan ternak."
                        )
                    elif berat_diff > 10:
                        recommendations.append(
                            "🔹 **Berat Hidup Superior:** Ternak betina ini lebih berat dari rata-rata bangsa. "
                            "Ini menunjukkan manajemen pemeliharaan yang baik. Jika ternak ini akan digunakan untuk "
                            "reproduksi, pertimbangkan untuk melestarikan genetiknya."
                        )
                else:
                    if berat_diff < -10:
                        recommendations.append(
                            "🔹 **Berat Hidup Sub-optimal:** Ternak jantan ini lebih ringan dari rata-rata bangsa. "
                            "Evaluasi sistem pemeliharaan, kualitas pakan, dan jadwal pemberian pakan. "
                            "Periode penggemukan lebih lama mungkin diperlukan untuk mencapai berat optimal."
                        )
                    elif berat_diff > 10:
                        recommendations.append(
                            "🔹 **Berat Hidup Superior:** Ternak jantan ini lebih berat dari rata-rata bangsa. "
                            "Ini bisa menjadi indikasi genetik unggul atau manajemen pemeliharaan yang sangat baik. "
                            "Jika ternak ini akan digunakan sebagai pejantan, genetiknya bernilai untuk dipertahankan."
                        )
                
                # Add general recommendations if no specific ones
                if not recommendations:
                    recommendations.append(
                        "🔹 **Kinerja Sesuai Standar:** Ternak ini menunjukkan kinerja sesuai dengan standar bangsa. "
                        "Lanjutkan dengan manajemen pemeliharaan yang saat ini diterapkan."
                    )
                else:
                    # Add a general recommendation at the end
                    recommendations.append(
                        "🔹 **Catatan Umum:** Performa ternak dipengaruhi oleh faktor genetik, pakan, kesehatan, "
                        "dan lingkungan. Perbandingan ini memberikan gambaran umum, tetapi evaluasi menyeluruh "
                        "harus mempertimbangkan kondisi spesifik lokasi dan sistem produksi."
                    )
                
                # Display all recommendations
                for rec in recommendations:
                    st.markdown(rec)
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
        
        categories = []
        if jenis_ternak == "Sapi":
            categories = ibt.get_breed_categories("sapi")
        elif jenis_ternak == "Kambing":
            categories = ibt.get_breed_categories("kambing")
        elif jenis_ternak == "Domba":
            categories = ibt.get_breed_categories("domba")
        
        selected_category = "Semua Kategori"
        if categories:
            category_options = ["Semua Kategori"] + [cat.capitalize() for cat in categories]
            selected_category = st.selectbox(
                f"Filter Kategori {jenis_ternak}:",
                category_options
            )
        
        daftar_bangsa = []
        if jenis_ternak == "Sapi":
            if selected_category == "Semua Kategori":
                daftar_bangsa = ibt.get_all_breed_names("sapi")
            else:
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
