# DefectDojo Scan results importer
Upload scan results from the Security tools into Self hosted Defect Dojo with this simple python script
## requirement
Python3 
pip install argparse
pip install requests
pip install os

## Setup Defect Dojo with Docker compose
https://github.com/DefectDojo/django-DefectDojo/blob/master/readme-docs/DOCKER.md


## script usage
python3 dojo-upload.py 
-host HOST ( Hostname/hostip:port, currently supports HTTP only)  
--api_key API_KEY ( Currently support API V2 keys only)
--engagement_name ENGAGEMENT_NAME ( Engagement name)
--result_file RESULT_FILE  (Scanner Output file name: Refer to link for format: https://defectdojo.com/integrations)
--scanner SCANNER (Scanner Name: Refer to link for naming convention: https://defectdojo.com/integrations)
--product_name PRODUCT_NAME (
