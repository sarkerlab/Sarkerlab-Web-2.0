---
title: Automatic Detection of Intimate Partner Violence Victims
tags:
  - NLP
  - Machine Learning
  - Social Media
image: /images/research/
---

## Self-Report IPV on Twitter
Intimate partner violence (IPV) is a preventable public health problem that affects millions of people worldwide.
Approximately one in four women are estimated to be or have been victims of severe violence at some point in
their lives, irrespective of age, ethnicity, and economic status. Victims often report IPV experiences on social
media, and automatic detection of such reports via machine learning may enable improved surveillance and
targeted distribution of support and/or interventions for those in need. However, no artificial intelligence
systems for automatic detection currently exists, and we attempted to address this research gap. We collected
posts from Twitter using a list of IPV-related keywords, manually reviewed subsets of retrieved posts, and
prepared annotation guidelines to categorize tweets into IPV-report or non-IPV-report. We annotated 6,348
tweets in total, with the inter-annotator agreement (IAA) of 0.86 (Cohen’s kappa) among 1,834 double-
annotated tweets. The class distribution in the annotated dataset was highly imbalanced, with only 668 posts
(~11%) labeled as IPV-report. We then developed an effective natural language processing model to identify
IPV-reporting tweets automatically. The developed model achieved classification F1-scores of 0.76 for the IPV-
report class and 0.97 for the non-IPV-report class. We also conducted post-classification analyses to determine
the causes of system errors and to ensure that the system did not exhibit biases in its decisionmaking,
particularly with respect to race and gender. Our automatic model can be an essential component for a proactive
social media-based intervention and support framework, while also aiding population-level surveillance and
large-scale cohort studies.

## Self-Report IPV on Reddit

Social media platforms are increasingly being used by intimate partner violence (IPV) victims to share
experiences and seek support. If such information is automatically curated, it may be possible to conduct social
media based surveillance and even design interventions over such platforms. In this paper, we describe the
development of a supervised classification system that automatically characterizes IPV-related posts on the
social network Reddit. We collected data from four IPV-related subreddits and manually annotated the data to
indicate whether a post is a self-report of IPV or not. Using the annotated data (N=289), we trained, evaluated,
and compared supervised machine learning systems. A transformer-based classifier, RoBERTa, obtained the
best classification performance with overall accuracy of 78% and IPV-self-report class -score of 0.67. Post-
classification error analyses revealed that misclassifications often occur for posts that are very long or are non-
first-person reports of IPV. Despite the relatively small, annotated data, our classification methods obtained
promising results, indicating that it may be possible to detect and, hence, provide support to IPV victims over
Reddit.

### Funding and Disclosures
+ The study was funded by the Injury Prevention Research Center at
Emory (IPRCE), Emory University
+ Disclosure: The published contents are solely the responsibilities of
the authors of the publications.

### Publications
+ Al-Garadi M, Sarker A, Guo Y, Warren E, Yang YC, Kim S. Automatic Identification
of Intimate Partner Violence Victims From Social Media. Inj Prev [Internet].
2022;28(1353–8047):A48--A48. Available from:
https://injuryprevention.bmj.com/content/28/Suppl_1/A48.1
+ Guo Y, Kim S, Warren E, Yang YC, Sahithi L, Sarker A. Automatic Detection of
Intimate Partner Violence Victims from Social Media for Proactive Delivery of
Support. In: AMIA 2023 Informatics Summit. 2023.
