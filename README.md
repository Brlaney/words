# English Phrases and Words 📰📃😃

## Table of Contents

- [English Phrases and Words 📰📃😃](#english-phrases-and-words-)
  - [Table of Contents](#table-of-contents)
    - [Phrases 📃:](#phrases-)
    - [Words 📃:](#words-)
    - [To-Do](#to-do)
    - [Requirements (**.txt**)](#requirements-txt)

<br/>

---

### Phrases 📃:

[along the](md/phrases/along_the.md)

---

### Words 📃:

[alley](md/words/alley.md)

<br/>

---

### To-Do

- [X] Fix recordings that are too long with *blank/no noise*. Write script to scan for and output all files with `duration > 3 seconds`. 
  
- [ ] If the md file will say *List of words:* then write a message like `This word or phrase doesn't seem to exist in the English dictionary - maybe I misunderstood the text in your image`

- [ ] `pip install` the package for env variables - then fix the api_req file to remove from .gitignore
- [ ] Mark the edited audio files w/ a flag to not have the volumex(2) used again during the video creation
- [ ] Need to replace all json objects in the words.json file with their new durations from after.json 

- [ ] write script to seperate these into two categories: *1. Phrases* and *2. Words*.
- [ ] Finish the MoviePy script to prompt to record `using each word in a sentence` 
- [ ] Only pages *5* and *6* are left to complete
- [ ] Update the long-entries/before.json file
- [ ] Write script to separate into batches by *date*
- [ ] Currently at: `Harsh` (*id = 124*) as of 10/07/2024

<br/>

---

### Requirements (**.txt**)

- `certifi==2024.8.30`
- `charset-normalizer==3.3.2`
- `comtypes==1.4.7`
- `idna==3.9`
- `PyAudio==0.2.14`
- `pydub==0.25.1`
- `pypiwin32==223`
- `pyttsx3==2.97`
- `pywin32==306`
- `requests==2.32.3`
- `setuptools==74.1.2`
- `SpeechRecognition==3.10.4`
- `typing_extensions==4.12.2`
- `urllib3==2.2.3`
