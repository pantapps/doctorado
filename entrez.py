
# coding: utf-8

# In[4]:

#http://biopython.org

get_ipython().system('pip install biopython')

from Bio import Entrez
Entrez.email = "edupgv@gmail.com"
handle = Entrez.einfo()
result = handle.read()
handle.close()

print(result)


# In[ ]:

handle = Entrez.esummary(db="pubmed", id="19304878,14630660", retmode="xml")
records = Entrez.parse(handle)
for record in records:
    # each record is a Python dictionary or list.
    print(record['Title'])

handle.close()

