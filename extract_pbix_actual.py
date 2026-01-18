#!/usr/bin/env python3
"""
Attempt to extract actual data from PBIX DataModel.
The DataModel uses Microsoft XPress9 compression which is proprietary.
This script attempts multiple methods to decompress and extract the data.
"""

import os
import sys
import zipfile
import struct
import tempfile
import shutil

def extract_pbix(pbix_path):
    """Extract PBIX contents"""
    temp_dir = tempfile.mkdtemp(prefix='pbix_extract_')
    with zipfile.ZipFile(pbix_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    return temp_dir

def analyze_datamodel(datamodel_path):
    """Analyze the DataModel file structure"""
    with open(datamodel_path, 'rb') as f:
        # Read first few bytes
        header = f.read(100)
        
        print("DataModel header analysis:")
        print(f"  Size: {os.path.getsize(datamodel_path):,} bytes")
        print(f"  First 100 bytes (as string): {header[:100]}")
        
        # Check for compression signatures
        if b'XPress' in header or b'xpress' in header.lower():
            print("  ✓ Detected XPress compression signature")
        
        # Try to find JSON or XML content (uncompressed parts)
        f.seek(0)
        content = f.read(10000)
        
        if b'{' in content or b'<' in content:
            print("  ✓ Found potential JSON/XML content")
            # Try to extract it
            try:
                start_idx = content.find(b'{')
                if start_idx > 0:
                    print(f"  JSON starts at byte {start_idx}")
            except:
                pass

def try_decompress_xpress(compressed_data):
    """
    Attempt to decompress XPress compressed data.
    XPress is proprietary Microsoft compression.
    """
    try:
        # Try lz4 (similar to XPress in some cases)
        import lz4.block
        try:
            decompressed = lz4.block.decompress(compressed_data)
            return decompressed, "lz4"
        except:
            pass
    except ImportError:
        pass
    
    try:
        # Try zstandard
        import zstandard
        dctx = zstandard.ZstdDecompressor()
        try:
            decompressed = dctx.decompress(compressed_data)
            return decompressed, "zstandard"
        except:
            pass
    except ImportError:
        pass
    
    return None, None

def check_for_bim_file(temp_dir):
    """Check if there's a BIM (JSON) file we can parse"""
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            if file.endswith('.bim') or 'model' in file.lower():
                file_path = os.path.join(root, file)
                print(f"\nFound model file: {file_path}")
                
                # Try to read it
                try:
                    with open(file_path, 'rb') as f:
                        content = f.read(1000)
                        if content.startswith(b'{'):
                            print("  ✓ This appears to be a JSON file")
                            return file_path
                        else:
                            print("  ! This appears to be compressed")
                except:
                    pass
    return None

def extract_with_tabular_editor_command(pbix_path, output_dir):
    """
    Generate instructions for using Tabular Editor with command line.
    Tabular Editor 3 has CLI capabilities.
    """
    script = f"""
# PowerShell script to extract data using Tabular Editor 3 CLI (Windows only)
# Download Tabular Editor 3 from: https://tabulareditor.com/

$pbixPath = "{pbix_path}"
$outputDir = "{output_dir}"

# Example command (adjust path to your Tabular Editor installation)
$te3 = "C:\\Program Files\\Tabular Editor 3\\TabularEditor3.exe"

# Connect and export
& $te3 $pbixPath -S "ExportData.cs"

# Where ExportData.cs is a C# script that exports each table to CSV
"""
    
    script_path = os.path.join(output_dir, "extract_with_te3.ps1")
    with open(script_path, 'w') as f:
        f.write(script)
    
    print(f"\nGenerated PowerShell script: {script_path}")
    print("This script requires Tabular Editor 3 (Windows) to run")

def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_pbix_actual.py <pbix-file> <output-directory>")
        sys.exit(1)
    
    pbix_file = sys.argv[1]
    output_dir = sys.argv[2]
    
    if not os.path.exists(pbix_file):
        print(f"Error: PBIX file not found: {pbix_file}")
        sys.exit(1)
    
    print(f"="*70)
    print(f"Extracting data from: {pbix_file}")
    print(f"Output directory: {output_dir}")
    print(f"="*70)
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract PBIX
    print("\n1. Extracting PBIX archive...")
    temp_dir = extract_pbix(pbix_file)
    print(f"   ✓ Extracted to: {temp_dir}")
    
    try:
        # Check for BIM files
        print("\n2. Searching for model files...")
        bim_file = check_for_bim_file(temp_dir)
        
        # Analyze DataModel
        datamodel_path = os.path.join(temp_dir, 'DataModel')
        if os.path.exists(datamodel_path):
            print("\n3. Analyzing DataModel...")
            analyze_datamodel(datamodel_path)
            
            # Try to decompress
            print("\n4. Attempting decompression...")
            with open(datamodel_path, 'rb') as f:
                compressed_data = f.read()
            
            decompressed, method = try_decompress_xpress(compressed_data)
            
            if decompressed:
                print(f"   ✓ Successfully decompressed using {method}!")
                output_file = os.path.join(output_dir, 'DataModel_decompressed.bin')
                with open(output_file, 'wb') as f:
                    f.write(decompressed)
                print(f"   ✓ Saved to: {output_file}")
            else:
                print("   ✗ Standard decompression methods failed")
                print("   The DataModel uses proprietary Microsoft XPress9 compression")
        
        # Generate helper scripts
        print("\n5. Generating helper scripts...")
        extract_with_tabular_editor_command(pbix_file, output_dir)
        
        print("\n" + "="*70)
        print("CONCLUSION")
        print("="*70)
        print("\nThe PBIX DataModel uses Microsoft XPress9 compression which is")
        print("proprietary and not supported by standard Python libraries.")
        print("\nTo extract the actual data, please use one of these methods:")
        print("\n✓ DAX Studio (easiest):")
        print("  https://daxstudio.org/")
        print("\n✓ Tabular Editor 2/3:")
        print("  https://tabulareditor.com/")
        print("\n✓ Power BI Desktop:")
        print("  Transform Data → Export tables")
        print("\nSee data/README.md for detailed instructions.")
        print("="*70)
        
    finally:
        # Cleanup
        shutil.rmtree(temp_dir)
        print(f"\nCleaned up temporary files")

if __name__ == "__main__":
    main()
