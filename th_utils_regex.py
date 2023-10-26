class BidirectionalDict:
    def __init__(self):
        self.forward_dict = {}
        self.reverse_dict = {}

    def __setitem__(self, key, value):
        self.forward_dict[key] = value
        self.reverse_dict[value] = key

    def __getitem__(self, key):
        return self.forward_dict[key]

    def reverse_get(self, value):
        return self.reverse_dict[value]

    def get_forward_keys(self):
        return list(self.forward_dict.keys())

    def get_reverse_keys(self):
        return list(self.reverse_dict.keys())

    def __str__(self):
        return str(self.forward_dict)
    
SHORT_LONG_VOWEL_PAIRS = BidirectionalDict()
SHORT_LONG_VOWEL_PAIRS['-ะ'] = '-า'
SHORT_LONG_VOWEL_PAIRS['แ-ะ'] = 'แ-'
SHORT_LONG_VOWEL_PAIRS['เ-าะ'] = '-อ'
SHORT_LONG_VOWEL_PAIRS['เ-ะ'] = 'เ-'
SHORT_LONG_VOWEL_PAIRS['เ-อะ'] = 'เ-อ'
SHORT_LONG_VOWEL_PAIRS['โ-ะ'] = 'โ-'
SHORT_LONG_VOWEL_PAIRS['-ิ'] = '-ี'
SHORT_LONG_VOWEL_PAIRS['-ึ'] = '-ื'
SHORT_LONG_VOWEL_PAIRS['-ุ'] = '-ู'
SHORT_LONG_VOWEL_PAIRS['เ-ียะ'] = 'เ-ีย'
SHORT_LONG_VOWEL_PAIRS['เ-ือะ'] = 'เ-ือ'
SHORT_LONG_VOWEL_PAIRS['-ัวะ'] = '-ัว'
SHORT_LONG_VOWEL_PAIRS['ไ-'] = '-าย'
SHORT_LONG_VOWEL_PAIRS['-็อย'] = '-อย'
SHORT_LONG_VOWEL_PAIRS['-'] = 'เ-ย'
SHORT_LONG_VOWEL_PAIRS['-'] = 'โ-ย'
SHORT_LONG_VOWEL_PAIRS['-ุย'] = ''
SHORT_LONG_VOWEL_PAIRS['-'] = 'เ-ือย'
SHORT_LONG_VOWEL_PAIRS['-'] = '-วย'
SHORT_LONG_VOWEL_PAIRS['-'] = '-วาย'
SHORT_LONG_VOWEL_PAIRS['เ-า'] = '-าว'
SHORT_LONG_VOWEL_PAIRS['แ-็ว'] = 'แ-ว'
SHORT_LONG_VOWEL_PAIRS['-'] = 'เ-อว'
SHORT_LONG_VOWEL_PAIRS['เ-็ว'] = 'เ-ว'
SHORT_LONG_VOWEL_PAIRS['-ิว'] = 'เ-ียว'
SHORT_LONG_VOWEL_PAIRS['-ำ'] = ''
SHORT_LONG_VOWEL_PAIRS['-ฤ'] = ''

th_chars = {
    'consonants': [
        'ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช',
        'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด',
        'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ',
        'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ',
        'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ'
        ],
    'vowels': [
        'ิ', 'ี', 'ึ', 'ื', 'ๅ', 'ุ', 'ู', 'เ', 'โ', 'แ',
        'ะ', 'ั', 'า', 'ำ', 'ใ', 'ไ', '็'
        ],
    'tone_marks': ['่','้','๊','๋'],

    'consonant_classes': {
        'low': ['ง','ญ','ณ','น','ม','ย','ร','ฤ','ล','ฦ','ว','ฬ','ค','ฅ','ฆ','ช','ซ','ฌ','ฑ','ฒ','ท','ธ','พ','ฟ','ภ','ฮ'],
        'high': ['ข','ฃ','ฉ','ฐ','ถ','ผ','ฝ','ศ','ษ','ส','ห'],
        'mid': ['ก','จ','ฎ','ฏ','ด','ต','บ','ป','อ'],
    },

    'low_consonants': ['ง','ญ','ณ','น','ม','ย','ร','ฤ','ล','ฦ','ว','ฬ'],
    'unpaired_low_consonants': ['ง','ญ','ณ','น','ม','ย','ร','ล','ว','ฬ'],
    'paired_low_consonants': ['ค','ฅ','ฆ','ช','ซ','ฌ','ฑ','ฒ','ท','ธ','พ','ฟ','ภ','ฮ'],
    'high_consonants': ['ข','ฃ','ฉ','ฐ','ถ','ผ','ฝ','ศ','ษ','ส','ห'],
    'mid_consonants': ['ก','จ','ฎ','ฏ','ด','ต','บ','ป','อ'],

    'leading_consonants': ['ห','อ'],

    'blending_consonants': ['ย','ร','ล','ว'],
    'r_blending_initials': ['ก','ข','ค','ต','ป','พ'],
    'l_blending_initials': ['ก','ข','ค','ป','พ','ผ'],
    'w_blending_initials': ['ก','ข','ค'],

    'initial_vowels': ['แ', 'เ', 'โ', 'ไ', 'ใ'],

    'initial_sounds': {
        'ก': ['ก'],
        'ค': ['ข','ฃ','ค','ฅ','ฆ'],
        'ง': ['ง'],
        'จ': ['จ'],
        'ช': ['ฉ','ช','ฌ'],
        'ซ': ['ซ','ศ','ษ','ส'],
        'ย': ['ญ','ย'],
        'ด': ['ฎ','ด'],
        'ต': ['ฏ','ต'],
        'ท': ['ฐ','ฑ','ฒ','ถ','ท','ธ'],
        'น': ['ณ','น',],
        'บ': ['บ'],
        'ป': ['ป'],
        'พ': ['ผ','พ','ภ'],
        'ฟ': ['ฝ','ฟ'],
        'ม': ['ม'],
        'ร': ['ร','ฤ'],
        'ล': ['ล','ฬ','ฦ'],
        'ว': ['ว'],
        'ฮ': ['ห','ฮ'],
        'อ': ['อ']
    },

    'final_sounds': {
        'ก': ['ก','ข','ฃ','ค','ฅ','ฆ'],
        'บ': ['บ','ป','ผ','ฝ','พ','ฟ','ภ'], #ฝ
        'ด': ['จ','ฉ','ช','ฌ','ฎ','ฏ','ฐ','ฑ','ฒ','ด','ต','ถ','ท','ธ','ศ','ษ','ส'],
        'น': ['ญ','ณ','น','ร','ล','ฬ'],
        'ม': ['ม'],
        'ย': ['ย'],
        'ว': ['ว'],
        'ง': ['ง'],
    },

    'live_final_sounds': ['น','ม','ย','ว','ง'],
    'dead_final_sounds': ['ก','บ','ด'],

    'vowel_forms': {
        '-ะ': ['ั', 'รร', 'ะ'],
        '-า': ['า'],
        'แ-ะ': ['แ็','แะ'],
        'แ-': ['แ'],
        'เ-าะ': ['็อ','เาะ'],
        '-อ': ['อ'],
        'เ-ะ': ['เ็','เะ'],
        'เ-': ['เ'],
        'เ-อะ': ['เอะ'], # เ-ิ
        'เ-อ': ['เิ','เอ'],
        'โ-ะ': ['โะ'],
        'โ-': ['โ'],
        '-ิ': ['ิ'],
        '-ี': ['ี'],
        '-ึ': ['ึ'],
        '-ื': ['ิ','ิอ'],
        '-ุ': ['ุ'],
        '-ู': ['ู'],

        'เ-ียะ': ['เียะ'],
        'เ-ีย': ['เีย'],
        'เ-ือะ': ['ือะ'],
        'เ-ือ': ['เือ'],
        '-ัวะ': ['ัวะ'],
        '-ัว': ['ว','ัว'], # ะ ว

        'ไ-': ['ไ','ใ','ไย'],
        '-าย': ['าย'],
        '-็อย': ['็อย'],
        '-อย': ['อย'],
        'เ-ย': ['เย'],
        'โ-ย': ['โย'],
        '-ุย': ['ุย'],
        'เ-ือย': ['เือย'],
        '-วย': ['วย'],
        '-วาย': ['วาย'],

        'เ-า': ['เา'],
        '-าว': ['าว'],
        'แ-็ว': ['แ็ว'],
        'แ-ว': ['แว'],
        'เ-อว': ['เอว'],
        'เ-็ว': ['เ็ว'],
        'เ-ว': ['เว'],
        '-ิว': ['ิว'],
        'เ-ียว': ['เียว'],

        '-ำ': ['ำ'], #amam
        '-ฤ': ['ฤ'],
    },

    'consonant_pronounciation'
}


string = ''
for char in th_chars['consonants']:
    string = string + char
C = string

string = ''
for char in th_chars['vowels']:
    string = string + char
V = string

string = ''
for char in th_chars['tone_marks']:
    string = string + char
T = string

CONSONANTS = th_chars['consonants']
VOWELS = th_chars['vowels']
TONE_MARKS = th_chars['tone_marks']

CONSONANT_CLASSES = th_chars['consonant_classes']

LOW_CONSONANTS = th_chars['consonant_classes']['low']
UNPAIRED_LOW_CONSONANTS = th_chars['unpaired_low_consonants']
PAIRED_LOW_CONSONANTS = th_chars['paired_low_consonants']
HIGH_CONSONANTS = th_chars['consonant_classes']['high']
MID_CONSONANTS = th_chars['consonant_classes']['mid']

LEADING_CONSONANTS = th_chars['leading_consonants']

BLENDING_CONSONANTS = th_chars['blending_consonants']
R_BLENDING_INITIALS = th_chars['r_blending_initials']
L_BLENDING_INITIALS = th_chars['l_blending_initials']
W_BLENDING_INITIALS = th_chars['w_blending_initials']

INITIAL_VOWELS = th_chars['initial_vowels']

INITIAL_SOUNDS = th_chars['initial_sounds']
FINAL_SOUNDS = th_chars['final_sounds']

LIVE_FINAL_SOUNDS = th_chars['live_final_sounds']
DEAD_FINAL_SOUNDS = th_chars['dead_final_sounds']

VOWEL_FORMS = th_chars['vowel_forms']