from rake_nltk import Rake
import pandas as pd


rake = Rake()
 
df = pd.read_csv("KeywordExtractors/aclImdb_v1/aclImdb/train/pos/55_9.txt")
print(df.head())

rake.extract_keywords_from_text(df)


#print(rake.get_ranked_phrases())

    #[‘words irrespective’, ‘used’, ‘text’, ‘text’, ‘rake’, ‘keywords’, ‘extracting’, ‘domain’]

print(rake.get_ranked_phrases_with_scores())

    #[(4.0, ‘words irrespective’), (1.0, ‘used’), (1.0, ‘text’), (1.0, ‘text’), (1.0, ‘rake’), (1.0, ‘keywords’), (1.0, ‘extracting’), (1.0, ‘domain’)]