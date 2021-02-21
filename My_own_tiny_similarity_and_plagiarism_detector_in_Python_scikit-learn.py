#!/usr/bin/env python
# coding: utf-8

# # My own tiny similarity and plagiarism detector in Python scikit-learn
# 
# - I want to try to have a small similarity and plagiarism detector, for any files!

# ## First try
# 
# - Source: <https://kalebujordan.com/make-your-own-plagiarism-detector-in-python/>

# In[1]:


import os

extension = 'txt'
extension = 'ml'
extension = 'java'


# In[2]:


student_files = [doc for doc in os.listdir() if doc.endswith(f'.{extension}')]
print("students_files:", student_files)

student_notes =[open(File).read() for File in  student_files]


# In[5]:


len(student_notes)
len(student_notes[0])


# In[7]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[8]:


vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

vectors = vectorize(student_notes)
s_vectors = list(zip(student_files, vectors))


# In[9]:


def check_plagiarism(s_vectors):
    plagiarism_results = set()
    for student_a, text_vector_a in s_vectors:
        new_vectors =s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b , text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            score = (student_pair[0], student_pair[1],sim_score)
            plagiarism_results.add(score)
    return plagiarism_results


# Now let's sort by increasing similarity index:

# In[19]:


def sort_plagiarism(s_vectors):
    data_plagiarism = check_plagiarism(s_vectors)
    sorted_data = sorted(data_plagiarism, key=lambda n1n2score: n1n2score[::-1])
    return sorted_data


# And then filter also:

# In[22]:


def filter_plagiarism(sorted_data, threshold=0.70):
    return [ scoren1n2 for scoren1n2 in sorted_data if scoren1n2[-1] >= threshold ]


# In[31]:


for n1, n2, score in filter_plagiarism(sort_plagiarism(s_vectors)):
    name1 = n1.replace(f'.{extension}', '')[:5]
    name2 = n2.replace(f'.{extension}', '')[:5]
    print(f"Files {name1} and {name2} have similarity = {score:.2%}")


# It's already pretty good!

# In[ ]:




