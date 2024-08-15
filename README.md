# EasyWhisper

This is an easy implementation of Whisper by OpenAI. 
It makes use of the following repositories:
- https://github.com/openai/whisper
- https://github.com/pyannote/pyannote-audio

## Purpose
The puprose of this repository is to make transcription of reserach interviews as easy as possible.
The reporistory was created based on the needs of researchers working at *The School of Health Professions Education (SHE)* and *The Department for Educational Development & Research (EDUC)* at *The Faculty of Health, Medicine, and Life Sciences (FHML)* of *Maastricht University (UM)*. It can of course be used by anyone who finds use in it. 

## Functionality
With this implementation of Whisper you can either
1. Get a simple transcription of your interviews 
    e.g.:
    ```
    This is what speaker 1 said. This is what speaker 2 said. 
    This is what speaker 3 said. This is what speaker 2 said.
    ```

or

2. A diarized transcription of your interviews where each speaker is indicated throughout the transcript
    e.g.:
    ```
    SPEAKER 1: This is what speaker 1 said.

    SPEAKER 2: This is what speaker 2 said.

    SPEAKER 3: This is what speaker 3 said.

    SPEAKER 2: This is what speaker 2 said.
    ```

This latter option is achieved by using [pyannote-audio](https://github.com/pyannote/pyannote-audio). 

## How to Use
See [a detailed tutorial for all the steps from installing Python to running the code here](https://niklaswenzel.notion.site/Installing-Using-WHISPER-for-Transcription-of-Interviews-e20049cf9ebe4fea92f5b8112cb7b35c?pvs=4)