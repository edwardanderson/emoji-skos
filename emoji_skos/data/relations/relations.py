
import json

from rdflib import Graph, URIRef
from rdflib.namespace import SKOS
from rdflib.util import from_n3
from pathlib import Path

# Build the graph iteratively, while RDFLib does not support parsing relative URIs.
# See <https://github.com/RDFLib/rdflib/issues/677>.

path = Path(__file__).parent / 'relations.json'
with open(path, 'r') as file:
    data = json.load(file)

RELATIONS = Graph()

context = data['@context']
predicate_uris = {}
for obj in data['@graph']:
    key = obj.pop('id')
    emoji = URIRef(key)
    for predicate in obj:
        if predicate not in predicate_uris:
            predicate_uri = from_n3(context[predicate]['@id'])
            predicate_uris[predicate] = predicate_uri

        values = obj[predicate]
        if not isinstance(values, list):
            continue

        for value in values:
            RELATIONS.add((emoji, predicate_uri, URIRef(value)))
