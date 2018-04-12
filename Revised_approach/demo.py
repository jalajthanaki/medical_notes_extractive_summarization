import summarize

ss = summarize.SimpleSummarizer()
input = "The patient is an 86-year-old female admitted for evaluation of abdominal pain and bloody stools. " \
        "The patient has colitis and also diverticulitis, undergoing treatment. " \
        "During the hospitalization, the patient complains of shortness of breath, which is worsening. " \
        "The patient underwent an echocardiogram, which shows severe mitral regurgitation and also large pleural effusion." \
        "This consultation is for further evaluation in this regard. As per the patient, she is an 86-year-old female, has limited activity level. " \
        "She has been having shortness of breath for many years. She also was told that she has a heart murmur, which was not followed through on a regular basis."
input_str = "Mr. ABC is a 60-year-old gentleman who had a markedly abnormal stress test earlier today in my office with severe chest pain after 5 minutes of exercise on the standard Bruce with horizontal ST depressions and moderate apical ischemia on stress imaging only. " \
            "He required 3 sublingual nitroglycerin in total (please see also admission history and physical for full details). " \
            "The patient underwent cardiac catheterization with myself today which showed mild-to-moderate left main distal disease of 30%, moderate proximal LAD with a severe mid-LAD lesion of 99%, and a mid-left circumflex lesion of 80% with normal LV function and some mild luminal irregularities in the right coronary artery with some moderate stenosis seen in the mid to distal right PDA." \
            "I discussed these results with the patient, and he had been relating to me that he was having rest anginal symptoms, as well as nocturnal anginal symptoms, and especially given the severity of the mid left anterior descending lesion, with a markedly abnormal stress test, I felt he was best suited for transfer for PCI. I discussed the case with Dr. X at Medical Center who has kindly accepted the patient in transfer."

print ss.summarize(input, 3)
print """--------------------------------------"""
print ss.summarize(input_str, 3)
