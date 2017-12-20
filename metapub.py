
# coding: utf-8

# In[14]:

get_ipython().system('pip install metapub')

from metapub import PubMedFetcher
from metapub import MedGenFetcher
from metapub import ClinVarFetcher


# In[15]:

fetch = PubMedFetcher()

# get the first 5 pmids matching "breast neoplasm" keyword search
pmids = fetch.pmids_for_query('breast neoplasm', retmax=5)

# get abstract for each article:
for pmid in pmids:
    article = fetch.article_by_pmid(pmid)
    print(article.title)
    print(article.journal, article.year, article.volume, article.issue)
    print(article.authors)


# In[16]:

'''
The MedGen (medical genetics) database is a clinical dictionary linking medical 
concepts across multiple medical ontologies and dictionaries such as OMIM and SNOMED.
'''

fetch = MedGenFetcher()

concept = fetch.concept_by_uid('336867')
print(concept)


# In[17]:

'''
The ClinVar database contains information submitted by genetic researchers, labs, and 
testing companies around the world.
'''

clinvar = ClinVarFetcher()

pubmed_citations = clinvar.pmids_for_hgvs('NM_000249.3:c.1958T>G')
print(pubmed_citations)

