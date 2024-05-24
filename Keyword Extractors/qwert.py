from rake_nltk import Rake

# Initialize RAKE

r = Rake()

# Define the text

text = "Feature extraction is not that complex. There are many algorithms available that can help you with feature extraction. Rapid Automatic Key Word Extraction is one of those"

# Extract keywords from the text

r.extract_keywords_from_text(text)

# Get the ranked phrases

keywords_rake = r.get_ranked_phrases()

print(keywords_rake)

score = r.get_ranked_phrases_with_scores()

print(score)
