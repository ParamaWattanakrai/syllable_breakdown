def check_ambiguous_blend(vowel, first_char, second_char):
    ambiguous_table = {
        ('แ','ก','ร'): True,
        ('แ','ก','ล'): True,
        ('แ','ก','ว'): False,
        ('แ','ข','ร'): True,
        ('แ','ข','ล'): False,
        ('แ','ข','ว'): True,
        ('แ','ค','ร'): True,
        ('แ','ค','ล'): False,
        ('แ','ค','ว'): True,
        ('แ','ป','ร'): True,
        ('แ','ป','ล'): True,
        ('แ','พ','ร'): True,
        ('แ','พ','ล'): True,
        ('แ','ต','ร'): True,
        ('แ','ผ','ล'): True,
        
        ('เ','ก','ร'): True,
        ('เ','ก','ล'): False,
        ('เ','ก','ว'): False, #Blank
        ('เ','ข','ร'): False, #Blank
        ('เ','ข','ล'): False,
        ('เ','ข','ว'): True,
        ('เ','ค','ร'): True,
        ('เ','ค','ล'): False,
        ('เ','ค','ว'): True,
        ('เ','ป','ร'): True,
        ('เ','ป','ล'): True,
        ('เ','พ','ร'): True,
        ('เ','พ','ล'): False,
        ('เ','ต','ร'): True,
        ('เ','ผ','ล'): True,

        ('โ','ก','ร'): True,
        ('โ','ก','ล'): True,
        ('โ','ก','ว'): False,
        ('โ','ข','ร'): True,
        ('โ','ข','ล'): False,
        ('โ','ข','ว'): True, #Blank
        ('โ','ค','ร'): True,
        ('โ','ค','ล'): True,
        ('โ','ค','ว'): True,
        ('โ','ป','ร'): True,
        ('โ','ป','ล'): False,
        ('โ','พ','ร'): True,
        ('โ','พ','ล'): False,
        ('โ','ต','ร'): True,
        ('โ','ผ','ล'): True,

        ('โ','ห','ง'): False,
        ('โ','ห','ญ'): False,
        ('โ','ห','ณ'): False,
        ('โ','ห','น'): False,
        ('โ','ห','ม'): False,
        ('โ','ห','ย'): False,
        ('โ','ห','ร'): True,
        ('โ','ห','ล'): True,
        ('โ','ห','ว'): True,
        ('โ','ห','ฬ'): False,
    }
    return ambiguous_table[(vowel, first_char, second_char)]

def get_tone(initial_class, live_dead, duration, tone_mark):
    tone_table = {
        ('middle','live','short',''): 'middle',
        ('middle','live','short','่'): 'low',
        ('middle','live','short','้'): 'falling',
        ('middle','live','short','๊'): 'high',
        ('middle','live','short','๋'): 'rising',

        ('middle','live','long',''): 'middle',
        ('middle','live','long','่'): 'low',
        ('middle','live','long','้'): 'falling',
        ('middle','live','long','๊'): 'high',
        ('middle','live','long','๋'): 'rising',

        ('middle','dead','short',''): 'low',
        ('middle','dead','short','้'): 'falling',
        ('middle','dead','short','๊'): 'high',
        ('middle','dead','short','๋'): 'rising',

        ('middle','dead','long',''): 'low',
        ('middle','dead','long','้'): 'falling',
        ('middle','dead','long','๊'): 'high',
        ('middle','dead','long','๋'): 'rising',

        ('high','live','short','่'): 'low',
        ('high','live','short','้'): 'falling',
        ('high','live','short',''): 'rising',

        ('high','live','long','่'): 'low',
        ('high','live','long','้'): 'falling',
        ('high','live','long',''): 'rising',

        ('high','dead','short',''): 'low',
        ('high','dead','short','้'): 'falling',

        ('high','dead','long',''): 'low',
        ('high','dead','long','้'): 'falling',

        ('low','live','short',''): 'middle',
        ('low','live','short','่'): 'falling',
        ('low','live','short','้'): 'high',

        ('low','live','long',''): 'middle',
        ('low','live','long','่'): 'falling',
        ('low','live','long','้'): 'high',

        ('low','dead','short','่'): 'falling',
        ('low','dead','short',''): 'high',
        ('low','dead','short','๋'): 'rising',

        ('low','dead','long',''): 'falling',
        ('low','dead','long','้'): 'high',
        ('low','dead','long','๋'): 'rising',
    }
    return tone_table[(initial_class, live_dead, duration, tone_mark)]