from pydub.generators import Sine
from pydub import AudioSegment

# Create a whimsical melodic sequence
egg = (Sine(523).to_audio_segment(duration=200) +  # C5
       Sine(659).to_audio_segment(duration=200) +  # E5
       Sine(784).to_audio_segment(duration=200))   # G5
egg = egg.fade_in(50).fade_out(100)

# Export as MP3
egg.export("egg.mp3", format="mp3")

