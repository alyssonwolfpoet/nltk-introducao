import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import re
from nltk.probability import FreqDist

nltk.download('machado')
nltk.download('stopwords')
nltk.download('punkt')

# retorna lista de stopwords em portugues
stopwords = nltk.corpus.stopwords.words('portuguese')

# id do corpus 
# no nosso caso estamos usando id machado
nltk_id = 'machado'

# eh necessario baixar o corpus
nltk.download(nltk_id)

# agora o corpus esta acessivel 
# visualizando as obras disponiveis
print(nltk.corpus.machado.readme())
# ou
print(nltk.corpus.machado.fileids())

# apos escolher a obra
# salvamos a string em uma variavel
dom_casmurro = nltk.corpus.machado.raw('romance/marm08.txt')

# stemmatizando com Lancaster
lancaster = nltk.LancasterStemmer()
[lancaster.stem(t) for t in dom_casmurro]

# stemmatizando com Porter
porter = nltk.PorterStemmer()
[porter.stem(t) for t in dom_casmurro]

# lemmatizando com wordnet
wnl = nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for t in dom_casmurro]

tokens = word_tokenize(dom_casmurro)
print(tokens)

sent_tokens = sent_tokenize(dom_casmurro)
print(sent_tokens)

def pre_processamento(texto):
  
    # seleciona apenas letras e coloca todas em minúsculo 
    letras_min =  re.findall(r'\b[A-zÀ-úü]+\b', texto.lower())

    # remove stopwords
    stopwords = nltk.corpus.stopwords.words('portuguese')
    stop = set(stopwords)
    sem_stopwords = [w for w in letras_min if w not in stop]

    # juntando os tokens novamente em formato de texto
    texto_limpo = " ".join(sem_stopwords)

    return texto_limpo

# corpus dom casmurro
corpus_dom_casmurro = nltk.corpus.machado.raw('romance/marm08.txt')

# pre processamento
texto = pre_processamento(corpus_dom_casmurro)

# tokenizando 
tokens = word_tokenize(texto)

# contagem de frequencia
fd = FreqDist(tokens)
print("20 palavras mais frequentes:")
print(fd.most_common(20))

# plot
import matplotlib.pyplot as plt
plt.figure(figsize = (13, 8))
fd.plot(30, title = "Frequência de Palavras")