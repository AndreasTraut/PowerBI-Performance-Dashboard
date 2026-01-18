# Power BI Performance Dashboard - Data Model Documentation

## Overview

This document describes the data model (semantic model) for the Power BI Performance Dashboard. The model follows a **star schema** design pattern, optimized for analytical queries and business intelligence reporting.

## Model Architecture

The data model is organized around business processes with clearly separated **fact tables** (containing measurable transactions) and **dimension tables** (containing descriptive attributes).

### Star Schema Design

```
                    dim_date
                        |
    dim_channel    dim_region    dim_customer    dim_product    dim_return_reason
         |              |              |              |              |
         +------+-------+------+-------+------+-------+------+-------+
                |                                                     |
         fact_visits  fact_sales  fact_orders              fact_returns
                                                                     |
                                                          fact_return_amount
                                  |
                      fact_financial_insights
```

## Fact Tables

Fact tables contain the quantitative business data and foreign keys to dimension tables.

### 1. fact_sales
**Purpose**: Tracks sales transactions and revenue metrics

**Key Metrics**:
- Net Sales
- Gross Sales
- COGS (Cost of Goods Sold)
- Gross Profit
- Quantity Sold
- Sales per Order

**Grain**: One row per sales transaction

**Related Dimensions**: Customer, Product, Date, Region, Channel

---

### 2. fact_orders
**Purpose**: Tracks order lifecycle and operational metrics

**Key Metrics**:
- Total Orders
- Order Status (Completed, Cancelled)
- Average Order Value (AOV)
- Order Completion Rate
- Order Cancellation Rate
- On-time Delivery Performance
- Delivery Time

**Grain**: One row per order

**Related Dimensions**: Customer, Product, Date, Region, Channel

---

### 3. fact_returns
**Purpose**: Tracks product returns and return behavior

**Key Metrics**:
- Return Volume
- Return Rate
- Return Sales Value
- Return Processing Status

**Grain**: One row per return transaction

**Related Dimensions**: Customer, Product, Date, Region, Return Reason

---

### 4. fact_visits
**Purpose**: Tracks customer engagement and website/store visits

**Key Metrics**:
- Visit Count
- Customer Engagement Metrics

**Grain**: One row per customer visit

**Related Dimensions**: Customer, Date, Channel

---

### 5. fact_return_amount
**Purpose**: Aggregated return amounts and financial impact

**Key Metrics**:
- Total Return Amount
- Return Value by Category

**Grain**: Aggregated return amounts

**Related Dimensions**: Date, Product, Customer

---

### 6. fact_financial_insights
**Purpose**: Financial summary and performance indicators

**Key Metrics**:
- Financial KPIs
- Profitability Metrics
- Revenue Analysis

**Grain**: Aggregated financial data

**Related Dimensions**: Date, Customer, Product

---

## Dimension Tables

Dimension tables provide descriptive context for analyzing facts.

### 1. dim_customer
**Purpose**: Customer master data and attributes

**Key Attributes**:
- Customer ID
- Customer Name
- Customer Type (B2B / B2C)
- Customer Priority/Segment
- Customer Loyalty Status
- Geographic Location

**Type**: Slowly Changing Dimension (SCD)

---

### 2. dim_product
**Purpose**: Product hierarchy and classifications

**Key Attributes**:
- Product ID / SKU
- Product Name
- Category
- Sub-category
- Brand
- Product Attributes

**Hierarchy**: Brand → Category → Sub-category → SKU

---

### 3. dim_region
**Purpose**: Geographic hierarchy for location-based analysis

**Key Attributes**:
- Region ID
- Region Name (America, Europe, Asia)
- Country
- City
- Geographic Coordinates (for map visualizations)

**Hierarchy**: Region → Country → City

---

### 4. dim_date
**Purpose**: Time intelligence and date-based filtering

**Key Attributes**:
- Date
- Year
- Quarter
- Month
- Month Name
- Week
- Day
- Day of Week
- Is Weekend
- Fiscal Period

**Type**: Date dimension with continuous date range

**Special Features**:
- Supports Year-over-Year (YoY) comparisons
- Previous Year calculations
- Month-over-Month trends

---

### 5. dim_channel
**Purpose**: Sales and distribution channel classification

**Key Attributes**:
- Channel ID
- Channel Name
- Channel Type
- Channel Category

**Examples**: Online, Retail, Wholesale, Partner

---

### 6. dim_return_reason
**Purpose**: Classification of return reasons for quality analysis

**Key Attributes**:
- Reason ID
- Reason Code
- Reason Description
- Reason Category

**Examples**: Defective, Wrong Item, Not as Described, Customer Changed Mind

---

## Supporting Tables

### KPI_Summary_Table
**Purpose**: Pre-calculated KPI summary values for dashboard performance optimization

**Content**:
- Core business KPIs
- Aggregated metrics
- Comparison values (Current vs Previous Period)

---

### Parameter Tables

#### Parameter
**Purpose**: User-selected parameters for dynamic filtering and calculations

#### Parameter (Overview)
**Purpose**: Parameters specific to the Overview dashboard page

---

## Relationships

The model uses standard **star schema relationships**:

- **One-to-Many** relationships from dimensions to facts
- **Cardinality**: Dimension (1) → Fact (Many)
- **Cross-filter Direction**: Single direction (from dimension to fact) for most relationships
- **Referential Integrity**: Enforced through Power BI relationships

### Key Relationships:

1. **dim_date** → Multiple fact tables (Sales, Orders, Returns, Visits)
2. **dim_customer** → fact_sales, fact_orders, fact_returns, fact_visits
3. **dim_product** → fact_sales, fact_orders, fact_returns
4. **dim_region** → fact_sales, fact_orders, fact_returns
5. **dim_channel** → fact_sales, fact_orders, fact_visits
6. **dim_return_reason** → fact_returns
7. **fact_returns** → fact_return_amount (aggregation relationship)

---

## DAX Measures and Calculations

The model includes extensive DAX (Data Analysis Expressions) calculations for:

### Time Intelligence
- Current Year (CY) metrics
- Previous Year (PY) metrics
- Year-over-Year (YoY) comparisons
- YoY Growth %
- Month-over-Month trends

### Customer Analytics
- New Customers
- Returning Customers
- Customer Retention Rate
- Customer Lifetime Value

### Sales Metrics
- Net Sales = Gross Sales - Returns
- Gross Profit = Sales - COGS
- Gross Profit Margin %
- Average Sales per Order

### Order Metrics
- Order Completion Rate
- Order Cancellation Rate
- Average Order Value (AOV)

### Return Metrics
- Return Rate = Returns / Total Orders
- Return Value Impact

---

## Data Model Properties

### Format
- **Model Type**: Tabular (Analysis Services)
- **Compatibility Level**: 1520 or higher
- **Compression**: XPress9 (VertiPaq)
- **Storage Mode**: Import

### Performance Optimizations
- **Star Schema**: Optimized for query performance
- **Pre-aggregated Tables**: KPI_Summary_Table for fast dashboard loading
- **Relationships**: Properly indexed for efficient joins
- **Data Types**: Optimized column data types
- **Hierarchies**: Defined for drill-down analysis

---

## Usage Context

This data model supports the following dashboard pages:

1. **Overview**: High-level business snapshot with core KPIs
2. **Sales Analysis**: Revenue and financial performance
3. **Customers Analysis**: Customer behavior and retention
4. **Orders Analysis**: Operational efficiency
5. **Returns Analysis**: Product quality and return patterns

---

## Data Sources

Based on the model structure, the data is loaded from:
- Transactional systems (Sales, Orders, Returns)
- Customer relationship management (CRM) system
- Product catalog
- Geographic reference data
- Date/Calendar table (generated)

---

## Model File

The complete model definition is stored in:
- **File**: `Model.bim` (in repository root)
- **Format**: Binary (XPress9 compressed Tabular Model)
- **Source**: Extracted from `Performance Dashboard.pbix`

### Viewing the Model

To view the full model structure:

1. **Using Power BI Desktop**:
   - Open `Performance Dashboard.pbix`
   - Go to Model view
   - View tables, relationships, and measures

2. **Using Tabular Editor** (recommended for advanced model analysis):
   - Download [Tabular Editor](https://tabulareditor.com/)
   - File → Open → From Database (connect to PBIX)
   - or extract and open Model.bim with decompression tools

3. **Using DAX Studio** (for measure analysis):
   - Download [DAX Studio](https://daxstudio.org/)
   - Connect to the PBIX file
   - Analyze measures and performance

---

## Best Practices Applied

✅ **Star Schema Design**: Clear separation of facts and dimensions  
✅ **Naming Conventions**: Consistent `fact_` and `dim_` prefixes  
✅ **Date Dimension**: Comprehensive date table for time intelligence  
✅ **Optimized Relationships**: One-to-many, single direction  
✅ **Measure Organization**: DAX measures grouped logically  
✅ **Data Types**: Appropriate data types for performance  
✅ **Hierarchies**: Pre-defined for common drill-downs  

---

## Model Maintenance

### Refresh Strategy
- **Full Refresh**: Updates all tables with latest data
- **Incremental Refresh**: Can be configured for large fact tables
- **Refresh Frequency**: Depends on business requirements (daily, weekly, etc.)

### Version Control
- Model changes should be documented
- Use Tabular Editor for version control of model metadata
- Export Model.bim for backup and comparison

---

## Additional Resources

- [Power BI Data Modeling Best Practices](https://docs.microsoft.com/en-us/power-bi/guidance/star-schema)
- [DAX Reference](https://dax.guide/)
- [Tabular Editor Documentation](https://docs.tabulareditor.com/)

---

*Last Updated: January 2026*  
*Model Version: Compatible with the Performance Dashboard PBIX file*
