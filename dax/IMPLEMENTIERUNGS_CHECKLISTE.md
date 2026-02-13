# Implementierungs-Checkliste - Warenkorbanalyse

Verwenden Sie diese Checkliste bei der Implementierung der Warenkorbanalyse in Power BI Desktop.

---

## ✅ Checkliste vor der Implementierung

- [ ] Power BI Desktop ist installiert und auf dem neuesten Stand
- [ ] Die Projektdatei `Performance Dashboard.pbip` ist zugänglich
- [ ] Ein Backup der ursprünglichen PBIX-Datei wurde erstellt
- [ ] Sie haben die Dokumentation in WARENKORBANALYSE.md gelesen

---

## 📋 Schritt-für-Schritt-Implementierung

### Schritt 1: Unverbundene Tabelle erstellen

- [ ] Öffnen Sie das Projekt, indem Sie die Datei `Performance Dashboard.pbip` in Power BI Desktop öffnen.
- [ ] Gehen Sie zur Registerkarte **Modellierung**
- [ ] Klicken Sie auf **Neue Tabelle**
- [ ] Kopieren Sie den DAX-Code aus `dim_product_comparison.dax`:
  ```dax
  dim_product_comparison = dim_product
  ```
- [ ] Drücken Sie **Enter**, um die Tabelle zu erstellen
- [ ] Überprüfen Sie, ob die Tabelle im Bereich "Felder" erscheint
- [ ] **WICHTIG**: Bestätigen Sie, dass für diese Tabelle KEINE Beziehungen bestehen
  - Gehen Sie zur **Modellansicht**
  - Prüfen Sie, dass `dim_product_comparison` keine Beziehungslinien hat
  - Falls Beziehungen bestehen, löschen Sie diese (Rechtsklick → Löschen)

**Überprüfung**:
- [ ] Die Tabelle `dim_product_comparison` existiert
- [ ] Die Tabelle hat dieselben Spalten wie `dim_product`
- [ ] Die Tabelle ist unverbunden (keine Beziehungslinien in der Modellansicht)

---

### Schritt 2: Haupt-Measure erstellen

- [ ] Gehen Sie zur Registerkarte **Modellierung** (oder bleiben Sie dort)
- [ ] Klicken Sie auf **Neues Measure**
- [ ] Kopieren Sie den DAX-Code aus `/dax/Orders_containing_both.dax`
- [ ] Fügen Sie ihn in die Bearbeitungsleiste ein
- [ ] Drücken Sie **Enter**, um das Measure zu erstellen
- [ ] Überprüfen Sie, ob das Measure im Bereich "Felder" erscheint

**Überprüfung**:
- [ ] Das Measure `Orders containing both` existiert
- [ ] Das Measure zeigt keine Fehler in der Bearbeitungsleiste
- [ ] Das Measure ist im Bereich "Felder" sichtbar

---

### Schritt 3: Grundlegende Funktionalität testen

#### Ein Test-Visual erstellen

- [ ] Fügen Sie ein **Karten**-Visual zum Berichtsblatt hinzu
- [ ] Fügen Sie das Measure `Orders containing both` zur Karte hinzu
- [ ] Fügen Sie einen **Datenschnitt** für `dim_product_comparison[ProductName]` hinzu
- [ ] Wählen Sie ein Produkt im Datenschnitt aus
- [ ] Überprüfen Sie, ob die Karte eine Zahl anzeigt (nicht leer oder Fehler)
- [ ] Fügen Sie einen weiteren **Datenschnitt** für `dim_product[ProductName]` hinzu
- [ ] Wählen Sie auch in diesem Datenschnitt ein Produkt aus
- [ ] Überprüfen Sie, ob die Karte aktualisiert wird und die Anzahl der Bestellungen mit beiden Produkten anzeigt

**Überprüfung**:
- [ ] Die Auswahl von Produkten aktualisiert den Wert der Karte
- [ ] Die beiden Datenschnitte funktionieren unabhängig voneinander
- [ ] Das Measure zeigt plausible Werte (nicht zu hoch/niedrig)

---

### Schritt 4: Produkt-Affinitäts-Matrix erstellen (Empfohlen)

- [ ] Fügen Sie ein **Matrix**-Visual zum Berichtsblatt hinzu
- [ ] Konfigurieren Sie die Matrix:
  - **Zeilen**: Ziehen Sie `dim_product[ProductName]` auf "Zeilen"
  - **Spalten**: Ziehen Sie `dim_product_comparison[ProductName]` auf "Spalten"
  - **Werte**: Ziehen Sie `Orders containing both` auf "Werte"
- [ ] Ändern Sie die Größe der Matrix, um mehrere Produkte zu sehen
- [ ] Überprüfen Sie die Ergebnisse - die Zellen sollten die Anzahl der gemeinsamen Vorkommen anzeigen

**Optionale Erweiterungen**:
- [ ] Fügen Sie eine bedingte Formatierung hinzu, um hohe Werte hervorzuheben
  - Rechtsklick auf `Orders containing both` im Werte-Bereich
  - Wählen Sie **Bedingte Formatierung** → **Hintergrundfarbe**
  - Wählen Sie eine Farbskala (z.B. weiß nach grün)
- [ ] Filtern Sie auf Top-Produkte für eine bessere Performance
  - Klicken Sie auf `dim_product[ProductName]` im Zeilen-Bereich
  - Fügen Sie einen Top-N-Filter hinzu (z.B. Top 20 nach Umsatz)

**Überprüfung**:
- [ ] Die Matrix zeigt Produktnamen in Zeilen und Spalten an
- [ ] Die Zellen zeigen die Anzahl der gemeinsamen Vorkommen
- [ ] Diagonale Zellen (gleiches Produkt) können ignoriert werden
- [ ] Die Werte sind aus geschäftlicher Sicht sinnvoll

---

### Schritt 5: Optionale Measures hinzufügen (Empfohlen)

Wählen Sie Measures aus `/dax/additional_measures.dax` je nach Ihren Anforderungen:

#### Essentielle Measures (Dringend empfohlen):

- [ ] **Co-occurrence Rate %**
  - Zeigt den Prozentsatz der Bestellungen von Produkt 1, die auch Produkt 2 enthalten
  - Kopieren aus `additional_measures.dax` → Als neues Measure einfügen
  
- [ ] **Lift**
  - Zeigt die Stärke der Assoziation (>1 = stark, =1 = zufällig, <1 = schwach)
  - Kopieren aus `additional_measures.dax` → Als neues Measure einfügen

#### Unterstützende Measures (Gut zu haben):

- [ ] **Orders with Product 1**
  - Gesamtbestellungen, die Produkt 1 enthalten
  
- [ ] **Orders with Product 2**
  - Gesamtbestellungen, die Produkt 2 enthalten

#### Erweiterte Measures (Optional):

- [ ] **Support %** - Gesamt-Häufigkeit des Paares
- [ ] **Jaccard Similarity %** - Alternative Ähnlichkeitsmetrik
- [ ] **Is Strong Association** - Boolescher Filter für starke Paare

**Überprüfung**:
- [ ] Alle ausgewählten Measures werden ohne Fehler erstellt
- [ ] Measures erscheinen im Bereich "Felder"
- [ ] Testen Sie jedes Measure in einem Karten-Visual

---

### Schritt 6: Business-Dashboard erstellen

#### Option A: Executive Summary Karte

Erstellen Sie ein Dashboard mit:
- [ ] Zwei Datenschnitten: Einer für jede Produkttabelle
- [ ] Karte, die `Orders containing both` anzeigt
- [ ] Karte, die `Co-occurrence Rate %` anzeigt
- [ ] Karte, die `Lift` anzeigt

#### Option B: Detaillierte Analyse-Matrix

Erstellen Sie eine Matrix, die anzeigt:
- [ ] Zeilen: Produktnamen aus `dim_product`
- [ ] Spalten: Produktnamen aus `dim_product_comparison`
- [ ] Werte: Mehrere Measures
  - `Orders containing both`
  - `Co-occurrence Rate %`
  - `Lift`

#### Option C: Top-Paare-Tabelle

Erstellen Sie eine Tabelle, die anzeigt:
- [ ] Spalte: `Product Pair` (berechnetes Measure aus `additional_measures.dax`)
- [ ] Spalte: `Orders containing both`
- [ ] Spalte: `Lift`
- [ ] Filter: Top 20 nach `Orders containing both`
- [ ] Sortierung: Absteigend nach `Orders containing both`

**Überprüfung**:
- [ ] Das Dashboard ist visuell übersichtlich
- [ ] Filter funktionieren korrekt
- [ ] Werte werden bei Auswahländerungen aktualisiert
- [ ] Die Einblicke sind handlungsorientiert

---

## 🧪 Testen & Validierung

### Tests zur Datengenauigkeit

- [ ] **Test 1: Bekanntes Produktpaar**
  - Wählen Sie zwei Produkte aus, von denen Sie wissen, dass sie zusammen verkauft werden
  - Überprüfen Sie, ob die Anzahl Ihren Erwartungen entspricht
  - Vergleichen Sie, wenn möglich, mit einer manuellen SQL-Abfrage

- [ ] **Test 2: Unabhängige Produkte**
  - Wählen Sie zwei Produkte aus verschiedenen Kategorien, die wahrscheinlich nicht zusammen verkauft werden
  - Überprüfen Sie, ob die Anzahl niedrig oder null ist

- [ ] **Test 3: Gleiches Produkt**
  - Wählen Sie in beiden Datenschnitten dasselbe Produkt aus
  - Die Anzahl sollte den Gesamtbestellungen für dieses Produkt entsprechen
  - (Oder implementieren Sie Logik, um bei gleichem Produkt BLANK anzuzeigen)

### Performance-Tests

- [ ] **Test mit vollständigem Datensatz**
  - Entfernen Sie alle Filter
  - Prüfen Sie, ob die Matrix in angemessener Zeit lädt (<10 Sekunden)
  - Wenn langsam, implementieren Sie Top-N-Filter

- [ ] **Test mit Datenschnitten**
  - Wenden Sie verschiedene Datenschnitt-Kombinationen an
  - Überprüfen Sie die Reaktionsfähigkeit

### Tests für Randfälle

- [ ] **Keine Auswahl**: Überprüfen Sie, ob das Measure BLANK anzeigt, wenn kein Produkt ausgewählt ist
- [ ] **Einzelne Auswahl**: Überprüfen Sie, ob das Measure BLANK anzeigt, wenn nur ein Produkt ausgewählt ist
- [ ] **Datumsfilter**: Wenden Sie Datums-Datenschnitte an und überprüfen Sie, ob die Zählungen korrekt aktualisiert werden

**Überprüfung**:
- [ ] Alle Tests sind erfolgreich
- [ ] In den Visuals erscheinen keine Fehler
- [ ] Die Performance ist akzeptabel

---

## 📊 Dokumentation

- [ ] Fügen Sie Ihrem Bericht ein Textfeld hinzu, das erklärt, wie die Analyse zu verwenden ist
- [ ] Dokumentieren Sie alle benutzerdefinierten Filter oder Änderungen
- [ ] Speichern Sie die PBIX-Datei mit einer neuen Versionsnummer
- [ ] Exportieren Sie die Dokumentation bei Bedarf als PDF

---

## 🎯 Zu validierende Geschäftsanwendungsfälle

Testen Sie diese realen Szenarien:

- [ ] **Cross-Selling**: Finden Sie die Top 5 Produkte, die mit Produkt X empfohlen werden sollen
- [ ] **Bundle-Erstellung**: Identifizieren Sie Produktpaare mit einem Lift > 2
- [ ] **Bestandsplanung**: Finden Sie Produkte, die häufig zusammen gekauft werden
- [ ] **Marketing-Kampagnen**: Sprechen Sie Kunden, die Produkt A kaufen, mit Angeboten für Produkt B an

---

## 🐛 Fehlerbehebung

Wenn Probleme auftreten, überprüfen Sie:

- [ ] `dim_product_comparison` hat keine Beziehungen (häufigstes Problem)
- [ ] Spaltennamen stimmen exakt überein (`ProductID`, `ProductName`, `OrderID`)
- [ ] Die Tabelle `fact_sales` existiert und hat die erforderlichen Spalten
- [ ] Beziehungen zwischen `dim_product` und `fact_sales` sind aktiv
- [ ] DAX-Syntax ist korrekt (keine Tippfehler)
- [ ] Die Power BI Desktop-Version unterstützt die verwendeten DAX-Funktionen

**Häufige Probleme**:

| Problem | Lösung |
|-------|----------|
| Measure immer leer | Wählen Sie ein Produkt aus `dim_product_comparison` aus |
| Alle Werte sind gleich | Löschen Sie die Beziehungen von `dim_product_comparison` |
| Performance langsam | Fügen Sie Top-N-Filter hinzu, aggregieren Sie Daten |
| Fehler im DAX | Überprüfen Sie, ob die Spaltennamen mit Ihrem Modell übereinstimmen |

---

## ✨ Nach der Implementierung

Nach erfolgreicher Implementierung:

- [ ] Speichern Sie die PBIX-Datei
- [ ] Testen Sie mit Stakeholdern
- [ ] Sammeln Sie Feedback zu den Einblicken
- [ ] Planen Sie die Datenaktualisierung (bei Verwendung des Power BI Service)
- [ ] Teilen Sie die Ergebnisse mit den Geschäftsbereichen
- [ ] Dokumentieren Sie die wichtigsten gewonnenen Erkenntnisse
- [ ] Planen Sie die nächsten Schritte (Bundles, Kampagnen usw.)

---

## 📚 Zusätzliche Ressourcen

- Siehe WARENKORBANALYSE.md (DE) oder IMPLEMENTATION_SUMMARY.md (EN) für eine detaillierte technische Dokumentation.
- Siehe EXAMPLES.md für Visualisierungsbeispiele.
- Siehe SCHNELLANLEITUNG.md für eine deutsche Kurzanleitung.
- Siehe Power BI-Dokumentation für DAX-Hilfe

---

## ✅ Abschließende Checkliste

Bevor Sie die Implementierung als abgeschlossen betrachten:

- [ ] Alle Measures erstellt und funktionsfähig
- [ ] Mindestens ein Visual erstellt und getestet
- [ ] Datengenauigkeit validiert
- [ ] Performance ist akzeptabel
- [ ] Dokumentation ist vorhanden
- [ ] Stakeholder über die Verwendung informiert
- [ ] Backup der funktionierenden PBIX-Datei gespeichert

---

**Implementierungsstatus**: ⬜ Nicht begonnen | 🟡 In Arbeit | ✅ Abgeschlossen

**Datum der Fertigstellung**: _______________

**Implementiert von**: _______________

**Notizen**: 

```
[Fügen Sie hier Notizen zu Anpassungen, aufgetretenen Problemen oder getroffenen Entscheidungen hinzu]
```

---

*Diese Checkliste ist Teil der Implementierung der Warenkorbanalyse für das Power BI Performance Dashboard.*