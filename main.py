import torch
from pprint import pprint
from omegaconf import OmegaConf
from IPython.display import Audio, display

torch.hub.download_url_to_file('https://raw.githubusercontent.com/snakers4/silero-models/master/models.yml', 'latest_silero_models.yml', progress=True)
models = OmegaConf.load('latest_silero_models.yml')

language = 'en'
model_id = 'v3_en'
device = torch.device('cpu')
model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models', model='silero_tts', language=language, speaker=model_id)
model.to(device)  # gpu or cpu

sample_rate = 24000
speaker = "en_24"
put_accent=False
put_yo=False
example_text = 'Tom Brady. New blood test more convenient for measuring important omega-3 levels'

audio = model.apply_tts(text=example_text, speaker=speaker, sample_rate=sample_rate, put_accent=put_accent, put_yo=put_yo)
audio_obj = Audio(audio, rate=sample_rate)
with open('output.mp3', 'wb') as f: f.write(audio_obj.data)
