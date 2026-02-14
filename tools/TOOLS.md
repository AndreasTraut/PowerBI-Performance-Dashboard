# 🔧 Python Tools - Dokumentation

Diese Dokumentation beschreibt die Python-Skripte im Verzeichnis `/tools`, die zur Datenextraktion und -generierung für das Power BI Performance Dashboard entwickelt wurden.

> ➡️ **Details siehe:** [Repository-Evolution im README](README.md#-projektübersicht--status)  
> 💾 **Verzeichnis:** `/tools`  
> 📖 **Anforderungen:** `requirements.txt`

---

## 📋 Inhaltsverzeichnis

- [Übersicht der Tools](#-übersicht-der-tools)
- [Installation & Setup](#-installation--setup)
- [Tool-Beschreibungen](#-tool-beschreibungen)
  - [generate_sample_data.py](#1-generate_sample_datapy)
  - [extract_pbix_data.py](#2-extract_pbix_datapy)
  - [extract_pbix_actual.py](#3-extract_pbix_actualpy)
  - [extract_actual_data.py](#4-extract_actual_datapy)
- [Verwendungsbeispiele](#-verwendungsbeispiele)
- [Troubleshooting](#-troubleshooting)

---

## 🚀 Übersicht der Tools

Das Verzeichnis `/tools` enthält vier Python-Skripte mit unterschiedlichen Zwecken:

| Skript | Zweck | Status | Empfehlung |
|--------|-------|--------|------------|
| **generate_sample_data.py** | Generiert Beispieldaten im CSV-Format | ✅ Voll funktionsfähig | ⭐ **Empfohlen** |
| **extract_pbix_data.py** | Basisversion der PBIX-Extraktion | ⚠️ Eingeschränkt | Informativ |
| **extract_pbix_actual.py** | Erweiterte PBIX-Analyse mit Hilfe-Skripten | ⚠️ Eingeschränkt | Informativ |
| **extract_actual_data.py** | Versuch mit .NET Analysis Services | ⚠️ Experimental | Nicht empfohlen |

### 🎯 Kernaussage

**Die PBIX-Datenextraktion ist durch das proprietäre XPress9-Kompressionsformat von Microsoft technisch eingeschränkt.** Daher ist das **generate_sample_data.py**-Skript der empfohlene Weg, um mit strukturierten Daten zu arbeiten, die dem Dashboard-Schema entsprechen.

Für die Extraktion **echter Daten** aus der PBIX-Datei sollten Sie stattdessen spezialisierte Tools wie **DAX Studio** oder **Tabular Editor** verwenden (siehe [data/DATA.md](data/DATA.md)).

---

## 🔧 Installation & Setup

### Voraussetzungen

- **Python 3.7+** (empfohlen: Python 3.9 oder höher)
- **pip** (Python Package Manager)

### Schritt-für-Schritt Installation

#### 1. Repository klonen (falls noch nicht geschehen)

```bash
git clone https://github.com/AndreasTraut/PowerBI-Performance-Dashboard.git
cd PowerBI-Performance-Dashboard
```

#### 2. Virtuelle Umgebung erstellen (optional, aber empfohlen)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Abhängigkeiten installieren

```bash
cd tools
pip install -r requirements.txt
```

**Inhalt von `requirements.txt`:**
```
pandas
numpy
```

Für die experimentellen Extraktions-Skripte werden zusätzliche Bibliotheken erwähnt (aber nicht zwingend erforderlich):
- `pythonnet` (für .NET-Integration, nur Windows)
- `lz4` (für Kompression)
- `zstandard` (für Kompression)

Diese werden **nicht** in `requirements.txt` aufgeführt, da sie nicht für die empfohlene Nutzung benötigt werden.

---

## 📖 Tool-Beschreibungen

### 1. `generate_sample_data.py`

> ⭐ **Empfohlen**: Dieses Skript ist der zuverlässigste Weg, um mit Daten zu arbeiten.

#### 📝 Beschreibung

Generiert **synthetische Beispieldaten**, die exakt dem Schema des Power BI Performance Dashboards entsprechen. Die Daten sind realistisch strukturiert und enthalten:

- **Dimensionstabellen**: Kunden, Produkte, Geografie, Datum
- **Faktentabellen**: Verkäufe (Sales), Bestellungen (Orders), Rücksendungen (Returns)
- **Referenzielle Integrität**: Alle Fremdschlüssel-Beziehungen sind korrekt verknüpft
- **Reproduzierbarkeit**: Verwendet feste Random Seeds für konsistente Ergebnisse

#### 🎯 Anwendungsfälle

- Testen des Dashboards mit vollständigen Daten
- Entwicklung ohne Zugriff auf Power BI Desktop
- Externe Analysen mit Python/R/SQL
- Schulungs- und Demonstrationszwecke
- Prototyping neuer Dashboard-Features

#### 🔧 Verwendung

**Syntax:**
```bash
python generate_sample_data.py [output_directory]
```

**Parameter:**
- `output_directory` (optional): Zielverzeichnis für CSV-Dateien
  - **Standard**: `./data` (relativ zum Skript-Verzeichnis)

**Beispiele:**

```bash
# Standardausgabe in ./data
python generate_sample_data.py

# Benutzerdefiniertes Verzeichnis
python generate_sample_data.py /tmp/powerbi_data

# Windows-Pfad
python generate_sample_data.py C:\Users\YourName\Documents\PowerBI_Data
```

#### 📊 Generierte Dateien

| Datei | Beschreibung | Zeilen |
|-------|-------------|--------|
| `dim_date.csv` | Datumsdimension 2022-2024 | ~1.096 |
| `dim_geography.csv` | 13 Länder in 3 Regionen | 13 |
| `dim_product.csv` | Produkte mit Kategorien/Marken | 160 |
| `dim_customer.csv` | Kundenstammdaten | 5.000 |
| `fact_orders.csv` | Bestellpositionen | ~50.000+ |
| `fact_sales.csv` | Aggregierte Verkäufe | ~50.000 |
| `fact_returns.csv` | Rücksendungen (~5% der Bestellungen) | ~2.500 |

#### 🔍 Datenmerkmale

**Dimensionen:**
- **Datumsdimension**: 2022-01-01 bis 2024-12-31 mit allen Kalenderhierarchien (Jahr, Quartal, Monat, Woche, Tag)
- **Geografie**: Americas, Europe, Asia mit 13 Ländern
- **Produkte**: 4 Hauptkategorien (Electronics, Home & Garden, Sports & Outdoors, Clothing) mit je 4 Unterkategorien
- **Kunden**: B2B/B2C-Mix mit Prioritäts-Levels und verschiedenen Kanälen

**Transaktionsdaten:**
- **Bestellungen**: Mehrere Positionen pro Bestellung, realistische Preisschwankungen
- **Status**: Completed, Cancelled, Pending, Processing
- **Lieferstatus**: On-Time, Late, Early
- **Rücksendungen**: 8 verschiedene Rückgabegründe (Defective, Wrong Item, etc.)

#### 💻 Code-Struktur

Das Skript ist modular aufgebaut:

```python
generate_date_dimension()      # Erstellt Kalendertabelle
generate_geography_dimension()  # Erstellt Geografiedimension
generate_product_dimension()    # Erstellt Produktkatalog
generate_customer_dimension()   # Erstellt Kundenstammdaten
generate_fact_orders()          # Erstellt Bestelldaten
generate_fact_returns()         # Erstellt Rücksendungen
```

Jede Funktion gibt ein Pandas DataFrame zurück, das dann als CSV gespeichert wird.

---

### 2. `extract_pbix_data.py`

> ℹ️ **Informativ**: Zeigt die Grundlagen der PBIX-Struktur, aber begrenzte Datenextraktion.

#### 📝 Beschreibung

Basisversion eines Extraktions-Tools, das die **Struktur einer PBIX-Datei** analysiert. PBIX-Dateien sind ZIP-Archive, die verschiedene Komponenten enthalten:

- `DataModel`: Komprimiertes Datenmodell (XPress9)
- `Report/`: Visuals und Layout-Definitionen
- `SecurityBindings`: Sicherheitseinstellungen
- `Metadata`: Metadaten

**Limitation**: Kann die eigentlichen Daten nicht extrahieren, da das `DataModel` mit proprietärer Microsoft XPress9-Kompression verschlüsselt ist.

#### 🔧 Verwendung

```bash
python extract_pbix_data.py <pbix-file> <output-directory>
```

**Beispiel:**
```bash
python extract_pbix_data.py "../Performance Dashboard.pbix" /tmp/pbix_analysis
```

#### 📋 Ausgabe

Das Skript:
1. Extrahiert die PBIX-Datei (als ZIP) in ein temporäres Verzeichnis
2. Listet alle enthaltenen Dateien mit Größen auf
3. Identifiziert das DataModel und zeigt dessen Größe
4. Erklärt die Einschränkungen und empfiehlt Alternativen

**Empfohlene Alternativen** (werden im Output angezeigt):
- Power BI Desktop: Manueller Datenexport
- Tabular Editor 2: Skript-basierter Export
- DAX Studio: DAX-Queries zum Datenexport

---

### 3. `extract_pbix_actual.py`

> ℹ️ **Informativ**: Erweiterte Analyse mit hilfreichen Extraktions-Anleitungen.

#### 📝 Beschreibung

Erweiterte Version des Extraktionsversuchs, die mehrere Ansätze kombiniert:

1. **Strukturanalyse**: Untersucht PBIX-Inhalte und Header
2. **Dekompressionsversuche**: Testet verschiedene Algorithmen (lz4, zstandard)
3. **BIM-Datei-Suche**: Sucht nach unkomprimierten Modelldefinitionen
4. **Hilfs-Skripte**: Generiert PowerShell-Skripte für Windows-Benutzer

Das Skript erkennt XPress9-Kompression und bietet **Cross-Platform-Lösungen** an.

#### 🔧 Verwendung

```bash
python extract_pbix_actual.py <pbix-file> <output-directory>
```

**Beispiel:**
```bash
python extract_pbix_actual.py "../Performance Dashboard.pbix" ./extracted_data
```

#### 📋 Ausgabe

Das Skript erstellt:

1. **EXTRACTION_INSTRUCTIONS.txt**: Allgemeine Anleitungen für alle Plattformen
2. **extract_with_te3.ps1**: PowerShell-Skript für Windows mit Tabular Editor 3

**Analyseschritte:**
```
1. Extracting PBIX archive...
   ✓ Extracted to: /tmp/pbix_extract_xxx
   
2. Searching for model files...
   
3. Analyzing DataModel...
   Size: xxx bytes
   First 100 bytes: ...
   
4. Attempting decompression...
   ✗ Standard decompression methods failed
   
5. Generating helper scripts...
   ✓ PowerShell script: extract_with_te3.ps1
   ✓ Instructions: EXTRACTION_INSTRUCTIONS.txt
```

#### 🔍 Technische Details

**Versuchte Dekomprimierungsmethoden:**
- **LZ4**: Ähnlich zu XPress in einigen Fällen
- **Zstandard**: Moderner Kompressionsalgorithmus

Beide scheitern bei XPress9, da es ein proprietäres Microsoft-Format ist.

**Empfohlene Tools in der Ausgabe:**
- DAX Studio (https://daxstudio.org/)
- Tabular Editor 2/3 (https://tabulareditor.com/)
- Power BI Desktop (Manueller Export)

---

### 4. `extract_actual_data.py`

> ⚠️ **Experimental**: Versuch mit .NET-Bibliotheken, nicht für Produktivnutzung geeignet.

#### 📝 Beschreibung

Experimentelles Skript, das versucht, **Microsoft Analysis Services .NET-Bibliotheken** über `pythonnet` zu nutzen. Dies würde theoretisch direkten Zugriff auf das Tabellenmodell ermöglichen.

**Herausforderungen:**
1. Erfordert `pythonnet` (nur Windows, komplexe Installation)
2. Benötigt Microsoft.AnalysisServices.Tabular DLL
3. DataModel muss erst dekomprimiert werden (XPress9-Problem)
4. Plattformspezifisch (Windows-only)

#### 🔧 Verwendung

```bash
python extract_actual_data.py <pbix-file> <output-directory>
```

**Hinweis**: Funktioniert nicht out-of-the-box, da .NET-Bibliotheken fehlen.

#### 📋 Erwartete Ausgabe

```
Error loading Analysis Services: ...
Analysis Services DLL not found in common locations.

ALTERNATIVE SOLUTION REQUIRED
========================================
The DataModel in PBIX uses Microsoft XPress9 compression.

1. Use Power BI Desktop (Recommended):
   - Open: 'Performance Dashboard.pbix'
   - Transform data -> Transform data
   - Right-click on each table -> Advanced Editor

2. Use DAX Studio (Free tool):
   - Download from: https://daxstudio.org/
   - Connect to the PBIX file
   - Run: EVALUATE 'TableName'
   - Export to CSV
   
[weitere Alternativen...]
```

#### 🚫 Warum nicht empfohlen?

- **Komplexe Abhängigkeiten**: Erfordert .NET-Bibliotheken
- **Plattform-Lock-in**: Nur Windows
- **Nicht zuverlässig**: Selbst mit allen Bibliotheken scheitert es an XPress9
- **Bessere Alternativen**: DAX Studio und Tabular Editor sind ausgereifter

---

## 💡 Verwendungsbeispiele

### Szenario 1: Schnellstart mit Beispieldaten

**Ziel**: Dashboard testen ohne Power BI Desktop

```bash
# 1. In das tools-Verzeichnis wechseln
cd tools

# 2. Beispieldaten generieren
python generate_sample_data.py

# 3. Ausgabe prüfen
ls -lh data/
```

**Ergebnis**: CSV-Dateien im `./data` Verzeichnis, bereit zum Import in Power BI, Excel, Python, etc.

---

### Szenario 2: Daten für externe Python-Analyse

**Ziel**: Daten in einem Jupyter Notebook analysieren

```bash
# Daten in spezifisches Verzeichnis generieren
python generate_sample_data.py ~/jupyter_projects/powerbi_analysis
```

**Dann in Jupyter:**
```python
import pandas as pd

# Daten laden
customers = pd.read_csv('dim_customer.csv')
orders = pd.read_csv('fact_orders.csv')

# Analysen durchführen
top_customers = orders.groupby('CustomerKey')['LineTotal'].sum().sort_values(ascending=False).head(10)
print(top_customers)
```

---

### Szenario 3: PBIX-Struktur untersuchen

**Ziel**: Verstehen, was in der PBIX-Datei enthalten ist

```bash
# Basis-Analyse
python extract_pbix_data.py "../Performance Dashboard.pbix" /tmp/pbix_info

# Erweiterte Analyse mit Dekompressionsversuchen
python extract_pbix_actual.py "../Performance Dashboard.pbix" /tmp/pbix_detailed
```

**Ergebnis**: Informationen über PBIX-Struktur und Anleitungen zur Datenextraktion

---

### Szenario 4: Automatisierte Datenbereitstellung

**Ziel**: Regelmäßig frische Testdaten generieren (z.B. für CI/CD)

```bash
#!/bin/bash
# generate_test_data.sh

OUTPUT_DIR="./test_data_$(date +%Y%m%d)"
cd tools
python generate_sample_data.py "$OUTPUT_DIR"

echo "Test data generated in: $OUTPUT_DIR"
ls -lh "$OUTPUT_DIR"
```

Ausführen:
```bash
chmod +x generate_test_data.sh
./generate_test_data.sh
```

---

## 🔍 Troubleshooting

### Problem 1: `ModuleNotFoundError: No module named 'pandas'`

**Ursache**: Abhängigkeiten nicht installiert

**Lösung**:
```bash
cd tools
pip install -r requirements.txt
```

Falls `pip` nicht gefunden wird:
```bash
# Windows
python -m pip install -r requirements.txt

# macOS/Linux
python3 -m pip install -r requirements.txt
```

---

### Problem 2: `Permission denied` beim Schreiben der CSV-Dateien

**Ursache**: Keine Schreibrechte im Zielverzeichnis

**Lösung**:
```bash
# 1. Anderes Verzeichnis verwenden
python generate_sample_data.py /tmp/data

# 2. Oder Berechtigungen anpassen (Linux/macOS)
chmod -R 755 data/

# 3. Oder als Administrator ausführen (Windows)
# PowerShell als Administrator öffnen
```

---

### Problem 3: Generierte Daten entsprechen nicht den Erwartungen

**Ursache**: Random Seed kann in verschiedenen Pandas-Versionen variieren

**Lösung**:
```bash
# Pandas-Version prüfen
pip show pandas

# Falls zu alt, aktualisieren
pip install --upgrade pandas numpy
```

**Anpassen des Skripts** (optional):
```python
# In generate_sample_data.py, Zeile 17-18
random.seed(42)      # Für reproduzierbare Namen, Kategorien
np.random.seed(42)   # Für reproduzierbare Zahlen

# Ändern zu einem anderen Seed für andere Daten
random.seed(123)
np.random.seed(123)
```

---

### Problem 4: Extraktions-Skripte funktionieren nicht

**Ursache**: XPress9-Kompression ist nicht unterstützt

**Lösung**: Verwenden Sie die **empfohlenen alternativen Tools**:

#### ✅ DAX Studio (Kostenlos, am einfachsten)

1. Download: https://daxstudio.org/
2. Installation: Standard-Setup
3. PBIX öffnen in Power BI Desktop
4. DAX Studio starten, mit PBIX verbinden
5. Tabellen exportieren:
   ```dax
   EVALUATE 'dim_customer'
   ```
6. Export → Data → CSV

#### ✅ Tabular Editor 2 (Kostenlos, für Fortgeschrittene)

1. Download: https://github.com/TabularEditor/TabularEditor/releases
2. File → Open → From File → PBIX auswählen
3. Advanced Scripting für Datenexport

#### ✅ Power BI Desktop (Immer verfügbar)

1. PBIX öffnen
2. Daten transformieren (öffnet Power Query Editor)
3. Jede Tabelle: Rechtsklick → "Advanced Editor" oder Export

---

### Problem 5: `UnicodeDecodeError` beim Lesen/Schreiben

**Ursache**: Encoding-Probleme mit Umlauten oder Sonderzeichen

**Lösung**:
```python
# CSV lesen mit explizitem Encoding
df = pd.read_csv('dim_product.csv', encoding='utf-8')

# CSV schreiben mit UTF-8
df.to_csv('output.csv', encoding='utf-8', index=False)
```

Falls das Skript selbst betroffen ist, Zeile 1 prüfen:
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

---

### Problem 6: Sehr langsame Ausführung von `generate_sample_data.py`

**Ursache**: Große Datenmengen (Standard: 50.000 Bestellungen)

**Lösung**: Anzahl reduzieren (Skript anpassen):
```python
# Zeile 277 in generate_sample_data.py
fact_orders = generate_fact_orders(dim_customer, dim_product, dim_date, n_orders=10000)  # statt 50000

# Zeile 271 für weniger Kunden
dim_customer = generate_customer_dimension(n_customers=1000)  # statt 5000
```

**Oder**: Parallel-Ausführung nicht starten, falls noch andere Programme laufen.

---

## 📚 Weiterführende Ressourcen

### Offizielle Dokumentation

- **Pandas**: https://pandas.pydata.org/docs/
- **NumPy**: https://numpy.org/doc/
- **Power BI**: https://docs.microsoft.com/power-bi/

### Empfohlene Tools für PBIX-Arbeit

| Tool | Link | Zweck |
|------|------|-------|
| DAX Studio | https://daxstudio.org/ | DAX-Queries & Datenexport |
| Tabular Editor 2 | https://tabulareditor.com/ | Modell-Bearbeitung & Skripting |
| Power BI Desktop | https://powerbi.microsoft.com/desktop/ | Dashboard-Entwicklung |

### Repository-Dokumentation

- **[data/DATA.md](data/DATA.md)**: Detaillierte Extraktionsanleitungen
- **[doc/MODEL_DOKUMENTATION.md](doc/MODEL_DOKUMENTATION.md)**: Datenmodell-Dokumentation
- **[README.md](README.md)**: Projekt-Übersicht

---

## ❓ Häufig gestellte Fragen (FAQ)

### Warum funktioniert die direkte PBIX-Extraktion nicht?

Power BI verwendet **Microsoft XPress9**, eine proprietäre Kompression, die nicht durch Standard-Python-Bibliotheken unterstützt wird. Microsoft stellt keine öffentlichen APIs zur Dekompression bereit.

### Sind die generierten Beispieldaten realistisch?

Ja, die Daten sind **strukturell korrekt** und folgen realistischen Geschäftsregeln:
- Zeitliche Konsistenz (Rücksendungen nach Bestellungen)
- Referenzielle Integrität (alle FKs valide)
- Realistische Verteilungen (z.B. 5% Rücksendequote)

Jedoch sind die **Werte synthetisch** und nicht aus echten Geschäftsdaten abgeleitet.

### Kann ich die Skripte für eigene Dashboards anpassen?

**Ja!** Alle Skripte sind Open Source. Passen Sie einfach die Dimensionen und Faktentabellen in `generate_sample_data.py` an:

```python
# Eigene Produktkategorien
categories = ['Eigene Kategorie 1', 'Eigene Kategorie 2']

# Eigene Geografie
geographies = [
    {'GeographyKey': 1, 'Country': 'Österreich', 'Region': 'DACH'},
    # ...
]
```

### Unterstützen die Skripte auch Power BI Service?

Die **Extraktions-Skripte** arbeiten nur mit lokalen PBIX-Dateien. Für Power BI Service verwenden Sie den integrierten "Daten exportieren"-Button in den Visuals.

Das **Generierungs-Skript** (`generate_sample_data.py`) ist unabhängig und kann überall eingesetzt werden.

### Welches Python-Version wird mindestens benötigt?

- **Minimum**: Python 3.7
- **Empfohlen**: Python 3.9+
- **Getestet**: Python 3.9, 3.10, 3.11

Pandas und NumPy sind ab Python 3.7 vollständig kompatibel.

---

## 🎓 Zusammenfassung

| Was Sie wissen sollten | Empfehlung |
|------------------------|------------|
| **Datengenerierung** | ✅ Verwenden Sie `generate_sample_data.py` |
| **PBIX-Datenextraktion** | ✅ Verwenden Sie DAX Studio oder Tabular Editor |
| **Python-Extraktion** | ❌ Nicht zuverlässig (XPress9-Problem) |
| **Learning-Zwecke** | ✅ Alle Skripte sind lehrreich für PBIX-Struktur |

---

**📌 Wichtigste Empfehlung:**

Für produktive Arbeit mit Daten:
1. **Datengenerierung**: `generate_sample_data.py`
2. **Echte Daten extrahieren**: DAX Studio

Für Lern- und Analysezwecke:
- Alle Skripte durchlesen und verstehen, wie PBIX intern funktioniert

---

**✨ Viel Erfolg mit den Tools!**

Bei Fragen oder Problemen öffnen Sie gerne ein Issue im [GitHub Repository](https://github.com/AndreasTraut/PowerBI-Performance-Dashboard).
