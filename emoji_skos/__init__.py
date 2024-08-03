from emoji_skos.data import ALEXMICK, CARPEDM20, RELATIONS
from rdflib import Graph, URIRef
from rdflib.namespace import SKOS


EMOJI_SKOS = Graph()

for graph in [ALEXMICK, CARPEDM20, RELATIONS]:
    EMOJI_SKOS += graph

# :human skos:broader :person
humans = ['👨', '👩', '👩', '👶']
for item in humans:
    EMOJI_SKOS.add((URIRef(item), SKOS.broader, URIRef('🧑')))
