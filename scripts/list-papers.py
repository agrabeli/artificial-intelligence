import requests

# see: http://libguides.mit.edu/apis
#      http://arxiv.org/help/api/index
arxiv_base_url = "http://export.arxiv.org/api/query"
output_file_path = "somefile.csv"

r = requests.get(arxiv_base_url, params={"search_query": "all:artificial intelligence",
                                         "start": 0})
print r.text
