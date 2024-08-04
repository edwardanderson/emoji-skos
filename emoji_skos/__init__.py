from emoji_skos.data import ALEXMICK, CARPEDM20, RELATIONS
from pathlib import Path
from rdflib import Graph, URIRef
from rdflib.namespace import SKOS


EMOJI_SKOS = Graph()

for graph in [ALEXMICK, CARPEDM20, RELATIONS]:
    EMOJI_SKOS += graph

# :human skos:broader :person
humans = ['👨', '👩', '👩', '👶']
for item in humans:
    EMOJI_SKOS.add((URIRef(item), SKOS.broader, URIRef('🧑')))

# owl:sameAs
path = Path(__file__).parent / 'same_as.rq'
with open(path, 'r') as file:
    query = file.read()

same_as = EMOJI_SKOS.query(query)
EMOJI_SKOS += same_as
