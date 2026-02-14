# Copilot Instructions: Power BI Performance Dashboard

Diese Datei enthält Kontextinformationen und Anweisungen für GitHub Copilot, basierend auf der Projektstruktur und den README-Inhalten.

## 🚀 Projekt-Kontext (aus README)

Dieses Repository beinhaltet ein **End-to-End Business Performance Dashboard** in **Power BI**.
Es dient zur Analyse von **Verkäufen, Kunden, Bestellungen und Rücksendungen** über Regionen, Kanäle und Zeiträume hinweg.

### Repository-Struktur (v2.0)
Das Projekt wurde von einer einfachen PBIX-Datei zu einem professionellen Entwickler-Repository weiterentwickelt:

- **Power BI Project:** `Performance Dashboard.pbip` und `Performance Dashboard.Report/` (Developer Mode).
- **Daten (📁 `/data`):** Extrahierte CSV-Dateien (dim_customer, dim_date, fact_sales, etc.) für externe Analysen.
- **Dokumentation (📁 `/doc`):** Umfassende Modell-Dokumentation, Sicherheitsaudits und Extraktionsanleitungen.
- **Tools (📁 `/tools`):** Python-Skripte zur Datenextraktion und Generierung von Beispieldaten.
- **Entwicklung (📁 `.devcontainer`):** VS Code DevContainer Konfiguration.

### Datenmodell & Features
- **Architektur:** Sternschema (Star Schema).
- **Fakten:** Sales, Orders, Returns, Visits, Financial Insights.
- **Dimensionen:** Customer, Product, Date, Region, Channel, Return Reason.
- **Features:** Executive KPIs, YoY-Vergleiche, Fokusmodus, Drill-downs.

---

## 📝 Anweisungen für Copilot

Befolge bei der Erstellung von Antworten, Dokumentation oder Code die folgenden Stil-Richtlinien.

### **Metadaten-Block** (Blockquote mit wichtigen Links)
   
**Standard-Layout (immer in dieser Reihenfolge verwenden):**
```markdown
> ➡️ **Details siehe:** [Phase {N} in Projekt-Evolution]()  
> 💼 **[LinkedIn Post: Titel](https://www.linkedin.com/posts/...)**  
> 💾 **Modul:** `phase{n}_module_name/file.py`
```
   
**Variationen je nach Kontext:**
- Für README-Sektionen: `➡️ **Details siehe:**` mit internem Link
- Für Phasen-Docs: `📖 **Implementierung:**` mit Code-Link
- Optional: `🧠 **Dokumentation:**` für weiterführende Docs

### Formatierungs-Regeln

- **Emojis:** Nutze thematisch passende Emojis für Überschriften und Aufzählungen
  - 📁 Dateien/Ordner
  - 🚀 Features/Start
  - ✅ Erfolg/Fertig
  - 🔧 Installation/Setup
  - 💾 Code/Module
  - 🧠 KI/Intelligence
  - 📊 Daten/Analysen
  - ⚠️ Warnung
  - ❓ Fragen
  
- **Listen:**
  - Nutze `-` für unsortierte Listen
  - Nutze `1.` für sortierte Listen (Schritte, Anleitungen)
  - Nutze Checkmarks für Status: ✅ ❌ 🔧

### SQL-Blöcke

**Format (falls in Zukunft relevant):**
```sql
-- Beschreibung der Query
SELECT 
    column1,
    column2,
    COUNT(*) as anzahl
FROM 
    table_name
WHERE 
    condition = 'value'
GROUP BY 
    column1, column2
ORDER BY 
    anzahl DESC;
```

**Datenfluss (Format-Beispiel):**
```
Google Photos Takeout
    ↓
Phase 1: Sortierung (YYYY-MM-DD)
    ↓
Phase 2: Intelligence (Embeddings, Faces, Emotions)
    ↓
RAG-System (Semantische Suche)
```