---
layout: default
title: Breast Cancer Research with Social Media Data
cover: breast-cancer.png
description: Breast cancer patients often discontinue their long-term treatments, such as hormone therapy, increasing the risk of cancer recurrence. These discontinuations are often caused by adverse patient-centered outcomes (PCOs) due to hormonal drug side effects or other factors...
permalink: 'research/breast-cancer'
weight: 3
category: blog
---


Breast Cancer Research with Social Media Data
----------------------------------------------

Last Update: Dec 11, 2020

### Overview

* * *

Breast cancer patients often discontinue their long-term treatments, such as hormone therapy, increasing the risk of cancer recurrence. These discontinuations are often caused by adverse patient-centered outcomes (PCOs) due to hormonal drug side effects or other factors. PCOs are not detectable through laboratory tests, and are sparsely documented in electronic health records. Thus, there is a need to explore other sources of information for PCOs associated with breast cancer treatments. Social media is a promising resource, but extracting true PCOs from it first requires the accurate detection of breast cancer patients. We describe a natural language processing (NLP) architecture for automatically detecting breast cancer patients from Twitter based on their self-reports. The architecture employs breast cancer related keywords to collect streaming data from Twitter, applies NLP patterns to pre-filter noisy posts, and then employs a machine learning classifier trained using manually-annotated data (n=5019) for distinguishing firsthand self-reports of breast cancer from other tweets. A classifier based on bidirectional encoder representations from transformers (BERT) showed human-like performance and achieved F1-score of 0.857 (inter-annotator agreement: 0.845; Cohen's kappa) for the positive class, considerably outper-forming the next best classifier--a deep neural network (F1-score: 0.665). Qualitative analyses of posts from automatically-detected users revealed discussions about side effects, non-adherence and mental health conditions, illustrating the feasibility of our social media-based approach for studying breast cancer related PCOs from a large population.

Publication:  
Al-Garadi M.A. et al. (2020) Automatic Breast Cancer Cohort Detection from Social Media for Studying Factors Affecting Patient-Centered Outcomes. In: Michalowski M., Moskovitch R. (eds) Artificial Intelligence in Medicine. AIME 2020. Lecture Notes in Computer Science, vol 12299. Springer, Cham.  
Data: [available here](https://drive.google.com/file/d/1pavaeanWcxgjtc-5Ye7-6AZh6deFThJ1/view?usp=sharing)
