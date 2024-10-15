# Monitor and Transcribe

The main idea is to create a script that monitors a specific folder for video/audio files and produces a transcript or captions using OpenAI Whisper (or a fork of it that has additional features e.g. diarization).

## Instructions

- `git clone` this repository.
- Install all required dependencies `pip install -r requirements.txt`
- Create a `.env` file in the same folder. First line should be `FOLDER_NAME = ` followed by the path to the folder that you want monitored.
- [On Windows] Set up your Task Scheduler to run this script as frequently as you want.