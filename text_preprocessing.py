import contractions
import emoji
from spellchecker import SpellChecker
import re

def preprocess_text(text):
    try:
        # Step 1: Handle contractions
        expanded_text = contractions.fix(text)
        
        # Step 2: Handle emojis
        emoji_text = emoji.demojize(expanded_text)
        
        # Step 3: Spell checking
        spell = SpellChecker()
        words = emoji_text.split()
        corrected_words = []
        for word in words:
            if word:
                correction = spell.correction(word)
                # Ensure we have a valid string
                if correction is not None and isinstance(correction, str):
                    corrected_words.append(correction)
                else:
                    corrected_words.append(word)
        
        # Step 4: Remove special characters and extra spaces
        corrected_text = ' '.join(corrected_words)
        corrected_text = re.sub(r'[^a-zA-Z0-9\s]', '', corrected_text)
        corrected_text = re.sub(r'\s+', ' ', corrected_text).strip()
        
        # Step 5: Convert to lowercase
        corrected_text = corrected_text.lower()

        return corrected_text
    
    except Exception as e:
        print(f"Error in preprocessing: {e}")
        return text.strip().lower()
    
    