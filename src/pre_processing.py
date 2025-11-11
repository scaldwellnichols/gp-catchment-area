import os
import requests
import zipfile
import pathlib

import src.config as config

def download_and_extract_gp_catchment_data():
    """
    Downloads and extracts the GP catchment area data from the NHS Health GIS website.
    """
    os.makedirs(config.data_dir, exist_ok=True)

    zip_path = config.data_dir / pathlib.Path(config.gp_catchment_area_url).name

    # Download the file
    with requests.get(config.gp_catchment_area_url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(zip_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

    # Extract the zip into ./data
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(config.data_dir)