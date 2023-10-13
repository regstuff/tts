import pyttsx3
engine = pyttsx3.init()
txt = """New blood test more convenient for measuring important omega-3 levels"""
engine.save_to_file(txt, 'test.mp3')
print('MP3 created')
engine.runAndWait()
