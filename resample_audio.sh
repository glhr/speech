mkdir -p audio/resampled
cd audio
for file in *.wav; do sox ${file} -r 16000 ./resampled/${file}; done
