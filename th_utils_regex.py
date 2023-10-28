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
        'middle': ['ก','จ','ฎ','ฏ','ด','ต','บ','ป','อ'],
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
        '-อ': ['อ', '็','่'],
        'เ-ะ': ['เ็','เะ'],
        'เ-': ['เ'],
        'เ-อะ': ['เอะ'], # เ-ิ
        'เ-อ': ['เิ','เอ'],
        'โ-ะ': ['โะ'],
        'โ-': ['โ'],
        '-ิ': ['ิ'],
        '-ี': ['ี'],
        '-ึ': ['ึ'],
        '-ื': ['ื','ือ'],
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
}

conversion_dicts = {
    'th_en_initial_sounds': {
        'ก': 'k',
        'ค': 'kh',
        'ง': 'ng',
        'จ': 'j',
        'ช': 'ch',
        'ซ': 's',
        'ย': 'y',
        'ด': 'd',
        'ต': 't',
        'ท': 'th',
        'น': 'n',
        'บ': 'b',
        'ป': 'p',
        'พ': 'ph',
        'ฟ': 'f',
        'ม': 'm',
        'ร': 'r',
        'ล': 'l',
        'ว': 'w',
        'ฮ': 'h',
        'อ': '-',
    },

    'th_en_vowel_sounds': {
        '-ะ': 'a',
        '-า': 'a',
        'แ-ะ': 'ae',
        'แ-': 'ae',
        'เ-าะ': 'o',
        '-อ': 'o',
        'เ-ะ': 'e',
        'เ-': 'e',
        'เ-อะ': 'eo',
        'เ-อ': 'eo',
        'โ-ะ': 'oh',
        'โ-': 'oh',
        '-ิ': 'i',
        '-ี': 'i',
        '-ึ': 'ue',
        '-ื': 'ue',
        '-ุ': 'u',
        '-ู': 'u',

        'เ-ียะ': 'ia',
        'เ-ีย': 'ia',
        'เ-ือะ': 'uea',
        'เ-ือ': 'uea',
        '-ัวะ': 'ua',
        '-ัว': 'ua',

        'ไ-': 'ai',
        '-าย': 'ai',
        '-็อย': 'oi',
        '-อย': 'oi',
        'เ-ย': 'eoi',
        'โ-ย': 'eoi',
        '-ุย': 'ui',
        'เ-ือย': 'ueai',
        '-วย': 'uai',
        '-วาย': 'uai',

        'เ-า': 'ao',
        '-าว': 'ao',
        'แ-็ว': 'aeo',
        'แ-ว': 'aeo',
        'เ-อว': 'eou',
        'เ-็ว': 'eu',
        'เ-ว': 'eu',
        '-ิว': 'iw',
        'เ-ียว': 'iao',

        '-ำ': 'am',
        '-ฤ': 'rue',
    },

    'th_en_final_sounds': {
        'ก': 'k',
        'บ': 'p',
        'ด': 't',
        'น': 'n',
        'ม': 'm',
        'ย': 'y',
        'ว': 'w',
        'ง': 'ng',
        '-': '-'
    },

    'en_th_tones': {
        'middle': 'สามัญ',
        'low': 'เอก',
        'falling': 'โท',
        'high': 'ตรี',
        'rising': 'จัตวา',
    },

    'en_th_duration': {
        'long': 'ยาว',
        'short': 'สั้น',
    },

    'en_th_live_dead': {
        'live': 'เป็น',
        'dead': 'ตาย',
    },

    'en_th_classes': {
        'middle': 'กลาง',
        'high': 'สูง',
        'low': 'ต่ำ',
    }
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
MIDDLE_CONSONANTS = th_chars['consonant_classes']['middle']

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

TH_EN_INITIAL_SOUNDS = conversion_dicts['th_en_initial_sounds']
TH_EN_VOWEL_SOUNDS = conversion_dicts['th_en_vowel_sounds']
TH_EN_FINAL_SOUNDS = conversion_dicts['th_en_final_sounds']
EN_TH_TONES = conversion_dicts['en_th_tones']
EN_TH_DURATION = conversion_dicts['en_th_duration']
EN_TH_LIVE_DEAD = conversion_dicts['en_th_live_dead']
EN_TH_CLASSES = conversion_dicts['en_th_classes']