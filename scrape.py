import re
import json

import requests
from bs4 import BeautifulSoup

import settings
import hf

classifiers_response = requests.post(settings.getClassifierUrl())
classifier_node = BeautifulSoup(classifiers_response.text, 'html.parser')

division_elements = classifier_node.select('#calc_selDiv > option')
divisions = [{'id': opt.get('value'), 'name': opt.text}
             for opt in division_elements]

classifier_elements = classifier_node.select('#calc_selClassifier > option')
classifiers = [
    {
        'id': opt.get('value'),
        'stage_number': re.split('\s{7}', opt.text)[0],
        'name': re.split('\s{7}', opt.text)[1]
    } for opt in classifier_elements
]

# print(divisions[0:1])

for classifier in classifiers[0:1]:
    classifier['divisions'] = {
        division['name'].lower(): hf.getHitFactors(classifier, division)
        for division in divisions[0:1]
    }

output = {
    'classifiers': classifiers,
    'divisions': divisions
}


print(json.dumps(output))
