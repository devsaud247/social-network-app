import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def make_request_with_retries(url):
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[500, 502, 503, 504],
        method_whitelist=["GET", "POST"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    response = session.get(url)
    return response
