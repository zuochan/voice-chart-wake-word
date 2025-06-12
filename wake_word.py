
# Imports
import openwakeword
import pyaudio
import numpy as np
from openwakeword.model import Model
import argparse

# Parse input arguments
parser=argparse.ArgumentParser()
parser.add_argument(
    "--chunk_size",
    help="How much audio (in number of samples) to predict on at once",
    type=int,
    default=1280,
    required=False
)
parser.add_argument(
    "--model_path",
    help="The path of a specific model to load",
    type=str,
    default="./voiceChat.onnx,./odaijini.onnx",
    required=False
)
parser.add_argument(
    "--inference_framework",
    help="The inference framework to use (either 'onnx' or 'tflite'",
    type=str,
    default='onnx',
    required=False
)

args=parser.parse_args()

#start/stop wakeword

start = "voiceChat"
stop = "odaijini"

# Get microphone stream
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = args.chunk_size
audio = pyaudio.PyAudio()
mic_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# Load pre-trained openwakeword models
if args.model_path != "":
    model_paths = args.model_path.split(",")
    owwModel = Model(wakeword_models=model_paths, inference_framework=args.inference_framework)
else:
    owwModel = Model(inference_framework=args.inference_framework)

n_models = len(owwModel.models.keys())

# Run capture loop continuosly, checking for wakewords
if __name__ == "__main__":
    start_triggered = False
    stop_triggered = False
    # Generate output string header
    print("\n\n")
    print("#"*100)
    print("Listening for wakewords...")
    print("#"*100)
    print("\n"*(n_models*3))

    while True:
        # Get audio
        audio = np.frombuffer(mic_stream.read(CHUNK), dtype=np.int16)

        # Feed to openWakeWord model
        prediction = owwModel.predict(audio)
        
        # トリガー処理（モデル名ごとに判定）
        start_scores = list(owwModel.prediction_buffer.get(start, []))
        stop_scores = list(owwModel.prediction_buffer.get(stop, []))
        
    
        
        if start_scores and start_scores[-1] > 0.5 and not start_triggered:
            print(">>> START TRIGGERED <<<")
            print(start_scores[-1])
            start_triggered = True
        

        if stop_scores and stop_scores[-1] > 0.5 and start_triggered and not stop_triggered:
            print(">>> STOP TRIGGERED <<<")
            print(stop_scores[-1])
            stop_triggered = True
        
        
