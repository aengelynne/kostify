import streamlit as st
import pandas as pd

# =========================================================
# KOSTIFY — Modern Cozy Living
# =========================================================

st.set_page_config(
    page_title="Kostify | Find, Filter, and Fit",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------- DESIGN -------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
        --cream: #F8F7F2;
        --white: #FFFFFF;
        --green: #355747;
        --green-dark: #294638;
        --green-light: #E8EFE7;
        --sage: #A9BDA8;
        --text: #25382F;
        --muted: #7C8980;
        --border: #E6E9E1;
    }

    .stApp {
        background: var(--cream);
        color: var(--text);
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] { background: transparent; }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: var(--text);
        font-family: 'Manrope', sans-serif !important;
        letter-spacing: -0.6px;
    }

    h1 { font-weight: 800 !important; }
    h2, h3 { font-weight: 700 !important; }


/* SIDEBAR — DARK FOREST GREEN */
[data-testid="stSidebar"] {
    background: #294638 !important;
    border-right: 1px solid #3F5C4B;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.5rem;
}

[data-testid="stSidebar"] .brand-mark {
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] .sidebar-subtitle {
    color: #D5E0D4 !important;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] h4,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"],
[data-testid="stSidebar"] [data-testid="stWidgetLabel"],
[data-testid="stSidebar"] label {
    color: #F5F5ED !important;
}

[data-testid="stSidebar"] input,
[data-testid="stSidebar"] textarea {
    background-color: #FFFFFF !important;
    color: #25382F !important;
    -webkit-text-fill-color: #25382F !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #25382F !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] input {
    color: #25382F !important;
    -webkit-text-fill-color: #25382F !important;
}

[data-testid="stSidebar"] [data-testid="stCheckbox"] label,
[data-testid="stSidebar"] [data-testid="stCheckbox"] p {
    color: #F5F5ED !important;
}

[data-testid="stSidebar"] hr {
    border-color: #526B5A !important;
}

    .brand-mark {
        font-family: 'Manrope', sans-serif;
        font-size: 25px;
        font-weight: 800;
        letter-spacing: -1px;
        color: #FFFFFF;
        margin-bottom: 2px;
    }

    .sidebar-subtitle {
        color: #D5E0D4;
        font-size: 12px;
        line-height: 1.6;
        margin-bottom: 15px;
    }

    .hero {
        background: linear-gradient(120deg, #294638 0%, #54745B 100%);
        padding: 38px 38px 34px 38px;
        border-radius: 25px;
        margin-bottom: 26px;
        box-shadow: 0 12px 35px rgba(41, 70, 56, 0.12);
    }

    .hero-tag {
        color: #294638;
        background: #E0E9D8;
        display: inline-block;
        padding: 7px 13px;
        border-radius: 30px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.1px;
    }

    .hero h1 {
        color: #FFFFFF !important;
        font-size: clamp(30px, 4vw, 46px);
        line-height: 1.15;
        margin: 15px 0 12px 0;
    }

    .hero p {
        color: #E0E9DE !important;
        font-size: 15px;
        line-height: 1.8;
        max-width: 650px;
        margin-bottom: 0;
    }

    .section-eyebrow {
        color: #6E8472;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 5px;
    }

    .section-intro {
        color: #78857C;
        font-size: 14px;
        line-height: 1.7;
        margin-top: -5px;
        margin-bottom: 20px;
    }

    div[data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid var(--border);
        padding: 19px 21px;
        border-radius: 17px;
        box-shadow: 0 4px 15px rgba(37, 56, 47, 0.025);
    }

    div[data-testid="stMetricLabel"] {
        color: var(--muted);
        font-weight: 500;
    }

    div[data-testid="stMetricValue"] {
        color: var(--green);
        font-family: 'Manrope', sans-serif;
        font-weight: 800;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: #FFFFFF;
        border: 1px solid var(--border);
        border-radius: 19px;
        padding: 7px;
        box-shadow: 0 5px 20px rgba(37, 56, 47, 0.035);
    }

    .stButton > button,
    .stFormSubmitButton > button {
        border-radius: 11px;
        font-weight: 700;
        min-height: 42px;
        transition: all 0.2s ease;
    }

    .stButton > button[kind="primary"],
    .stFormSubmitButton > button[kind="primary"] {
        background: var(--green);
        color: white;
        border: 1px solid var(--green);
    }

    .stButton > button[kind="primary"]:hover,
    .stFormSubmitButton > button[kind="primary"]:hover {
        background: #456D55;
        border-color: #456D55;
        transform: translateY(-1px);
    }

    .stTextInput input,
    .stNumberInput input,
    [data-baseweb="select"] > div {
        border-radius: 10px;
    }

    [data-testid="stDataFrame"] {
        border: 1px solid var(--border);
        border-radius: 13px;
        overflow: hidden;
    }

    [data-testid="stAlert"] {
        border-radius: 13px;
    }

    [data-testid="stExpander"] {
        background: #FFFFFF;
        border: 1px solid var(--border);
        border-radius: 13px;
    }

    hr { border-color: var(--border); }

    .small-note {
        color: var(--muted);
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.2px;
    }

    .price {
        color: #355747;
        font-size: 27px;
        font-weight: 800;
        font-family: 'Manrope', sans-serif;
    }

    .price span {
        color: #7C8980;
        font-size: 13px;
        font-weight: 500;
        font-family: 'DM Sans', sans-serif;
    }

    .pill {
        display: inline-block;
        background: #E8EFE7;
        color: #355747;
        border-radius: 20px;
        padding: 6px 10px;
        font-size: 12px;
        font-weight: 600;
        margin: 3px 3px 3px 0;
    }

    .footer-note {
        color: #89948B;
        font-size: 12px;
        text-align: center;
        padding-top: 22px;
    }

    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }

    @media (max-width: 700px) {
        .hero { padding: 28px 23px; border-radius: 19px; }
        .block-container { padding-top: 1rem; }
    }
    
/* EMPTY STATE & ALERT MESSAGES */
[data-testid="stAlert"] {
    background-color: #EAF0E6 !important;
    border: 1px solid #D4E1D0 !important;
    border-radius: 13px;
}

[data-testid="stAlert"] p,
[data-testid="stAlert"] div,
[data-testid="stAlert"] span {
    color: #294638 !important;
}

/* GENERAL TEXT CONTRAST */
.stApp p,
.stApp li,
.stApp label,
.stApp [data-testid="stMarkdownContainer"] {
    color: #34483B;
}

/* INPUT PLACEHOLDERS */
.stApp input::placeholder,
.stApp textarea::placeholder {
    color: #78877A !important;
    -webkit-text-fill-color: #78877A !important;
}

/* EXPANDER TITLES */
[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary p {
    color: #294638 !important;
}

/* CHECKBOX LABELS */
.stApp [data-testid="stCheckbox"] label,
.stApp [data-testid="stCheckbox"] p {
    color: #294638 !important;
}

/* EMPTY TABLE TEXT */
[data-testid="stDataFrame"] {
    color: #294638;
}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------- DATA ---------------------------

DEFAULT_KRITERIA = {
    "harga_maks": 1_500_000.0,
    "bobot_harga": 3,
    "jarak_maks": 3.0,
    "bobot_jarak": 2,
    "luas_min": 10.0,
    "bobot_luas": 2,
    "ac": "n",
    "bobot_ac": 1,
    "kamar_mandi": "n",
    "bobot_kamar_mandi": 1,
    "furnished": "n",
    "bobot_furnished": 1,
    "parkir": "n",
    "bobot_parkir": 1,
    "ruang_hijau": "n",
    "bobot_ruang_hijau": 1,
    "transportasi": "n",
    "bobot_transportasi": 1,
}

FACILITIES = [
    ("ac", "AC", "❄️"),
    ("kamar_mandi", "Kamar mandi dalam", "🚿"),
    ("furnished", "Full furnished", "🪑"),
    ("parkir", "Parkir", "🛵"),
    ("ruang_hijau", "Akses ruang hijau", "🌿"),
    ("transportasi", "Dekat transportasi umum", "🚌"),
]

CRITERIA_LABELS = {
    "harga": "Harga",
    "jarak": "Jarak dari kampus",
    "luas": "Luas kamar",
    "ac": "AC",
    "kamar_mandi": "Kamar mandi dalam",
    "furnished": "Full furnished",
    "parkir": "Parkir",
    "ruang_hijau": "Akses ruang hijau",
    "transportasi": "Transportasi umum",
}

if "daftar_kost" not in st.session_state:
    st.session_state.daftar_kost = []

if "kriteria" not in st.session_state:
    st.session_state.kriteria = DEFAULT_KRITERIA.copy()

daftar_kost = st.session_state.daftar_kost
kriteria = st.session_state.kriteria


# ------------------------- HELPERS ------------------------

def rupiah(nilai):
    return f"Rp{nilai:,.0f}".replace(",", ".")


def ya_tidak(nilai):
    return "Ya" if nilai == "y" else "Tidak"


def hitung_skor(kost):
    if kost["harga"] <= 1_000_000:
        skor_harga = 3
    elif kost["harga"] <= 1_500_000:
        skor_harga = 2
    else:
        skor_harga = 1

    if kost["jarak"] <= 1:
        skor_jarak = 3
    elif kost["jarak"] <= 2:
        skor_jarak = 2
    else:
        skor_jarak = 1

    if kost["luas"] >= 18:
        skor_luas = 3
    elif kost["luas"] >= 14:
        skor_luas = 2
    else:
        skor_luas = 1

    skor = {
        "harga": skor_harga,
        "jarak": skor_jarak,
        "luas": skor_luas,
    }

    for nama, _, _ in FACILITIES:
        skor[nama] = 3 if kost[nama] == "y" else 1

    total = sum(
        skor[nama] * kriteria[f"bobot_{nama}"]
        for nama in CRITERIA_LABELS
    )

    return {"rincian": skor, "total": total}


def cari_hasil():
    hasil = []

    for kost in daftar_kost:
        if kost["kamar_tersisa"] <= 0:
            continue
        if kost["harga"] > kriteria["harga_maks"]:
            continue
        if kost["jarak"] > kriteria["jarak_maks"]:
            continue
        if kost["luas"] < kriteria["luas_min"]:
            continue

        if any(
            kriteria[nama] == "y" and kost[nama] != "y"
            for nama, _, _ in FACILITIES
        ):
            continue

        hasil.append({"kost": kost, "skor": hitung_skor(kost)})

    hasil.sort(
        key=lambda item: (
            -item["skor"]["total"],
            item["kost"]["harga"],
            item["kost"]["jarak"],
        )
    )
    return hasil


def render_fasilitas(kost):
    return "　·　".join(
        f"{ikon} {label}: {'✓' if kost[nama] == 'y' else '—'}"
        for nama, label, ikon in FACILITIES
    )


def render_kartu_kost(item, peringkat, detail_skor=True):
    kost = item["kost"]
    skor = item["skor"]

    with st.container(border=True):
        left, right = st.columns([3, 1])

        with left:
            st.markdown(
                f"<div class='small-note'>REKOMENDASI #{peringkat}</div>",
                unsafe_allow_html=True,
            )
            st.markdown(f"### 🏡 {kost['nama']}")
            st.markdown(
                f"<div class='price'>{rupiah(kost['harga'])}"
                f"<span> / bulan</span></div>",
                unsafe_allow_html=True,
            )

        with right:
            st.metric("⭐ Total skor", skor["total"])

        a, b, c = st.columns(3)
        a.metric("📍 Jarak", f"{kost['jarak']:g} km")
        b.metric("📐 Luas kamar", f"{kost['luas']:g} m²")
        c.metric("🛏️ Kamar tersedia", int(kost["kamar_tersisa"]))

        st.markdown("**Fasilitas**")
        st.caption(render_fasilitas(kost))

        if detail_skor:
            with st.expander("📊 Lihat rincian skor dan bobot"):
                data_skor = []
                for nama, label in CRITERIA_LABELS.items():
                    nilai_skor = skor["rincian"][nama]
                    bobot = kriteria[f"bobot_{nama}"]
                    data_skor.append(
                        {
                            "Kriteria": label,
                            "Skor": nilai_skor,
                            "Bobot": bobot,
                            "Skor × Bobot": nilai_skor * bobot,
                        }
                    )
                st.dataframe(
                    pd.DataFrame(data_skor),
                    use_container_width=True,
                    hide_index=True,
                )
                st.markdown(f"**Total skor: {skor['total']}**")


# ------------------------- SIDEBAR ------------------------

with st.sidebar:
    st.markdown("<div class='brand-mark'>🏡 Kostify</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='sidebar-subtitle'>Find a place to call home.<br>"
        "Your next chapter starts here.</div>",
        unsafe_allow_html=True,
    )
    st.divider()

    halaman = st.radio(
        "MENU UTAMA",
        [
            "🏠 Beranda",
            "🔎 Cari Kost",
            "➕ Tambah Kost",
            "📋 Data Kost",
            "⚙️ Kriteria & Bobot",
            "📖 Tutorial",
        ],
        label_visibility="visible",
    )

    st.divider()
    st.caption("MAKE YOURSELF AT HOME 🌿")
    st.caption(f"{len(daftar_kost)} data kost tersimpan di sesi ini")


# ------------------------- BERANDA -------------------------

if halaman == "🏠 Beranda":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-tag">YOUR NEXT CHAPTER STARTS HERE</div>
            <h1>Find a place<br>to call <em>home.</em> 🌿</h1>
            <p>
                Temukan kost yang cocok dengan gaya hidupmu.
                Sesuaikan budget, pilih fasilitas favorit, dan temukan
                tempat yang terasa seperti rumah.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    hasil = cari_hasil()
    total_kamar = sum(k["kamar_tersisa"] for k in daftar_kost)

    st.markdown("<div class='section-eyebrow'>YOUR OVERVIEW</div>", unsafe_allow_html=True)
    st.subheader("A little overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("🏘️ Total data kost", len(daftar_kost))
    col2.metric("🛏️ Kamar tersedia", int(total_kamar))
    col3.metric("✨ Sesuai kriteriamu", len(hasil))

    st.write("")
    st.markdown("<div class='section-eyebrow'>HANDPICKED FOR YOU</div>", unsafe_allow_html=True)
    st.subheader("Rekomendasi teratas")
    st.markdown(
        "<div class='section-intro'>Pilihan dengan skor tertinggi berdasarkan kriteria dan prioritasmu.</div>",
        unsafe_allow_html=True,
    )

    if not daftar_kost:
        st.info("Belum ada data kost. Mulai dengan membuka menu **Tambah Kost**.")
        if st.button("➕ Tambah kost pertama", type="primary"):
            st.session_state["navigasi_bantuan"] = True
            st.info("Pilih menu **Tambah Kost** di sidebar untuk mulai.")
    elif not hasil:
        st.warning("Belum ada kost yang cocok dengan kriteriamu.")
        st.caption("Coba sesuaikan batas harga, jarak, luas kamar, atau fasilitas wajib.")
    else:
        for nomor, item in enumerate(hasil[:3], start=1):
            render_kartu_kost(item, nomor, detail_skor=False)

    st.markdown(
        "<div class='footer-note'>Kostify · Find your comfort, find your place.</div>",
        unsafe_allow_html=True,
    )


# ------------------------- CARI KOST -----------------------

elif halaman == "🔎 Cari Kost":
    st.markdown("<div class='section-eyebrow'>DISCOVER YOUR SPACE</div>", unsafe_allow_html=True)
    st.title("Cari kost yang cocok")
    st.markdown(
        "<div class='section-intro'>Semua rekomendasi diurutkan berdasarkan skor dan bobot pilihanmu.</div>",
        unsafe_allow_html=True,
    )

    if not daftar_kost:
        st.warning("Belum ada data kost. Tambahkan data melalui menu **Tambah Kost**.")
    else:
        hasil = cari_hasil()
        if not hasil:
            st.warning("Tidak ada kost yang memenuhi kriteria saat ini.")
            st.caption("Coba naikkan batas harga, perluas jarak, atau ubah fasilitas wajib.")
        else:
            st.success(f"Ditemukan {len(hasil)} kost yang sesuai.")
            for nomor, item in enumerate(hasil, start=1):
                render_kartu_kost(item, nomor)


# ------------------------- TAMBAH KOST ---------------------

elif halaman == "➕ Tambah Kost":
    st.markdown("<div class='section-eyebrow'>GROW OUR DIRECTORY</div>", unsafe_allow_html=True)
    st.title("Tambah data kost")
    st.markdown(
        "<div class='section-intro'>Masukkan informasi kost agar bisa dibandingkan dan direkomendasikan.</div>",
        unsafe_allow_html=True,
    )

    with st.form("form_tambah_kost", clear_on_submit=True):
        st.subheader("Informasi utama")
        nama = st.text_input("Nama kost *", placeholder="Contoh: Kost Green House")

        col1, col2 = st.columns(2)
        with col1:
            harga = st.number_input(
                "Harga per bulan (Rp) *",
                min_value=0,
                value=1_000_000,
                step=50_000,
            )
            jarak = st.number_input(
                "Jarak dari kampus (km) *",
                min_value=0.0,
                value=1.0,
                step=0.1,
                format="%.1f",
            )
        with col2:
            luas = st.number_input(
                "Luas kamar (m²) *",
                min_value=0.0,
                value=12.0,
                step=0.5,
                format="%.1f",
            )
            kamar_tersisa = st.number_input(
                "Jumlah kamar tersedia *",
                min_value=0,
                value=1,
                step=1,
            )

        st.divider()
        st.subheader("Fasilitas yang tersedia")
        col1, col2 = st.columns(2)

        with col1:
            ac = st.selectbox("❄️ AC", ["y", "n"], format_func=ya_tidak)
            kamar_mandi = st.selectbox(
                "🚿 Kamar mandi dalam", ["y", "n"], format_func=ya_tidak
            )
            furnished = st.selectbox(
                "🪑 Full furnished", ["y", "n"], format_func=ya_tidak
            )

        with col2:
            parkir = st.selectbox("🛵 Parkir", ["y", "n"], format_func=ya_tidak)
            ruang_hijau = st.selectbox(
                "🌿 Akses ruang hijau", ["y", "n"], format_func=ya_tidak
            )
            transportasi = st.selectbox(
                "🚌 Dekat transportasi umum", ["y", "n"], format_func=ya_tidak
            )

        submitted = st.form_submit_button(
            "💾 Simpan data kost",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        nama_bersih = nama.strip()
        if not nama_bersih:
            st.error("Nama kost tidak boleh kosong.")
        elif any(k["nama"].casefold() == nama_bersih.casefold() for k in daftar_kost):
            st.error("Nama kost tersebut sudah terdaftar. Gunakan nama yang berbeda.")
        else:
            kost_baru = {
                "nama": nama_bersih,
                "harga": float(harga),
                "jarak": float(jarak),
                "luas": float(luas),
                "ac": ac,
                "kamar_mandi": kamar_mandi,
                "furnished": furnished,
                "parkir": parkir,
                "ruang_hijau": ruang_hijau,
                "transportasi": transportasi,
                "kamar_tersisa": int(kamar_tersisa),
            }
            st.session_state.daftar_kost.append(kost_baru)
            st.success(f"Data '{nama_bersih}' berhasil ditambahkan!")
            st.rerun()


# ------------------------- DATA KOST -----------------------

elif halaman == "📋 Data Kost":
    st.markdown("<div class='section-eyebrow'>YOUR DIRECTORY</div>", unsafe_allow_html=True)
    st.title("Seluruh data kost")
    st.markdown(
        "<div class='section-intro'>Cari, tinjau, dan kelola data kost yang telah dimasukkan.</div>",
        unsafe_allow_html=True,
    )

    if not daftar_kost:
        st.info("Belum ada data kost yang dimasukkan.")
    else:
        pencarian = st.text_input(
            "🔍 Cari nama kost",
            placeholder="Ketik nama kost yang ingin ditemukan...",
        )
        data_tampil = [
            kost for kost in daftar_kost
            if pencarian.strip().casefold() in kost["nama"].casefold()
        ]

        if data_tampil:
            rows = []
            for kost in data_tampil:
                rows.append(
                    {
                        "Nama Kost": kost["nama"],
                        "Harga/Bulan": rupiah(kost["harga"]),
                        "Jarak (km)": kost["jarak"],
                        "Luas (m²)": kost["luas"],
                        "AC": ya_tidak(kost["ac"]),
                        "KM Dalam": ya_tidak(kost["kamar_mandi"]),
                        "Furnished": ya_tidak(kost["furnished"]),
                        "Parkir": ya_tidak(kost["parkir"]),
                        "Ruang Hijau": ya_tidak(kost["ruang_hijau"]),
                        "Transportasi": ya_tidak(kost["transportasi"]),
                        "Kamar Tersisa": kost["kamar_tersisa"],
                    }
                )
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
            st.caption(f"Menampilkan {len(data_tampil)} data kost.")

        else:
            st.info("Tidak ada kost dengan nama tersebut.")

        st.divider()
        st.subheader("Hapus data kost")
        nama_hapus = st.selectbox(
            "Pilih kost yang ingin dihapus",
            [kost["nama"] for kost in daftar_kost],
        )
        konfirmasi = st.checkbox(f"Saya yakin ingin menghapus data {nama_hapus}")

        if st.button("🗑️ Hapus data terpilih", type="primary"):
            if konfirmasi:
                st.session_state.daftar_kost = [
                    kost for kost in daftar_kost if kost["nama"] != nama_hapus
                ]
                st.success(f"Data '{nama_hapus}' berhasil dihapus.")
                st.rerun()
            else:
                st.warning("Centang konfirmasi terlebih dahulu.")


# ------------------------- KRITERIA & BOBOT ----------------

elif halaman == "⚙️ Kriteria & Bobot":
    st.markdown("<div class='section-eyebrow'>MAKE IT YOURS</div>", unsafe_allow_html=True)
    st.title("Kriteria & bobot")
    st.markdown(
        "<div class='section-intro'>Tentukan batas pencarian dan prioritas yang paling penting buatmu.</div>",
        unsafe_allow_html=True,
    )

    st.info(
        "Rating 1 berarti kurang penting, 3 cukup penting, dan 5 sangat penting. "
        "Rating yang lebih tinggi memberi pengaruh lebih besar pada skor akhir."
    )

    with st.form("form_kriteria"):
        st.subheader("Batas pencarian")
        col1, col2, col3 = st.columns(3)

        with col1:
            harga_maks = st.number_input(
                "Harga maksimal (Rp)",
                min_value=0,
                value=int(kriteria["harga_maks"]),
                step=50_000,
            )
        with col2:
            jarak_maks = st.number_input(
                "Jarak maksimal (km)",
                min_value=0.0,
                value=float(kriteria["jarak_maks"]),
                step=0.5,
                format="%.1f",
            )
        with col3:
            luas_min = st.number_input(
                "Luas kamar minimal (m²)",
                min_value=0.0,
                value=float(kriteria["luas_min"]),
                step=1.0,
                format="%.1f",
            )

        st.divider()
        st.subheader("Rating kepentingan")
        st.caption("Geser setiap rating dari 1 sampai 5.")

        bobot_baru = {}
        for nama, label in CRITERIA_LABELS.items():
            bobot_baru[nama] = st.slider(
                label,
                min_value=1,
                max_value=5,
                value=int(kriteria[f"bobot_{nama}"]),
                key=f"bobot_slider_{nama}",
            )

        st.divider()
        st.subheader("Fasilitas wajib")
        st.caption(
            "Jika diaktifkan, kost yang tidak memiliki fasilitas tersebut "
            "tidak akan ditampilkan pada hasil pencarian."
        )

        fasilitas_baru = {}
        col1, col2 = st.columns(2)
        for indeks, (nama, label, ikon) in enumerate(FACILITIES):
            target = col1 if indeks % 2 == 0 else col2
            with target:
                fasilitas_baru[nama] = st.checkbox(
                    f"{ikon} {label} wajib",
                    value=(kriteria[nama] == "y"),
                    key=f"wajib_{nama}",
                )

        simpan = st.form_submit_button(
            "💾 Simpan preferensi",
            type="primary",
            use_container_width=True,
        )

    if simpan:
        kriteria_baru = {
            "harga_maks": float(harga_maks),
            "bobot_harga": int(bobot_baru["harga"]),
            "jarak_maks": float(jarak_maks),
            "bobot_jarak": int(bobot_baru["jarak"]),
            "luas_min": float(luas_min),
            "bobot_luas": int(bobot_baru["luas"]),
        }

        for nama, _, _ in FACILITIES:
            kriteria_baru[nama] = "y" if fasilitas_baru[nama] else "n"
            kriteria_baru[f"bobot_{nama}"] = int(bobot_baru[nama])

        st.session_state.kriteria = kriteria_baru
        st.success("Preferensi berhasil diperbarui!")
        st.rerun()

    if st.button("↩️ Reset ke pengaturan awal"):
        st.session_state.kriteria = DEFAULT_KRITERIA.copy()
        st.rerun()


# ------------------------- TUTORIAL ------------------------

elif halaman == "📖 Tutorial":
    st.markdown("<div class='section-eyebrow'>A QUICK GUIDE</div>", unsafe_allow_html=True)
    st.title("Cara menggunakan Kostify")
    st.markdown(
        "<div class='section-intro'>Beberapa langkah sederhana untuk menemukan kost yang sesuai.</div>",
        unsafe_allow_html=True,
    )

    tutorial_items = [
        (
            "01 · Tambahkan data kost",
            "Buka menu Tambah Kost. Masukkan nama, harga, jarak, luas kamar, "
            "fasilitas, dan jumlah kamar yang tersedia.",
        ),
        (
            "02 · Atur preferensi",
            "Di menu Kriteria & Bobot, tentukan batas harga, jarak, luas minimum, "
            "rating kepentingan, dan fasilitas wajib.",
        ),
        (
            "03 · Lihat rekomendasi",
            "Buka Cari Kost untuk melihat kost yang lolos kriteria dan diurutkan "
            "berdasarkan skor tertinggi.",
        ),
        (
            "04 · Pahami sistem skor",
            "Setiap kriteria memiliki skor dasar. Skor dikalikan rating kepentingan "
            "lalu dijumlahkan. Jika total skor sama, kost yang lebih murah "
            "akan berada di posisi lebih atas.",
        ),
        (
            "05 · Kelola data",
            "Menu Data Kost memungkinkanmu meninjau, mencari, dan menghapus data.",
        ),
    ]

    for judul, isi in tutorial_items:
        with st.expander(judul):
            st.write(isi)

    st.warning(
        "Catatan penyimpanan: versi ini menyimpan data selama sesi aplikasi berjalan. "
        "Data dapat hilang saat sesi di-reset atau aplikasi dimulai ulang. "
        "Untuk penyimpanan permanen, hubungkan aplikasi ke database atau file."
    )

st.markdown(
    "<div class='footer-note'>Made with care · Kostify 🌿</div>",
    unsafe_allow_html=True,
)
