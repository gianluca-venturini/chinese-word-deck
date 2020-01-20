import genanki
from spreadsheet import retrieve_words
from text_to_speech import gen_media_file

my_model = genanki.Model(
    1314758901,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'MyMedia'},
    ],
    templates=[
        {
        'name': 'Card 1',
        'qfmt': '{{Question}}<br>{{MyMedia}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])


my_deck = genanki.Deck(
    1415635835,
    'Chinese::Word of the day')

words = retrieve_words()
for word in words:
    print('Generating card for {}, {}, {}...'.format(word[1], word[0], word[2]))
    audio_filename = '{}.mp3'.format(word[2])
    gen_media_file(word[2], audio_filename)
    my_note = genanki.Note(
        model=my_model,
        fields=[
            '{word[0]} {word[2]}'.format(word=word), # Pinyin, Chinese
            word[1],  # English
            '[sound:{}]'.format(audio_filename)
        ])
    my_deck.add_note(my_note)

genanki.Package(my_deck).write_to_file('output.apkg')