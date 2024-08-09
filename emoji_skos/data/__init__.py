from emoji_skos.data.core import ALEXMICK, CARPEDM20
from pathlib import Path


EMOJI_SKOS = ALEXMICK
EMOJI_SKOS += CARPEDM20

# skos:exactMatch
path = Path(__file__).parent / 'exact_match.rq'
query = path.read_text()
result = EMOJI_SKOS.query(query)
EMOJI_SKOS += result.graph

if __name__ == '__main__':
    print(EMOJI_SKOS.serialize(format='longturtle'))
