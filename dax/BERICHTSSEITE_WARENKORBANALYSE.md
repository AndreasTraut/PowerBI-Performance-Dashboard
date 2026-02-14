# 📊 Berichtsseite „Warenkorbanalyse" – Dokumentation

> ➡️ **Details siehe:** [WARENKORBANALYSE.md](/dax/WARENKORBANALYSE.md) / Zusammenfassung ( [DE](/dax/IMPLEMENTIERUNGS_ZUSAMMENFASSUNG.md) / [EN](/dax/IMPLEMENTATION_SUMMARY.md) )  
> 📖 **Implementierung:** [Orders_containing_both.dax](/dax/Orders_containing_both.dax)  
> 💾 **Modul:** `Performance Dashboard.Report/definition/pages/6385cf1f12bf4fe9b4e1/`

---

## 🚀 Überblick

Dieses Dokument beschreibt die Erstellung einer neuen Berichtsseite **„Warenkorbanalyse"** im Power BI Performance Dashboard. Die Seite wurde im PBIP-Format (Power BI Project) als JSON-Konfiguration erstellt und visualisiert die Warenkorbanalyse-Kennzahlen (Market Basket Analysis) aus dem `/dax`-Verzeichnis.

Die Berichtsseite ist farbenfroh und ansprechend gestaltet, mit einem dunklen Header, farbcodierten KPI-Karten und einer klaren visuellen Struktur.

---

## 📋 Was wurde gemacht?

### 1. Neue Berichtsseite erstellt

Eine neue Seite wurde im PBIP-Projektformat angelegt:

```
Performance Dashboard.Report/
└── definition/
    └── pages/
        └── 6385cf1f12bf4fe9b4e1/   ← Neue Seite „Warenkorbanalyse"
            ├── page.json            ← Seitendefinition
            └── visuals/             ← 31 Visual-Definitionen
                ├── 9ed0d8abe17b4e72a492/visual.json
                ├── cd1a302a66dd4e3ab46b/visual.json
                ├── ...
                └── fb3abe0ec47a4758a442/visual.json
```

### 2. Seite in `pages.json` registriert

Die Datei `Performance Dashboard.Report/definition/pages/pages.json` wurde aktualisiert:

- Die neue Seite wurde in die `pageOrder`-Liste eingefügt (vor „Page 1")
- `activePageName` wurde auf die neue Seite gesetzt

### 3. Seiteneinstellungen (`page.json`)

| Eigenschaft     | Wert                        |
|-----------------|----------------------------|
| **displayName** | `Warenkorbanalyse`         |
| **displayOption** | `FitToPage`              |
| **Breite**      | 2240 px                    |
| **Höhe**        | 1420 px                    |
| **Hintergrund** | Hellblau-grau (`#F0F4F8`)  |

---

## 🎨 Seitenlayout und Design

### Farbschema

Die Seite verwendet ein buntes, ansprechendes Farbschema:

| Bereich                    | Farbe       | Hex-Code   |
|---------------------------|-------------|-----------|
| 🔵 Header-Hintergrund     | Dunkles Navy | `#1B2A4A` |
| 🔴 Orders containing both | Korallrot   | `#FF6B6B` |
| 🟢 Co-occurrence Rate     | Türkis/Teal | `#4ECDC4` |
| 🟡 Lift                   | Gelb        | `#FFE66D` |
| 🟩 Support %              | Mintgrün    | `#A8E6CF` |
| 🟣 Jaccard Similarity     | Pflaume     | `#DDA0DD` |
| 🔵 Product Pair           | Himmelblau  | `#87CEEB` |
| ⬜ Seitenhintergrund      | Hellblau-grau | `#F0F4F8` |
| ⬜ Karten/Container       | Weiß        | `#FFFFFF` |

### Layout-Bereiche

```
┌──────────────────────────────────────────────────────────────┐
│  🔵 HEADER: 🛒 Warenkorbanalyse                             │
│     Market Basket Analysis | Welche Produkte werden ...      │
├──────────────────────────────────────────────────────────────┤
│  🔴 Orders  🟢 Co-occ.  🟡 Lift  🟩 Support  🟣 Jaccard  🔵 Pair │
│  (KPI)      (KPI)       (KPI)    (KPI)       (KPI)    (KPI) │
├─────────┬──────────────────────┬─────────────────────────────┤
│ 🔍 Filter│ 📊 Produkt-Affinitäts│ 🏆 Top Produkt-             │
│ Produkt  │    Matrix            │    Kombinationen            │
│ Vergl.   │ (pivotTable)         │ (Balkendiagramm)            │
│ Kategorie│                      │                             │
├─────────┴──────────────────────┼─────────────────────────────┤
│ 📋 Detaillierte Kennzahlen     │ 🎯 Assoziationsmetriken     │
│ (Tabelle mit 7 Spalten)        │ Orders Prod 1/2, Confidence │
│                                │ Reverse Co-occ., Is Strong  │
│                                │ 📄 Page Navigator           │
└────────────────────────────────┴─────────────────────────────┘
```

---

## 📦 Erstellte Visuals (31 Stück)

### 🎨 Header & Design-Elemente (7 Visuals)

| Visual-ID                | Typ       | Beschreibung                                                |
|--------------------------|-----------|-------------------------------------------------------------|
| `9ed0d8abe17b4e72a492`   | shape     | Header-Hintergrund (dunkles Navy `#1B2A4A`, volle Breite)   |
| `cd1a302a66dd4e3ab46b`   | textbox   | Titel: „🛒 Warenkorbanalyse" (weiß, 28pt, fett)            |
| `8757e898697a4c3d9fe7`   | textbox   | Untertitel: „Market Basket Analysis \| Welche Produkte..." (weiß, 14pt) |
| `64a38b33c6f740cbb2ea`   | shape     | Filter-Bereich Hintergrund (weiß, abgerundet, Schatten)    |
| `b0280cbac25d4537b76c`   | shape     | Matrix-Bereich Hintergrund (weiß, abgerundet, Schatten)    |
| `b5ada2a7612845199296`   | shape     | Balkendiagramm-Bereich Hintergrund (weiß, abgerundet)      |
| `4a8e29c0f9a94a80a6db`   | shape     | Detailtabelle-Bereich Hintergrund (weiß, abgerundet)       |
| `cda9dcebcfe243f7a7e3`   | shape     | Metriken-Bereich Hintergrund (weiß, abgerundet)            |

### 📈 KPI-Karten – Obere Zeile (6 Visuals)

| Visual-ID                | Measure                  | Randfarbe  | Beschreibung                                    |
|--------------------------|--------------------------|------------|------------------------------------------------|
| `cf6becf4004c44c8b828`   | Orders containing both   | `#FF6B6B`  | Anzahl Bestellungen mit beiden Produkten        |
| `4ba56e065b5740518d0e`   | Co-occurrence Rate %     | `#4ECDC4`  | Wie oft Produkt 2 bei Produkt 1 vorkommt        |
| `fb3abe0ec47a4758a442`   | Lift                     | `#FFE66D`  | Stärke der Assoziation (>1 = stark)             |
| `abb427f35ac9460fbe67`   | Support %                | `#A8E6CF`  | Anteil aller Bestellungen mit diesem Paar       |
| `9f6fac8349d9412a96b7`   | Jaccard Similarity %     | `#DDA0DD`  | Alternative Ähnlichkeitsmetrik                  |
| `6e92decba134425f85ce`   | Product Pair             | `#87CEEB`  | Lesbare Bezeichnung des Produktpaars            |

### 🔍 Filter / Datenschnitte (3 Visuals)

| Visual-ID                | Feld                                   | Beschreibung                        |
|--------------------------|----------------------------------------|-------------------------------------|
| `41b339c5545d45708e86`   | `dim_product[ProductName]`             | Produkt-Auswahl (Dropdown)          |
| `336095fb5d2d41a69ab1`   | `dim_product_comparison[ProductName]`  | Vergleichsprodukt-Auswahl (Dropdown)|
| `cdba3211cde24f4b9f10`   | `dim_product[Category]`               | Kategorie-Filter (Dropdown)         |

### 📊 Datenvisualisierungen (3 Visuals)

| Visual-ID                | Typ               | Beschreibung                                                          |
|--------------------------|--------------------|----------------------------------------------------------------------|
| `a10bed135a374e44a631`   | pivotTable         | Produkt-Affinitäts-Matrix (Zeilen: Produkt, Spalten: Vergleichsprodukt, Werte: Orders containing both) |
| `68de5e84c57d4a888049`   | clusteredBarChart  | Top Produkt-Kombinationen (Balkendiagramm, korallrot `#FF6B6B`)      |
| `1ef3de6e950f474a9335`   | tableEx            | Detail-Tabelle mit 7 Spalten (ProductName, Vergleichsprodukt, Orders, Co-occurrence, Lift, Support, Is Strong Association) |

### 🎯 Zusätzliche Metrik-Karten (5 Visuals)

| Visual-ID                | Measure                       | Randfarbe  | Beschreibung                            |
|--------------------------|-------------------------------|------------|----------------------------------------|
| `cb2a005312cd45c3ac18`   | Orders with Product 1         | `#FF6B6B`  | Bestellungen mit Produkt 1 (Basis)      |
| `7626ec5f53b547ce9aca`   | Orders with Product 2         | `#4ECDC4`  | Bestellungen mit Produkt 2 (Basis)      |
| `9bb3a2e342b64a8b9ae3`   | Confidence %                  | `#FFE66D`  | Konfidenz der Assoziation               |
| `4880d6fc58fc4c1bb95d`   | Reverse Co-occurrence Rate %  | `#DDA0DD`  | Rückwärts-Co-occurrence (Prod 2 → 1)    |
| `05dbe8576bd24e3c8178`   | Is Strong Association         | `#A8E6CF`  | Starke Assoziation (Ja/Nein)            |

### 📝 Bereichstitel & Navigation (4 Visuals)

| Visual-ID                | Typ            | Text / Funktion                       |
|--------------------------|----------------|---------------------------------------|
| `23041c4717c94f709f38`   | textbox        | „🔍 Filter" (Filterbereich-Überschrift) |
| `080980d3840a47bda0e4`   | textbox        | „📊 Produkt-Affinitäts-Matrix"          |
| `4e63fe635196472fb4d7`   | textbox        | „🏆 Top Produkt-Kombinationen"          |
| `138e9714dabe401e97f7`   | textbox        | „📋 Detaillierte Kennzahlen"            |
| `83c4b76dc7c943f6a616`   | textbox        | „🎯 Assoziationsmetriken"               |
| `6d2ad477c0124a4298c1`   | pageNavigator  | Seitennavigation (vertikal, 12pt)       |

---

## 🔧 Technische Details

### Verwendete Measures (aus `KPI_Summary_Table`)

Alle KPI-Karten und Datenvisuals referenzieren Measures aus der Entität `KPI_Summary_Table`:

| Measure                       | Verwendung                                   |
|-------------------------------|----------------------------------------------|
| Orders containing both        | KPI-Karte, Matrix, Balkendiagramm, Tabelle   |
| Co-occurrence Rate %          | KPI-Karte, Tabelle                           |
| Lift                          | KPI-Karte, Tabelle                           |
| Support %                     | KPI-Karte, Tabelle                           |
| Jaccard Similarity %          | KPI-Karte                                    |
| Product Pair                  | KPI-Karte                                    |
| Orders with Product 1         | Metrik-Karte                                 |
| Orders with Product 2         | Metrik-Karte                                 |
| Confidence %                  | Metrik-Karte                                 |
| Reverse Co-occurrence Rate %  | Metrik-Karte                                 |
| Is Strong Association         | Metrik-Karte, Tabelle                        |

### Verwendete Datenfelder

| Entität                     | Feld            | Verwendung                              |
|-----------------------------|-----------------|-----------------------------------------|
| `dim_product`               | `ProductName`   | Matrix-Zeilen, Tabelle, Slicer          |
| `dim_product`               | `Category`      | Kategorie-Slicer                        |
| `dim_product_comparison`    | `ProductName`   | Matrix-Spalten, Tabelle, Slicer, Balken |

### PBIP-Dateien – Gesamtüberblick der Änderungen

| Datei                                          | Aktion     | Beschreibung                      |
|------------------------------------------------|------------|-----------------------------------|
| `pages/pages.json`                             | Geändert   | Neue Seite registriert            |
| `pages/6385cf1f12bf4fe9b4e1/page.json`         | Erstellt   | Seitendefinition                  |
| `pages/6385cf1f12bf4fe9b4e1/visuals/*/visual.json` | Erstellt | 31 Visual-Definitionen            |

**Gesamt:** 32 neue Dateien + 1 geänderte Datei

---

## 📐 Seitenstruktur im Detail

### Positionierung der Hauptbereiche

| Bereich                     | Position (x, y)  | Größe (B × H)  |
|-----------------------------|-------------------|-----------------|
| Header-Hintergrund          | (0, 0)            | 2240 × 120      |
| Titel                       | (80, 20)          | 700 × 50        |
| Untertitel                  | (80, 70)          | 900 × 35        |
| KPI-Karten (6 Stück)       | (80–1880, 150)    | je 330 × 120    |
| Filter-Panel                | (40, 300)         | 280 × 400       |
| Matrix                      | (350, 300)        | 900 × 530       |
| Balkendiagramm              | (1280, 300)       | 930 × 530       |
| Detail-Tabelle              | (40, 860)         | 1070 × 530      |
| Metriken-Panel              | (1140, 860)       | 1070 × 530      |
| Page Navigator              | (1880, 870)       | 170 × 500       |

---

## ✅ Zusammenfassung

Die neue Berichtsseite „Warenkorbanalyse" bietet:

- 🎨 **Buntes, ansprechendes Design** mit farbcodierten KPI-Karten und dunklem Header
- 📊 **Interaktive Analyse** durch 3 Dropdown-Datenschnitte (Produkt, Vergleichsprodukt, Kategorie)
- 📈 **11 Kennzahlen** aus der Market Basket Analysis (Orders, Co-occurrence, Lift, Support, Jaccard, Confidence, etc.)
- 🔢 **Produkt-Affinitäts-Matrix** zur Visualisierung von Produktkombinationen
- 📊 **Balkendiagramm** für die Top-Produkt-Kombinationen
- 📋 **Detail-Tabelle** mit 7 Spalten für tiefere Analyse
- 📄 **Seitennavigation** zur einfachen Navigation im Dashboard

### Nächste Schritte

1. ✅ PBIP-Datei in Power BI Desktop öffnen
2. ✅ Prüfen, ob `dim_product_comparison` und alle Measures im Modell existieren
3. ✅ Berichtsseite „Warenkorbanalyse" testen
4. ✅ Datenschnitte und Filter ausprobieren

---

> 💡 **Hinweis:** Diese Berichtsseite wurde vollständig im PBIP-Format (Power BI Project) als JSON-Konfiguration erstellt. Zum Anzeigen muss die Datei `Performance Dashboard.pbip` in Power BI Desktop geöffnet werden.

---

*Erstellt im Rahmen der Warenkorbanalyse-Implementierung für das Power BI Performance Dashboard.*
