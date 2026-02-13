# Warenkorbanalyse - Implementierungsbeispiele

> ➡️ **Details siehe:** [WARENKORBANALYSE.md](/dax/WARENKORBANALYSE.md) / Zusammenassung ( [DE](/dax/IMPLEMENTIERUNGS_ZUSAMMENFASSUNG.md) / [EN](dax/IMPLEMENTATION_SUMMARY.md) )  
> 📖 **Implementierung:** [Orders_containing_both.dax](/dax/Orders_containing_both.dax)  
> 🧠 **Dokumentation:** Implementierungs-Checkliste ( [DE](/dax/IMPLEMENTIERUNGS_CHECKLISTE.md) / [EN](/dax/IMPLEMENTATION_CHECKLIST.md) )

## 🚀 Visueller Einrichtungsleitfaden

Dieses Dokument bietet visuelle Anleitungen und Beispiele für die Implementierung der Warenkorbanalyse (Market Basket Analysis) in Power BI.

---

## 📊 Beispiel 1: Produkt-Affinitäts-Matrix

### Visualisierungstyp: Matrix

**Zweck**: Zeigt ein vollständiges Raster an, wie oft jedes Produktpaar zusammen in Bestellungen erscheint.

### 🔧 Konfiguration:
```
Matrix Visual:
├─ Zeilen: dim_product[ProductName]
├─ Spalten: dim_product_comparison[ProductName]
└─ Werte: Orders containing both
```

### ✅ Erwartetes Ergebnis:
```
                     | Laptop A | Laptop B | Mouse X | Keyboard Y |
---------------------|----------|----------|---------|------------|
Laptop A             |    -     |    15    |   89    |    67      |
Laptop B             |    15    |    -     |   45    |    34      |
Mouse X              |    89    |    45    |   -     |   123      |
Keyboard Y           |    67    |    34    |  123    |    -       |
```

**🧠 Interpretation**:
- Diagonale Zellen können ignoriert werden (ein Produkt erscheint immer mit sich selbst).
- Hohe Werte zeigen eine starke Produkt-Affinität an.
- Beispiel: Mouse X und Keyboard Y erscheinen zusammen in 123 Bestellungen.

### Bedingte Formatierung (Empfohlen):
- Hintergrundfarbskalen: Höhere Werte → Dunklere Farbe
- Hilft, starke Beziehungen auf einen Blick zu erkennen.

---

## 📊 Beispiel 2: Top Produkt-Kombinationen für ein spezifisches Produkt

### Visualisierungstyp: Tabelle oder Balkendiagramm

**Zweck**: Zeigt für ein ausgewähltes Produkt an, welche anderen Produkte am häufigsten zusammen gekauft werden.

### 🔧 Konfiguration:
```
Datenschnitt (Slicer):
└─ dim_product[ProductName] = "TechPro Laptops Model 1"

Tabelle Visual:
├─ Spalte 1: dim_product_comparison[ProductName]
├─ Spalte 2: Orders containing both
└─ Sortieren nach: Orders containing both (Absteigend)
```

### ✅ Erwartetes Ergebnis:
```
Comparison Product          | Orders containing both
----------------------------|----------------------
Premium Mouse Pro           |          156
TechPro Keyboard Elite      |          142
Premium Monitor 27"         |          98
SmartHome USB Hub           |          76
Premium Headphones          |          54
```

**Geschäftsanwendung**:
- Cross-Selling-Empfehlungen
- Erstellung von Produktbündeln (Bundles)
- Produktplatzierungsstrategien

---

## 📊 Beispiel 3: Kategorie Cross-Selling Analyse

### Visualisierungstyp: Matrix mit Kategorie-Hierarchie

**Zweck**: Analysiert, welche Produktkategorien zusammen gekauft werden.

### 🔧 Konfiguration:
```
Matrix Visual:
├─ Zeilen: dim_product[Category] → dim_product[ProductName]
├─ Spalten: dim_product_comparison[Category] → dim_product_comparison[ProductName]
└─ Werte: Orders containing both
```

### ✅ Erwartetes Ergebnis:
```
                        | Electronics           | Accessories
                        |--------               |------------
                        | Laptops | Monitors    | Mice | Keyboards
------------------------|---------|-------------|------|----------
Electronics             |         |             |      |
  Laptops               |    -    |     234     |  456 |   389
  Monitors              |   234   |      -      |  178 |   156
Accessories             |         |             |      |
  Mice                  |   456   |     178     |   -  |   567
  Keyboards             |   389   |     156     |  567 |    -
```

**Erkenntnisse**:
- Laptops und Mäuse haben eine hohe Affinität (456 Bestellungen).
- Mäuse und Tastaturen werden häufig zusammen gekauft (567 Bestellungen).
- Kategorieübergreifende Muster informieren über Bündelungsstrategien.

---

## 📊 Beispiel 4: Interaktives Produkt-Vergleichs-Dashboard

### Layout:
```
┌────────────────────────────────────────────────┐
│  Wähle Produkt 1:          Wähle Produkt 2:   │
│  [Slicer: dim_product]     [Slicer: dim_...   │
│                            product_comparison] │
├────────────────────────────────────────────────┤
│  Bestellungen mit beiden:                      │
│  ┌──────────┐                                  │
│  │   142    │  (Karte Visual)                  │
│  └──────────┘                                  │
├────────────────────────────────────────────────┤
│  Details:                                      │
│  Bestellungen nur mit Prod 1:     234          │
│  Bestellungen nur mit Prod 2:     198          │
│  Co-occurrence Rate:              60.7%        │
│  Lift:                            2.34         │
└────────────────────────────────────────────────┘
```

### 🧠 KPIs Erklärt:

**Orders containing both**: 142
- Direkte Anzahl der Bestellungen mit beiden Produkten.

**Orders with Product 1 only**: 234
- Gesamtbestellungen, die Produkt 1 enthalten.

**Co-occurrence Rate**: 60.7%
- Formel: (142 / 234) × 100
- Bedeutung: 60,7% der Bestellungen von Produkt 1 enthalten auch Produkt 2.

**Lift**: 2.34
- Lift > 1 bedeutet, Produkte werden HÄUFIGER zusammen gekauft als durch Zufall erwartet.
- Lift = 1 bedeutet keine spezielle Affinität (Zufall).
- Lift < 1 bedeutet, Produkte werden selten zusammen gekauft.

---

## 📊 Beispiel 5: Top 10 Produkt-Paare

### Visualisierungstyp: Tabelle mit beiden Produkten

**Zweck**: Entdecken der stärksten Produktkombinationen insgesamt.

### 💾 DAX für kombiniertes Produkt-Paar:
```dax
Product Pair = 
VAR Product1 = SELECTEDVALUE(dim_product[ProductName])
VAR Product2 = SELECTEDVALUE(dim_product_comparison[ProductName])
RETURN
    IF(
        NOT ISBLANK(Product1) && NOT ISBLANK(Product2),
        Product1 & " + " & Product2,
        BLANK()
    )
```

### 🔧 Konfiguration:
```
Tabelle Visual:
├─ Spalte 1: Product Pair (berechnetes Measure oben)
├─ Spalte 2: Orders containing both
├─ Top N Filter: Top 10 nach Orders containing both
└─ Sortieren nach: Orders containing both (Absteigend)
```

### ✅ Erwartetes Ergebnis:
```
Product Pair                                    | Orders
------------------------------------------------|--------
Premium Mouse Pro + Premium Keyboard Elite      |   234
TechPro Laptop + Premium Monitor 27"            |   198
SmartHome Hub + SmartHome Camera                |   176
Premium Headphones + Premium Mouse Pro          |   145
TechPro Laptop + TechPro Keyboard               |   142
...
```

---

## 📊 Beispiel 6: Heatmap Visualisierung

### Visualisierungstyp: Matrix mit bedingter Formatierung

**Zweck**: Visuelle Heatmap zur schnellen Identifizierung starker Produktbeziehungen.

### 🔧 Konfiguration:
```
Matrix Visual:
├─ Zeilen: dim_product[ProductName] (Filter auf Top 20 Produkte)
├─ Spalten: dim_product_comparison[ProductName] (Filter auf Top 20 Produkte)
└─ Werte: Orders containing both

Bedingte Formatierung:
├─ Basiert auf: Orders containing both
├─ Farbskala: Weiß (0) → Grün (Niedrig) → Dunkelgrün (Hoch)
└─ Werte anzeigen: Optional
```

### Visuelles Erscheinungsbild:
```
         | Prod1 | Prod2 | Prod3 | Prod4 |
---------|-------|-------|-------|-------|
Prod1    |  ███  |  ░░░  |  ▓▓▓  |  ░░░  |
Prod2    |  ░░░  |  ███  |  ▒▒▒  |  ▓▓▓  |
Prod3    |  ▓▓▓  |  ▒▒▒  |  ███  |  ░░░  |
Prod4    |  ░░░  |  ▓▓▓  |  ░░░  |  ███  |

Legende: ░░░ = Niedrig    ▒▒▒ = Mittel    ▓▓▓ = Hoch    ███ = Gleiches Produkt
```

**Vorteile**:
- Schnelle Mustererkennung
- Identifizierung von Clustern verwandter Produkte
- Erkennen von Anomalien oder unerwarteten Kombinationen

---

## 🚀 Best Practices

### 1. Performance-Optimierung
- **Filter auf Top N Produkte** für große Datensätze.
- Vor-Aggregation häufiger Paare in einer Übersichtstabelle, falls nötig.
- Verwendung von Datenschnitten (Slicers), um das Datenvolumen zu reduzieren.

### 2. Benutzererfahrung (UX)
- **Klare Bezeichnungen**: Produktnamen verwenden, keine IDs.
- **Sortierung nach Affinität**: Höchste Anzahl zuerst anzeigen.
- **Kontextbezogene Hilfe**: Tooltips hinzufügen, die die Metriken erklären.

### 3. Geschäftsanwendung
- **Bundle-Erstellung**: Produkte mit hoher gemeinsamer Vorkommenshäufigkeit.
- **Cross-Sell-Hinweise**: "Kunden, die X kauften, kauften auch Y".
- **Bestandsplanung**: Verwandte Produkte zusammen lagern.
- **Marketingkampagnen**: Produktpaare mit hoher Affinität bewerben.

### 4. Datenqualitäts-Prüfungen
- Stornierte Bestellungen ausschließen: `Filter fact_orders where OrderStatus = "Completed"`.
- Mindestbestellmenge: Nur Paare mit mindestens 5 Vorkommen anzeigen.
- Datumsfilter: Aktuelle Trends vs. historische Muster analysieren.

---

## 🧠 Erweiterte Measures (Optional)

### Support (%)
Zeigt an, wie viel Prozent ALLER Bestellungen dieses Produktpaar enthalten.

```dax
Support % = 
VAR OrdersBoth = [Orders containing both]
VAR TotalOrders = CALCULATE(DISTINCTCOUNT(fact_sales[OrderID]), ALL(dim_product), ALL(dim_product_comparison))
RETURN
    DIVIDE(OrdersBoth, TotalOrders, 0) * 100
```

### Confidence (%)
Wenn Produkt 1 gekauft wird, wie hoch ist die Wahrscheinlichkeit, dass auch Produkt 2 gekauft wird?

```dax
Confidence % = 
VAR OrdersBoth = [Orders containing both]
VAR OrdersProduct1 = [Orders with Product 1]
RETURN
    DIVIDE(OrdersBoth, OrdersProduct1, 0) * 100
```

### Lift
Wie viel wahrscheinlicher werden diese Produkte zusammen gekauft im Vergleich zum unabhängigen Kauf?

```dax
Lift = 
VAR OrdersBoth = [Orders containing both]
VAR OrdersProduct1 = [Orders with Product 1]
VAR OrdersProduct2 = [Orders with Product 2]
VAR TotalOrders = CALCULATE(DISTINCTCOUNT(fact_orders[OrderID]), ALL())
VAR ExpectedCoOccurrence = DIVIDE(OrdersProduct1 * OrdersProduct2, TotalOrders, 0)
RETURN
    DIVIDE(OrdersBoth, ExpectedCoOccurrence, 0)
```

**Interpretation**:
- **Lift = 1**: Keine Assoziation (Zufall).
- **Lift > 1**: Positive Assoziation (werden öfter zusammen gekauft).
- **Lift < 1**: Negative Assoziation (werden selten zusammen gekauft).

**Beispiel**:
- Support = 2%: Dieses Paar erscheint in 2% aller Bestellungen.
- Confidence = 40%: Wenn Produkt 1 gekauft wird, folgt Produkt 2 in 40% der Fälle.
- Lift = 2.5: Dieses Paar tritt 2,5× häufiger auf als durch Zufall erwartet.

---

## ❓ Fehlerbehebung bei Visualisierungen

### Problem: Leere Werte in der Matrix
**Ursache**: Kein Produkt aus `dim_product_comparison` ausgewählt.
**Lösung**: Fügen Sie einen Datenschnitt hinzu oder stellen Sie sicher, dass die Spalten aus `dim_product_comparison` stammen.

### Problem: Alle Zellen zeigen den gleichen Wert
**Ursache**: `dim_product_comparison` hat Beziehungen (sollte unverbunden sein).
**Lösung**: Löschen Sie alle Beziehungen zu `dim_product_comparison`.

### Problem: Performance ist langsam
**Lösung**: 
- Filtern auf Top-Produkte (z. B. Top 50 nach Umsatz).
- Aggregationen verwenden.
- DAX mit Variablen optimieren.

### Problem: Diagonale Zellen (gleiches Produkt) zeigen hohe Werte
**Erwartet**: Ein Produkt erscheint immer mit sich selbst.
**Lösung**: 
- Ausfiltern: Measure-Logik hinzufügen, um BLANK() anzuzeigen, wenn Product1 = Product2.
- Oder diagonale Werte bei der Interpretation einfach ignorieren.

---

## ✅ Nächste Schritte

1. **Implementieren der Basis-Matrix** (Beispiel 1)
2. **Hinzufügen von Datenschnitten** für interaktive Erkundung
3. **Erstellen fokussierter Ansichten** für spezifische Anwendungsfälle (Cross-Selling, Bundles)
4. **Hinzufügen erweiterter Metriken** (Lift, Confidence, Support)
5. **Aufbau einer Empfehlungsmaschine** basierend auf Top-Produktpaaren
6. **Aktualisierungen planen**, um die Analyse aktuell zu halten

---

*Für DAX-Code siehe die Dateien im Verzeichnis `/dax`.*
