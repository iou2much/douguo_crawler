import newspaper
#douguo_paper = newspaper.build('http://www.douguo.com/')
douguo_paper = newspaper.build('http://club.alibabatech.org/resources.htm')
#sina_paper = newspaper.build('http://www.lemonde.fr/', language='fr')
for article in douguo_paper.articles:
    print article.url 
