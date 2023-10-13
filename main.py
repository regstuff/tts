import rlvoice
engine = rlvoice.init("coqui_ai_tts")
txt = """New blood test more convenient for measuring important omega-3 levels"""
print('MP3 created')
engine.save_to_file(txt, 'test.mp3')
engine.runAndWait()
