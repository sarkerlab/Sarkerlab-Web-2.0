---
title: Identification of Transgender Patients
tags:
  - Clinic care
  - EHR
image: /images/research/pexels-alexander-grey-3868990.jpg
---

## Introduction

Transgender people are a group of individuals whose gender identity and gender expression differ from their sex assigned at birth. The importance of transgender health research has gained increasing recognition in recent years with specific focus on mental health, cardiovascular diseases cancer, and other conditions. Nevertheless, very few large-scale longitudinal data are available to understand factors that influence transgender health. Electronic health records (EHRs) allow for systematic identification of transgender people to obtain an unbiased sample of sufficient size; however, manually reviewing EHRs can be time consuming and resource intensive. In this work, we developed natual language processing models using traditional machine learning models and deep learning models to automate identification of transgender persons based on free-text clinical notes.

## Methods 

The Study of Transition, Outcomes and Gender (STRONG) is based on a cohort of transgender members enrolled in Kaiser Permanente (KP) integrated healthcare plans from 2006 to 2014. Recently the cohort was expanded to include new transgender members through 2022. The original STRONG cohort was validated by manual review of keyword-containing text strings pertaining to 11,529 individuals whose clinical notes were used for developing text classification models. Data were divided into training (n=6917, 60%), validation (n=2306, 20%), and test (n=2306, 20%) sets by stratified splitting. Cohort validation was first conducted using traditional machine learning models, referred to as non-deep neural network architectures, which included support vector machines (SVM), random forests (RF; decision tree family), shallow neural networks (NN; neural network family), and k-nearest neighbor (k-NN; nearest-neighbors family). Grid search was performed to find the key hyper-parameters that can optimize the classification performance in validation data. In addition to traditional machine learning models, two deep learning models, Bidirectional Long Short-Term Memory Network (BiLSTM) and Transformer (RoBERTa), were also applied. Classification performance of models was evaluated based on F1-score, precision and recall metrics of the positive class. For the optimal text classification model, a range of thresholds of predicted values was explored by balancing the trade-off between false negative and false positive results. 

## Results

Among traditional machine learning algorithms, random forest and SVM produced the highest F1-scores (0.89 and 0.90, respectively) for identification of transgender people. BiLSTM yielded comparable performance (i.e., F1-score: 0.90), despite significantly more computational power needed as a deep learning classifier. Application of RoBERTa improved the performance to the F1-score of 0.95, with a recall of 0.97 and a precision of 0.94. The thresholds of predicted values from RoBERTa ranged from 0.5 to 0.8 providing a good balance of sensitivity (0.89-0.96), specificity (0.92-0.96) and accuracy (0.92-0.94).  


## Conclusions

Our developed NLP models can provide an efficient way for automated EHR-based identification of transgender people. Our experimental results shows that the transformer-based pre-training model, RoBERTa, greatly improved the performance and can achieve a good balance of sensitivity, specificity, and accuracy.


### Funding and Disclosures
 + Funding: TBD
 + Disclosure: The published contents are solely the responsibilities of the authors of the publications.
