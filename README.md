# Emoji SKOS

Builds a [Simple Knowledge Organization System](https://www.w3.org/2004/02/skos/) vocabulary of [emojis](https://unicode.org/emoji/charts/full-emoji-list.html) as an [`rdflib.Graph`](https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.html#rdflib.Graph).

> [!WARNING]
> Emoji SKOS is an on-going research project and is not yet ready for use in production.

## Quickstart

### Install

```bash
pip install git+https://github.com/edwardanderson/emoji-skos
```

### CLI

```bash
emoji-skos 👩‍🚒
```

```bash
emoji-skos woman firefighter
```

### Module

```python
from emoji_skos import EMOJI_SKOS


description = EMOJI_SKOS.query('describe <👩‍🚒>')
print(description.serialize(format='longturtle').decode('utf-8'))
```

```turtle
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

<👩‍🚒>
    a skos:Concept ;
    dc:identifier "woman firefighter"@en ;
    skos:altLabel
        "سيدة إطفاء"@ar ,
        "feuerwehrfrau"@de ,
        "woman firefighter"@en ,
        "bombera"@es ,
        "آتش نشان زن"@fa ,
        "pompier femme"@fr ,
        "pemadam kebakaran wanita"@id ,
        "pompiere donna"@it ,
        "女性消防士"@ja ,
        "여자 소방관"@ko ,
        "bombeira"@pt ,
        "женщина пожарный"@ru ,
        "kadın itfaiyeci"@tr ,
        "女消防员"@zh ;
    skos:inScheme
        <https://unicode.org/Public/9.0.0> ,
        <https://unicode.org/Public/emoji/4.0> ;
    skos:notation "1F469-200D-1F692" ;
    skos:prefLabel "👩‍🚒" ;
    skos:related
        <👩🏻‍🚒> ,
        <👩🏼‍🚒> ,
        <👩🏽‍🚒> ,
        <👩🏾‍🚒> ,
        <👩🏿‍🚒> ;
.
```

## Data

The SKOS representation is transformed from data provided by the following packages:

- <https://github.com/alexmick/emoji-data-python>
- <https://github.com/carpedm20/emoji>

Mappings to other vocabularies are maintained in [emoji_skos/data/relations/relations.json](emoji_skos/data/relations/relations.json).

## Acknowledgements

Unicode Data Files are distributed under the [Unicode License v3](https://www.unicode.org/license.txt) which is included in this repository at [docs/unicode_license_v3.txt](docs/unicode_license_v3.txt).
