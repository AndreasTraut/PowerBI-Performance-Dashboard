# Dokumentationsverzeichnis

Dieses Verzeichnis enthält die technische Dokumentation für das Power BI Performance Dashboard-Projekt.

## Inhalt

### [model-documentation.md](model-documentation.md)
Umfassende Dokumentation des Datenmodells (semantisches Modell) einschließlich:
- Sternschema-Architektur
- Faktentabellen (Sales, Orders, Returns, Visits, etc.)
- Dimensionstabellen (Customer, Product, Date, Region, etc.)
- Beziehungen und DAX-Measures
- Performance-Optimierungen
- Verwendungsrichtlinien

## Modelldatei

Das Datenmodell ist auch im Repository-Hauptverzeichnis verfügbar:
- **Datei**: `../Model.bim`
- **Format**: Binär (XPress9-komprimiertes Analysis Services Tabular Model)
- **Größe**: ~5 MB
- **Quelle**: Extrahiert aus `Performance Dashboard.pbix`

### Über das Model.bim Format

Die `Model.bim` Datei ist in ihrem nativen komprimierten Format gespeichert, wie sie aus der PBIX-Datei extrahiert wurde. Dies ist das Standardformat, das von Power BI Desktop und Analysis Services verwendet wird.

**Um das Modell anzuzeigen oder zu bearbeiten:**
1. Öffnen Sie `Performance Dashboard.pbix` in Power BI Desktop
2. Verwenden Sie Tabular Editor (Open-Source-Tool), um sich mit der PBIX zu verbinden
3. Verwenden Sie DAX Studio, um Measures und Performance zu analysieren

Die Modelldokumentation in diesem Verzeichnis bietet eine menschenlesbare Übersicht der Modellstruktur, ohne dass spezialisierte Tools erforderlich sind.

## Zweck

Diese Dokumentation hilft Entwicklern, Analysten und Stakeholdern:
- Die Datenmodell-Architektur zu verstehen
- Verfügbare Metriken und Dimensionen kennenzulernen
- Report-Entwicklung und -Erweiterungen zu planen
- Das Modell zu warten und zu optimieren
- Neue Teammitglieder einzuarbeiten

---

Für Fragen oder Anregungen zur Dokumentation öffnen Sie bitte ein Issue im Repository.
