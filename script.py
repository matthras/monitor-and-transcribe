from dotenv import load_dotenv
import os
load_dotenv()

# If .env variables are empty, set defaults
## Create folder for the user to put their files in

# Scan files
## If a file already has a transcript (file name would be <filename>_transcript.txt), skip it.
## Else
### If it's an audio file (e.g. podcast), run with settings so that output is a transcript 
### If it's a video file, run with settings so that output is timed captions
#### If it's a short video file (e.g. for Yt Shorts/TikTok), caption timing & colouring should be different
#### If it's a long video file (e.g. long form Youtube videos), then captions should be default settings