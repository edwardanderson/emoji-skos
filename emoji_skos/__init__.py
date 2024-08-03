from emoji_skos.data import ALEXMICK, CARPEDM20
from pathlib import Path
from rdflib import Graph


EMOJI_SKOS = Graph()

for graph in [ALEXMICK, CARPEDM20]:
    EMOJI_SKOS += graph

broader_query_file = Path(__file__).parent / 'broader.rq'
with open(broader_query_file, 'r') as file:
    construct = file.read()

result = EMOJI_SKOS.query(construct)
EMOJI_SKOS += result
