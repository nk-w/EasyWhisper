from pydub import AudioSegment
from pathlib import Path
import os
import whisper
import shutil
import sys

def get_model_size():
    
    model_sizes = ["tiny", "base", "small", "medium", "large"]

    print("Please enter the number of the model that you would like to use:")
    
    print()
    
    for idx, size in enumerate(model_sizes):
        print(f"{idx}:{size}")
    
    print()
    
    while True:
        try:
            user_input = input()
            value = int(user_input)
            model_size = model_sizes[value]
            return model_size
        
        except ValueError:
            print()
            print("Error: Please enter a valid integer.")
            print()
    
    

def check_model(model_size):
    
    model_path = f"models/{model_size}.pt"
    
    if os.path.isfile(model_path):
        print()
        print(f"{model_size}.pt exists already. Moving on to converting audio.")
        print()
    else:
        print()
        print(f"{model_size}.pt does not yet exists. Downloading model:")
        print()
    
        model = whisper.load_model(model_size, download_root="models")
        
    print()
    print()
    print("Your ethical board may require from you to turn of your internet.")
    print("You can do this now.")
    print()
    
    while True:
        
        user_input = input("Please enter 'y' when you would like to move on:\n")
        
        if user_input == "y":
            print()
            print("Continuing to transcription...")
            print()
            break
        else:
            print()
            print("Error: Please enter 'y' to continue.")
            print()

def get_audio_files(folder_path):
    """This function loads all audio files from the input folder"""
    # Create a list to store audio file paths
    audio_files = []

    # Common audio file extensions
    audio_extensions = [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".aiff", ".wma", ".alac", ".opus", ".ape", ".pcm"]

    # Iterate through files in the folder
    for file_path in folder_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in audio_extensions:
            audio_files.append(file_path)

    return audio_files

def extract_audio_filename(path):
    """This function extracts the file name of the audio file without extensions"""
    # Get the base name (file name with extension) from the path
    base_name = os.path.basename(path)
    
    # Split the base name into filename and extension
    file_name, file_extension = os.path.splitext(base_name)
    
    return file_name

def convert_audio(audio_file_list):
    """This function converts each audio file to the appropriate .wav format"""
    
    # Iterating through the list of audio files to convert them one by one
    for file in audio_file_list:
    
        # Getting the filename using the above specified function
        file_name = extract_audio_filename(path=file)
        
        print()
        print("------------")
        print(f"Converting: {file_name}...")
        print()
        
        audio = AudioSegment.from_file(file)
        audio.export(f"converted/{file_name}.wav", format='wav', parameters=['-ar', '16000', '-ac', '1', '-c:a', 'pcm_s16le'])
        
        print()
        print(f"{file_name} converted!")
        print("------------")
        print()

def transcribe_audio(model_size, transcription_files):
    
    print()
    print("------------")
    print("Loading Model:")
    print()
    
    model = whisper.load_model(model_size, download_root="models")
    
    for file in transcription_files:
        file_name = extract_audio_filename(path=str(file))
        
        print()
        print("------------")
        print(f"Transcribing: {file_name}...")
        print()
        
        result = model.transcribe(str(file), verbose=True)
        
        with open(f"transcripts/Transcript_{file_name}.txt", "w") as f:
            f.write(result['text'])
            f.close()
        
        print()
        print(f"{file_name} transcribed!")
        print("------------")
        print()
    
        
def delete_folder_contents(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


def Transcription():
    # Getting Model Size
    model_size = get_model_size()    
    
    check_model(model_size=model_size)
    # Getting Audiofile List
    audio_file_list = get_audio_files(folder_path=Path("input"))

    # Converting each audio file to wav so that whisper can transcribe them
    convert_audio(audio_file_list)

    # Getting list of converted files for transcription
    
    transcription_files = get_audio_files(folder_path=Path("converted"))

    transcribe_audio(model_size=model_size, transcription_files=transcription_files)

    delete_folder_contents(folder_path="converted")
    
    print()
    print("------------")
    print("TRANSCRIPTION COMPLETED")
    print("------------")
    print()
    

Transcription()