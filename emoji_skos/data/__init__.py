from emoji_skos.data.core import ALEXMICK, CARPEDM20
from pathlib import Path


EMOJI_SKOS = ALEXMICK
EMOJI_SKOS += CARPEDM20

# skos:exactMatch
path = Path(__file__).parent / 'exact_match.rq'
with open(path, 'r') as file:
    query = file.read()

result = EMOJI_SKOS.query(query)
EMOJI_SKOS += result.graph
