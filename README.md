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

**DeepSpeech**

```shell
# Install
python3 -m pip install deepspeech

# Download pre-trained English model and extract
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.6.1/deepspeech-0.6.1-models.tar.gz
tar xvf deepspeech-0.6.1-models.tar.gz
```
