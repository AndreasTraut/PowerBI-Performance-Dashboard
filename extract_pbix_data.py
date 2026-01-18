#!/usr/bin/env python3
"""
Script to extract data tables from Power BI PBIX file and save them as CSV files.
The PBIX file uses proprietary XPress9 compression which requires special handling.
"""

import os
import sys
import zipfile
import tempfile
import json
import subprocess
from pathlib import Path

def extract_pbix(pbix_path):
    """Extract PBIX file contents (PBIX is a ZIP file)"""
    temp_dir = tempfile.mkdtemp(prefix='pbix_extract_')
    print(f"Extracting PBIX to: {temp_dir}")
    
    with zipfile.ZipFile(pbix_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    return temp_dir

def list_files_in_extracted(temp_dir):
    """List all files in extracted PBIX"""
    print("\nExtracted files:")
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            rel_path = os.path.relpath(file_path, temp_dir)
            print(f"  {rel_path} ({size:,} bytes)")

def extract_with_dotnet(pbix_path, output_dir):
    """
    Use .NET and Power BI libraries to extract data.
    This requires Power BI or Analysis Services libraries.
    """
    try:
        # Try using DAX Studio or other tools via command line
        print("\nAttempting to use .NET tools for extraction...")
        
        # Note: This would require installing specific tools
        # For now, we'll document what's needed
        print("INFO: Direct extraction requires one of:")
        print("  1. Power BI Desktop with Export Data feature")
        print("  2. Tabular Editor 2/3 with data export capabilities")
        print("  3. DAX Studio for querying and exporting")
        print("  4. Custom .NET application using Microsoft.AnalysisServices libraries")
        
        return False
    except Exception as e:
        print(f"Error with .NET extraction: {e}")
        return False

def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_pbix_data.py <pbix-file> <output-directory>")
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
    
    # Extract PBIX contents
    temp_dir = extract_pbix(pbix_file)
    list_files_in_extracted(temp_dir)
    
    # Check for DataModel
    datamodel_path = os.path.join(temp_dir, 'DataModel')
    if os.path.exists(datamodel_path):
        size = os.path.getsize(datamodel_path)
        print(f"\nDataModel file found: {size:,} bytes")
        print("The DataModel is compressed with Microsoft XPress9 compression.")
        print("This requires specialized decompression tools.")
    
    # Try .NET extraction
    success = extract_with_dotnet(pbix_file, output_dir)
    
    if not success:
        print("\n" + "="*60)
        print("RECOMMENDATION:")
        print("="*60)
        print("To extract the actual data from the PBIX file, please use one of:")
        print("\n1. Power BI Desktop:")
        print("   - Open the PBIX file")
        print("   - Go to each table in Data view")
        print("   - Right-click on the table header")
        print("   - Select 'Copy Table' or export to CSV")
        print("\n2. Tabular Editor 2 (Free):")
        print("   - Open the PBIX file")
        print("   - Select a table")
        print("   - Use Scripts to export data to CSV")
        print("\n3. DAX Studio (Free):")
        print("   - Connect to the PBIX file")
        print("   - Query each table with: EVALUATE TableName")
        print("   - Export results to CSV")
        print("\nAlternatively, run the companion script 'generate_sample_data.py'")
        print("to create sample CSV files that match the schema.")
    
    # Cleanup
    import shutil
    shutil.rmtree(temp_dir)
    print(f"\nCleaned up temporary files: {temp_dir}")

if __name__ == "__main__":
    main()
