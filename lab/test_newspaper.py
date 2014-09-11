from newspaper import Article
import nltk

a = Article('http://www.douguo.com/cookbook/965175.html' , keep_article_html=True)
#a = Article('http://www.cnn.com/2014/01/12/world/asia/north-korea-charles-smith/index.html', keep_article_html=True)
a.download()
a.parse()
res = a.article_html
print res

print nltk.clean_html(res)

