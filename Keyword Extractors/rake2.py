from rake_nltk import Rake

rake = Rake()

rake.extract_keywords_from_text("RAKE is used for extracting the keywords from the text,It words irrespective of the text’s Domain")

print(rake.get_ranked_phrases())

    #[‘words irrespective’, ‘used’, ‘text’, ‘text’, ‘rake’, ‘keywords’, ‘extracting’, ‘domain’]

print(rake.get_ranked_phrases_with_scores())

    #[(4.0, ‘words irrespective’), (1.0, ‘used’), (1.0, ‘text’), (1.0, ‘text’), (1.0, ‘rake’), (1.0, ‘keywords’), (1.0, ‘extracting’), (1.0, ‘domain’)]