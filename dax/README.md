# Market Basket Analysis - DAX Implementation

## Overview

This directory contains DAX code for implementing Market Basket Analysis in the Power BI Performance Dashboard. Market Basket Analysis helps identify which products are frequently bought together, enabling cross-selling and upselling strategies.

## Files

### 1. `dim_product_comparison.dax`
**Type**: Calculated Table  
**Purpose**: Disconnected copy of `dim_product` for independent product selection

```dax
dim_product_comparison = dim_product
```

**Key Features**:
- Creates a complete copy of the `dim_product` table
- **Disconnected**: Has NO relationships to any fact tables in the model
- Allows selecting a "comparison product" independently from main product filters
- Essential for Market Basket Analysis to compare two products simultaneously

**Implementation in Power BI**:
1. Go to **Modeling** tab → **New Table**
2. Paste the DAX code from `dim_product_comparison.dax`
3. **Important**: Do NOT create any relationships from this table to fact tables
4. The table should remain disconnected for the analysis to work correctly

---

### 2. `Orders_containing_both.dax`
**Type**: Measure  
**Purpose**: Count unique OrderIDs containing both the selected product and comparison product

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

**How It Works**:

1. **Get Comparison Product**: 
   - Retrieves the ProductKey selected from `dim_product_comparison`
   - Uses `SELECTEDVALUE()` to get the single selected product

2. **Find Orders with Comparison Product**:
   - Uses `CALCULATETABLE()` to get all OrderIDs containing the comparison product
   - `ALL(dim_product)` removes any filter from the main product dimension
   - Filters `fact_orders` where ProductKey matches the comparison product

3. **Count Orders with Both Products**:
   - Counts distinct OrderIDs that are in the comparison product's order list
   - The main product filter (from `dim_product`) is automatically applied
   - Result: Count of orders containing BOTH products

4. **Handle Empty Selection**:
   - Returns `BLANK()` if no comparison product is selected
   - Prevents errors and improves visual clarity

**Implementation in Power BI**:
1. Go to **Modeling** tab → **New Measure**
2. Paste the DAX code from `Orders_containing_both.dax`
3. The measure will now be available for use in visuals

---

## Usage in Power BI Dashboard

### Setting Up the Market Basket Analysis Visual

1. **Create a Matrix Visual** (recommended) or Table:
   - **Rows**: `dim_product[ProductName]` or `dim_product[SKU]`
   - **Columns**: `dim_product_comparison[ProductName]` or `dim_product_comparison[SKU]`
   - **Values**: `Orders containing both` measure

2. **Create Slicers for Filtering**:
   - **Product Slicer**: From `dim_product` table
     - Filters the main product selection (rows)
   - **Comparison Product Slicer**: From `dim_product_comparison` table
     - Filters the comparison products (columns)
   - Both slicers work independently due to the disconnected table

3. **Enhanced Analysis** (Optional):
   - Add `dim_product[Category]` or `dim_product[Brand]` as additional rows
   - Add `dim_product_comparison[Category]` as additional columns
   - Add conditional formatting to highlight high co-occurrence counts

### Example Analysis Scenarios

#### Scenario 1: "What products are bought with Product A?"
- **Setup**: 
  - Slicer on `dim_product`: Select "Product A"
  - Matrix columns: `dim_product_comparison[ProductName]`
  - Values: `Orders containing both`
- **Result**: Shows all products and how many orders contain both Product A and each product

#### Scenario 2: "Which pairs of products from Category X and Category Y are bought together?"
- **Setup**:
  - Slicer on `dim_product[Category]`: Select "Category X"
  - Slicer on `dim_product_comparison[Category]`: Select "Category Y"
  - Matrix: Products from X vs Products from Y
- **Result**: Cross-category product affinity matrix

#### Scenario 3: "Complete product affinity matrix"
- **Setup**:
  - No slicers applied
  - Rows: `dim_product[ProductName]`
  - Columns: `dim_product_comparison[ProductName]`
  - Values: `Orders containing both`
- **Result**: Full N×N matrix showing all product combinations
- **Note**: May be large for many products; consider filtering by top products first

---

## Additional Measures for Enhanced Analysis

You may want to create these supplementary measures:

### 1. Total Orders with Product 1
```dax
Orders with Product 1 = DISTINCTCOUNT(fact_orders[OrderID])
```

### 2. Total Orders with Product 2
```dax
Orders with Product 2 = 
VAR SelectedComparisonProduct = SELECTEDVALUE(dim_product_comparison[ProductKey])
RETURN
    IF(
        NOT ISBLANK(SelectedComparisonProduct),
        CALCULATE(
            DISTINCTCOUNT(fact_orders[OrderID]),
            ALL(dim_product),
            fact_orders[ProductKey] = SelectedComparisonProduct
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

This shows what percentage of Product 1's orders also contain Product 2.

### 4. Lift (Market Basket Metric)
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

Lift > 1 indicates products are bought together more often than expected by chance.

---

## Data Model Requirements

### Required Tables
- ✅ `dim_product` - Product dimension (connected to model)
- ✅ `fact_orders` - Order fact table with granular order-product relationships

### Required Columns
- `dim_product[ProductKey]` - Primary key
- `fact_orders[OrderID]` - Order identifier
- `fact_orders[ProductKey]` - Foreign key to dim_product

### Relationships
- `dim_product[ProductKey]` → `fact_orders[ProductKey]` (One-to-Many)
- `dim_product_comparison` should have **NO relationships** (disconnected table)

---

## Troubleshooting

### Issue: "Orders containing both" always shows blank
**Solution**: 
- Ensure a product is selected from `dim_product_comparison`
- Check that the `ProductKey` column exists in both tables
- Verify the relationship between `dim_product` and `fact_orders` is active

### Issue: Same count for all comparison products
**Solution**:
- Verify `dim_product_comparison` has NO relationships
- Check that you're using fields from `dim_product_comparison` in slicers/columns, not from `dim_product`

### Issue: Performance is slow with large datasets
**Solution**:
- Pre-filter products using slicers (e.g., top 50 products by sales)
- Consider creating an aggregated table for common product pairs
- Use variables and optimize DAX code for your specific use case

---

## Technical Notes

### Why Use fact_orders Instead of fact_sales?
- `fact_orders` contains **order line items** with `OrderID` and `ProductKey`
- This granular data is essential for Market Basket Analysis
- `fact_sales` is aggregated and doesn't preserve product-level order details

### Why Use a Disconnected Table?
- Allows independent filtering of two products simultaneously
- Prevents automatic filter propagation from one product selection to the other
- Standard pattern for "what-if" analysis and comparative scenarios in Power BI

### DAX Pattern: Cross-filtering with Disconnected Tables
This implementation uses the **disconnected table pattern**:
1. Create a copy of a dimension table
2. Keep it disconnected (no relationships)
3. Use `CALCULATE` and `ALL` to manually control filter context
4. Common for parameter tables, what-if analysis, and comparative analysis

---

## References

- [Power BI Market Basket Analysis](https://docs.microsoft.com/power-bi/guidance/market-basket-analysis)
- [DAX Patterns - Disconnected Tables](https://www.daxpatterns.com/disconnected-tables/)
- [SQLBI - Market Basket Analysis in Power BI](https://www.sqlbi.com/)

---

## Version History

- **v1.0** (2026-01-29): Initial implementation
  - Created `dim_product_comparison` calculated table
  - Created `Orders containing both` measure
  - Documented setup and usage

---

## Support

For questions or issues with this implementation:
1. Review the troubleshooting section above
2. Check that your data model matches the requirements
3. Verify DAX syntax in DAX Studio or Power BI formula bar
4. Ensure Power BI Desktop is up to date

---

*This implementation is part of the Power BI Performance Dashboard project.*
