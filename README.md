# Search-Engine
Implementation of KMP algorithm for creating a search engine

## Introduction
A search query is taken as input & then processed in the following order:-
```python
  string = input("Enter the search query : ")
```  
1)Tokenized using nltk word tokenize<br />
```python
  from nltk.tokenize import word_tokenize
  nltk.download('punkt')
  tokens = nltk.word_tokenize(string)
```  
2)Removed the articles, pronouns & prepositions using stopwords<br />
```python
  from nltk.corpus import stopwords
  nltk.download('stopwords')
  stop_words = set(stopwords.words("english"))
  ```
3)Removed the affixes using stemmer<br />
```python
  from nltk.stem import PorterStemmer
  ps = PorterStemmer()
  stemmed_string = []
  for w in filtered_string:
       stemmed_string.append(ps.stem(w))
```

Now, we have the filtered string which'll be searched in the sample database.<br />
Sample database consists of a .txt file which has certain links to be parsed & searched for.<br />
```python
  resp = urllib.request.urlopen(url)
  html = resp.read()
  except urllib.error.URLError as e:
              contents = e.read()
            soup = BeautifulSoup(html,"html.parser")                        
            for script in soup(["script", "style"]):
                script.extract()   
            text = soup.get_text()  
```

The links are opened & searched via KMP Algorithm for pattern matching.<br /><br />

Normalizing the search results -> done using normalization score<br />
Normalization score -> (occurences of words in input string)/(total number of words)<br /><br />

By this normalization score, we calculate the relevance of the links. Now, we display them in decreasing order of their relevance. <br />
<br /> <br />

Before running, make sure you have the required libraries installed.
```python
  import nltk
  import math 
  import urllib.request
  from nltk.corpus import stopwords
  from nltk.tokenize import word_tokenize
  from nltk.stem import PorterStemmer
  from nltk.tokenize import word_tokenize
  from bs4 import BeautifulSoup
  from KMP import KMPSearch

  nltk.download('stopwords')
  nltk.download('punkt')

```

## Built With

* [Google Colab](https://colab.research.google.com/) - The all in one place for Python


