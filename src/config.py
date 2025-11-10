import pathlib

base_dir = pathlib.Path('.')
data_dir = base_dir / 'data'
output_dir = base_dir / 'outputs'

# GP catchment area data URL
gp_catchment_area_url = 'https://www.healthgis.nhs.uk/assets/shared/GP_catchments_data.zip'

# ODS API URL
ods_api_url = 'https://directory.spineservices.nhs.uk/ORD/2-0-0/'