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

skin_tones = [
    '🏻', # light
    '🏼', # medium light
    '🏽', # medium
    '🏾', # medium dark
    '🏿', # dark
]

characters = set()
for character in emoji_data:
    key = unified_to_char(character.unified)
    characters.add(key)
    for variation in character.skin_variations:
        characters.add(variation)

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
        if not label:
            continue

        label = sanitise_label(label)
        CARPEDM20.add((emoji, SKOS.altLabel, Literal(label, lang=language)))

    # skos:altLabel
    aliases = data.get('alias', [])
    for label in aliases:
        label = sanitise_label(label)
        CARPEDM20.add((emoji, SKOS.hiddenLabel, Literal(label, lang='en')))

    # skos:related
    for part in key:
        if part in characters and part != key:
            if part not in skin_tones:
                related = URIRef(part)
                CARPEDM20.add((emoji, SKOS.related, related))
                CARPEDM20.add((related, SKOS.related, emoji))
