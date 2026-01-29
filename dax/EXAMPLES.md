# Market Basket Analysis - Implementation Examples

## Visual Setup Guide

This document provides visual instructions and examples for implementing the Market Basket Analysis in Power BI.

---

## Example 1: Product Affinity Matrix

### Visual Type: Matrix

**Purpose**: Show a complete grid of how often each product pair appears together in orders.

### Configuration:
```
Matrix Visual:
├─ Rows: dim_product[ProductName]
├─ Columns: dim_product_comparison[ProductName]
└─ Values: Orders containing both
```

### Expected Output:
```
                     | Laptop A | Laptop B | Mouse X | Keyboard Y |
---------------------|----------|----------|---------|------------|
Laptop A             |    -     |    15    |   89    |    67      |
Laptop B             |    15    |    -     |   45    |    34      |
Mouse X              |    89    |    45    |   -     |   123      |
Keyboard Y           |    67    |    34    |  123    |    -       |
```

**Interpretation**:
- Diagonal cells can be hidden (a product always appears with itself)
- High values indicate strong product affinity
- Example: Mouse X and Keyboard Y appear together in 123 orders

### Conditional Formatting (Recommended):
- Background color scales: Higher values → Darker color
- Helps identify strong relationships at a glance

---

## Example 2: Top Product Combinations for a Specific Product

### Visual Type: Table or Bar Chart

**Purpose**: For a selected product, show which other products are most frequently bought together.

### Configuration:
```
Slicer:
└─ dim_product[ProductName] = "TechPro Laptops Model 1"

Table Visual:
├─ Column 1: dim_product_comparison[ProductName]
├─ Column 2: Orders containing both
└─ Sort by: Orders containing both (Descending)
```

### Expected Output:
```
Comparison Product          | Orders containing both
----------------------------|----------------------
Premium Mouse Pro           |          156
TechPro Keyboard Elite      |          142
Premium Monitor 27"         |          98
SmartHome USB Hub           |          76
Premium Headphones          |          54
```

**Business Use Case**:
- Cross-selling recommendations
- Bundle creation
- Product placement strategies

---

## Example 3: Category Cross-Selling Analysis

### Visual Type: Matrix with Category Hierarchy

**Purpose**: Analyze which product categories are bought together.

### Configuration:
```
Matrix Visual:
├─ Rows: dim_product[Category] → dim_product[ProductName]
├─ Columns: dim_product_comparison[Category] → dim_product_comparison[ProductName]
└─ Values: Orders containing both
```

### Expected Output:
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

**Insights**:
- Laptops and Mice have high affinity (456 orders)
- Mice and Keyboards are frequently bought together (567 orders)
- Cross-category patterns inform bundle strategies

---

## Example 4: Interactive Product Comparison Dashboard

### Layout:
```
┌────────────────────────────────────────────────┐
│  Select Product 1:         Select Product 2:  │
│  [Slicer: dim_product]     [Slicer: dim_...   │
│                            product_comparison] │
├────────────────────────────────────────────────┤
│  Orders containing both:                       │
│  ┌──────────┐                                  │
│  │   142    │  (Card Visual)                   │
│  └──────────┘                                  │
├────────────────────────────────────────────────┤
│  Details:                                      │
│  Orders with Product 1 only:      234          │
│  Orders with Product 2 only:      198          │
│  Co-occurrence Rate:              60.7%        │
│  Lift:                            2.34         │
└────────────────────────────────────────────────┘
```

### KPIs Explained:

**Orders containing both**: 142
- Direct count of orders with both products

**Orders with Product 1 only**: 234
- Total orders containing Product 1

**Co-occurrence Rate**: 60.7%
- Formula: (142 / 234) × 100
- Meaning: 60.7% of Product 1's orders also include Product 2

**Lift**: 2.34
- Lift > 1 means products are bought together MORE than expected by chance
- Lift = 1 means no special affinity (random)
- Lift < 1 means products are rarely bought together

---

## Example 5: Top 10 Product Pairs

### Visual Type: Table with Both Products

**Purpose**: Discover the strongest product combinations overall.

### DAX for Combined Product Pair:
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

### Configuration:
```
Table Visual:
├─ Column 1: Product Pair (calculated measure above)
├─ Column 2: Orders containing both
├─ Top N Filter: Top 10 by Orders containing both
└─ Sort by: Orders containing both (Descending)
```

### Expected Output:
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

## Example 6: Heatmap Visualization

### Visual Type: Matrix with Conditional Formatting

**Purpose**: Visual heatmap to quickly identify strong product relationships.

### Configuration:
```
Matrix Visual:
├─ Rows: dim_product[ProductName] (Filter to Top 20 products)
├─ Columns: dim_product_comparison[ProductName] (Filter to Top 20 products)
└─ Values: Orders containing both

Conditional Formatting:
├─ Based on: Orders containing both
├─ Color Scale: White (0) → Green (Low) → Dark Green (High)
└─ Show values: Optional
```

### Visual Appearance:
```
         | Prod1 | Prod2 | Prod3 | Prod4 |
---------|-------|-------|-------|-------|
Prod1    |  ███  |  ░░░  |  ▓▓▓  |  ░░░  |
Prod2    |  ░░░  |  ███  |  ▒▒▒  |  ▓▓▓  |
Prod3    |  ▓▓▓  |  ▒▒▒  |  ███  |  ░░░  |
Prod4    |  ░░░  |  ▓▓▓  |  ░░░  |  ███  |

Legend: ░░░ = Low    ▒▒▒ = Medium    ▓▓▓ = High    ███ = Same product
```

**Benefits**:
- Quick pattern recognition
- Identify clusters of related products
- Spot anomalies or unexpected combinations

---

## Best Practices

### 1. Performance Optimization
- **Filter to Top N products** for large datasets
- Pre-aggregate common pairs in a summary table if needed
- Use slicers to reduce the data volume

### 2. User Experience
- **Clear labels**: Use product names, not IDs
- **Sort by affinity**: Show highest counts first
- **Contextual help**: Add tooltips explaining the metrics

### 3. Business Application
- **Bundle creation**: Products with high co-occurrence
- **Cross-sell prompts**: "Customers who bought X also bought Y"
- **Inventory planning**: Stock related products together
- **Marketing campaigns**: Promote product pairs with high affinity

### 4. Data Quality Checks
- Exclude cancelled orders: `Filter fact_orders where OrderStatus = "Completed"`
- Minimum order count: Only show pairs with at least 5 occurrences
- Date filters: Analyze recent trends vs. historical patterns

---

## Advanced Measures (Optional)

### Support (%)
Shows what percentage of ALL orders contain this product pair.

```dax
Support % = 
VAR OrdersBoth = [Orders containing both]
VAR TotalOrders = CALCULATE(DISTINCTCOUNT(fact_orders[OrderID]), ALL())
RETURN
    DIVIDE(OrdersBoth, TotalOrders, 0) * 100
```

### Confidence (%)
Given Product 1 is purchased, what's the probability Product 2 is also purchased?

```dax
Confidence % = 
VAR OrdersBoth = [Orders containing both]
VAR OrdersProduct1 = [Orders with Product 1]
RETURN
    DIVIDE(OrdersBoth, OrdersProduct1, 0) * 100
```

### Lift
How much more likely are these products bought together vs. independently?

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
- **Lift = 1**: No association (random)
- **Lift > 1**: Positive association (bought together more often)
- **Lift < 1**: Negative association (rarely bought together)

**Example**:
- Support = 2%: This pair appears in 2% of all orders
- Confidence = 40%: When Product 1 is bought, Product 2 follows 40% of the time
- Lift = 2.5: This pair occurs 2.5× more often than expected by chance

---

## Troubleshooting Visualizations

### Issue: Blank values in matrix
**Cause**: No product selected from dim_product_comparison
**Solution**: Add a slicer or ensure columns are from dim_product_comparison

### Issue: All cells show the same value
**Cause**: dim_product_comparison has relationships (should be disconnected)
**Solution**: Delete any relationships to dim_product_comparison

### Issue: Performance is slow
**Solution**: 
- Filter to top products (e.g., top 50 by sales)
- Use aggregations
- Optimize DAX with variables

### Issue: Diagonal cells (same product) show high values
**Expected**: A product always appears with itself
**Solution**: 
- Filter out: Add measure logic to show BLANK() when Product1 = Product2
- Or simply ignore diagonal values in interpretation

---

## Next Steps

1. **Implement the basic matrix** (Example 1)
2. **Add slicers** for interactive exploration
3. **Create focused views** for specific use cases (cross-selling, bundles)
4. **Add advanced metrics** (Lift, Confidence, Support)
5. **Build recommendation engine** based on top product pairs
6. **Schedule refreshes** to keep analysis current

---

*For DAX code, see the files in the `/dax` directory.*
