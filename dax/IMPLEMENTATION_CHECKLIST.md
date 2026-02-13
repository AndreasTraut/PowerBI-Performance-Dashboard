# Implementation Checklist - Market Basket Analysis

Use this checklist when implementing the Market Basket Analysis in Power BI Desktop.

---

## ✅ Pre-Implementation Checklist

- [ ] Power BI Desktop is installed and up to date
- [ ] The `Performance Dashboard.pbip` project file is accessible
- [ ] Backup of the original PBIX file is created
- [ ] You have reviewed the documentation in `/dax/README.md`

---

## 📋 Step-by-Step Implementation

### Step 1: Create Disconnected Table

- [ ] Open the project by opening the `Performance Dashboard.pbip` file in Power BI Desktop.
- [ ] Go to **Modeling** tab
- [ ] Click **New Table**
- [ ] Copy the DAX code from `/dax/dim_product_comparison.dax`:
  ```dax
  dim_product_comparison = dim_product
  ```
- [ ] Press **Enter** to create the table
- [ ] Verify the table appears in the Fields pane
- [ ] **IMPORTANT**: Confirm NO relationships exist for this table
  - Go to **Model View**
  - Check that `dim_product_comparison` has no relationship lines
  - If relationships exist, delete them (right-click → Delete)

**Verification**:
- [ ] `dim_product_comparison` table exists
- [ ] Table has same columns as `dim_product`
- [ ] Table is disconnected (no relationship lines in Model View)

---

### Step 2: Create Main Measure

- [ ] Go to **Modeling** tab (or stay in Modeling)
- [ ] Click **New Measure**
- [ ] Copy the DAX code from `/dax/Orders_containing_both.dax`
- [ ] Paste into formula bar
- [ ] Press **Enter** to create the measure
- [ ] Verify the measure appears in the Fields pane

**Verification**:
- [ ] Measure `Orders containing both` exists
- [ ] Measure shows no errors in formula bar
- [ ] Measure is visible in Fields pane

---

### Step 3: Test Basic Functionality

#### Create a Test Visual

- [ ] Add a **Card** visual to the canvas
- [ ] Add measure `Orders containing both` to the card
- [ ] Add a **Slicer** for `dim_product_comparison[ProductName]`
- [ ] Select a product in the slicer
- [ ] Verify the card shows a number (not blank or error)
- [ ] Add another **Slicer** for `dim_product[ProductName]`
- [ ] Select a product in this slicer too
- [ ] Verify the card updates and shows count of orders with both products

**Verification**:
- [ ] Selecting products updates the card value
- [ ] The two slicers work independently
- [ ] Measure shows reasonable values (not too high/low)

---

### Step 4: Create Product Affinity Matrix (Recommended)

- [ ] Add a **Matrix** visual to the canvas
- [ ] Configure the matrix:
  - **Rows**: Drag `dim_product[ProductName]` to Rows
  - **Columns**: Drag `dim_product_comparison[ProductName]` to Columns
  - **Values**: Drag `Orders containing both` to Values
- [ ] Resize the matrix to see multiple products
- [ ] Review the results - cells should show co-occurrence counts

**Optional Enhancements**:
- [ ] Add conditional formatting to highlight high values
  - Right-click on `Orders containing both` in Values
  - Select **Conditional formatting** → **Background color**
  - Choose a color scale (e.g., white to green)
- [ ] Filter to top products for better performance
  - Click on `dim_product[ProductName]` in Rows
  - Add a Top N filter (e.g., Top 20 by Sales)

**Verification**:
- [ ] Matrix displays product names on rows and columns
- [ ] Cells show co-occurrence counts
- [ ] Diagonal cells (same product) can be ignored
- [ ] Values make business sense

---

### Step 5: Add Optional Measures (Recommended)

Choose measures from `/dax/additional_measures.dax` based on your needs:

#### Essential Measures (Highly Recommended):

- [ ] **Co-occurrence Rate %**
  - Shows percentage of Product 1's orders that include Product 2
  - Copy from `additional_measures.dax` → Paste as new measure
  
- [ ] **Lift**
  - Shows strength of association (>1 = strong, =1 = random, <1 = weak)
  - Copy from `additional_measures.dax` → Paste as new measure

#### Supporting Measures (Good to Have):

- [ ] **Orders with Product 1**
  - Total orders containing Product 1
  
- [ ] **Orders with Product 2**
  - Total orders containing Product 2

#### Advanced Measures (Optional):

- [ ] **Support %** - Overall frequency of the pair
- [ ] **Jaccard Similarity %** - Alternative similarity metric
- [ ] **Is Strong Association** - Boolean filter for strong pairs

**Verification**:
- [ ] All selected measures are created without errors
- [ ] Measures show in Fields pane
- [ ] Test each measure in a card visual

---

### Step 6: Create Business Dashboard

#### Option A: Executive Summary Card

Create a dashboard with:
- [ ] Two slicers: One for each product table
- [ ] Card showing `Orders containing both`
- [ ] Card showing `Co-occurrence Rate %`
- [ ] Card showing `Lift`

#### Option B: Detailed Analysis Matrix

Create a matrix showing:
- [ ] Rows: Product names from `dim_product`
- [ ] Columns: Product names from `dim_product_comparison`
- [ ] Values: Multiple measures
  - `Orders containing both`
  - `Co-occurrence Rate %`
  - `Lift`

#### Option C: Top Pairs Table

Create a table showing:
- [ ] Column: `Product Pair` (calculated measure from `additional_measures.dax`)
- [ ] Column: `Orders containing both`
- [ ] Column: `Lift`
- [ ] Filter: Top 20 by `Orders containing both`
- [ ] Sort: Descending by `Orders containing both`

**Verification**:
- [ ] Dashboard is visually clear
- [ ] Filters work correctly
- [ ] Values update when selections change
- [ ] Insights are actionable

---

## 🧪 Testing & Validation

### Data Accuracy Tests

- [ ] **Test 1: Known Product Pair**
  - Select two products you know are sold together
  - Verify the count matches your expectations
  - Compare with manual SQL query if possible

- [ ] **Test 2: Independent Products**
  - Select two products from different categories unlikely to be sold together
  - Verify count is low or zero

- [ ] **Test 3: Same Product**
  - Select same product in both slicers
  - Count should equal total orders for that product
  - (Or implement logic to show BLANK for same product)

### Performance Tests

- [ ] **Test with Full Dataset**
  - Remove all filters
  - Check if matrix loads in reasonable time (<10 seconds)
  - If slow, implement Top N filters

- [ ] **Test with Slicers**
  - Apply various slicer combinations
  - Verify responsiveness

### Edge Case Tests

- [ ] **No Selection**: Verify measure shows BLANK when no product is selected
- [ ] **Single Selection**: Verify measure shows BLANK when only one product is selected
- [ ] **Date Filters**: Apply date slicers and verify counts update correctly

**Verification**:
- [ ] All tests pass
- [ ] No errors appear in visuals
- [ ] Performance is acceptable

---

## 📊 Documentation

- [ ] Add a text box to your report explaining how to use the analysis
- [ ] Document any custom filters or modifications
- [ ] Save the PBIX file with a new version number
- [ ] Export documentation to PDF if needed

---

## 🎯 Business Use Cases to Validate

Test these real-world scenarios:

- [ ] **Cross-Selling**: Find top 5 products to recommend with Product X
- [ ] **Bundle Creation**: Identify product pairs with Lift > 2
- [ ] **Inventory Planning**: Find products frequently bought together
- [ ] **Marketing Campaigns**: Target customers who buy Product A with offers for Product B

---

## 🐛 Troubleshooting

If you encounter issues, check:

- [ ] `dim_product_comparison` has no relationships (most common issue)
- [ ] Column names match exactly (`ProductID`, `ProductName`, `OrderID`)
- [ ] `fact_sales` table exists and has required columns
- [ ] Relationships between `dim_product` and `fact_sales` are active
- [ ] DAX syntax is correct (no typos)
- [ ] Power BI Desktop version supports DAX functions used

**Common Issues**:

| Issue | Solution |
|-------|----------|
| Measure always blank | Select a product from `dim_product_comparison` |
| All values the same | Delete relationships from `dim_product_comparison` |
| Performance slow | Add Top N filters, aggregate data |
| Errors in DAX | Check column names match your model |

---

## ✨ Post-Implementation

After successful implementation:

- [ ] Save the PBIX file
- [ ] Test with stakeholders
- [ ] Gather feedback on insights
- [ ] Schedule data refresh (if using Power BI Service)
- [ ] Share findings with business teams
- [ ] Document key insights discovered
- [ ] Plan next steps (bundles, campaigns, etc.)

---

## 📚 Additional Resources

- See `/dax/README.md` for detailed technical documentation
- See `/dax/EXAMPLES.md` for visualization examples
- See `/dax/SCHNELLANLEITUNG.md` for German quick guide
- See Power BI documentation for DAX help

---

## ✅ Final Checklist

Before considering implementation complete:

- [ ] All measures created and working
- [ ] At least one visual created and tested
- [ ] Data accuracy validated
- [ ] Performance is acceptable
- [ ] Documentation is in place
- [ ] Stakeholders briefed on how to use
- [ ] Backup of working PBIX file saved

---

**Implementation Status**: ⬜ Not Started | 🟡 In Progress | ✅ Complete

**Date Completed**: _______________

**Implemented By**: _______________

**Notes**: 

```
[Add any notes about customizations, issues encountered, or specific decisions made]
```

---

*This checklist is part of the Power BI Performance Dashboard - Market Basket Analysis implementation.*
