# Schnellanleitung: Market Basket Analysis (Warenkorbanalyse)

## Zusammenfassung

Diese Anleitung erklärt, wie Sie die Warenkorbanalyse in Ihrem Power BI Performance Dashboard implementieren, um zu analysieren, welche Produkte häufig zusammen gekauft werden.

## Schritte zur Implementierung

### Schritt 1: Berechnete Tabelle erstellen

1. Öffnen Sie die Datei `Performance Dashboard.pbix` in Power BI Desktop
2. Gehen Sie zur Registerkarte **Modellierung**
3. Klicken Sie auf **Neue Tabelle**
4. Kopieren Sie folgenden DAX-Code:

```dax
dim_product_comparison = dim_product
```

5. Drücken Sie **Enter**
6. ✅ **Wichtig**: Erstellen Sie KEINE Beziehungen von dieser Tabelle zu anderen Tabellen!

**Was macht diese Tabelle?**
- Erstellt eine Kopie der Produktdimension
- Bleibt "disconnected" (ohne Beziehungen)
- Ermöglicht die unabhängige Auswahl von Vergleichsprodukten

---

### Schritt 2: Measure (Kennzahl) erstellen

1. Gehen Sie zur Registerkarte **Modellierung**
2. Klicken Sie auf **Neues Measure**
3. Kopieren Sie folgenden DAX-Code:

```dax
Orders containing both = 
VAR SelectedComparisonProduct = SELECTEDVALUE(dim_product_comparison[ProductKey])
VAR OrdersWithComparisonProduct = 
    CALCULATETABLE(
        VALUES(fact_orders[OrderID]),
        ALL(dim_product),
        fact_orders[ProductKey] = SelectedComparisonProduct
    )
RETURN
    IF(
        NOT ISBLANK(SelectedComparisonProduct),
        CALCULATE(
            DISTINCTCOUNT(fact_orders[OrderID]),
            fact_orders[OrderID] IN OrdersWithComparisonProduct
        ),
        BLANK()
    )
```

4. Drücken Sie **Enter**

**Was macht diese Kennzahl?**
- Zählt Bestellungen (OrderIDs), die BEIDE Produkte enthalten:
  - Produkt 1: Ausgewählt aus `dim_product` (Hauptprodukt)
  - Produkt 2: Ausgewählt aus `dim_product_comparison` (Vergleichsprodukt)

---

### Schritt 3: Visualisierung erstellen

#### Option A: Matrix-Visualisierung (empfohlen)

1. **Matrix hinzufügen**:
   - Klicken Sie auf das Matrix-Symbol in der Visualisierungsliste
   
2. **Felder konfigurieren**:
   - **Zeilen**: `dim_product[ProductName]`
   - **Spalten**: `dim_product_comparison[ProductName]`
   - **Werte**: `Orders containing both`

3. **Ergebnis**: 
   - Eine Matrix, die zeigt, wie oft jedes Produktpaar zusammen bestellt wurde

#### Option B: Tabelle mit Datenschnitten

1. **Zwei Datenschnitte erstellen**:
   - **Datenschnitt 1**: `dim_product[ProductName]` → Wählt das Hauptprodukt
   - **Datenschnitt 2**: `dim_product_comparison[ProductName]` → Wählt das Vergleichsprodukt

2. **Tabelle erstellen**:
   - **Spalte 1**: `dim_product[ProductName]`
   - **Spalte 2**: `dim_product_comparison[ProductName]`
   - **Spalte 3**: `Orders containing both`

3. **Karte (Card) für das Ergebnis**:
   - Fügen Sie eine Karte hinzu
   - Wert: `Orders containing both`
   - Zeigt die Anzahl der Bestellungen mit beiden ausgewählten Produkten

---

## Anwendungsbeispiele

### Beispiel 1: "Mit welchen Produkten wird Produkt A gekauft?"

**Setup**:
- Datenschnitt auf `dim_product`: "TechPro Laptops Model 1" auswählen
- Matrix mit Spalten: `dim_product_comparison[ProductName]`
- Werte: `Orders containing both`

**Ergebnis**: Zeigt alle Produkte und wie oft sie mit "TechPro Laptops Model 1" zusammen bestellt wurden.

---

### Beispiel 2: "Welche Produkte aus Kategorie X werden mit Produkten aus Kategorie Y gekauft?"

**Setup**:
- Datenschnitt auf `dim_product[Category]`: "Electronics" auswählen
- Datenschnitt auf `dim_product_comparison[Category]`: "Accessories" auswählen
- Matrix: Produkte × Produkte
- Werte: `Orders containing both`

**Ergebnis**: Cross-Selling-Matrix zwischen Kategorien.

---

## Erweiterte Analyse (Optional)

### Zusätzliche Kennzahlen

#### 1. Bestellungen mit Produkt 1
```dax
Orders with Product 1 = DISTINCTCOUNT(fact_orders[OrderID])
```

#### 2. Co-occurrence Rate (%)
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

---

## Prüfung der Implementierung

### ✅ Checkliste

- [ ] Tabelle `dim_product_comparison` erstellt
- [ ] `dim_product_comparison` hat KEINE Beziehungen
- [ ] Measure `Orders containing both` erstellt
- [ ] Matrix-Visualisierung funktioniert
- [ ] Datenschnitte filtern unabhängig voneinander

### ❓ Problembehebung

**Problem**: Measure zeigt immer leere Werte
- **Lösung**: Wählen Sie ein Produkt aus `dim_product_comparison` aus

**Problem**: Alle Werte sind gleich
- **Lösung**: Überprüfen Sie, dass `dim_product_comparison` keine Beziehungen hat

---

## Datenmodell-Anforderungen

### Erforderliche Tabellen
- ✅ `dim_product` - Produktdimension (mit Beziehungen)
- ✅ `fact_orders` - Bestellfakten mit OrderID und ProductKey

### Erforderliche Spalten
- `dim_product[ProductKey]`
- `fact_orders[OrderID]`
- `fact_orders[ProductKey]`

### Beziehungen
- `dim_product[ProductKey]` → `fact_orders[ProductKey]` (1:n)
- `dim_product_comparison` → **KEINE Beziehungen**

---

## Nächste Schritte

Nach der Implementierung können Sie:

1. **Top Product Pairs identifizieren**: Sortieren Sie die Matrix nach `Orders containing both`
2. **Bundle-Strategien entwickeln**: Produkte mit hohen Co-occurrence Rates zusammen anbieten
3. **Cross-Selling optimieren**: Empfehlungen basierend auf häufigen Produktkombinationen
4. **A/B-Tests durchführen**: Testen Sie verschiedene Produktkombinationen

---

## Dateien

Alle DAX-Codes finden Sie im Verzeichnis `/dax/`:
- `dim_product_comparison.dax` - Berechnete Tabelle
- `Orders_containing_both.dax` - Measure
- `README.md` - Ausführliche Dokumentation (Englisch)

---

*Version 1.0 - 29. Januar 2026*
