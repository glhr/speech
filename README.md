## Use-guide

Currently supported methods:
* Google from [SpeechRecognition](https://github.com/Uberi/speech_recognition)
* [DeepSpeech](https://github.com/mozilla/DeepSpeech) by Mozilla

Run:
```shell
python3 stt_wrapper.py # use default STT method
python3 stt_wrapper.py deepspeech # specify STT method
```
the script will try to find a file called `output.wav` in the `audio` directory. If it doesn't exist, it will record audio and save it as `output.wav`. It will then transcribe the audio file using the specified method, or the default method (Google from SpeechRecognition) if no argument is provided.

Here's how you can use this Speech-to-Text wrapper from a script:

```python
from stt_wrapper import generate_text

filename = "output.wav"
for method in ['google', 'deepspeech']:
    text = generate_text(filename, method=method)
    print("--> {}: {}".format(method, text))
```

## Requirements

**PyAudio**

```shell
sudo apt-get install -y portaudio19-dev python-pyaudio python3-pyaudio
python3 -m pip install pyaudio
```

**SpeechRecognition**

```shell
python3 -m pip install speechrecognition
```

**PocketSphinx**
```shell
sudo apt-get install python python-all-dev python-pip build-essential swig git libpulse-dev libasound2-dev
python3 -m pip install pocketsphinx
```

**DeepSpeech**

```shell
# Install
python3 -m pip install deepspeech

# Download pre-trained English model and extract
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.6.1/deepspeech-0.6.1-models.tar.gz
tar xvf deepspeech-0.6.1-models.tar.gz
```
