# Anleitung zur Datenextraktion für das Power BI Performance Dashboard

Dieses Verzeichnis enthält CSV-Dateien für das Power BI Performance Dashboard.

## Aktueller Status

Das Verzeichnis `data/` enthält derzeit **Beispieldaten**, die so generiert wurden, dass sie dem Schema des Power BI Dashboards entsprechen. Diese Dateien dienen als Ausgangspunkt und zeigen die erwartete Struktur.

## Extraktion echter Daten aus der PBIX-Datei

Um die **echten Daten** aus der Datei `Performance Dashboard.pbix` zu extrahieren, können Sie eine der folgenden Methoden verwenden:

### Methode 1: Power BI Desktop (Empfohlen für die meisten Anwender)

1. **PBIX-Datei öffnen:**
   - Öffnen Sie `Performance Dashboard.pbix` in Power BI Desktop

2. **Power Query Editor aufrufen:**
   - Klicken Sie auf "Daten transformieren" in der Symbolleiste
   - Der Power Query Editor wird geöffnet

3. **Jede Tabelle exportieren:**
   - Für jede Tabelle im linken Bereich:
     - Rechtsklick auf den Tabellennamen
     - "Erweiterter Editor" auswählen, um die Datenquelle zu sehen
     - Oder: Start → Schließen & laden in → Tabelle → Laden
   - In der Datenansicht die Tabelle auswählen
   - Auf die Tabellenecke klicken (Zellauswahl oben links)
   - Tabelle kopieren (Strg+C)
   - In Excel oder einen Texteditor einfügen
   - Als CSV speichern

### Methode 2: DAX Studio (Am besten für Datenexport)

DAX Studio ist ein kostenloses, quelloffenes Tool, das speziell für die Arbeit mit Power BI Datenmodellen entwickelt wurde.

1. **DAX Studio herunterladen und installieren:**
   - Download unter: https://daxstudio.org/

2. **Mit der PBIX-Datei verbinden:**
   - DAX Studio öffnen
   - Auf "PBI / SSDT Model" klicken
   - Die geöffnete `Performance Dashboard.pbix` Datei auswählen

3. **Tabellen exportieren:**
   ```dax
   EVALUATE 'dim_customer'
   ```
   - Diese Abfrage für jede Tabelle ausführen
   - "Export" → "Data" → "CSV" klicken
   - Für alle Tabellen wiederholen:
     - `dim_customer`
     - `dim_date`  
     - `dim_geography`
     - `dim_product`
     - `fact_orders`
     - `fact_returns`
     - `fact_sales`

### Methode 3: Tabular Editor 2 (Für fortgeschrittene Benutzer)

Tabular Editor ist ein quelloffenes Tool zur Bearbeitung von Power BI Datenmodellen.

1. **Tabular Editor 2 herunterladen:**
   - Download unter: https://github.com/TabularEditor/TabularEditor/releases

2. **PBIX öffnen:**
   - Datei → Öffnen → Von Datei
   - `Performance Dashboard.pbix` auswählen

3. **C#-Skripte zum Datenexport verwenden:**
   - Advanced Scripting → C# Scripts
   - Export-Skripte aus der Community verwenden

### Methode 4: Power BI Service (Falls veröffentlicht)

Wenn das Dashboard im Power BI Service veröffentlicht ist:
1. Bericht im Power BI Service öffnen
2. Für jedes Visual:
   - Auf das "..." Menü klicken
   - "Daten exportieren" auswählen
   - Zwischen "Zusammengefasste Daten" oder "Zugrunde liegende Daten" wählen
   - Als CSV herunterladen

## Datenstruktur

Die folgenden Tabellen werden im Power BI Dashboard verwendet:

### Dimensionstabellen

1. **dim_date.csv** - Datumsdimension
   - DateKey, Date, Year, Quarter, Month, Week, etc.

2. **dim_geography.csv** - Geografische Dimension
   - GeographyKey, Country, Region, Continent

3. **dim_product.csv** - Produktdimension
   - ProductKey, SKU, ProductName, Category, SubCategory, Brand, UnitCost, UnitPrice

4. **dim_customer.csv** - Kundendimension
   - CustomerKey, CustomerID, CustomerName, CustomerType, PriorityLevel, Channel, FirstOrderDate

### Faktentabellen

5. **fact_orders.csv** - Bestelltransaktionen
   - OrderKey, OrderID, OrderDateKey, CustomerKey, ProductKey, Quantity, UnitPrice, LineTotal, COGS, Status, etc.

6. **fact_sales.csv** - Verkaufsaggregate
   - SalesKey, SalesDateKey, CustomerKey, GrossSales, NetSales, COGS, GrossProfit

7. **fact_returns.csv** - Rücksendungen
   - ReturnKey, ReturnID, ReturnDateKey, OrderKey, CustomerKey, ProductKey, ReturnQuantity, ReturnReason, Status

## Beispieldaten neu generieren

Falls Sie die Beispieldaten neu generieren müssen (z.B. für Testzwecke), führen Sie folgenden Befehl aus:

```bash
python generate_sample_data.py
```

Dies erstellt neue CSV-Beispieldateien im Verzeichnis `data/` mit realistischen Mustern, die dem Dashboard-Schema entsprechen.

## Technische Details

Das Power BI `.pbix`-Dateiformat ist ein ZIP-Archiv, das Folgendes enthält:
- `DataModel` - Komprimiertes tabulares Modell (verwendet Microsoft XPress9-Komprimierung)
- `Report/Layout` - Berichtslayout und Visuals
- `DiagramLayout` - Modelldiagramm
- Weitere Metadaten-Dateien

Das `DataModel` verwendet eine proprietäre Komprimierung, die spezielle Tools zur Dekomprimierung und programmatischen Datenextraktion erfordert. Die oben genannten Methoden nutzen unterstützte Microsoft-Tools, um auf die Daten zuzugreifen, ohne manuelle Dekomprimierung.

## Support

Bei Problemen mit der Datenextraktion:
1. Stellen Sie sicher, dass Sie die neueste Version von Power BI Desktop verwenden
2. Überprüfen Sie, ob die PBIX-Datei korrekt geöffnet wird
3. Bei DAX Studio-Problemen: https://daxstudio.org/documentation/
4. Bei Tabular Editor-Problemen: https://docs.tabulareditor.com/

## Hinweise

- Die Beispieldaten dienen nur zu Demonstrations- und Testzwecken
- Echte Daten können andere Volumina und Verteilungen aufweisen
- Erstellen Sie immer ein Backup der Original-PBIX-Datei vor Änderungen
- Die Datenextraktion berücksichtigt die Power BI Datenaktualisierungs- und Transformationslogik