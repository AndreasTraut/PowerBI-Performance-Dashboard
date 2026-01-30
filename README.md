# Power BI Performance Dashboard

Ein interaktives **End-to-End Business Performance Dashboard** in **Power BI**, entwickelt zur Analyse von **Verkäufen, Kunden, Bestellungen und Rücksendungen** über Regionen, Kanäle und Zeiträume hinweg.

Das Dashboard konzentriert sich auf **Executive KPIs**, **operative Einblicke** und **Treiberanalysen** mit einer app-ähnlichen Benutzererfahrung (Fokusmodus, Navigation und Datenschnitt-Umschaltung).

---

## 📋 Inhaltsverzeichnis

- [Dashboard-Walkthrough](#-dashboard-walkthrough-demo)
- [Hauptfunktionen](#-hauptfunktionen)
- [Dashboard-Seiten](#-dashboard-seiten-übersicht)
- [Schnellstart](#-schnellstart)
- [Daten & Modell](#-daten--modell)
- [Dokumentation](#-dokumentation)
- [Tools & Technologien](#-tools--technologien)
- [Design-Hinweise](#-design-hinweise)

---

## 🎥 Dashboard-Walkthrough (Demo)

Ein kurzer Walkthrough, der die Dashboard-Navigation, Datenschnitte, den Fokusmodus und wichtige Einblicke auf allen Seiten demonstriert.

https://github.com/user-attachments/assets/c8376858-bfeb-4149-b9aa-04d0635b48e8

---

## 🎯 Hauptfunktionen

- Dynamische KPI-Karten mit **Aktuelles Jahr vs. Vorjahr**
- **Fokusmodus** für tiefgehende Analysen (Trendanalyse & Haupttreiber)
- Zentrales **Datenschnitt-Panel** mit Umschaltsteuerung
- App-ähnliche **Seitennavigation**
- Drill-down in **Regionen, Länder, Produkte, Kunden und Kanäle**
- Detaillierte **Matrizen auf Transaktionsebene** für Analysen

---

## 📊 Dashboard-Seiten Übersicht

### 1️⃣ Übersicht
Geschäftsüberblick auf hoher Ebene mit:
- Kern-KPIs: **Verkäufe, Kunden, Bestellungen, Rücksendungen**
- Monatliche Performance-Trends
- Regionale Performance (Amerika, Europa, Asien)
- Top-Marken, Kanäle, Kategorien und Kundentypen (B2B / B2C)

![Overview](assets/overview.png)

---

### 2️⃣ Verkaufsanalyse
Verkaufsperformance und finanzielle Treiber:
- Nettoumsatz, verkaufte Menge, durchschnittlicher Umsatz pro Bestellung
- Verkäufe auf Länderebene & Kartenansicht
- Top-Unterkategorien und SKUs
- Finanzzusammenfassung: **Bruttoumsatz, Wareneinsatz, Bruttogewinn**
- Korrelation zwischen Verkauf und Gewinn sowie monatliche Trends

![Sales](assets/sales.png)

---

### 3️⃣ Kundenanalyse
Kundenverhalten und Retention-Einblicke:
- Gesamt-, Neu- und wiederkehrende Kunden
- Kundenbindungsrate
- Aufschlüsselung nach Land und Kundentyp
- Kundensegmentierung (Priorität, Kanal, Loyalität)
- Detaillierte Kundenmatrix mit Verkaufs- und Bestellkennzahlen

![Customers](assets/customers.png)

---

### 4️⃣ Bestellanalyse
Operative und Bestelleffizienz-Kennzahlen:
- Gesamtbestellungen, AOV, Abschluss- & Stornierungsraten
- Bestellungen nach Land, Kundentyp und Status
- Pünktliche Lieferperformance
- Bestellwertsegmentierung & Lieferzeitkorrelation

![Orders](assets/orders.png)

---

### 5️⃣ Rücksendungsanalyse
Rücksendeverhalten und Qualitätseinblicke:
- Rücksendevolumen, -rate und Rücksendewert
- Aufschlüsselung nach Land, Kundentyp und Kategorie
- Rücksendegründe (Diagramm & Heatmap)
- Detaillierte Matrix auf Rücksende-Ebene mit Bearbeitungsstatus

![Returns](assets/returns.png)

---

## � Schnellstart

1. **Herunterladen** der `.pbix` Datei  
2. **Öffnen** in **Power BI Desktop**
3. **Erkunden** des Dashboards mit Datenschnitten, Navigation und Fokusmodus
4. **Prüfen** der [Dokumentation](#-dokumentation) für technische Details

---

## 📁 Daten & Modell

### Datendateien

Das [/data](data/) Verzeichnis enthält CSV-Dateien für das Datenmodell:

- **Dimensionstabellen**: Kunde, Datum, Geografie, Produkt
- **Faktentabellen**: Verkäufe, Bestellungen, Rücksendungen

📖 **Siehe [/data/README.md](data/README.md)** für:
- Datenextraktionsanleitungen
- Schema-Übersicht
- Anleitung zur Extraktion echter Daten aus der PBIX

### Datenmodell

Das semantische Modell (`Model.bim`) verwendet eine **Sternschema-Architektur** mit optimierten Beziehungen und DAX-Measures.

📖 **Siehe [Modell-Dokumentation](doc/model-documentation.md)** für:
- Vollständige Modellstruktur
- Fakten- und Dimensionstabellen
- DAX-Measures und Berechnungen
- Performance-Optimierungen

---

## 📚 Dokumentation

Umfassende technische Dokumentation ist im [/doc](doc/) Verzeichnis verfügbar:

### Kerndokumentation

- **[Modell-Dokumentation](doc/model-documentation.md)**  
  Vollständige Datenmodell-Architektur, Sternschema, Fakten-/Dimensionstabellen, Beziehungen und DAX-Measures

- **[Datenextraktions-Leitfaden](doc/DATA_EXTRACTION_SUMMARY.md)**  
  Wie Daten aus PBIX extrahiert wurden, verfügbare Tools und Schritt-für-Schritt-Anleitungen

- **[Sicherheitszusammenfassung](doc/SECURITY_SUMMARY.md)**  
  Sicherheitsüberprüfung aller Skripte, Code-Sicherheitsanalyse und Best Practices

### Hauptthemen

| Thema | Dokumentation |
|-------|--------------|
| 🗂️ Modellstruktur | [model-documentation.md](doc/model-documentation.md) |
| 📊 Datenextraktion | [DATA_EXTRACTION_SUMMARY.md](doc/DATA_EXTRACTION_SUMMARY.md) |
| 🔒 Sicherheit | [SECURITY_SUMMARY.md](doc/SECURITY_SUMMARY.md) |
| 💾 Datendateien | [/data/README.md](data/README.md) |

---

## 🛠 Tools & Technologien

- **Power BI Desktop** - Dashboard und Reporting
- **Power Query** - Datenbereinigung & Transformation
- **DAX** - KPIs, YoY-Vergleiche, Retention-Logik
- **Datenmodellierung** - Sternschema, Beziehungen
- **Python** - Datenextraktion und Beispieldaten-Generierung

### Enthaltene Skripte

- [generate_sample_data.py](tools/generate_sample_data.py) - Generierung von Beispieldaten zum Testen
- [extract_pbix_actual.py](tools/extract_pbix_actual.py) - Analysieren und Extrahieren aus PBIX
- [extract_pbix_data.py](tools/extract_pbix_data.py) - Datenextraktions-Dienstprogramme

---

## 📌 Design-Hinweise

- **Daten**: Beispieldaten für Demonstrationszwecke bereitgestellt
- **Fokus**: Klarheit, Performance und Benutzerfreundlichkeit
- **Design-Inspiration**: Benutzeroberflächen-Layout und visuelle Gestaltung inspiriert durch die Arbeit von Nicholas Lea-Trengrouse, öffentlich geteilt auf LinkedIn

---

## 📄 Lizenz

Siehe [LICENSE](LICENSE) für Details.
