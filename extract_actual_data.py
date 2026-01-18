#!/usr/bin/env python3
"""
Extract actual data from Power BI PBIX file using .NET libraries via pythonnet.
This script uses the Microsoft.AnalysisServices.Tabular library to read the model and export data.
"""

import os
import sys
import zipfile
import tempfile
import shutil
import csv
import clr  # pythonnet

def setup_analysis_services():
    """Load Analysis Services libraries"""
    try:
        # Add reference to Analysis Services
        clr.AddReference("System")
        clr.AddReference("System.IO")
        
        # Try to load Microsoft.AnalysisServices
        dll_path = "/home/runner/.nuget/packages/microsoft.analysisservices.netcore.retail.amd64/19.84.1/lib/netcoreapp3.0/Microsoft.AnalysisServices.Tabular.dll"
        
        if os.path.exists(dll_path):
            clr.AddReference(dll_path)
            import Microsoft.AnalysisServices.Tabular as Tabular
            return Tabular
        else:
            print(f"Analysis Services DLL not found at: {dll_path}")
            return None
    except Exception as e:
        print(f"Error loading Analysis Services: {e}")
        return None

def extract_pbix_to_temp(pbix_path):
    """Extract PBIX file to temporary directory"""
    temp_dir = tempfile.mkdtemp(prefix='pbix_extract_')
    print(f"Extracting PBIX to: {temp_dir}")
    
    with zipfile.ZipFile(pbix_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    return temp_dir

def extract_data_with_analysis_services(datamodel_path, output_dir):
    """Extract data using Analysis Services Tabular Object Model"""
    
    Tabular = setup_analysis_services()
    if not Tabular:
        return False
    
    try:
        # Create a server connection
        server = Tabular.Server()
        
        # Try to connect to the datamodel file
        # Note: This requires the file to be decompressed first
        print("Attempting to load datamodel...")
        
        # The DataModel file is compressed - we would need to decompress it first
        # This is the challenging part as it uses proprietary XPress9 compression
        
        print("INFO: DataModel uses XPress9 compression which requires special handling")
        return False
        
    except Exception as e:
        print(f"Error extracting with Analysis Services: {e}")
        return False

def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_actual_data.py <pbix-file> <output-directory>")
        sys.exit(1)
    
    pbix_file = sys.argv[1]
    output_dir = sys.argv[2]
    
    if not os.path.exists(pbix_file):
        print(f"Error: PBIX file not found: {pbix_file}")
        sys.exit(1)
    
    print(f"Extracting data from: {pbix_file}")
    print(f"Output directory: {output_dir}")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract PBIX
    temp_dir = extract_pbix_to_temp(pbix_file)
    
    try:
        # Check for DataModel
        datamodel_path = os.path.join(temp_dir, 'DataModel')
        if os.path.exists(datamodel_path):
            print(f"\nFound DataModel: {os.path.getsize(datamodel_path):,} bytes")
            
            # Try extraction
            success = extract_data_with_analysis_services(datamodel_path, output_dir)
            
            if not success:
                print("\n" + "="*70)
                print("ALTERNATIVE SOLUTION REQUIRED")
                print("="*70)
                print("\nThe DataModel in PBIX uses Microsoft XPress9 compression.")
                print("To extract the actual data, you have these options:")
                print("\n1. Use Power BI Desktop (Recommended):")
                print("   - Open: 'Performance Dashboard.pbix'")
                print("   - Transform data -> Transform data (opens Power Query Editor)")
                print("   - Right-click on each table -> Advanced Editor")
                print("   - Or export each table's data manually")
                print("\n2. Use DAX Studio (Free tool):")
                print("   - Download from: https://daxstudio.org/")
                print("   - Connect to the PBIX file")
                print("   - Run: EVALUATE 'TableName'")
                print("   - Export to CSV")
                print("\n3. Use Tabular Editor 2 (Free):")
                print("   - Download from: https://tabulareditor.com/")
                print("   - Open the PBIX/VPAX file")
                print("   - Use C# scripts to export table data")
                print("\n4. Generate sample data with matching schema:")
                print("   - Run: python generate_sample_data.py")
                print("="*70)
        
    finally:
        # Cleanup
        shutil.rmtree(temp_dir)
        print(f"\nCleaned up temporary files")

if __name__ == "__main__":
    main()
