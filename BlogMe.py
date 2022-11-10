import pandas as pd

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data = pd.read_excel('articles.xlsx')

data.describe()

#counting the number of article per source

data.groupby(['source_id'])['article_id'].count() 

#counting the numnber of reaction by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum() 

#dropping a column engagement_comment_plugin_count

data = data.drop('engagement_comment_plugin_count', axis=1)

#creating a keyword flag


# keyword = 'crash'
# l = len(data)
# keyword_flag = []
# for x in range(0,l):
#   heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)
    
def keywordflag(keyword):  
        l = len(data)
        keyword_flag = []
        for x in range(0,l):
            heading = data['title'][x]
            try:
                if keyword in heading:
                        flag = 1
                else:
                        flag = 0
            except:
                flag = 0
            keyword_flag.append(flag)
        return keyword_flag
        
k = keywordflag('support') 
            
#creating a new column in a datarame

data['keyword_flag']= pd.Series(k)

#sentimentanalyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']


#using for  extract sentiment per title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length= len(data)

for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg= 0
        pos= 0
        neu= 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment 
data['title_neu_sentiment'] = title_neu_sentiment

#creating cleaned excel data file
data.to_excel('blogme_clean.xlsx',sheet_name = 'blogmedata', index= False)
   