import sounddevice as sd
import soundfile as sf
from contextlib import redirect_stdout

def write_log():
    with open('output.txt', 'w') as file:
        with redirect_stdout(file):
            devices = sd.query_devices()
            for idx, device in enumerate(devices):
                print(f"Device ID: {idx}", file=file, flush=True)
                print(f"Name: {device['name']}", file=file, flush=True)
                print(f"Max Input Channels: {device['max_input_channels']}", file=file, flush=True)
                print(f"Max Output Channels: {device['max_output_channels']}",  file=file, flush=True)
                print(f"Default Sample Rate: {device['default_samplerate']} Hz",  file=file, flush=True)
                print("-" * 40)

# Load the audio file
data, fs = sf.read('sample.mp3', dtype='float32')

# Initial your audio device list
#write_log()


# Suppose you must should choose your own VB Device ID
sd.default.device = 50

print("Playing audio...")

# Play the audio file
sd.play(data, fs)
sd.wait()  

print("Finished!")