import base64

def convert_to_mp3(input: str, output: str):
    with open(input, "rb") as f:
        audio_data = base64.b64decode(f.read())

    with open(output, "wb") as f:
        f.write(audio_data)

if __name__ == "__main__":
    convert_to_mp3("weird.b64", "magic_music.mp3")
