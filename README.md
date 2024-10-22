# Transcript Editor

## Purpose

Use it to finetune your transcripts from research interviews or others.

## Development

It was developed only by using Claude AI and ChatGPT with some minor manual changes.
In the end it is just a basic html file with some javascript logic.

## How to use?

### Prerequisites

1. If you recorded a video extract the audio part as mp3 (e.g. using `ffmpeg -i input.mkv -vn -c:a libmp3lame -y output.mp3`)
2. Transcribe the audio file (I used Groq.com with the whisper model)
    * Save the produced json transcription

### Usage

1. Open the html file in a webbrowser.
2. Upload the audio file
3. Upload the json file
4. Press play and prove if the audio matches the transcription on the right.
    * You can add speakers if there are different speakers present in the interview or recording.

## Screenshots
![Screenshot TranscriptEditor](/Demo.png)