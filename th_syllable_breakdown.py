import re

from th_utils_classes import *
from th_utils_regex import *
from th_utils_tables import *

pattern = f'เ[{C}]([{C}]|)ี([{T}]|)ยะ'

syllable = ThaiSyllable("ไหล")
syllable_string = syllable.syllable_string
print(syllable_string)

def check_true_blend(first_char, second_char):
    if second_char == 'ร' and first_char in R_BLENDING_INITIALS:
        return True
    if second_char == 'ล' and first_char in L_BLENDING_INITIALS:
        return True
    if second_char == 'ว' and first_char in W_BLENDING_INITIALS:
        return True
    return False

def check_leading(first_char, second_char):
    if first_char == 'อ' and second_char == 'ย':
        return 'o'
    if first_char == 'ห' and second_char in UNPAIRED_LOW_CONSONANTS:
        return 'h'
    return False

def process_cluster(syllable, init_vowel_char='', vert_vowel_char='', fin_vowel_chars='', has_tone=True):

    def cluster_final_consonants(start_index):
        if len(syllable.thchars) <= start_index:
            return
        for i in range(start_index, len(syllable.thchars)):
            if syllable.thchars[i].char in TONE_MARKS:
                thchar.selfCluster('tone_marks_cluster')
                continue
            syllable.thchars[i].selfCluster('final_consonants_cluster')

    if init_vowel_char and not vert_vowel_char and not fin_vowel_chars:
        syllable.thchars[0].selfCluster('initial_vowels_cluster')
        if init_vowel_char == 'ไ' or init_vowel_char == 'ใ':
            if (check_true_blend(syllable.thchars[1].char, syllable.thchars[1].getAfterChar(0)) or check_leading(syllable.thchars[1].char, syllable.thchars[1].getAfterChar(0))) and \
                syllable.thchars[1].getAfterChar(1) != '์':
                syllable.thchars[1].selfCluster('initial_consonants_cluster')
                syllable.thchars[1].getAfter(0).selfCluster('initial_consonants_cluster')
                cluster_final_consonants(3)
            else:
                syllable.thchars[1].selfCluster('initial_consonants_cluster')
                cluster_final_consonants(3)

        elif check_true_blend(syllable.thchars[1].char, syllable.thchars[1].getAfterChar(0)) or \
            check_leading(syllable.thchars[1].char, syllable.thchars[1].getAfterChar(0)) == 'h':
            if syllable.thchars[1].getAfterChar(1) in TONE_MARKS:
                syllable.thchars[1].selfCluster('initial_consonants_cluster')
                syllable.thchars[1].getAfter(0).selfCluster('initial_consonants_cluster')
                cluster_final_consonants(3)
            elif syllable.thchars[1].getAfterChar(1) and syllable.thchars[1].getAfterChar(2) != '์':
                syllable.thchars[1].selfCluster('initial_consonants_cluster')
                syllable.thchars[1].getAfter(0).selfCluster('initial_consonants_cluster')
                cluster_final_consonants(3)
            else:
                if check_ambiguous_initial(syllable.thchars[0].char, syllable.thchars[1].char, syllable.thchars[2].char):
                    syllable.thchars[1].selfCluster('initial_consonants_cluster')
                    syllable.thchars[1].getAfter(0).selfCluster('initial_consonants_cluster')
                    cluster_final_consonants(3)
                else:
                    syllable.thchars[1].selfCluster('initial_consonants_cluster')
                    cluster_final_consonants(2)
        elif not syllable.thchars[1].getAfterChar(1) or syllable.thchars[1].getAfterChar(2) != '์':
                syllable.thchars[1].selfCluster('initial_consonants_cluster')
                cluster_final_consonants(2)
        if syllable.thchars[-1].char == '์':
            syllable.thchars[-1].selfCluster('final_consonants_cluster')
            syllable.thchars[-2].selfCluster('final_consonants_cluster')
        return

    init_vowel_index = -1
    vert_vowel_index = len(syllable.thchars) + 1
    fin_vowel_indexes = [len(syllable.thchars) + 1]
    for thchar in syllable.thchars:
        if init_vowel_char:
            if thchar.char == init_vowel_char:
                thchar.selfCluster('initial_vowels_cluster')
                init_vowel_index = thchar.getPosition()
        if vert_vowel_char:
            if thchar.char == vert_vowel_char:
                thchar.selfCluster('final_vowels_cluster')
                vert_vowel_index = thchar.getPosition()
        if fin_vowel_chars:
            if len(fin_vowel_chars) == 2:
                if thchar.char == fin_vowel_chars[0] and thchar.getAfterChar(0) == fin_vowel_chars[1]:
                    thchar.selfCluster('final_vowels_cluster')
                    thchar.getAfter(0).selfCluster('final_vowels_cluster')
                    fin_vowel_indexes[0] = thchar.getPosition()
                    fin_vowel_indexes.append(thchar.getAfter(0).getPosition())
            elif thchar.char == fin_vowel_chars[0]:
                thchar.selfCluster('final_vowels_cluster')
                fin_vowel_indexes[0] = thchar.getPosition()

    for i, thchar in enumerate(syllable.thchars):
        if i > init_vowel_index and i < vert_vowel_index and i < fin_vowel_indexes[0]:
            if has_tone and thchar.char in TONE_MARKS:
                thchar.selfCluster('tone_marks_cluster')
                continue
            thchar.selfCluster('initial_consonants_cluster')
        if i > vert_vowel_index and i < fin_vowel_indexes[0]:
            if has_tone and thchar.char in TONE_MARKS:
                thchar.selfCluster('tone_marks_cluster')
                continue
            thchar.selfCluster('final_consonants_cluster')
        if i > fin_vowel_indexes[-1]:
            thchar.selfCluster('final_consonants_cluster')

def process_roles(syllable):

    initial_vowels_cluster = syllable.getInitialVowelsClusterList()
    initial_consonants_cluster = syllable.getInitialConsonantsClusterList()
    final_vowels_cluster = syllable.getFinalVowelsClusterList()
    final_consonants_cluster = syllable.getFinalConsonantsClusterList()

    for thchar in initial_vowels_cluster + final_vowels_cluster:
        thchar.selfRole('vowel')
    
    if syllable.getToneMarksClusterList():
        for thchar in syllable.getToneMarksClusterList():
            thchar.selfRole('tone_mark')

    if len(initial_consonants_cluster) == 2:
        if check_leading(initial_consonants_cluster[0].char, initial_consonants_cluster[1].char):
            initial_consonants_cluster[0].selfRole('leading_consonant')
            initial_consonants_cluster[0].getAfter(0).selfRole('initial_consonant')
        elif initial_consonants_cluster[-1] is not initial_consonants_cluster[0]:
            initial_consonants_cluster[0].selfRole('initial_consonant')
            initial_consonants_cluster[-1].selfRole('blending_consonant')
    elif initial_consonants_cluster[-1] is initial_consonants_cluster[0]:
        initial_consonants_cluster[0].selfRole('initial_consonant')
    
    if final_consonants_cluster:
        final_consonants_cluster[0].selfRole('final_consonant')
        if final_consonants_cluster[-1].char == '์':
            final_consonants_cluster[-1].selfRole('silent_character')
            final_consonants_cluster[-2].selfRole('silent_character')

def process_blend(syllable):
    syllable.true_blend = check_true_blend(syllable.getInitialConsonantChar(), syllable.getBlendingConsonantChar())

def process_initial_sound(syllable):
    for initial_sound_key in INITIAL_SOUNDS.keys():
        if syllable.initial_consonants[0].char in INITIAL_SOUNDS[initial_sound_key]:
            syllable.initial_sound = initial_sound_key

def process_initial_class(syllable):
    syllable.initial_class = syllable.initial_consonants_cluster[0].consonant_class

def process_final_sound(syllable):
    final_sound = '-'
    vowel_string = syllable.getVowelString()
    if not vowel_string:
        syllable.final_sound = final_sound
        return
    if not syllable.final_consonants:
        if vowel_string[-1] == 'ำ':
            final_sound = 'ม'
        if vowel_string[0] == 'ไ' or vowel_string[0] == 'ใ':
            final_sound = 'ย'
        if vowel_string[0] == 'เ' and vowel_string[1] == 'า':
            final_sound = 'ว'
        syllable.final_sound = final_sound
        return
    for final_sound_key in FINAL_SOUNDS.keys():
        if syllable.final_consonants[0].char in FINAL_SOUNDS[final_sound_key]:
            final_sound = final_sound_key
    syllable.final_sound = final_sound

def get_default_vowel(vowel_string):
    for vowel_forms_key in VOWEL_FORMS.keys():
        if vowel_string in VOWEL_FORMS[vowel_forms_key]:
            return vowel_forms_key

def process_vowel(syllable):
    vowel_string = syllable.getVowelString()
    if not vowel_string:
        if not syllable.final_consonants:
            syllable.vowel_default = '-ะ'
        else:
            syllable.vowel_default = 'โ-ะ'
    else:
        syllable.vowel_default = get_default_vowel(vowel_string)

    if syllable.vowel_default in SHORT_LONG_VOWEL_PAIRS.get_forward_keys():
        syllable.vowel_duration = 'short'
        syllable.vowel_short = syllable.vowel_default
        syllable.vowel_long = SHORT_LONG_VOWEL_PAIRS[syllable.vowel_default]
    else:
        syllable.vowel_duration = 'long'
        syllable.vowel_short = SHORT_LONG_VOWEL_PAIRS.reverse_get(syllable.vowel_default)
        syllable.vowel_long = syllable.vowel_default

def process_live_dead(syllable):
    if syllable.final_sound == '-':
        if syllable.vowel_duration == 'short':
            syllable.live_dead = 'dead'
        if syllable.vowel_duration == 'long':
            syllable.live_dead = 'live'
        return
    if syllable.final_sound in DEAD_FINAL_SOUNDS:
        syllable.live_dead = 'dead'
    elif syllable.final_sound in LIVE_FINAL_SOUNDS:
        syllable.live_dead = 'live'

def process_tone(syllable):
    tone_mark = syllable.getToneMarksClusterString()
    print(tone_mark)
    syllable.tone_mark = tone_mark
    syllable.tone = get_tone(syllable.initial_class, syllable.live_dead, syllable.vowel_duration, tone_mark)

if re.search(f'[{C}]ึ', syllable_string):
    syllable.vowel_default = '-ึ'
    process_cluster(syllable, vert_vowel_char='ึ')
elif re.search(f'[{C}]ุ', syllable_string):
    process_cluster(syllable, vert_vowel_char='ุ')
elif re.search(f'[{C}]ู', syllable_string):
    process_cluster(syllable, vert_vowel_char='ู')
elif re.search(f'[{C}]รร', syllable_string):
    process_cluster(syllable, fin_vowel_chars='รร', has_tone=False)
elif re.search(f'[{C}]([{T}]|)ำ', syllable_string):
    process_cluster(syllable, fin_vowel_chars='ำ')
elif re.search(f'[{C}]ฤ', syllable_string):
    process_cluster(syllable, fin_vowel_chars='ฤ', has_tone=False)

elif re.search(f'แ[{C}]([{C}]|)็[{C}]', syllable_string):
    process_cluster(syllable, fin_vowel_chars='็', has_tone=False)
elif re.search(f'แ[{C}]([{C}]|)([{T}]|)ะ', syllable_string):
    process_cluster(syllable, init_vowel_char='แ', fin_vowel_chars='ะ')
elif re.search(f'แ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='แ')

elif re.search(f'เ[{C}]([{C}]|)ี([{T}]|)ยะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ี', fin_vowel_chars='ยะ')
elif re.search(f'เ[{C}]([{C}]|)ื([{T}]|)อะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ื', fin_vowel_chars='อะ')
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)อะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='อะ')
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)าะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='าะ')
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)ะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='ะ')
elif re.search(f'เ[{C}]([{C}]|)ี([{T}]|)ย([^์]|)', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ี', fin_vowel_chars='ย')
elif re.search(f'เ[{C}]([{C}]|)ื([{T}]|)อ([^์]|)', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ื', fin_vowel_chars='อ')
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)อ([^์]|)', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='อ')
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)า', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='า')
elif re.search(f'เ[{C}]([{C}]|)ิ([{T}]|)[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ิ')
elif re.search(f'เ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='เ')
elif re.search(f'[{C}]([{T}]|)า', syllable_string):
    process_cluster(syllable, fin_vowel_chars='า')
    process_cluster_one_final(syllable, 'า')
elif re.search(f'[{C}]ิ', syllable_string):
    process_cluster(syllable, vert_vowel_char='ิ')
elif re.search(f'[{C}]ี', syllable_string):
    process_cluster(syllable, vert_vowel_char='ี')

elif re.search(f'[{C}]([{C}]|)ื([{T}]|)อ', syllable_string):
    process_cluster(syllable, vert_vowel_char='ื', fin_vowel_chars='อ')
elif re.search(f'[{C}]ื([{T}]|)[{C}]', syllable_string):
    process_cluster(syllable, vert_vowel_char='ื')

elif re.search(f'โ[{C}]([{C}]|)([{T}]|)ะ', syllable_string):
    process_cluster(syllable, init_vowel_char='โ', fin_vowel_chars='ะ')
elif re.search(f'โ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='โ')

elif re.search(f'ไ[{C}]ย([^์]|)', syllable_string):
    process_cluster(syllable, init_vowel_char='ไ', fin_vowel_chars='ย')
elif re.search(f'ไ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='ไ')
elif re.search(f'ใ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='ใ')

elif re.search(f'[{C}]ั([{T}]|)วะ', syllable_string):
    process_cluster(syllable, vert_vowel_char='ั', fin_vowel_chars='วะ')
elif re.search(f'[{C}]ั([{T}]|)ว', syllable_string):
    process_cluster(syllable, vert_vowel_char='ั', fin_vowel_chars='ว')
elif re.search(f'[{C}]ั([{T}]|)[{C}]', syllable_string):
    process_cluster(syllable, vert_vowel_char='ั')
    process_cluster_one_final(syllable, 'ั')
elif re.search(f'[{C}]([{T}]|)ะ', syllable_string):
    process_cluster(syllable, fin_vowel_chars='ะ')
    process_cluster_one_final(syllable, 'ะ')

elif re.search(f'[{C}]็อ[{C}]', syllable_string):
    process_cluster(syllable, vert_vowel_char='็', fin_vowel_chars='อ', has_tone=False)
elif re.search(f'[{C}]([{T}]|)อ', syllable_string):
    process_cluster(syllable, fin_vowel_chars='อ')

elif re.search(f'[{C}]([{T}]|)ว[{C}]', syllable_string):
    process_cluster(syllable, fin_vowel_chars='ว')
    process_cluster_one_final(syllable, 'ว')

elif re.search(f'[{C}][{C}]', syllable_string):
    print('implied oh')

print('cluster')
for thchar in syllable.thchars:
    print(thchar.cluster)

process_roles(syllable)

print('role')
for thchar in syllable.thchars:
    print(thchar.role)

process_blend(syllable)
process_initial_sound(syllable)
process_initial_class(syllable)
process_final_sound(syllable)
process_vowel(syllable)
process_live_dead(syllable)
process_tone(syllable)

print(syllable.getInformation())