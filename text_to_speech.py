"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
import tempfile
import shutil
from pathlib import Path

client = texttospeech.TextToSpeechClient()

voice = texttospeech.types.VoiceSelectionParams(
    language_code='cmn-CN',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

def gen_media_file(chinese_characters, file_name, out_dir='audio'):
    print('Generating {} audio file...'.format(file_name))
    synthesis_input = texttospeech.types.SynthesisInput(text=chinese_characters)
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    Path(out_dir).mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile() as outfile:
        # The response's audio_content is binary.
        outfile.write(response.audio_content)
        outfile.flush()
        # Copy the file to the output directory only after successfully writing in it
        shutil.copy2(outfile.name, '{}/{}'.format(out_dir, file_name))

if __name__ == '__main__':
    print('Testing text-to-speech')
    gen_media_file("冬天", 'test', 'test')
