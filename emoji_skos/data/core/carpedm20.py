# The <https://github.com/carpedm20/emoji> dataset contains multi-lingual
# label information.


from emoji import EMOJI_DATA
from emoji_data_python import emoji_data, unified_to_char
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import DC, RDF, SKOS


def sanitise_label(label: str) -> str:
    sanitised = (
        label
        .replace(':', '')
        .replace('_', ' ')
    )
    return sanitised


CARPEDM20 = Graph()

languages = [
    'ar',
    'de',
    'en',
    'es',
    'fa',
    'fr',
    'id',
    'it',
    'ja',
    'ko',
    'pt',
    'ru',
    'tr',
    'zh'
]

for key, data in EMOJI_DATA.items():
    emoji = URIRef(key)
    CARPEDM20.add((emoji, RDF.type, SKOS.Concept))

    # skos:prefLabel
    CARPEDM20.add((emoji, SKOS.prefLabel, Literal(key)))

    # dc:identifier
    identifier = sanitise_label(data['en'])
    CARPEDM20.add((emoji, DC.identifier, Literal(identifier, lang='en')))

    # skos:altLabel
    for language in languages:
        label = data.get(language)
        if label:
            label = sanitise_label(label)
            CARPEDM20.add((emoji, SKOS.altLabel, Literal(label, lang=language)))

    # skos:hiddenLabel
    aliases = data.get('alias', [])
    for label in aliases:
        label = sanitise_label(label)
        CARPEDM20.add((emoji, SKOS.hiddenLabel, Literal(label, lang='en')))

if __name__ == '__main__':
    print(CARPEDM20.serialize(format='longturtle'))
