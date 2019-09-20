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

print("\t \t \t Search Engine using KMP Algorithm in Python")
string = input("Enter the search query : ")

tokens = nltk.word_tokenize(string)

stop_words = set(stopwords.words("english"))

filtered_string = []
for w in tokens:
       if w not in stop_words:
          filtered_string.append(w)
 
 
ps = PorterStemmer()
stemmed_string = []
for w in filtered_string:
       stemmed_string.append(ps.stem(w))
n = len(stemmed_string)


print("Searching.........................................")
print("\n")
text_file = open("links.txt","r")
normalizedict = dict()
countelem = [0]*len(stemmed_string)
for link in text_file.readlines():
        if (link == '\n'):
            pass
        else :
            p = 0
            url = link
            print("-----------------------------------------------------------------------------------------------------")
            print("URL of the webpage is : ",url)
            try:
              resp = urllib.request.urlopen(url)
              html = resp.read()
            except urllib.error.URLError as e:
              contents = e.read()
            soup = BeautifulSoup(html,"html.parser")                        
            for script in soup(["script", "style"]):
                script.extract()   
            text = soup.get_text()                           
            lines = (line.strip() for line in text.splitlines()) 
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))   
            text = '\n'.join(chunk for chunk in chunks if chunk) 
            mydict = dict()
            d = 0
            e = 0
            
            for word in stemmed_string:
                 KMPSearch(word, text, mydict)
                 
            for items in mydict.keys():
                  
                        if mydict[items] == 0:
                            pass
                        else:
                            countelem[p] = countelem[p] + 1
                        p = p + 1

            for i in mydict:
                d = d + mydict[i]
            e = d*1.0/len(text)
            if e == 0:
              pass
            else:
              normalizedict.update({link:e})
            print(mydict)
            print("Normalized value (sum of values present)/(length of text) is :  ",e)
print("-----------------------------------------------------------------------------------------------------")

print("\n")

print("\n############### Results ###############")
print("\n")
sorted_list = [k for v,k in sorted([(v,k) for k,v in normalizedict.items()], reverse = True)]
for i in sorted_list:
     print(i)
print("\n")
