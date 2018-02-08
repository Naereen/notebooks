
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Data-Challenge-:-Mangaki---September-2017" data-toc-modified-id="Data-Challenge-:-Mangaki---September-2017-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Data Challenge : Mangaki - September 2017</a></div><div class="lev2 toc-item"><a href="#Reading-data" data-toc-modified-id="Reading-data-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Reading data</a></div><div class="lev2 toc-item"><a href="#First-prediction-model" data-toc-modified-id="First-prediction-model-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>First prediction model</a></div><div class="lev2 toc-item"><a href="#Better-predicted-models" data-toc-modified-id="Better-predicted-models-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Better predicted models</a></div><div class="lev3 toc-item"><a href="#Using-watched.csv" data-toc-modified-id="Using-watched.csv-131"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Using <code>watched.csv</code></a></div><div class="lev4 toc-item"><a href="#Maping-string-rating-to-probability-of-seeing-the-movie" data-toc-modified-id="Maping-string-rating-to-probability-of-seeing-the-movie-1311"><span class="toc-item-num">1.3.1.1&nbsp;&nbsp;</span>Maping string-rating to probability of seeing the movie</a></div><div class="lev3 toc-item"><a href="#Using-titles.csv" data-toc-modified-id="Using-titles.csv-132"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Using <code>titles.csv</code></a></div><div class="lev2 toc-item"><a href="#Evaluation-from-the-data-challenge-platform" data-toc-modified-id="Evaluation-from-the-data-challenge-platform-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Evaluation from the data challenge platform</a></div>

# # Data Challenge : Mangaki - September 2017
# 
# > - See [here for more information](http://universityofbigdata.net/competition/5085548788056064?lang=en).
# > - Author: [Lilian Besson](http://perso.crans.org/besson/).
# > - License: [MIT License](https://lbesson.mit-license.org/).

# ## Reading data
# We have a few CSV files, let start by reading them.

# In[1]:


from tqdm import tqdm
import numpy as np
import pandas as pd


# In[2]:


get_ipython().system('ls -larth *.csv')


# In[3]:


get_ipython().system('cp -vf submission.csv submission.csv.old')


# In[57]:


train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
titles = pd.read_csv("titles.csv")
watched = pd.read_csv("watched.csv")


# In[56]:


np.unique(titles.category)


# Just to check they have correctly been read:

# In[58]:


train[:5]
len(train)
min(train['user_id']), max(train['user_id'])
min(train['work_id']), max(train['work_id'])


# In[6]:


test[:5]
len(test)
min(test['user_id']), max(test['user_id'])
min(test['work_id']), max(test['work_id'])


# In[7]:


watched[:5]
len(watched)
min(watched['user_id']), max(watched['user_id'])
min(watched['work_id']), max(watched['work_id'])


# ## First prediction model
# 
# - For each movie, compute the empirical average `rating` of users who saw it, using data from the train data.
# - And simply use this to predict for the other users in test data.

# In[32]:


submission = test.copy()


# In[33]:


total_average_rating = train.rating.mean()


# In[34]:


submission[:5]
len(submission)


# In[35]:


works_id = np.unique(np.append(test.work_id.unique(), train.work_id.unique()))


# In[36]:


mean_ratings = pd.DataFrame(data={'mean_rating': 0}, index=works_id)
mean_ratings[:5]
len(mean_ratings)


# In[37]:


computed_means = pd.DataFrame(data={'mean_rating': train.groupby('work_id').mean()['rating']}, index=works_id)
computed_means[:5]
len(computed_means)


# In[38]:


mean_ratings.update(computed_means)


# In[39]:


mean_ratings[:10]
len(mean_ratings)


# In[41]:


submission = submission.join(mean_ratings, on='work_id')
submission.rename_axis({'mean_rating': 'prob_willsee'}, axis="columns", inplace=True)


# In[43]:


# in case of mean on empty values
submission.fillna(value=total_average_rating, inplace=True)


# In[51]:


submission[:10]


# Let save it to `submission_naive1.csv`:

# In[52]:


submission.to_csv("submission_naive1.csv", index=False)


# In[49]:


get_ipython().system('ls -larth submission_naive1.csv')


# ## Better predicted models

# ### Using `watched.csv`

# The bonus data set `watched` can give a lot of information. There is 200000 entries in it and only 100000 in `test.csv`.

# In[66]:


len(test), len(watched)


# In[68]:


ratings = np.unique(watched.rating).tolist()
ratings


# In[67]:


watched[:5]


# #### Maping string-rating to probability of seeing the movie
# By using the train data `(user, work)` that are also in `watched`, we can learn to map string rating, i.e., `'dislike', 'neutral', 'like', 'love'`, to probability of having see the movie.

# In[84]:


watched.rename_axis({'rating': 'strrating'}, axis="columns", inplace=True)


# In[85]:


watched[:5]


# In[69]:


train[:5]


# Is there pairs `(user, work)` for which both train data and watched data are available (i.e., both see/notsee and liked/disliked) ?

# In[109]:


train.merge(watched, on=['user_id', 'work_id'])


# And what about test data?

# In[108]:


test.merge(watched, on=['user_id', 'work_id'])


# In[144]:


test.merge(watched, on=['work_id'])


# No! So we can forget about the `user_id`, and we will learn how to map liked/disliked to see/notsee for each movie.

# In[105]:


all_train = watched.merge(train, on='work_id')
all_train[:5]


# In[106]:


del all_train['user_id_x']
del all_train['user_id_y']


# We can delete the `user_id` axes.

# In[107]:


all_train[:5]


# We can first get the average rating of each work:

# In[130]:


all_train.groupby('work_id').rating.mean()[:10]


# This table now contains, for each work, a list of mapping from `strrating` to `rating`.
# It can be combined into a concise mapping, like in this form:

# In[80]:


mapping_strrating_probwillsee = {
    'dislike': 0,
    'neutral': 0.50,
    'like': 0.75,
    'love': 1,
}


# Manually, for instance for one movie:

# In[129]:


all_train[(all_train.work_id == 8025) & (all_train.strrating == 'dislike')]


# In[133]:


all_train[all_train.work_id == 8025].rating.mean()


# In[134]:


len(all_train[(all_train.work_id == 8025) & (all_train.strrating == 'dislike')].rating)
all_train[(all_train.work_id == 8025) & (all_train.strrating == 'dislike')].rating.mean()


# In[135]:


len(all_train[(all_train.work_id == 8025) & (all_train.strrating == 'neutral')].rating)
all_train[(all_train.work_id == 8025) & (all_train.strrating == 'neutral')].rating.mean()


# In[141]:


len(all_train[(all_train.work_id == 8025) & (all_train.strrating == 'like')].rating)
all_train[(all_train.work_id == 8025) & (all_train.strrating == 'like')].rating.mean()


# In[142]:


len(all_train[(all_train.work_id == 8025) & (all_train.strrating == 'love')].rating)
all_train[(all_train.work_id == 8025) & (all_train.strrating == 'love')].rating.mean()


# That's weird!

# ### Using `titles.csv`
# I don't think I want to use the titles, but clustering the works by categories could help, maybe.

# In[63]:


categories = np.unique(titles.category).tolist()
categories


# In[132]:


for cat in categories:
    print("There is {:>5} work(s) in category '{}'.".format(sum(titles.category == cat), cat))


# One category is alone, let rewrite it to `'anime'`.

# In[65]:


categories = {
    'anime': 0,
    'album': 0,
    'manga': 1,
}


# TODO !

# ## Evaluation from the data challenge platform

# TODO !
