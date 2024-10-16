from dotenv import load_dotenv
import os

if os.path.exists('.env'):
  load_dotenv()
else:
  FOLDER_PATH == 'put-media-files-here'
  if not os.path.exists(FOLDER_PATH):
    os.makedirs(FOLDER_PATH)

# Scan files
list_of_files = os.listdir('/put-media-files-here') # Assumes files are listed in alphabetical/lexicographical order
for file in list_of_files:
  current_file_name = list_of_files.pop(0).split('.')[0]
  if current_file_name in list_of_files[0]:
    list_of_files.pop(0)
  else:
    ### If it's an audio file (e.g. podcast), run with settings so that output is a transcript 
    ### If it's a video file, run with settings so that output is timed captions
    #### If it's a short video file (e.g. for Yt Shorts/TikTok), caption timing & colouring should be different
    #### If it's a long video file (e.g. long form Youtube videos), then captions should be default settings