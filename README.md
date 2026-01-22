# Power BI Performance Dashboard

An interactive **end-to-end business performance dashboard** built in **Power BI**, designed to analyze **Sales, Customers, Orders, and Returns** across regions, channels, and time.

The dashboard focuses on **executive KPIs**, **operational insights**, and **driver analysis**, with an app-like user experience (focus mode, navigation, and slicer toggle).

---

## 📋 Table of Contents

- [Dashboard Walkthrough](#-dashboard-walkthrough-demo)
- [Key Features](#-key-features)
- [Dashboard Pages](#-dashboard-pages-overview)
- [Quick Start](#-quick-start)
- [Data & Model](#-data--model)
- [Documentation](#-documentation)
- [Tools & Technologies](#-tools--technologies)
- [Design Notes](#-design-notes)

---

## 🎥 Dashboard Walkthrough (Demo)

A short walkthrough demonstrating dashboard navigation, slicers, focus mode, and key insights across all pages.

https://github.com/user-attachments/assets/c8376858-bfeb-4149-b9aa-04d0635b48e8

---

## 🎯 Key Features

- Dynamic KPI cards with **Current Year vs Previous Year**
- **Focus Mode** for deep dives (trend analysis & key drivers)
- Centralized **slicer panel** with toggle control
- App-style **page navigation**
- Drill-down into **regions, countries, products, customers, and channels**
- Detailed **transaction-level matrices** for analysis

---

## 📊 Dashboard Pages Overview

### 1️⃣ Overview
High-level business snapshot with:
- Core KPIs: **Sales, Customers, Orders, Returns**
- Monthly performance trends
- Regional performance (America, Europe, Asia)
- Top brands, channels, categories, and customer types (B2B / B2C)

![Overview](assets/overview.png)

---

### 2️⃣ Sales Analysis
Sales performance and financial drivers:
- Net Sales, Quantity Sold, Avg Sales per Order
- Country-level sales & map view
- Top sub-categories and SKUs
- Financial summary: **Gross Sales, COGS, Gross Profit**
- Sales vs Profit correlation and monthly trends

![Sales](assets/sales.png)

---

### 3️⃣ Customers Analysis
Customer behavior and retention insights:
- Total, New, Returning Customers
- Customer Retention Rate
- Breakdown by country and customer type
- Customer segmentation (priority, channel, loyalty)
- Detailed customer matrix with sales & order metrics

![Customers](assets/customers.png)

---

### 4️⃣ Orders Analysis
Operational and order efficiency metrics:
- Total Orders, AOV, Completion & Cancellation Rates
- Orders by country, customer type, and status
- On-time delivery performance
- Order value segmentation & delivery time correlation

![Orders](assets/orders.png)

---

### 5️⃣ Returns Analysis
Return behavior and quality insights:
- Return volume, rate, and return sales value
- Breakdown by country, customer type, and category
- Reasons for returns (chart & heatmap)
- Detailed return-level matrix with processing status

![Returns](assets/returns.png)

---

## � Quick Start

1. **Download** the `.pbix` file  
2. **Open** in **Power BI Desktop**
3. **Explore** the dashboard using slicers, navigation, and focus mode
4. **Review** the [documentation](#-documentation) for technical details

---

## 📁 Data & Model

### Data Files

The [/data](data/) directory contains CSV files for the data model:

- **Dimension Tables**: Customer, Date, Geography, Product
- **Fact Tables**: Sales, Orders, Returns

📖 **See [/data/README.md](data/README.md)** for:
- Data extraction instructions
- Schema overview
- How to extract actual data from the PBIX

### Data Model

The semantic model (`Model.bim`) uses a **star schema architecture** with optimized relationships and DAX measures.

📖 **See [Model Documentation](doc/model-documentation.md)** for:
- Complete model structure
- Fact and dimension tables
- DAX measures and calculations
- Performance optimizations

---

## 📚 Documentation

Comprehensive technical documentation is available in the [/doc](doc/) directory:

### Core Documentation

- **[Model Documentation](doc/model-documentation.md)**  
  Complete data model architecture, star schema, fact/dimension tables, relationships, and DAX measures

- **[Data Extraction Guide](doc/DATA_EXTRACTION_SUMMARY.md)**  
  How data was extracted from PBIX, available tools, and step-by-step extraction instructions

- **[Security Summary](doc/SECURITY_SUMMARY.md)**  
  Security review of all scripts, code safety analysis, and best practices

### Key Topics

| Topic | Documentation |
|-------|--------------|
| 🗂️ Model Structure | [model-documentation.md](doc/model-documentation.md) |
| 📊 Data Extraction | [DATA_EXTRACTION_SUMMARY.md](doc/DATA_EXTRACTION_SUMMARY.md) |
| 🔒 Security | [SECURITY_SUMMARY.md](doc/SECURITY_SUMMARY.md) |
| 💾 Data Files | [/data/README.md](data/README.md) |

---

## 🛠 Tools & Technologies

- **Power BI Desktop** - Dashboard and reporting
- **Power Query** - Data cleaning & transformation
- **DAX** - KPIs, YoY comparisons, retention logic
- **Data Modeling** - Star schema, relationships
- **Python** - Data extraction and sample data generation

### Included Scripts

- [generate_sample_data.py](tools/generate_sample_data.py) - Generate sample data for testing
- [extract_pbix_actual.py](tools/extract_pbix_actual.py) - Analyze and extract from PBIX
- [extract_pbix_data.py](tools/extract_pbix_data.py) - Data extraction utilities

---

## 📌 Design Notes

- **Data**: Sample data provided for demonstration purposes
- **Focus**: Clarity, performance, and usability
- **Design Inspiration**: User interface layout and visual styling inspired by the work of Nicholas Lea-Trengrouse shared publicly on LinkedIn

---

## 📄 License

See [LICENSE](LICENSE) for details.
