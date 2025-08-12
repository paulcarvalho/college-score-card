""""
Download College Scorecard dataset from Kaggle
"""

from pathlib import Path
import kaggle.api

def main(download_path):
    # Create download directory
    Path(download_path).mkdir(parents=True, exist_ok=True)
    
    print(f"Downloading to: {download_path}")
    
    # Use the EXACT same code that works in Jupyter
    kaggle.api.dataset_download_files(
        'kaggle/college-scorecard',
        path=download_path,
        unzip=True
    )
    
    print("Download complete!")
    
    # Show what was downloaded
    data_dir = Path(download_path)
    files = list(data_dir.iterdir())
    print(f"Downloaded {len(files)} files:")
    for f in files:
        if f.is_file():
            print(f"  - {f.name}")

if __name__ == "__main__":
    print("College scorecard downloader")
    print("="*50)

    user_path = input("Enter download path:").strip()

    try:
        main(user_path)
        print("Download successful")
    except Exception as e:
        print("Download failed")
     