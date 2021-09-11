import requests
from sample_data import sample_data , transaction_report_mapping
import time

print('Start Checking to See if Elasticsearch Up')

def check_elastic():
    try:
        r = requests.get('http://opensearch-node:9200/_cluster/health')
        r = r.json()
        if r['status'] in ['green', 'yellow']:
            return True
    except:
        return False

while check_elastic() == False:
    print('Waiting For Elasticsearch to Come Up')
    time.sleep(6)

print('ElasticSearch Up Loading Data')

### Delete Existing Index
r = requests.delete('http://opensearch-node:9200/transaction-report', timeout=60)
print(r.text)

### Delete Existing Template
r = requests.delete('http://opensearch-node:9200/_index_template/transaction-report')
print(r.text)

### Load Mapping
r = requests.put('http://opensearch-node:9200/_index_template/transaction-report',
                   json=transaction_report_mapping)
print(r.text)

### Load Sample Data
r = requests.post('http://opensearch-node:9200/transaction-report/_doc/1', json=sample_data
)
print(r.text)
