from rake_nltk import Rake
import os
import pandas as pd


rake = Rake()

os.system("cat /home/alysson/PycharmProjects/nltk-introducao/Keyword\ Extractors/aclImdb_v1/aclImdb/train/pos/*.txt >> textao.txt") 
df = pd.read_csv("textao.txt")

rake.extract_keywords_from_text(df)


#print(rake.get_ranked_phrases())

    #[‘words irrespective’, ‘used’, ‘text’, ‘text’, ‘rake’, ‘keywords’, ‘extracting’, ‘domain’]

print(rake.get_ranked_phrases_with_scores())

    #[(4.0, ‘words irrespective’), (1.0, ‘used’), (1.0, ‘text’), (1.0, ‘text’), (1.0, ‘rake’), (1.0, ‘keywords’), (1.0, ‘extracting’), (1.0, ‘domain’)]