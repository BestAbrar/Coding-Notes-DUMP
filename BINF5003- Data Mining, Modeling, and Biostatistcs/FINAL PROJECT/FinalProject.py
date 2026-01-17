import pandas as pd

df = pd.read_csv('GTA Vice_city.csv')

df = df.dropna()

word_count=[]
unique_word_count = []

for review in  df["review"]:
    words = {}
    line = review.split(" ")
    for word in line:
        if(word.lower() in words):
            words[word.lower()]+=1
        else:
            words[word.lower()]=1
    word_count.append(len(line))
    unique_word_count.append(len(words))

df["word_count"] = word_count
df["unique_word_count"] = unique_word_count

dates = []
for date in df["created"]:
    dates.append(date[:10])
df["created_date"]=dates

selected_columns = df.loc[:, ["id", "review", "created", "created_date", "voted_up", "votes_up",
                               "comment_count", "steam_purchase", "author_num_games_owned",
                               "author_num_reviews", "author_playtime_forever","author_playtime_last_two_weeks",
                               "author_playtime_at_review","author_last_played","word_count","unique_word_count"]]

selected_columns.to_csv("GTA Vice_city(cleaned).csv", index = False)