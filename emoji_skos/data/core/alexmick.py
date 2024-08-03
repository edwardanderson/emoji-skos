# The <https://emoji-data-python.readthedocs.io/en/latest/> contains collection
# set membership information.


from emoji_data_python import emoji_data, unified_to_char
from rdflib import Graph, Literal, URIRef
from rdflib.namespace import DCTERMS, RDF, SKOS


def get_schemes(version: float) -> list[URIRef]:
    schemes = []

    # Data File Comment: Unicode Version, Emoji Version
    versions = {
        0.6: (6.0, None),
        0.7: (7.0, None),
        1.0: (8.0, 1.0),
        2.0: (8.0, 2.0),
        3.0: (9.0, 3.0),
        4.0: (9.0, 4.0),
        5.0: (10.0, 5.0),
        11.0: (11.0, 11.0),
        12.0: (12.0, 12.0),
        12.1: (12.1, 12.1),
        13.0: (13.0, 13.0),
        13.1: (13.0, 13.1),
        14.0: (14.0, 14.0),
        15.0: (15.0, 15.0),
        15.1: (15.1, 15.1)
    }

    root = 'https://unicode.org/Public/'
    data_file_version = float(version)
    (unicode_version, emoji_version) = versions.get(data_file_version)

    if emoji_version:
        scheme = root + f'emoji/{emoji_version}'
        schemes.append(URIRef(scheme))

    if unicode_version:
        scheme = root + f'{unicode_version}.0'
        schemes.append(URIRef(scheme))

    return schemes


ALEXMICK = Graph()

characters = set()
for character in emoji_data:
    key = unified_to_char(character.unified)
    characters.add(key)
    for variation in character.skin_variations:
        characters.add(variation)

categories = {}
for character in emoji_data:
    key = unified_to_char(character.unified)
    emoji = URIRef(key)

    # skos:Concept
    ALEXMICK.add((emoji, RDF.type, SKOS.Concept))

    # skos:notation
    ALEXMICK.add((emoji, SKOS.notation, Literal(character.unified)))

    # skos:inScheme
    schemes = get_schemes(float(character.added_in))
    for scheme in schemes:
        ALEXMICK.add((emoji, SKOS.inScheme, scheme))

    # skos:exactMatch
    for _, variation in character.skin_variations.items():
        match = URIRef(unified_to_char(variation.unified))
        ALEXMICK.add((emoji, SKOS.exactMatch, match))
        ALEXMICK.add((match, RDF.type, SKOS.Concept))
        # skos:notation
        ALEXMICK.add((match, SKOS.notation, Literal(variation.unified)))
        # skos:inScheme
        schemes = get_schemes(float(variation.added_in))
        for scheme in schemes:
            ALEXMICK.add((match, SKOS.inScheme, scheme))

    # skos:related
    for part in key:
        if part in characters and part != key:
            related = URIRef(part)
            ALEXMICK.add((emoji, SKOS.related, related))
            ALEXMICK.add((related, SKOS.related, emoji))

    # dc:isReplacedBy
    if character.obsoletes:
        obsolete = unified_to_char(character.obsoletes)
        ALEXMICK.add((URIRef(obsolete), DCTERMS.isReplacedBy, emoji))

    # dc:isReplacedBy
    if character.obsoleted_by:
        replacement = unified_to_char(character.obsoleted_by)
        ALEXMICK.add((emoji, DCTERMS.isReplacedBy, URIRef(replacement)))

    # Agggregate collection membership references.
    category = character.category
    try:
        categories[category].append(key)
    except KeyError:
        categories[category] = [key]

# skos:Collection
for category_label, members in categories.items():
    identifier = (
        category_label
        .replace(' ', '-')
        .replace('&', 'and')
        .lower()
    )
    category = URIRef(f'collection/{identifier}')
    label = Literal(category_label, lang='en')
    ALEXMICK.add((category, RDF.type, SKOS.Collection))
    ALEXMICK.add((category, SKOS.prefLabel, label))

    # skos:member
    for member in members:
        ALEXMICK.add((category, SKOS.member, URIRef(member)))
