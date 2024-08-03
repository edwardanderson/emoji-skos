# Emoji SKOS

Builds a [Simple Knowledge Organization System](https://www.w3.org/2004/02/skos/) vocabulary of [emojis](https://unicode.org/emoji/charts/full-emoji-list.html) as an [`rdflib.Graph`](https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.html#rdflib.Graph).

![emoji-skos graph diagram](docs/emoji-skos.png)

## Quickstart

### Install

```bash
pip install emoji-skos
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
    skos:broader
        <👩> ,
        <🚒> ;
    skos:closeMatch
        <👩🏻‍🚒> ,
        <👩🏼‍🚒> ,
        <👩🏽‍🚒> ,
        <👩🏾‍🚒> ,
        <👩🏿‍🚒> ;
    skos:inScheme
        <https://unicode.org/Public/9.0.0> ,
        <https://unicode.org/Public/emoji/4.0> ;
    skos:notation "1F469-200D-1F692" ;
    skos:prefLabel "👩‍🚒" ;
.
```

