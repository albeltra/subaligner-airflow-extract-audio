import os
from pathlib import Path

from helper import MediaHelper

mediaFile = os.environ.get('mediaFile')
mediaInfo = os.environ.get('mediaInfo')
audio_channel = os.environ.get('audio_channel', '0')

extract_audio = MediaHelper().extract_audio

kwargs = {'video_file_path':  mediaFile['path'],
          'TEMP_DIR_PATH': "/TEMP-SUBS/" + Path(mediaFile['path']).name + '.wav',
          'channel': audio_channel,
          'decompress': True}

extract_audio(**kwargs)