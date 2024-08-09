import emoji
import pickle

from argparse import ArgumentParser
from pathlib import Path


def main():
    parser = ArgumentParser()
    parser.add_argument(
        'emoji',
        nargs='+',
        type=str
    )
    parser.add_argument(
        '--no-cache',
        action='store_false'
    )
    args = parser.parse_args()
    character = ' '.join(args.emoji)

    if emoji.is_emoji(character):
        query = f'describe <{character}>'
    else:
        query = f'''
        prefix dc: <http://purl.org/dc/elements/1.1/>

        describe ?emoji where {{
            ?emoji dc:identifier "{character}"@en .
        }}
        '''

    path = Path(__file__).parent / 'emoji_skos.pkl'
    if path.is_file() and args.no_cache:
        with open(path, 'rb') as file:
            EMOJI_SKOS = pickle.load(file)
    else:
        from emoji_skos.data import EMOJI_SKOS

        with open(path, 'wb') as file:
            pickle.dump(EMOJI_SKOS, file)

    description = EMOJI_SKOS.query(query)
    print(description.serialize(format='longturtle').decode('utf-8'))


if __name__ == '__main__':
    main()
