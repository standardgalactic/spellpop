from pydub.generators import Sine
from pydub import AudioSegment

# Create a quick high-pitched pop sound
pop = Sine(1000).to_audio_segment(duration=80).fade_out(40) + Sine(800).to_audio_segment(duration=50).fade_out(30)

# Export as MP3
pop.export("pop.mp3", format="mp3")

