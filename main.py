import sounddevice as sd
import soundfile as sf
from contextlib import redirect_stdout
import keyboard
import threading

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

def play_sound():
        
    # Load the audio file
    data, fs = sf.read('audio/yippie.mp3', dtype='float64')
    # Suppose you must should choose your own VB Device ID
    #sd.default.device = 50
    sd.default.device = 46


    print("Playing audio...")

    # Play the audio file
    sd.play(data, fs)

    print("Finished!")

def play_sound_threaded():
    threading.Thread(target=play_sound).start()


print("Soundboard is started!")

# Test trigger hotkeys
keyboard.add_hotkey('ctrl+shift+a', play_sound)

keyboard.wait('esc') 



# Initial your audio device list
#write_log()

