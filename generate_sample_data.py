#!/usr/bin/env python3
"""
Generate sample CSV data files that match the Power BI Performance Dashboard schema.
Based on the dashboard requirements: Sales, Customers, Orders, and Returns analysis.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import random

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

def generate_date_dimension(start_date='2022-01-01', end_date='2024-12-31'):
    """Generate date dimension table"""
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    df = pd.DataFrame({
        'DateKey': [int(d.strftime('%Y%m%d')) for d in dates],
        'Date': dates,
        'Year': dates.year,
        'Quarter': dates.quarter,
        'Month': dates.month,
        'MonthName': dates.strftime('%B'),
        'MonthShort': dates.strftime('%b'),
        'Week': dates.isocalendar().week,
        'DayOfWeek': dates.dayofweek + 1,
        'DayName': dates.strftime('%A'),
        'DayShort': dates.strftime('%a'),
        'DayOfMonth': dates.day,
        'DayOfYear': dates.dayofyear,
        'IsWeekend': dates.dayofweek >= 5,
        'YearMonth': dates.strftime('%Y-%m'),
        'YearQuarter': dates.year.astype(str) + '-Q' + dates.quarter.astype(str)
    })
    
    return df

def generate_geography_dimension():
    """Generate geography dimension with countries, regions, etc."""
    geographies = [
        # Americas
        {'GeographyKey': 1, 'Country': 'USA', 'Region': 'Americas', 'Continent': 'North America'},
        {'GeographyKey': 2, 'Country': 'Canada', 'Region': 'Americas', 'Continent': 'North America'},
        {'GeographyKey': 3, 'Country': 'Mexico', 'Region': 'Americas', 'Continent': 'North America'},
        {'GeographyKey': 4, 'Country': 'Brazil', 'Region': 'Americas', 'Continent': 'South America'},
        
        # Europe
        {'GeographyKey': 5, 'Country': 'Germany', 'Region': 'Europe', 'Continent': 'Europe'},
        {'GeographyKey': 6, 'Country': 'France', 'Region': 'Europe', 'Continent': 'Europe'},
        {'GeographyKey': 7, 'Country': 'UK', 'Region': 'Europe', 'Continent': 'Europe'},
        {'GeographyKey': 8, 'Country': 'Spain', 'Region': 'Europe', 'Continent': 'Europe'},
        {'GeographyKey': 9, 'Country': 'Italy', 'Region': 'Europe', 'Continent': 'Europe'},
        
        # Asia
        {'GeographyKey': 10, 'Country': 'China', 'Region': 'Asia', 'Continent': 'Asia'},
        {'GeographyKey': 11, 'Country': 'Japan', 'Region': 'Asia', 'Continent': 'Asia'},
        {'GeographyKey': 12, 'Country': 'India', 'Region': 'Asia', 'Continent': 'Asia'},
        {'GeographyKey': 13, 'Country': 'Australia', 'Region': 'Asia', 'Continent': 'Oceania'},
    ]
    
    return pd.DataFrame(geographies)

def generate_product_dimension():
    """Generate product dimension with categories, subcategories, SKUs, brands"""
    brands = ['TechPro', 'SmartHome', 'ActiveLife', 'EcoGear', 'Premium']
    categories = ['Electronics', 'Home & Garden', 'Sports & Outdoors', 'Clothing']
    
    subcategories = {
        'Electronics': ['Laptops', 'Phones', 'Tablets', 'Accessories'],
        'Home & Garden': ['Furniture', 'Kitchen', 'Decor', 'Tools'],
        'Sports & Outdoors': ['Fitness', 'Camping', 'Cycling', 'Water Sports'],
        'Clothing': ['Men', 'Women', 'Kids', 'Accessories']
    }
    
    products = []
    product_id = 1
    
    for category in categories:
        for subcategory in subcategories[category]:
            for i in range(10):  # 10 products per subcategory
                brand = random.choice(brands)
                products.append({
                    'ProductKey': product_id,
                    'SKU': f'SKU{product_id:05d}',
                    'ProductName': f'{brand} {subcategory} Model {i+1}',
                    'Category': category,
                    'SubCategory': subcategory,
                    'Brand': brand,
                    'UnitCost': round(random.uniform(10, 500), 2),
                    'UnitPrice': round(random.uniform(20, 1000), 2),
                })
                product_id += 1
    
    df = pd.DataFrame(products)
    df['GrossMargin'] = ((df['UnitPrice'] - df['UnitCost']) / df['UnitPrice'] * 100).round(2)
    return df

def generate_customer_dimension(n_customers=5000):
    """Generate customer dimension"""
    customer_types = ['B2B', 'B2C']
    priority_levels = ['High', 'Medium', 'Low']
    channels = ['Online', 'Retail', 'Partner', 'Direct']
    
    customers = []
    for i in range(1, n_customers + 1):
        # First customer appears in 2022, others spread across time
        first_order_date = datetime(2022, 1, 1) + timedelta(days=random.randint(0, 730))
        
        customers.append({
            'CustomerKey': i,
            'CustomerID': f'CUST{i:06d}',
            'CustomerName': f'Customer {i}',
            'CustomerType': random.choice(customer_types),
            'PriorityLevel': random.choice(priority_levels),
            'Channel': random.choice(channels),
            'FirstOrderDate': first_order_date.strftime('%Y-%m-%d'),
            'GeographyKey': random.randint(1, 13)
        })
    
    return pd.DataFrame(customers)

def generate_fact_orders(customers, products, dates, n_orders=50000):
    """Generate orders fact table"""
    order_statuses = ['Completed', 'Completed', 'Completed', 'Completed', 'Completed', 
                      'Cancelled', 'Pending', 'Processing']
    delivery_statuses = ['On-Time', 'On-Time', 'On-Time', 'On-Time', 'Late', 'Early']
    
    orders = []
    order_id = 1
    
    # Get date keys for the period
    date_keys = dates['DateKey'].values
    min_date = dates['Date'].min()
    
    for _ in range(n_orders):
        # Pick a random date
        order_date_key = random.choice(date_keys)
        order_date = pd.to_datetime(str(order_date_key), format='%Y%m%d')
        
        # Pick customer
        customer_key = random.randint(1, len(customers))
        customer = customers[customers['CustomerKey'] == customer_key].iloc[0]
        
        # Ensure order date is after customer's first order date
        first_order = pd.to_datetime(customer['FirstOrderDate'])
        if order_date < first_order:
            continue
        
        # Pick products for this order (1-5 items)
        n_items = random.randint(1, 5)
        order_products = products.sample(n=n_items)
        
        status = random.choice(order_statuses)
        
        for _, product in order_products.iterrows():
            quantity = random.randint(1, 10)
            unit_price = product['UnitPrice'] * random.uniform(0.9, 1.1)  # Some price variation
            
            # Calculate dates
            processing_days = random.randint(1, 3)
            shipping_days = random.randint(2, 14)
            delivery_date = order_date + timedelta(days=processing_days + shipping_days)
            expected_delivery = order_date + timedelta(days=7)
            
            orders.append({
                'OrderKey': order_id,
                'OrderID': f'ORD{order_id:08d}',
                'OrderLineID': f'ORD{order_id:08d}-{_+1}',
                'OrderDateKey': order_date_key,
                'OrderDate': order_date.strftime('%Y-%m-%d'),
                'CustomerKey': customer_key,
                'ProductKey': product['ProductKey'],
                'Quantity': quantity,
                'UnitPrice': round(unit_price, 2),
                'LineTotal': round(quantity * unit_price, 2),
                'UnitCost': product['UnitCost'],
                'COGS': round(quantity * product['UnitCost'], 2),
                'OrderStatus': status,
                'DeliveryStatus': random.choice(delivery_statuses) if status == 'Completed' else None,
                'ExpectedDeliveryDate': expected_delivery.strftime('%Y-%m-%d'),
                'ActualDeliveryDate': delivery_date.strftime('%Y-%m-%d') if status == 'Completed' else None,
            })
            order_id += 1
    
    df = pd.DataFrame(orders)
    df['GrossProfit'] = df['LineTotal'] - df['COGS']
    return df

def generate_fact_returns(orders, dates):
    """Generate returns fact table (about 5% of orders)"""
    return_reasons = [
        'Defective', 'Wrong Item', 'Not as Described', 'Changed Mind', 
        'Too Late', 'Damaged in Transit', 'Quality Issues', 'Other'
    ]
    return_statuses = ['Processed', 'Processing', 'Pending', 'Rejected']
    
    # Sample orders to return
    sample_orders = orders[orders['OrderStatus'] == 'Completed'].sample(frac=0.05, random_state=42)
    
    returns = []
    return_id = 1
    
    for _, order in sample_orders.iterrows():
        order_date = pd.to_datetime(order['OrderDate'])
        # Return happens 1-60 days after order
        return_date = order_date + timedelta(days=random.randint(1, 60))
        return_date_key = int(return_date.strftime('%Y%m%d'))
        
        # Only return if return date exists in our date dimension
        if return_date_key not in dates['DateKey'].values:
            continue
        
        return_quantity = random.randint(1, order['Quantity'])
        
        returns.append({
            'ReturnKey': return_id,
            'ReturnID': f'RET{return_id:08d}',
            'ReturnDateKey': return_date_key,
            'ReturnDate': return_date.strftime('%Y-%m-%d'),
            'OrderKey': order['OrderKey'],
            'OrderID': order['OrderID'],
            'CustomerKey': order['CustomerKey'],
            'ProductKey': order['ProductKey'],
            'ReturnQuantity': return_quantity,
            'ReturnAmount': round(return_quantity * order['UnitPrice'], 2),
            'ReturnReason': random.choice(return_reasons),
            'ReturnStatus': random.choice(return_statuses),
        })
        return_id += 1
    
    return pd.DataFrame(returns)

def main():
    print("Generating sample data for Power BI Performance Dashboard...")
    
    # Create output directory
    output_dir = '/home/runner/work/PowerBI-Performance-Dashboard/PowerBI-Performance-Dashboard/data'
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate dimensions
    print("Generating date dimension...")
    dim_date = generate_date_dimension()
    dim_date.to_csv(os.path.join(output_dir, 'dim_date.csv'), index=False)
    print(f"  Created dim_date.csv ({len(dim_date)} rows)")
    
    print("Generating geography dimension...")
    dim_geography = generate_geography_dimension()
    dim_geography.to_csv(os.path.join(output_dir, 'dim_geography.csv'), index=False)
    print(f"  Created dim_geography.csv ({len(dim_geography)} rows)")
    
    print("Generating product dimension...")
    dim_product = generate_product_dimension()
    dim_product.to_csv(os.path.join(output_dir, 'dim_product.csv'), index=False)
    print(f"  Created dim_product.csv ({len(dim_product)} rows)")
    
    print("Generating customer dimension...")
    dim_customer = generate_customer_dimension(n_customers=5000)
    dim_customer.to_csv(os.path.join(output_dir, 'dim_customer.csv'), index=False)
    print(f"  Created dim_customer.csv ({len(dim_customer)} rows)")
    
    # Generate facts
    print("Generating orders fact table...")
    fact_orders = generate_fact_orders(dim_customer, dim_product, dim_date, n_orders=50000)
    fact_orders.to_csv(os.path.join(output_dir, 'fact_orders.csv'), index=False)
    print(f"  Created fact_orders.csv ({len(fact_orders)} rows)")
    
    print("Generating returns fact table...")
    fact_returns = generate_fact_returns(fact_orders, dim_date)
    fact_returns.to_csv(os.path.join(output_dir, 'fact_returns.csv'), index=False)
    print(f"  Created fact_returns.csv ({len(fact_returns)} rows)")
    
    # Generate a sales view (aggregated from orders)
    print("Generating sales fact table...")
    fact_sales = fact_orders.groupby(['OrderKey', 'OrderID', 'OrderDateKey', 'OrderDate', 'CustomerKey']).agg({
        'LineTotal': 'sum',
        'COGS': 'sum',
        'GrossProfit': 'sum',
        'Quantity': 'sum'
    }).reset_index()
    fact_sales.rename(columns={
        'OrderKey': 'SalesKey',
        'OrderID': 'SalesID',
        'OrderDateKey': 'SalesDateKey',
        'OrderDate': 'SalesDate',
        'LineTotal': 'GrossSales',
        'Quantity': 'TotalQuantity'
    }, inplace=True)
    fact_sales['NetSales'] = fact_sales['GrossSales'] - (fact_sales['GrossSales'] * 0.05)  # 5% discount
    fact_sales.to_csv(os.path.join(output_dir, 'fact_sales.csv'), index=False)
    print(f"  Created fact_sales.csv ({len(fact_sales)} rows)")
    
    print(f"\n✓ All CSV files generated successfully in: {output_dir}")
    print("\nGenerated files:")
    for file in sorted(os.listdir(output_dir)):
        if file.endswith('.csv'):
            filepath = os.path.join(output_dir, file)
            size = os.path.getsize(filepath) / 1024  # KB
            print(f"  - {file} ({size:.1f} KB)")

if __name__ == "__main__":
    main()
