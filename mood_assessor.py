from pathlib import Path
import datetime

def user_mood():
    mood = input('How do you feel today? (happy, relaxed, apathetic, sad, angry) ')
    if mood == 'happy':
        return 2
    elif mood == 'relaxed':
        return 1
    elif mood == 'apathetic':
        return 0
    elif mood == 'sad':
        return -1
    elif mood == 'angry':
        return -2
    else:
        print('Invalid input')
        return None
  
def log_mood(mood):
    fp = Path('mood_diary.txt')
    last_updated = datetime.datetime.fromtimestamp(fp.stat().st_mtime).date()
    today= datetime.datetime.now().date()
    if today != last_updated:
        print ('You already logged today')
    else:
        with fp.open('a') as f:
            f.write(str(mood) + '\n')

def analyze_mood():
    fp = Path('mood_diary.txt')
    mood_counts= {'happy': 0, 'relaxed':0,'apathetic':0, 'sad':0, 'angry':0}
    total_mood = 0
    for mood in fp.read_text().splitlines():
        if mood =='2':
            mood_counts['happy'] += 1
        elif mood =='1':
            mood_counts['relaxed'] += 1
        elif mood =='0':
            mood_counts['apathetic'] += 1
        elif mood =='-1':
            mood_counts['sad'] += 1
        elif mood =='-2':
            mood_counts['angry'] += 1

        total_mood += 1

    happy_count = mood_counts['happy']
    sad_count = mood_counts['sad']
    apathetic_count = mood_counts['apathetic']
    diagnosis = ('stable')
    if happy_count >= 5:
        diagnosis =('manic')
    elif sad_count >= 4:
        diagnosis =('depressive')
    elif apathetic_count >= 6:
        diagnosis =('schizoid')
    print( f'Your diagnosis: {diagnosis}')
