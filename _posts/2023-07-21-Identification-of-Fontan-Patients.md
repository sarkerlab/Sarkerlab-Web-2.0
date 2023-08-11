---
title: Identification of Fontan Patients
tags:
  - Clinic Care
  - EHR
image: /images/research/pexels-karolina-grabowska-4046944.jpg
---

## Background

The Fontan operation palliates single ventricle heart defects and is associated with significant morbidity and premature mortality. Native anatomy varies; thus, Fontan cases cannot always be identified by International Classification of Diseases, Ninth and Tenth Revision, Clinical Modification (ICD-9-CM and ICD-10-CM) codes, making it challenging to create large Fontan patient cohorts. We sought to develop natural language processing (NLP) based machine learning (ML) models, which utilize free text notes from electronic health records, to automatically detect Fontan cases, and compare their performances with ICD code based classification.

## Methods and Results

We included free text notes of 10,935 manually validated patients, of whom 778 (7.1%) were Fontan and 10,157 (92.9%) non-Fontan patients, from two large, diverse healthcare systems. Using 5-fold cross validation on 80% of the patient data (derivation cohort), we trained and optimized multiple ML models, namely support vector machines (SVM) and a transformer based model for language understanding named RoBERTa (2 versions), for automatically identifying Fontan cases based on free text notes. To boost classifier performances, we experimented with different text representation techniques, including a sliding window strategy to overcome the length limit imposed by RoBERTa. We compared the performances of the ML models to ICD code based classification on 20% of the held-out patient data (validation cohort) using the F1 score metric. The ICD classification model, SVM, and RoBERTa achieved F1 scores of 0.81 (95% CI: 0.79-0.83), 0.95 (95% CI: 0.92-0.97), and 0.89 (95% CI: 0.88-0.85) for the positive (Fontan) class, respectively. SVM obtained the best performance (p<0.05), and both NLP models outperformed ICD code based classification (p<0.05). The novel sliding window strategy improved performance over the base RoBERTa model (p<0.05) but did not outperform SVM. ICD code based classification tended to have more false positives compared to both NLP models.

## Conclusions

Our proposed NLP models can automatically detect Fontan patients based on clinical notes with higher accuracy than ICD codes. Since the sensitivity of ICD codes is high but the positive predictive value is low, it may be beneficial to apply ICD codes as a filter prior to applying NLP/ML to achieve optimal performance.

### Funding and Disclosures
 + Centers for Disease Control and Prevention Cooperative Agreement, Congenital Heart Defects Surveillance across Time And Regions (CHD STAR) Grant/Award Number: CDC‐RFA‐DD19‐1902B
 + Disclosure: The published contents are solely the responsibilities of the authors of the publications.

### Publication

Guo Y, Al-Garadi MA, Book WM, et al. Supervised Text Classification System Detects Fontan Patients in Electronic Records With Higher Accuracy Than ICD Codes. J Am Heart Assoc. 2023;12(13):e030046. doi:10.1161/JAHA.123.030046
