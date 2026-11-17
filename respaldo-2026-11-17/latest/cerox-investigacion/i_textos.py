#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las cadenas de la pantalla IPTV, en los 15 idiomas del proyecto.

`TraduccionesPresentesTest` (publicada mucho antes que esta pantalla) exige que toda
cadena de `values/strings.xml` esté también en las catorce carpetas `values-<tag>`, y
que ninguna esté vacía. O sea que una cadena nueva son quince entradas, o la prueba
falla. Estas son las 22 que necesita la pantalla.

Los apóstrofos van escapados: en un recurso de Android un `'` sin `\\` delante no
compila. Las comillas angulares y las tipográficas sí son literales válidos, y se
usan en vez de `"` ASCII, que también habría que escapar.
"""

IDIOMAS = ["en", "ca", "pt", "fr", "id", "ja", "ko", "ru", "th", "tr", "uk", "vi", "zh", "ar"]

# (clave, {idioma: texto}) — "es" es la base, la que va en values/strings.xml.
CADENAS = [
    ("iptv_estado_inicial", {
        "es": "Añade una fuente, elígela y pulsa «Cargar». cero-X no trae ninguna lista de canales.",
        "en": "Add a source, select it and tap “Load”. cero-X ships no channel lists.",
        "ca": "Afegiu una font, trieu-la i premeu «Carrega». cero-X no inclou cap llista de canals.",
        "pt": "Adicione uma fonte, selecione-a e toque em «Carregar». O cero-X não traz listas de canais.",
        "fr": "Ajoutez une source, sélectionnez-la puis appuyez sur « Charger ». cero-X ne fournit aucune liste de chaînes.",
        "id": "Tambahkan sumber, pilih, lalu ketuk «Muat». cero-X tidak menyertakan daftar saluran apa pun.",
        "ja": "ソースを追加して選び、「読み込む」を押してください。cero-Xにチャンネル一覧は同梱されていません。",
        "ko": "소스를 추가하고 선택한 뒤 «불러오기»를 누르세요. cero-X에는 채널 목록이 들어 있지 않습니다.",
        "ru": "Добавьте источник, выберите его и нажмите «Загрузить». cero-X не содержит списков каналов.",
        "th": "เพิ่มแหล่ง เลือก แล้วแตะ «โหลด» cero-X ไม่มีรายการช่องมาให้",
        "tr": "Bir kaynak ekleyin, seçin ve «Yükle» düğmesine dokunun. cero-X hiçbir kanal listesi içermez.",
        "uk": "Додайте джерело, виберіть його та натисніть «Завантажити». cero-X не містить списків каналів.",
        "vi": "Hãy thêm nguồn, chọn nguồn rồi nhấn «Tải». cero-X không kèm danh sách kênh nào.",
        "zh": "添加一个来源，选中它，然后点按“加载”。cero-X 不附带任何频道列表。",
        "ar": "أضف مصدرًا ثم حدده واضغط على «تحميل». لا يتضمن cero-X أي قائمة قنوات.",
    }),
    ("iptv_nombre_fuente", {
        "es": "Nombre de la fuente", "en": "Source name", "ca": "Nom de la font",
        "pt": "Nome da fonte", "fr": "Nom de la source", "id": "Nama sumber",
        "ja": "ソース名", "ko": "소스 이름", "ru": "Название источника", "th": "ชื่อแหล่ง",
        "tr": "Kaynak adı", "uk": "Назва джерела", "vi": "Tên nguồn", "zh": "来源名称",
        "ar": "اسم المصدر",
    }),
    ("iptv_url_lista", {
        "es": "URL de la lista (M3U o XMLTV)", "en": "List URL (M3U or XMLTV)",
        "ca": "URL de la llista (M3U o XMLTV)", "pt": "URL da lista (M3U ou XMLTV)",
        "fr": "URL de la liste (M3U ou XMLTV)", "id": "URL daftar (M3U atau XMLTV)",
        "ja": "リストのURL（M3UまたはXMLTV）", "ko": "목록 URL(M3U 또는 XMLTV)",
        "ru": "URL списка (M3U или XMLTV)", "th": "URL ของรายการ (M3U หรือ XMLTV)",
        "tr": "Liste adresi (M3U veya XMLTV)", "uk": "URL списку (M3U або XMLTV)",
        "vi": "URL danh sách (M3U hoặc XMLTV)", "zh": "列表网址（M3U 或 XMLTV）",
        "ar": "رابط القائمة (M3U أو XMLTV)",
    }),
    ("iptv_huella_opcional", {
        "es": "SHA-256 esperado (opcional)", "en": "Expected SHA-256 (optional)",
        "ca": "SHA-256 esperat (opcional)", "pt": "SHA-256 esperado (opcional)",
        "fr": "SHA-256 attendu (facultatif)", "id": "SHA-256 yang diharapkan (opsional)",
        "ja": "期待するSHA-256（任意）", "ko": "예상 SHA-256(선택 사항)",
        "ru": "Ожидаемый SHA-256 (необязательно)", "th": "SHA-256 ที่คาดไว้ (ไม่บังคับ)",
        "tr": "Beklenen SHA-256 (isteğe bağlı)", "uk": "Очікуваний SHA-256 (необовʼязково)",
        "vi": "SHA-256 mong đợi (tùy chọn)", "zh": "预期的 SHA-256（可选）",
        "ar": "بصمة SHA-256 المتوقعة (اختياري)",
    }),
    ("iptv_tipo_lista", {
        "es": "Lista de canales (M3U)", "en": "Channel list (M3U)", "ca": "Llista de canals (M3U)",
        "pt": "Lista de canais (M3U)", "fr": "Liste de chaînes (M3U)", "id": "Daftar saluran (M3U)",
        "ja": "チャンネルリスト（M3U）", "ko": "채널 목록(M3U)", "ru": "Список каналов (M3U)",
        "th": "รายการช่อง (M3U)", "tr": "Kanal listesi (M3U)", "uk": "Список каналів (M3U)",
        "vi": "Danh sách kênh (M3U)", "zh": "频道列表（M3U）", "ar": "قائمة القنوات (M3U)",
    }),
    ("iptv_tipo_guia", {
        "es": "Guía de programas (XMLTV)", "en": "Programme guide (XMLTV)",
        "ca": "Guia de programes (XMLTV)", "pt": "Guia de programação (XMLTV)",
        "fr": "Guide des programmes (XMLTV)", "id": "Panduan acara (XMLTV)",
        "ja": "番組表（XMLTV）", "ko": "프로그램 가이드(XMLTV)", "ru": "Программа передач (XMLTV)",
        "th": "คู่มือรายการ (XMLTV)", "tr": "Yayın akışı rehberi (XMLTV)",
        "uk": "Програма передач (XMLTV)", "vi": "Lịch chương trình (XMLTV)",
        "zh": "节目指南（XMLTV）", "ar": "دليل البرامج (XMLTV)",
    }),
    ("iptv_anadir_fuente", {
        "es": "Añadir fuente", "en": "Add source", "ca": "Afegeix una font", "pt": "Adicionar fonte",
        "fr": "Ajouter une source", "id": "Tambah sumber", "ja": "ソースを追加", "ko": "소스 추가",
        "ru": "Добавить источник", "th": "เพิ่มแหล่ง", "tr": "Kaynak ekle", "uk": "Додати джерело",
        "vi": "Thêm nguồn", "zh": "添加来源", "ar": "إضافة مصدر",
    }),
    ("iptv_quitar", {
        "es": "Quitar", "en": "Remove", "ca": "Elimina", "pt": "Remover", "fr": "Retirer",
        "id": "Hapus", "ja": "削除", "ko": "제거", "ru": "Удалить", "th": "ลบ", "tr": "Kaldır",
        "uk": "Вилучити", "vi": "Gỡ", "zh": "移除", "ar": "إزالة",
    }),
    ("iptv_cargar", {
        "es": "Cargar", "en": "Load", "ca": "Carrega", "pt": "Carregar", "fr": "Charger",
        "id": "Muat", "ja": "読み込む", "ko": "불러오기", "ru": "Загрузить", "th": "โหลด",
        "tr": "Yükle", "uk": "Завантажити", "vi": "Tải", "zh": "加载", "ar": "تحميل",
    }),
    ("iptv_buscar_canal", {
        "es": "Buscar canal", "en": "Search channels", "ca": "Cerca canals", "pt": "Buscar canal",
        "fr": "Rechercher une chaîne", "id": "Cari saluran", "ja": "チャンネルを検索",
        "ko": "채널 검색", "ru": "Поиск канала", "th": "ค้นหาช่อง", "tr": "Kanal ara",
        "uk": "Пошук каналу", "vi": "Tìm kênh", "zh": "搜索频道", "ar": "البحث عن قناة",
    }),
    ("iptv_reproducir", {
        "es": "Reproducir", "en": "Play", "ca": "Reprodueix", "pt": "Reproduzir", "fr": "Lire",
        "id": "Putar", "ja": "再生", "ko": "재생", "ru": "Воспроизвести", "th": "เล่น",
        "tr": "Oynat", "uk": "Відтворити", "vi": "Phát", "zh": "播放", "ar": "تشغيل",
    }),
    ("iptv_pausa", {
        "es": "Pausa", "en": "Pause", "ca": "Pausa", "pt": "Pausar", "fr": "Pause", "id": "Jeda",
        "ja": "一時停止", "ko": "일시중지", "ru": "Пауза", "th": "หยุดชั่วคราว", "tr": "Duraklat",
        "uk": "Пауза", "vi": "Tạm dừng", "zh": "暂停", "ar": "إيقاف مؤقت",
    }),
    ("iptv_parar", {
        "es": "Parar", "en": "Stop", "ca": "Atura", "pt": "Parar", "fr": "Arrêter",
        "id": "Hentikan", "ja": "停止", "ko": "정지", "ru": "Остановить", "th": "หยุด",
        "tr": "Durdur", "uk": "Зупинити", "vi": "Dừng", "zh": "停止", "ar": "إيقاف",
    }),
    ("iptv_modulo_no_disponible", {
        "es": "El módulo IPTV no está disponible ahora mismo.",
        "en": "The IPTV module is not available right now.",
        "ca": "El mòdul IPTV no està disponible ara mateix.",
        "pt": "O módulo IPTV não está disponível neste momento.",
        "fr": "Le module IPTV nʼest pas disponible pour le moment.",
        "id": "Modul IPTV sedang tidak tersedia.",
        "ja": "IPTVモジュールは現在利用できません。",
        "ko": "IPTV 모듈을 지금은 사용할 수 없습니다.",
        "ru": "Модуль IPTV сейчас недоступен.",
        "th": "โมดูล IPTV ไม่พร้อมใช้งานในขณะนี้",
        "tr": "IPTV modülü şu anda kullanılamıyor.",
        "uk": "Модуль IPTV зараз недоступний.",
        "vi": "Mô-đun IPTV hiện không khả dụng.",
        "zh": "IPTV 模块当前不可用。",
        "ar": "وحدة IPTV غير متاحة في الوقت الحالي.",
    }),
    ("iptv_sin_fuentes", {
        "es": "No hay ninguna fuente instalada.", "en": "No source is installed.",
        "ca": "No hi ha cap font instal·lada.", "pt": "Nenhuma fonte instalada.",
        "fr": "Aucune source installée.", "id": "Tidak ada sumber yang terpasang.",
        "ja": "インストール済みのソースはありません。", "ko": "설치된 소스가 없습니다.",
        "ru": "Источники не установлены.", "th": "ยังไม่ได้ติดตั้งแหล่งใด",
        "tr": "Kurulu kaynak yok.", "uk": "Не встановлено жодного джерела.",
        "vi": "Chưa có nguồn nào được cài đặt.", "zh": "尚未安装任何来源。",
        "ar": "لا يوجد أي مصدر مثبَّت.",
    }),
    ("iptv_canales_cargados", {
        "es": "%1$d canales cargados de %2$s", "en": "%1$d channels loaded from %2$s",
        "ca": "%1$d canals carregats de %2$s", "pt": "%1$d canais carregados de %2$s",
        "fr": "%1$d chaînes chargées depuis %2$s", "id": "%1$d saluran dimuat dari %2$s",
        "ja": "%2$s から %1$d チャンネルを読み込みました", "ko": "%2$s에서 채널 %1$d개 불러옴",
        "ru": "Загружено каналов: %1$d из %2$s", "th": "โหลด %1$d ช่องจาก %2$s",
        "tr": "%2$s kaynağından %1$d kanal yüklendi", "uk": "Завантажено каналів: %1$d із %2$s",
        "vi": "Đã tải %1$d kênh từ %2$s", "zh": "已从 %2$s 加载 %1$d 个频道",
        "ar": "تم تحميل %1$d قناة من %2$s",
    }),
    ("iptv_fuente_anadida", {
        "es": "Fuente añadida: %1$s", "en": "Source added: %1$s", "ca": "Font afegida: %1$s",
        "pt": "Fonte adicionada: %1$s", "fr": "Source ajoutée : %1$s", "id": "Sumber ditambahkan: %1$s",
        "ja": "ソースを追加しました：%1$s", "ko": "소스 추가됨: %1$s", "ru": "Источник добавлен: %1$s",
        "th": "เพิ่มแหล่งแล้ว: %1$s", "tr": "Kaynak eklendi: %1$s", "uk": "Джерело додано: %1$s",
        "vi": "Đã thêm nguồn: %1$s", "zh": "已添加来源：%1$s", "ar": "تمت إضافة المصدر: %1$s",
    }),
    ("iptv_fuente_quitada", {
        "es": "Fuente quitada: %1$s", "en": "Source removed: %1$s", "ca": "Font eliminada: %1$s",
        "pt": "Fonte removida: %1$s", "fr": "Source retirée : %1$s", "id": "Sumber dihapus: %1$s",
        "ja": "ソースを削除しました：%1$s", "ko": "소스 제거됨: %1$s", "ru": "Источник удалён: %1$s",
        "th": "ลบแหล่งแล้ว: %1$s", "tr": "Kaynak kaldırıldı: %1$s", "uk": "Джерело вилучено: %1$s",
        "vi": "Đã gỡ nguồn: %1$s", "zh": "已移除来源：%1$s", "ar": "تمت إزالة المصدر: %1$s",
    }),
    ("iptv_reproduciendo", {
        "es": "Reproduciendo: %1$s", "en": "Playing: %1$s", "ca": "Reproduint: %1$s",
        "pt": "Reproduzindo: %1$s", "fr": "Lecture : %1$s", "id": "Memutar: %1$s",
        "ja": "再生中：%1$s", "ko": "재생 중: %1$s", "ru": "Воспроизводится: %1$s",
        "th": "กำลังเล่น: %1$s", "tr": "Oynatılıyor: %1$s", "uk": "Відтворюється: %1$s",
        "vi": "Đang phát: %1$s", "zh": "正在播放：%1$s", "ar": "قيد التشغيل: %1$s",
    }),
    ("iptv_sin_reproduccion", {
        "es": "Sin reproducción", "en": "Nothing playing", "ca": "Sense reproducció",
        "pt": "Nada em reprodução", "fr": "Aucune lecture", "id": "Tidak ada pemutaran",
        "ja": "再生していません", "ko": "재생 중이지 않음", "ru": "Ничего не воспроизводится",
        "th": "ไม่มีการเล่น", "tr": "Oynatma yok", "uk": "Нічого не відтворюється",
        "vi": "Không phát gì", "zh": "未在播放", "ar": "لا يوجد تشغيل",
    }),
    ("iptv_elige_fuente", {
        "es": "Elige primero una fuente de la lista.", "en": "Select a source from the list first.",
        "ca": "Trieu primer una font de la llista.", "pt": "Selecione primeiro uma fonte da lista.",
        "fr": "Sélectionnez dʼabord une source dans la liste.",
        "id": "Pilih dulu satu sumber dari daftar.", "ja": "まず一覧からソースを選んでください。",
        "ko": "먼저 목록에서 소스를 선택하세요.", "ru": "Сначала выберите источник из списка.",
        "th": "เลือกแหล่งจากรายการก่อน", "tr": "Önce listeden bir kaynak seçin.",
        "uk": "Спершу виберіть джерело зі списку.", "vi": "Trước tiên hãy chọn một nguồn trong danh sách.",
        "zh": "请先从列表中选择一个来源。", "ar": "اختر أولًا مصدرًا من القائمة.",
    }),
    ("iptv_elige_canal", {
        "es": "Elige un canal de la lista.", "en": "Select a channel from the list.",
        "ca": "Trieu un canal de la llista.", "pt": "Selecione um canal da lista.",
        "fr": "Sélectionnez une chaîne dans la liste.", "id": "Pilih satu saluran dari daftar.",
        "ja": "一覧からチャンネルを選んでください。", "ko": "목록에서 채널을 선택하세요.",
        "ru": "Выберите канал из списка.", "th": "เลือกช่องจากรายการ",
        "tr": "Listeden bir kanal seçin.", "uk": "Виберіть канал зі списку.",
        "vi": "Hãy chọn một kênh trong danh sách.", "zh": "请从列表中选择一个频道。",
        "ar": "اختر قناة من القائمة.",
    }),
]


def escapar(texto):
    """Lo que necesita un recurso de Android para no romper aapt2."""
    t = texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = t.replace("\\'", "'").replace('\\"', '"')      # por si venía ya escapado
    t = t.replace("'", "\\'").replace('"', '\\"')
    assert '"' not in t.replace('\\"', ""), "comilla sin escapar: " + texto
    return t
