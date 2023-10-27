# Thai Syllable Breakdown

A Python algorithm that could extract phonetic information and more from a Thai syllable.<br>
*A part of Waiyakon project*

## Demonstration

```bash
Input Thai string: เหลือง

        Components:
            Leading Consonant: ห
            Initial Consonant: ล
            Blending Consonant: None
            Vowel Form: เ-ือ
            Tone Mark:
            Duration: ยาว
            Final Consonants: ง
        Pronunciation:
            Initial Sound: ล
            Blending Consonant: None
            Vowel Sound: เ-ือ
            Tone: สามัญ
            Duration: ยาว
            Final Sound: ง
        Transliteration:
            Initial Sound: l
            Blending Consonant: None
            Vowel Sound: uea
            Tone: middle
            Duration: long
            Final Sound: ng
        Extra TH:
            Initial Class: ต่ำ
            Syllable Class: สูง
            Live Dead: เป็น
        Extra EN:
            Initial Class: low
            Syllable Class: high
            Live Dead: live
```

## What it can do
- **Find these components of a syllable**
```py
Leading Consonant: {syllable.getLeadingConsonantChar()}
Initial Consonant: {syllable.getInitialConsonantChar()}
Blending Consonant: {syllable.getBlendingConsonantChar()}
Vowel Form: {syllable.getVowelForm()}
Tone Mark: {syllable.getToneMarksClusterString()}
Duration: {syllable.getVowelDuration('th')}
Final Consonants: {syllable.getFinalConsonantsClusterString()}
```
- **Find these aspects of pronunciation in a syllable, in both Thai and English**
```py
Initial Sound: {syllable.getInitialSound('en')}
Blending Consonant: {syllable.getBlendingSound('en')}
Vowel Sound: {syllable.getVowelSound('en')}
Tone: {syllable.getTone('en')}
Duration: {syllable.getVowelDuration('en')}
Final Sound: {syllable.getFinalSound('en')}
```
- **Process these extra information of a syllable**
```py
Initial Class: {syllable.getInitialClass('en')}
Syllable Class: {syllable.getSyllableClass('en')}
Live Dead: {syllable.getLiveDead('en')}
```

## What it can't do
- **These things need machine learning models in assistance**
 - Process multiple syllable. (you can also use maximal matching algorithm, but it would not be able to handle exceptions)
 - Process irregular Thai syllables. (ex. ไม้, น้ำ, etc.)
 These shortcomings would be tackled by machine learning algorithms developed as a part of Waiyakon project.

## How to Use

### As a standalone algorithm
#### 1. Run the main Python code.
```bash
python th_syllable_breakdown.py
```
#### 2. Input a Thai syllable.
Emphasis on ***SYLLABLE***, this algorithm does not support multiple syllables.<br>
Afterthat, you're good to go! Read the output of all information provided by the context of one syllable.

### As a module
#### 1. Import the module into your project.
Currently, this algorithm has not been turned into a pip package yet. So you have to integrate it into your project manually.<br>
In a project with different routing. You might have to change the import path within the codes.<br>
These are some example of how the routing might change.

**In th_syllable_breakdown.py**
```py
import re

from .th_utils_classes import *
from .th_utils_regex import *
from .th_utils_tables import *
```

**In th_utils_classes.py**
```py
from .th_utils_regex import *
```
#### 2. Call the functions provided
All the functions and methods necessary are demonstrated in th_syllable_breakdown.
```py
if __name__ == '__main__':
```
So you can look for things there. Or see **What it can do** section.