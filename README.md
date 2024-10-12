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

| [a thrill swept](md/a-thrill-swept.md) | [along the](md/along-the.md) | [as high as](md/as-high-as.md) |
|-----------------------------------------------|-----------------------------------|-------------------------------------|
| [be labeled](md/be-labeled.md)          | [barely](md/barely.md)      | [betrayals](md/betrayals.md)  |
| [blood vessels](md/blood-vessels.md)    | [by then](md/by-then.md)    | [came marching](md/came-marching.md) |
| [car railing](md/car-railing.md)        | [check out](md/check-out.md) | [choking back](md/choking-back.md) |
| [climb upward](md/climb-upward.md)      | [cutting off](md/cutting-off.md) | [come up to me](md/come-up-to-me.md) |
| [dare fail](md/dare-fail.md)            | [dragging](md/dragging.md)  | [endless](md/endless.md)      |
| [eye examination chart](md/eye-examination-chart.md) | [first excelled among](md/first-excelled-among.md) | [get fitted](md/get-fitted.md) |
| [give rent](md/give-rent.md)            | [grudges](md/grudges.md)    | [halfway](md/halfway.md)      |
| [held me](md/held-me.md)                | [he reluctantly](md/he-reluctantly.md) | [hold on](md/hold-on.md)    |
| [i burst into tears](md/i-burst-into-tears.md) | [laid down](md/laid-down.md) | [look up](md/look-up.md)      |
| [not greatly](md/not-greatly.md)        | [nudged me into](md/nudged-me-into.md) | [painstaking](md/painstaking.md) |
| [pleading](md/pleading.md)              | [pulling ahead](md/pulling-ahead.md) | [railroad security men](md/railroad-security-men.md) |
| [reached](md/reached.md)                | [recoil](md/recoil.md)      | [reject](md/reject.md)        |
| [rush](md/rush.md)                      | [settle for](md/settle-for.md) | [slow down](md/slow-down.md)  |
| [somehow](md/somehow.md)                | [spelling bees](md/spelling-bees.md) | [stand out](md/stand-out.md)  |
| [stretched out](md/stretched-out.md)    | [sunshine slanting](md/sunshine-slanting.md) | [therefore](md/therefore.md)  |
| [toward me](md/toward-me.md)            | [unbounded](md/unbounded.md) | [up until](md/up-until.md)    |
| [widened](md/widened.md)                | [without squinting](md/without-squinting.md) | [zoomed upward](md/zoomed-upward.md) |

### Words 📃:

| [alley](md/alley.md)  | [aside](md/aside.md)  | [attempt](md/attempt.md)     |
|-----------------------------|-----------------------------|-----------------------------------|
| [bleeding](md/bleeding.md) | [brisk](md/brisk.md) | [burdened](md/burdened.md)  |
| [catch](md/catch.md)  | [choking back](md/choking-back.md) | [clotting](md/clotting.md)  |
| [command](md/command.md) | [dumbest kid](md/dumbest-kid.md) | [desire](md/desire.md)      |
| [envied](md/envied.md) | [frightened](md/frightened.md) | [gang](md/gang.md)          |
| [gaze](md/gaze.md)    | [grab](md/grab.md)    | [grasp](md/grasp.md)        |
| [growth](md/growth.md) | [grumbled](md/grumbled.md) | [had worsened](md/had-worsened.md) |
| [harsh](md/harsh.md)  | [hobo's](md/hobo's.md) | [huddled](md/huddled.md)    |
| [hop](md/hop.md)      | [i thrived](md/i-thrived.md) | [juncture](md/juncture.md)  |
| [knack](md/knack.md)  | [laying down](md/laying-down.md) | [magnifying glass](md/magnifying-glass.md) |
| [muttered](md/muttered.md) | [outstanding](md/outstanding.md) | [pale](md/pale.md)          |
| [pester](md/pester.md) | [pounded](md/pounded.md) | [samples](md/samples.md)    |
| [scheme](md/scheme.md) | [smiled](md/smiled.md) | [soared](md/soared.md)      |
| [sweat](md/sweat.md)  | [swiped](md/swiped.md) | [tingle](md/tingle.md)      |
| [tracks](md/tracks.md) | [twinkle](md/twinkle.md) | [unflagging](md/unflagging.md) |
| [urging](md/urging.md) | [whacked me](md/whacked-me.md) | [yearning](md/yearning.md)  |

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
