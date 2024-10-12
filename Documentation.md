# Documentation 📰📃😃

## Table of Contents

- [Documentation 📰📃😃](#documentation-)
  - [Table of Contents](#table-of-contents)
    - [Create and start a python virtual env](#create-and-start-a-python-virtual-env)
    - [Structure of the data](#structure-of-the-data)
    - [To-Do](#to-do)
      - [Completed](#completed)
      - [Pending](#pending)
    - [Requirements (**.txt**)](#requirements-txt)

---

### Create and start a python virtual env

```C
# Starting a virtual environment
py -m venv ll_env

# Activate the virtual environment
ll_env/scripts/activate
```

### Structure of the data

**Note**: all of the data is in the `data/` directory.

- `data/`
   - `audio/` (**folder**)
   - `backed-up/` (**folder**)
   - `dict/` (**folder**)
   - `sentences/` (**folder**)
   - `videos/` (**folder**)
   - `markdown_links.txt` (**text file**)
   - `mistakes.json` (**json file**)
   - `words.json` (**json file**)

---

   - `data/audio/` (**audio**) *brendan's recordings of pronunciations in .wav audio files*
      - `audio/phrases/` (**phrases**)
      - `audio/words/` (**words**)

---

   - `data/dict/` (**dict**) *stands for dictionary contains data saved from the webster [dictionary API](https://dictionaryapi.com/)*
      - `dict/audio/` (**.wav audio**) *downloaded from dictionary API's media endpoint*
        - `dict/audio/phrases/` (**phrases**)
        - `dict/audio/words/` (**words**)
      - `dict/json/` (**json**) *json response from dictionary API for {searched word} + .json*
        - `dict/json/phrases/` (**phrases**) phrases are camel case, `example`: **a_thrill_swept.json**
        - `dict/json/words/` (**words**)

---

### To-Do 

#### Completed

- [X] Fix recordings that are too long with *blank/no noise*. Write script to scan for and output all files with `duration > 3 seconds`. 
- [X] `pip install` the package for env variables - then fix the api_req file to remove from .gitignore
- [X] If the md file will say *List of words:* then write a message like `This word or phrase doesn't seem to exist in the English dictionary - maybe I misunderstood the text in your image`
- [X] Mark the edited audio files w/ a flag to not have the volumex(2) used again during the video creation
- [X] Need to replace all json objects in the words.json file with their new durations from after.json 
- [X] write script to seperate these into two categories: *1. Phrases* and *2. Words*.
- [X] Update the long-entries/before.json file

#### Pending

- [ ] Only pages *5* and *6* are left to complete
- [ ] Currently at: `Harsh` (*id = 124*) as of 10/07/2024
- [ ] Update the Requirements.txt
- [ ] Finish the MoviePy script to prompt to record `using each word in a sentence` 
- [ ] Write script to separate into batches by *date*

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
