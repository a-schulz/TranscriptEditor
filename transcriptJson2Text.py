import json

def parse_json(input_file: str, output_file: str):
    # Define speaker mapping
    speaker_map = {
        "speaker1": "I",
        "speaker2": "B"
    }

    # Read JSON data
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Process transcript
    transcript = []
    previous_speaker = None
    current_text = ""

    for entry in data:
        speaker = speaker_map.get(entry["speaker"], entry["speaker"])  # Default to original speaker name if not mapped
        text = entry["text"].strip()

        if speaker == previous_speaker or speaker == "":
            current_text += " " + text
        else:
            if previous_speaker is not None:
                transcript.append(f"{previous_speaker}: {current_text}")
            previous_speaker = speaker
            current_text = text

    if previous_speaker is not None:
        transcript.append(f"{previous_speaker}: {current_text}")

    # Write to output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(transcript))

def main():
    input_file = "interview_transcript.json"  # Update with your actual input file name
    output_file = "interview_transcript.txt"
    parse_json(input_file, output_file)
    print(f"Transcript saved to {output_file}")

if __name__ == "__main__":
    main()
