import json

from emoji_skos import EMOJI_SKOS
from pathlib import Path


query = '''
prefix dc: <http://purl.org/dc/elements/1.1/>
prefix skos: <http://www.w3.org/2004/02/skos/core#>

select ?emoji ?label ?identifier
where {
    ?emoji a skos:Concept ;
        skos:prefLabel ?label ;
        dc:identifier ?identifier .
}
order by asc(?label)
'''

data = {
    '@context': {
        '@version': 1.1,
        'dc': 'http://purl.org/dc/elements/1.1/',
        'skos': 'http://www.w3.org/2004/02/skos/core#',
        'id': '@id',
        'identifier': {
            '@id': 'dc:identifier'
        },
        'label': {
            '@id': 'skos:preflabel'
        },
        'broadMatch': {
            '@id': 'skos:broadMatch'
        },
        'exactMatch': {
            '@id': 'skos:exactMatch'
        }
    },
    '@graph': []
}

result = EMOJI_SKOS.query(query)
for row in result:
    (emoji, label, identifier) = row
    obj = {'id': emoji, 'label': label, 'identifier': identifier}
    data['@graph'].append(obj)

print(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True))
