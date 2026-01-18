# Documentation Directory

This directory contains technical documentation for the Power BI Performance Dashboard project.

## Contents

### [model-documentation.md](model-documentation.md)
Comprehensive documentation of the data model (semantic model) including:
- Star schema architecture
- Fact tables (Sales, Orders, Returns, Visits, etc.)
- Dimension tables (Customer, Product, Date, Region, etc.)
- Relationships and DAX measures
- Performance optimizations
- Usage guidelines

## Model File

The data model is also available in the repository root:
- **File**: `../Model.bim`
- **Format**: Binary (XPress9 compressed Analysis Services Tabular Model)
- **Size**: ~5 MB
- **Source**: Extracted from `Performance Dashboard.pbix`

### About Model.bim Format

The `Model.bim` file is stored in its native compressed format as extracted from the PBIX file. This is the standard format used by Power BI Desktop and Analysis Services.

**To view or edit the model:**
1. Open `Performance Dashboard.pbix` in Power BI Desktop
2. Use Tabular Editor (open-source tool) to connect to the PBIX
3. Use DAX Studio to analyze measures and performance

The model documentation in this directory provides a human-readable overview of the model structure without requiring specialized tools.

## Purpose

This documentation helps developers, analysts, and stakeholders:
- Understand the data model architecture
- Learn about available metrics and dimensions
- Plan report development and extensions
- Maintain and optimize the model
- Onboard new team members

---

For questions or suggestions about the documentation, please open an issue in the repository.
