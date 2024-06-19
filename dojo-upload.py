import argparse
import json
import os
import requests

def upload_results(host, api_key, scanner, product_name, result_file, engagement_name, verify=False):
    IMPORT_SCAN_URL = "http://" + host + "/api/v2/import-scan/"
    headers = {
        'accept': 'application/json',
        'X-CSRFTOKEN': '7K1ENl5uW1EyEsYczNMQCdcWdIEVJp0JWdrfDIZ2s3ojL5Yi57wRscmdsgzwzcBU',
        'Authorization': 'Token ' + api_key
    }
   
    files = {
        'product_type_name': (None, ''),
        'active': (None, 'true'),
        'endpoint_to_add': (None, ''),
        'verified': (None, 'true'),
        'close_old_findings': (None, 'true'),
        'test_title': (None, ''),
        'skip_duplicates': (None, 'true'),
        'engagement_name': (None, engagement_name),
        'build_id': (None, ''),
        'deduplication_on_engagement': (None, 'true'),
        'push_to_jira': (None, 'false'),
        'minimum_severity': (None, 'Low'),
        'close_old_findings_product_scope': (None, 'true'),
        'apply_tags_to_endpoints': (None, ''),
        'scan_date': (None, ''),
        'create_finding_groups_for_all_findings': (None, 'true'),
        'engagement_end_date': (None, ''),
        'environment': (None, ''),
        'service': (None, ''),
        'commit_hash': (None, ''),
        'group_by': (None, 'component_name'),
        'version': (None, ''),
        'tags': (None, ''),
        'apply_tags_to_findings': (None, ''),
        'api_scan_configuration': (None, ''),
        'product_name': (None, product_name),
        'file': (result_file, open(result_file, 'rb'), 'application/json'),
        'auto_create_context': (None, ''),
        'lead': (None, ''),
        'scan_type': (None, scanner),
        'branch_tag': (None, ''),
        'source_code_management_uri': (None, ''),
        'engagement': (None, ''),
    }

    response = requests.post(IMPORT_SCAN_URL, headers=headers, files=files)
    return response.status_code

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CI/CD integration for DefectDojo')
    parser.add_argument('--host', help="DefectDojo Hostname:port", required=True)
    parser.add_argument('--api_key', help="API V2 Key", required=True)
    parser.add_argument('--engagement_name', help="Engagement name", required=True)
    parser.add_argument('--result_file', help="Scanner file", required=True)
    parser.add_argument('--scanner', help="Type of scanner", required=True)
    parser.add_argument('--product_name', help="DefectDojo Product ID", required=True)

    args = vars(parser.parse_args())
    host = args["host"]
    api_key = args["api_key"]
    product_name = args["product_name"]
    result_file = args["result_file"]
    scanner = args["scanner"]
    engagement_name = args["engagement_name"]

    result = upload_results(host, api_key, scanner, product_name, result_file, engagement_name, verify=False)

    if result == 201:
        print("Successfully uploaded the results to Defect Dojo")
    else:
        print("Something went wrong, please debug " + str(result))
