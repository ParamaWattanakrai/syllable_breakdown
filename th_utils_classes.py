from th_utils_regex import *

class ThaiCharacter():
    def __init__(self, char, syllable=None, position=None, before=[], after=[], cluster='unknown', char_role='unknown'):
        self.char = char
        self.syllable = syllable
        self.position = position
        self.before = before
        self.after = after
        self.cluster = cluster
        self.role = char_role
        
        self.assignClass()
    def getInformation(self):
        chars_before = []
        chars_after = []
        for char in self.before:
            chars_before.append(char.char)
        for char in self.after:
            chars_after.append(char.char)
        return f'''
            Character: {self.char}
            In Syllable: {self.syllable.string}
            Position: {self.position}
            Class: {self.consonant_class}
            In Cluster: {self.cluster}
            Role: {self.role}\nChracters Before: {chars_before}\nCharacters After: {chars_after}
            '''
    def getChar(self):
        return self.char
    def getPosition(self):
        return self.position
    def getSyllable(self):
        return self.syllable
    def getClass(self):
        if not self.consonant_class:
            return None
    
    def getBefore(self, distance):
        distance += 1
        if len(self.before) < distance:
            return None
        return self.before[-distance]
    def getAfter(self, distance):
        if len(self.after) <= distance:
            return None
        return self.after[distance]
    def getBeforeChar(self, distance):
        if not self.getBefore(distance):
            return None
        return self.getBefore(distance).getChar()
    def getAfterChar(self, distance):
        if not self.getAfter(distance):
            return None
        return self.getAfter(distance).getChar()
    
    def selfCluster(self, cluster):
        return self.syllable.assignCluster(self, cluster)
    def selfRole(self, role):
        return self.syllable.assignRole(self, role)

    def assignClass(self):
        for consonant_class_key in CONSONANT_CLASSES.keys():
            if self.char in CONSONANT_CLASSES[consonant_class_key]:
                self.consonant_class = consonant_class_key

class ThaiSyllable:
    def __init__(self, syllable_string):
        self.syllable_string = syllable_string
        self.thchars = []
        
        self.initial_vowels_cluster = []
        self.initial_consonants_cluster = []
        self.tone_marks_cluster = []
        self.final_vowels_cluster = []
        self.final_consonants_cluster = []

        self.leading_consonants = []
        self.initial_consonants = []
        self.blending_consonants = []
        self.vowels = []
        self.tone_marks = []
        self.final_consonants = []
        self.silent_characters = []

        self.true_blend = False

        self.syllable_class = ''
        self.initial_class = ''
        self.final_sound = ''

        self.vowel_sound = ''
        self.vowel_duration = ''
        self.vowel_short = ''
        self.vowel_long = ''

        self.live_dead = ''

        self.tone_mark = ''
        self.tone = ''

        self.appendThChars()
        self.appendBeforeAfter()
        
    def appendThChars(self):
        for index, char in enumerate(self.syllable_string):
            thchar = ThaiCharacter(char, self, index)
            self.thchars.append(thchar)
    def appendBeforeAfter(self):
        for index, thchar in enumerate(self.thchars):
            thchar.before = self.thchars[:index]
            thchar.after = self.thchars[index+1:]
    def updateCluster(self):
        if self.getInitialVowelsClusterList():
            for thchar in self.getInitialVowelsClusterList():
                if thchar.cluster != 'initial_vowels_cluster':
                    self.initial_vowels_cluster.remove(thchar)
        if self.getInitialConsonantsClusterList():
            for thchar in self.getInitialConsonantsClusterList():
                if thchar.cluster != 'initial_consonants_cluster':
                    self.initial_consonants_cluster.remove(thchar)
        if self.getFinalVowelsClusterList():
            for thchar in self.getFinalVowelsClusterList():
                if thchar.cluster != 'final_vowels_cluster':
                    self.final_vowels_cluster.remove(thchar)
        if self.getToneMarksClusterList():
            for thchar in self.getToneMarksClusterList():
                if thchar.cluster != 'tone_marks_cluster':
                    self.tone_marks_cluster.remove(thchar)
        if self.getFinalConsonantsClusterList():
            for thchar in self.getFinalConsonantsClusterList():
                if thchar.cluster != 'final_consonants_cluster':
                    self.final_consonants_cluster.remove(thchar)
    def assignCluster(self, char, cluster):
        if cluster == 'initial_vowels_cluster':
            char.cluster = cluster
            self.initial_vowels_cluster.append(char)
        elif cluster == 'initial_consonants_cluster':
            char.cluster = cluster
            self.initial_consonants_cluster.append(char)
        elif cluster == 'tone_marks_cluster':
            char.cluster = cluster
            self.tone_marks_cluster.append(char)
        elif cluster == 'final_vowels_cluster':
            char.cluster = cluster
            self.final_vowels_cluster.append(char)
        elif cluster == 'final_consonants_cluster':
            char.cluster = cluster
            self.final_consonants_cluster.append(char)
        else:
            return None
        self.updateCluster()
    def assignRole(self, char, role):
        if role == 'leading_consonant':
            char.role = role
            self.leading_consonants.append(char)
        elif role == 'initial_consonant':
            char.role = role
            self.initial_consonants.append(char)    
        elif role == 'blending_consonant':
            char.role = role
            self.blending_consonants.append(char)
        elif role == 'vowel':
            char.role = role
            self.vowels.append(char)
        elif role == 'tone_mark':
            char.role = role
            self.tone_marks.append(char)
        elif role == 'final_consonant':
            char.role = role
            self.final_consonants.append(char)
        elif role == 'silent_character':
            char.role = role
            self.silent_characters.append(char)
        else:
            return None

    def getInitialVowelsClusterList(self):
        if not self.initial_vowels_cluster:
            return []
        return self.initial_vowels_cluster
    def getInitialVowelsClusterString(self):
        if not self.getInitialVowelsClusterList():
            return ''
        string = ''
        for thchar in self.getInitialVowelsClusterList():
            string = string + thchar.getChar()
        return string
    def getInitialConsonantsClusterList(self):
        if not self.initial_consonants_cluster:
            return []
        return self.initial_consonants_cluster
    def getInitialConsonantsClusterString(self):
        if not self.getInitialConsonantsClusterList():
            return ''
        string = ''
        for thchar in self.getInitialConsonantsClusterList():
            string = string + thchar.getChar()
        return string
    def getToneMarksClusterList(self):
        if not self.tone_marks_cluster:
            return []
        return self.tone_marks_cluster
    def getToneMarksClusterString(self):
        if not self.getToneMarksClusterList():
            return ''
        string = ''
        for thchar in self.getToneMarksClusterList():
            string = string + thchar.getChar()
        return string
    def getFinalVowelsClusterList(self):
        if not self.final_vowels_cluster:
            return []
        return self.final_vowels_cluster
    def getFinalVowelsClusterString(self):
        if not self.getFinalVowelsClusterList():
            return ''
        string = ''
        for thchar in self.getFinalVowelsClusterList():
            string = string + thchar.getChar()
        return string
    def getFinalConsonantsClusterList(self):
        if not self.final_consonants_cluster:
            return []
        return self.final_consonants_cluster
    def getFinalConsonantsClusterString(self):
        if not self.getFinalConsonantsClusterList():
            return ''
        string = ''
        for thchar in self.getFinalConsonantsClusterList():
            string = string + thchar.getChar()
        return string
    
    def getLeadingConsonantChar(self):
        for thchar in self.getInitialConsonantsClusterList():
            if thchar.role == 'leading_consonant':
                return thchar.char
        return None
    def getInitialConsonantChar(self):
        for thchar in self.getInitialConsonantsClusterList():
            if thchar.role == 'initial_consonant':
                return thchar.char
        return None
    def getInitialSound(self, lang):
        if lang == 'th':
            return self.initial_sound
        if lang == 'en':
            return TH_EN_INITIAL_SOUNDS[self.initial_sound]
    def getBlendingConsonantChar(self):
        for thchar in self.getInitialConsonantsClusterList():
            if thchar.role == 'blending_consonant':
                return thchar.char
        return None
    def getBlendingSound(self, lang):
        if not self.getBlendingConsonantChar():
            return None
        if lang == 'th':
            return self.getBlendingConsonantChar()
        if lang == 'en':
            return TH_EN_INITIAL_SOUNDS[self.getBlendingConsonantChar()]
    def getVowelSound(self, lang):
        if lang == 'th':
            return self.vowel_sound
        if lang == 'en':
            return TH_EN_VOWEL_SOUNDS[self.vowel_sound]
    def getTone(self, lang):
        if lang == 'en':
            return self.tone
        if lang == 'th':
            return EN_TH_TONES[self.tone]
    def getVowelDuration(self, lang):
        if lang == 'en':
            return self.vowel_duration
        if lang == 'th':
            return EN_TH_DURATION[self.vowel_duration]
    def getLiveDead(self, lang):
        if lang == 'en':
            return self.live_dead
        if lang == 'th':
            return EN_TH_LIVE_DEAD[self.live_dead]
    def getFinalSound(self, lang):
        if lang == 'th':
            return self.final_sound
        if lang == 'en':
            return TH_EN_FINAL_SOUNDS[self.final_sound]
    
    def getVowelList(self):
        if not self.initial_vowels_cluster and not self.final_vowels_cluster:
            return []
        return self.initial_vowels_cluster + self.final_vowels_cluster
    def getVowelString(self):
        if not self.getVowelList():
            return ''
        string = ''
        for thchar in self.getVowelList():
            string = string + thchar.getChar()
        return string
    def getVowelForm(self):
        vowel_form = ''
        if self.getFinalVowelsClusterString():
            vowel_form = '-' + self.getFinalVowelsClusterString()
        vowel_form = self.getInitialVowelsClusterString() + vowel_form
        return vowel_form

    def getInitialClass(self, lang):
        if lang == 'en':
            return self.initial_class
        if lang == 'th':
            return EN_TH_CLASSES[self.initial_class]
    def getSyllableClass(self, lang):
        if lang == 'en':
            return self.syllable_class
        if lang == 'th':
            return EN_TH_CLASSES[self.syllable_class]