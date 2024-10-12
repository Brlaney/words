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

- [as high as](md/phrases/as_high_as.md)
- [point out](md/phrases/point_out.md)
- [laid down](md/phrases/laid_down.md)
- [look up](md/phrases/look_up.md)
- [laying down](md/phrases/laying_down.md)
- [cutting off](md/phrases/cutting_off.md)
- [along the](md/phrases/along_the.md)
- [magnifying glass](md/phrases/magnifying_glass.md)
- [up until](md/phrases/up_until.md)
- [spelling bees](md/phrases/spelling_bees.md)
- [pulling ahead](md/phrases/pulling_ahead.md)
- [caught up](md/phrases/caught_up.md)
- [stand out](md/phrases/stand_out.md)
- [slow down](md/phrases/slow_down.md)
- [to bear](md/phrases/to_bear.md)
- [blood vessels](md/phrases/blood_vessels.md)
- [choking back](md/phrases/choking_back.md)

---

### Words 📃:

- [halfway](md/words/halfway.md)
- [barely](md/words/barely.md)
- [handicapped](md/words/handicapped.md)
- [unflagging](md/words/unflagging.md)
- [encouragement](md/words/encouragement.md)
- [soared](md/words/soared.md)
- [reached](md/words/reached.md)
- [urging](md/words/urging.md)
- [pleading](md/words/pleading.md)
- [grumbled](md/words/grumbled.md)
- [endless](md/words/endless.md)
- [unbounded](md/words/unbounded.md)
- [sweat](md/words/sweat.md)
- [pale](md/words/pale.md)
- [gaze](md/words/gaze.md)
- [muttered](md/words/muttered.md)
- [prodded](md/words/prodded.md)
- [gang](md/words/gang.md)
- [widened](md/words/widened.md)
- [flax](md/words/flax.md)
- [beamed](md/words/beamed.md)
- [growth](md/words/growth.md)
- [envied](md/words/envied.md)
- [surgeons](md/words/surgeons.md)
- [painstaking](md/words/painstaking.md)
- [rehearsals](md/words/rehearsals.md)
- [therefore](md/words/therefore.md)
- [sob's](md/words/sob's.md)
- [swiped](md/words/swiped.md)
- [twinkle](md/words/twinkle.md)
- [alley](md/words/alley.md)
- [pleading](md/words/pleading.md)
- [burdened](md/words/burdened.md)
- [betrayals](md/words/betrayals.md)
- [huddled](md/words/huddled.md)

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
