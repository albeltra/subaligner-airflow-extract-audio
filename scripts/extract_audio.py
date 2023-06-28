import ast
import os
from pathlib import Path

from helper import MediaHelper

mediaFile = ast.literal_eval(os.environ.get('mediaFile'))
mediaInfo = ast.literal_eval(os.environ.get('mediaInfo'))
audio_channel = os.environ.get('audio_channel', '0')

extract_audio = MediaHelper().extract_audio

output_file_path = "/audio-subs/" + Path(mediaFile['path']).name + '.wav'

kwargs = {'video_file_path':  mediaFile['path'],
          'TEMP_DIR_PATH': output_file_path,
          'channel': audio_channel,
          'decompress': True}

if not os.path.exists(output_file_path):
    extract_audio(**kwargs)