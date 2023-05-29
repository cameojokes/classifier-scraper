import os
import requests
from bs4 import BeautifulSoup

import settings


def getHitFactors(classifier, division):
    data = {
        'calculate': 'true',
        'selDiv': 2,
        'selClassifier': 2,
        'hitFactor': 1
    }
    headers = {
        'Cookie': 'session=' + os.environ.get('APP_SESSION_ID')
    }

    hit_factor_response = requests.post(
        settings.getHitFactorUrl(), data=data, headers=headers)
    hit_factor_node = BeautifulSoup(hit_factor_response.text, 'html.parser')

    hit_factor_rows = hit_factor_node.select('tbody > tr')

    hit_factors = [
        {
            'classification': row.select('td')[0].text.strip(),
            'minimum': row.select('td')[1].text.strip()
        } for row in hit_factor_rows
    ]

    return hit_factors
