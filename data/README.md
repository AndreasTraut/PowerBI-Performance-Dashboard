# Data Extraction Guide for Power BI Performance Dashboard

This directory contains CSV data files for the Power BI Performance Dashboard.

## Current Status

The `data/` directory currently contains **sample data** generated to match the schema used in the Power BI dashboard. These files provide a starting point and demonstrate the expected structure.

## Extracting Actual Data from the PBIX File

To extract the **actual data** from the `Performance Dashboard.pbix` file, you can use one of the following methods:

### Method 1: Power BI Desktop (Recommended for Most Users)

1. **Open the PBIX file:**
   - Open `Performance Dashboard.pbix` in Power BI Desktop

2. **Access Power Query Editor:**
   - Click on "Transform data" in the toolbar
   - This opens the Power Query Editor

3. **Export each table:**
   - For each table in the left panel:
     - Right-click the table name
     - Select "Advanced Editor" to see the data source
     - Or use Home → Close & Load To → Close & Load To → Table → Load
   - Then in Data view, select the table
   - Click on the table corner (top-left cell selector)
   - Copy the table (Ctrl+C)
   - Paste into Excel or a text editor
   - Save as CSV

### Method 2: DAX Studio (Best for Data Export)

[DAX Studio](https://daxstudio.org/) is a free, open-source tool specifically designed for working with Power BI data models.

1. **Download and install DAX Studio:**
   - Get it from: https://daxstudio.org/

2. **Connect to the PBIX file:**
   - Open DAX Studio
   - Click "PBI / SSDT Model"
   - Select the open `Performance Dashboard.pbix` file

3. **Export tables:**
   ```dax
   EVALUATE 'dim_customer'
   ```
   - Run this query for each table
   - Click "Export" → "Data" → "CSV"
   - Repeat for all tables:
     - `dim_customer`
     - `dim_date`  
     - `dim_geography`
     - `dim_product`
     - `fact_orders`
     - `fact_returns`
     - `fact_sales`

### Method 3: Tabular Editor 2 (For Advanced Users)

[Tabular Editor](https://tabulareditor.com/) is an open-source tool for editing Power BI data models.

1. **Download Tabular Editor 2:**
   - Get it from: https://github.com/TabularEditor/TabularEditor/releases

2. **Open the PBIX:**
   - File → Open → From File
   - Select `Performance Dashboard.pbix`

3. **Use C# scripts to export data:**
   - Advanced Scripting → C# Scripts
   - Use export scripts available in the community

### Method 4: Power BI Service (If Published)

If the dashboard is published to Power BI Service:
1. Open the report in Power BI Service
2. For each visual:
   - Click the "..." menu
   - Select "Export data"
   - Choose between "Summarized data" or "Underlying data"
   - Download as CSV

## Data Structure

The following tables are used in the Power BI dashboard:

### Dimension Tables

1. **dim_date.csv** - Date dimension
   - DateKey, Date, Year, Quarter, Month, Week, etc.

2. **dim_geography.csv** - Geographic dimension
   - GeographyKey, Country, Region, Continent

3. **dim_product.csv** - Product dimension
   - ProductKey, SKU, ProductName, Category, SubCategory, Brand, UnitCost, UnitPrice

4. **dim_customer.csv** - Customer dimension
   - CustomerKey, CustomerID, CustomerName, CustomerType, PriorityLevel, Channel, FirstOrderDate

### Fact Tables

5. **fact_orders.csv** - Order transactions
   - OrderKey, OrderID, OrderDateKey, CustomerKey, ProductKey, Quantity, UnitPrice, LineTotal, COGS, Status, etc.

6. **fact_sales.csv** - Sales aggregates
   - SalesKey, SalesDateKey, CustomerKey, GrossSales, NetSales, COGS, GrossProfit

7. **fact_returns.csv** - Return transactions
   - ReturnKey, ReturnID, ReturnDateKey, OrderKey, CustomerKey, ProductKey, ReturnQuantity, ReturnReason, Status

## Regenerating Sample Data

If you need to regenerate the sample data (for testing purposes), run:

```bash
python generate_sample_data.py
```

This will create new sample CSV files in the `data/` directory with realistic patterns matching the dashboard schema.

## Technical Details

The Power BI `.pbix` file format is a ZIP archive containing:
- `DataModel` - Compressed tabular model (uses Microsoft XPress9 compression)
- `Report/Layout` - Report layout and visuals
- `DiagramLayout` - Model diagram
- Other metadata files

The `DataModel` uses proprietary compression that requires specialized tools to decompress and extract data programmatically. The methods above use supported Microsoft tools to access the data without manual decompression.

## Support

For issues extracting data:
1. Ensure you have the latest version of Power BI Desktop
2. Check that the PBIX file opens correctly
3. For DAX Studio issues, visit: https://daxstudio.org/documentation/
4. For Tabular Editor issues, visit: https://docs.tabulareditor.com/

## Notes

- The sample data is for demonstration and testing purposes only
- Real data may have different volumes and distributions
- Always backup the original PBIX file before modifications
- Data extraction respects Power BI data refresh and transformation logic
