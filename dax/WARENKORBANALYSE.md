# Warenkorbanalyse (Market Basket Analysis) - DAX Implementierung

Dieses Verzeichnis enthält DAX-Code zur Implementierung einer Warenkorbanalyse im Power BI Performance Dashboard. Die Warenkorbanalyse hilft zu identifizieren, welche Produkte häufig zusammen gekauft werden, und ermöglicht so Cross-Selling- und Upselling-Strategien.

---

## 📋 Inhaltsverzeichnis

- [Schnellanleitung](#-schnellanleitung)
- [DAX-Dateien](#-dax-dateien)
- [Visualisierung erstellen](#-visualisierung-erstellen)
- [Anwendungsbeispiele](#-anwendungsbeispiele)
- [Erweiterte Measures](#-erweiterte-measures)
- [Datenmodell-Anforderungen](#-datenmodell-anforderungen)
- [Problembehebung](#-problembehebung)
- [Technische Hinweise](#-technische-hinweise)

---

## 🚀 Schnellanleitung

### Schritt 1: Berechnete Tabelle erstellen

1. Öffnen Sie das Projekt, indem Sie die Datei `Performance Dashboard.pbip` in Power BI Desktop öffnen.
2. Gehen Sie zur Registerkarte **Modellierung** → **Neue Tabelle**
3. Fügen Sie folgenden DAX-Code ein:

```dax
dim_product_comparison = dim_product
```

4. ✅ **Wichtig**: Erstellen Sie KEINE Beziehungen von dieser Tabelle zu anderen Tabellen!

### Schritt 2: Measure erstellen

1. Registerkarte **Modellierung** → **Neues Measure**
2. Fügen Sie folgenden DAX-Code ein:

```dax
Orders containing both = 
VAR SelectedComparisonProduct = SELECTEDVALUE(dim_product_comparison[ProductID])
VAR OrdersWithComparisonProduct = 
    CALCULATETABLE(
        VALUES(fact_sales[OrderID]),
        ALL(dim_product),
        fact_sales[ProductID] = SelectedComparisonProduct
    )
RETURN
    IF(
        NOT ISBLANK(SelectedComparisonProduct),
        CALCULATE(
            DISTINCTCOUNT(fact_sales[OrderID]),
            fact_sales[OrderID] IN OrdersWithComparisonProduct
        ),
        BLANK()
    )
```

### Schritt 3: Matrix-Visualisierung erstellen

- **Zeilen**: `dim_product[ProductName]`
- **Spalten**: `dim_product_comparison[ProductName]`
- **Werte**: `Orders containing both`

---

## 📁 DAX-Dateien

### 1. `dim_product_comparison.dax`

**Typ**: Berechnete Tabelle  
**Zweck**: Unverbundene Kopie von `dim_product` für unabhängige Produktauswahl

```dax
dim_product_comparison = dim_product
```

**Eigenschaften**:
- Erstellt eine vollständige Kopie der `dim_product`-Tabelle
- **Unverbunden (Disconnected)**: Hat KEINE Beziehungen zu Faktentabellen
- Ermöglicht die Auswahl eines "Vergleichsprodukts" unabhängig von Hauptproduktfiltern
- Essentiell für die Warenkorbanalyse, um zwei Produkte gleichzeitig zu vergleichen

---

### 2. `Orders_containing_both.dax`

**Typ**: Measure (Kennzahl)  
**Zweck**: Zählt eindeutige Bestellungen, die sowohl das ausgewählte Produkt als auch das Vergleichsprodukt enthalten

```dax
Orders containing both = 
VAR SelectedComparisonProduct = SELECTEDVALUE(dim_product_comparison[ProductID])
VAR OrdersWithComparisonProduct = 
    CALCULATETABLE(
        VALUES(fact_sales[OrderID]),
        ALL(dim_product),
        fact_sales[ProductID] = SelectedComparisonProduct
    )
RETURN
    IF(
        NOT ISBLANK(SelectedComparisonProduct),
        CALCULATE(
            DISTINCTCOUNT(fact_sales[OrderID]),
            fact_sales[OrderID] IN OrdersWithComparisonProduct
        ),
        BLANK()
    )
```

**Funktionsweise**:

1. **Vergleichsprodukt abrufen**: 
   - Ruft die ProductID aus `dim_product_comparison` ab
   - Verwendet `SELECTEDVALUE()` für das einzelne ausgewählte Produkt

2. **Bestellungen mit Vergleichsprodukt finden**:
   - Verwendet `CALCULATETABLE()` um alle Bestellungen mit dem Vergleichsprodukt zu ermitteln
   - `ALL(dim_product)` entfernt alle Filter der Hauptproduktdimension
   - Filtert `fact_sales` nach dem Vergleichsprodukt

3. **Bestellungen mit beiden Produkten zählen**:
   - Zählt eindeutige OrderIDs, die in der Vergleichsprodukt-Bestellliste sind
   - Der Hauptproduktfilter (aus `dim_product`) wird automatisch angewendet
   - Ergebnis: Anzahl der Bestellungen mit BEIDEN Produkten

4. **Leere Auswahl behandeln**:
   - Gibt `BLANK()` zurück, wenn kein Vergleichsprodukt ausgewählt ist

---

## 📊 Visualisierung erstellen

### Option A: Matrix-Visualisierung (empfohlen)

1. **Matrix hinzufügen** aus der Visualisierungsliste

2. **Felder konfigurieren**:
   - **Zeilen**: `dim_product[ProductName]` oder `dim_product[SKU]`
   - **Spalten**: `dim_product_comparison[ProductName]` oder `dim_product_comparison[SKU]`
   - **Werte**: `Orders containing both`

3. **Datenschnitte erstellen**:
   - **Produkt-Datenschnitt**: Aus `dim_product` (filtert Zeilen)
   - **Vergleichsprodukt-Datenschnitt**: Aus `dim_product_comparison` (filtert Spalten)
   - Beide Datenschnitte arbeiten unabhängig voneinander

4. **Erweiterte Optionen**:
   - `dim_product[Category]` oder `dim_product[Brand]` als zusätzliche Zeilen
   - `dim_product_comparison[Category]` als zusätzliche Spalten
   - Bedingte Formatierung für hohe Co-Occurrence-Werte

### Option B: Tabelle mit Datenschnitten

1. **Zwei Datenschnitte erstellen**:
   - Datenschnitt 1: `dim_product[ProductName]` → Hauptprodukt
   - Datenschnitt 2: `dim_product_comparison[ProductName]` → Vergleichsprodukt

2. **Karte (Card) für das Ergebnis**:
   - Wert: `Orders containing both`
   - Zeigt die Anzahl der Bestellungen mit beiden Produkten

---

## 🎯 Anwendungsbeispiele

### Beispiel 1: "Mit welchen Produkten wird Produkt A gekauft?"

**Setup**:
- Datenschnitt auf `dim_product`: "Produkt A" auswählen
- Matrix-Spalten: `dim_product_comparison[ProductName]`
- Werte: `Orders containing both`

**Ergebnis**: Zeigt alle Produkte und wie oft sie mit "Produkt A" zusammen bestellt wurden.

---

### Beispiel 2: "Cross-Selling zwischen Kategorien"

**Setup**:
- Datenschnitt auf `dim_product[Category]`: "Electronics" auswählen
- Datenschnitt auf `dim_product_comparison[Category]`: "Accessories" auswählen
- Matrix: Produkte aus Electronics × Produkte aus Accessories

**Ergebnis**: Cross-Kategorie-Produktaffinitätsmatrix.

---

### Beispiel 3: "Vollständige Produktaffinitätsmatrix"

**Setup**:
- Keine Datenschnitte angewendet
- Zeilen: `dim_product[ProductName]`
- Spalten: `dim_product_comparison[ProductName]`
- Werte: `Orders containing both`

**Ergebnis**: Vollständige N×N-Matrix aller Produktkombinationen.

**Hinweis**: Kann bei vielen Produkten groß sein; filtern Sie zuerst nach Top-Produkten.

---

## 📈 Erweiterte Measures

### 1. Bestellungen mit Produkt 1
```dax
Orders with Product 1 = DISTINCTCOUNT(fact_sales[OrderID])
```

### 2. Bestellungen mit Produkt 2
```dax
Orders with Product 2 = 
VAR SelectedComparisonProduct = SELECTEDVALUE(dim_product_comparison[ProductID])
RETURN
    IF(
        NOT ISBLANK(SelectedComparisonProduct),
        CALCULATE(
            DISTINCTCOUNT(fact_orders[OrderID]),
            ALL(dim_product),
            fact_orders[ProductID] = SelectedComparisonProduct
        ),
        BLANK()
    )
```

### 3. Co-occurrence Rate (%)
```dax
Co-occurrence Rate % = 
VAR OrdersBoth = [Orders containing both]
VAR OrdersProduct1 = [Orders with Product 1]
RETURN
    IF(
        NOT ISBLANK(OrdersBoth) && OrdersProduct1 > 0,
        DIVIDE(OrdersBoth, OrdersProduct1, 0) * 100,
        BLANK()
    )
```

**Bedeutung**: Welcher Prozentsatz der Bestellungen von Produkt 1 enthält auch Produkt 2?

### 4. Lift (Market Basket Metrik)
```dax
Lift = 
VAR OrdersBoth = [Orders containing both]
VAR OrdersProduct1 = [Orders with Product 1]
VAR OrdersProduct2 = [Orders with Product 2]
VAR TotalOrders = CALCULATE(DISTINCTCOUNT(fact_orders[OrderID]), ALL(dim_product), ALL(dim_product_comparison))
VAR ExpectedCoOccurrence = DIVIDE(OrdersProduct1 * OrdersProduct2, TotalOrders, 0)
RETURN
    IF(
        ExpectedCoOccurrence > 0,
        DIVIDE(OrdersBoth, ExpectedCoOccurrence, 0),
        BLANK()
    )
```

**Bedeutung**: Lift > 1 zeigt an, dass Produkte häufiger zusammen gekauft werden als zufällig erwartet.

---

## 📋 Datenmodell-Anforderungen

### Erforderliche Tabellen
- ✅ `dim_product` - Produktdimension (mit Beziehungen zum Modell)
- ✅ `fact_orders` - Bestellfakten mit granularen Bestell-Produkt-Beziehungen

### Erforderliche Spalten
- `dim_product[ProductID]` - Primärschlüssel
- `fact_orders[OrderID]` - Bestellkennung
- `fact_orders[ProductID]` - Fremdschlüssel zu dim_product

### Beziehungen
- `dim_product[ProductID]` → `fact_orders[ProductID]` (1:n)
- `dim_product_comparison` sollte **KEINE Beziehungen** haben (unverbundene Tabelle)

---

## ❓ Problembehebung

### Problem: "Orders containing both" zeigt immer leere Werte

**Lösung**: 
- Stellen Sie sicher, dass ein Produkt aus `dim_product_comparison` ausgewählt ist
- Überprüfen Sie, ob die Spalte `ProductID` in beiden Tabellen existiert
- Verifizieren Sie, dass die Beziehung zwischen `dim_product` und `fact_orders` aktiv ist

### Problem: Alle Werte sind gleich

**Lösung**:
- Überprüfen Sie, dass `dim_product_comparison` KEINE Beziehungen hat
- Stellen Sie sicher, dass Sie Felder aus `dim_product_comparison` in Datenschnitten/Spalten verwenden, nicht aus `dim_product`

### Problem: Performance ist bei großen Datensätzen langsam

**Lösung**:
- Filtern Sie Produkte mit Datenschnitten vor (z.B. Top 50 Produkte nach Umsatz)
- Erwägen Sie das Erstellen einer aggregierten Tabelle für häufige Produktpaare
- Verwenden Sie Variablen und optimieren Sie den DAX-Code

---

## 🔧 Technische Hinweise

### Warum fact_orders statt fact_sales?
- `fact_orders` enthält **Bestellpositionen** mit `OrderID` und `ProductID`
- Diese granularen Daten sind essentiell für die Warenkorbanalyse
- `fact_sales` ist aggregiert und bewahrt keine Produkt-Level-Bestelldetails

### Warum eine unverbundene Tabelle?
- Ermöglicht unabhängiges Filtern von zwei Produkten gleichzeitig
- Verhindert automatische Filterübertragung von einer Produktauswahl zur anderen
- Standard-Muster für "What-If"-Analysen und vergleichende Szenarien in Power BI

### DAX-Muster: Cross-Filtering mit unverbundenen Tabellen
Diese Implementierung verwendet das **Disconnected Table Pattern**:
1. Erstelle eine Kopie einer Dimensionstabelle
2. Halte sie unverbunden (keine Beziehungen)
3. Verwende `CALCULATE` und `ALL` zur manuellen Steuerung des Filterkontexts
4. Üblich für Parametertabellen, What-If-Analysen und vergleichende Analysen

---

## ✅ Implementierungs-Checkliste

- [ ] Tabelle `dim_product_comparison` erstellt
- [ ] `dim_product_comparison` hat KEINE Beziehungen
- [ ] Measure `Orders containing both` erstellt
- [ ] Matrix-Visualisierung funktioniert
- [ ] Datenschnitte filtern unabhängig voneinander

---

## 🎯 Nächste Schritte

Nach der Implementierung können Sie:

1. **Top Product Pairs identifizieren**: Sortieren Sie die Matrix nach `Orders containing both`
2. **Bundle-Strategien entwickeln**: Produkte mit hohen Co-occurrence Rates zusammen anbieten
3. **Cross-Selling optimieren**: Empfehlungen basierend auf häufigen Produktkombinationen
4. **A/B-Tests durchführen**: Testen Sie verschiedene Produktkombinationen

---

## 📚 Referenzen

- [Power BI Market Basket Analysis](https://learn.microsoft.com/en-us/power-bi/create-reports/sample-sales-returns)
- [DAX Patterns - Disconnected Tables](https://www.sqlbi.com/p/dax-patterns-parameter-table/)
- [SQLBI - DAX-Pattern Baske Analysis ](https://www.sqlbi.com/p/dax-patterns-basket-analysis/)

---

## 📜 Versionshistorie

- **v1.0** (29.01.2026): Initiale Implementierung
  - Berechnete Tabelle `dim_product_comparison` erstellt
  - Measure `Orders containing both` erstellt
  - Setup und Verwendung dokumentiert

---

*Diese Implementierung ist Teil des Power BI Performance Dashboard Projekts.*
