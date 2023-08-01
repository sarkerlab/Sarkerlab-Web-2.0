---
title: Classification of Fall Types in Parkinson Disease From Self-report Data Using Natural Language Processing
tags:
  - NLP
image: /images/research/
---

#### Introduction

Falls can result from multiple types of biomechanical perturbations, including perturbations to an
individual’s base of support (BoS; e.g., trips) or center of mass (CoM; e.g., overextension during bending)
[1]. People with Parkinson;s disease are more likely to fall and be frequent fallers than healthy older
adults [2]. Falling in this population can be incapacitating, often resulting in soft tissue injuries, and
disabling even early in disease progression [2]. It is of particular importance to predict and prevent falls in
this population. A necessary step in this pursuit is to track falls and fall circumstances because risk factors
for trips and slips might differ from those for falls due to impaired self-motion or other causes. Historically,
fall classes have been manually coded from these free-text descriptions (e.g., [3]), but this practice is
subjective, resource intensive, and difficult to scale. Recent advances in the field of natural language
processing (NLP) hold exciting promise to automate this. Here, we aimed to develop an NLP
classification model to distinguish CoM falls from other fall types in people with Parkinson’s disease
based on free-text descriptions.

#### Methods

We modeled the discrimination between CoM- and Other-class falls as a binary classification problem. We applied
a predefined 3-fold cross validation for (80% of data) training and (20% of data) evaluation. We experimented with
multiple classifiers, specifically: naïve Bayes (NB), K-Nearest Neighbors (KNN; weighted KNNa and unweighted
KNNb), SVM, RF, Adaboost with single split trees as base classifiers, Decision Tree (DT; weighted DTa,
unweighted DTb) classifiers, and a hard-voting ensemble classifier with contributions from each of the previously
mentioned classifiers. We also experimented with the RoBERTa transformer model. The model was trained for 2, 5,
and 10 epochs. Performance was measured by taking the median of the F 1 -macro score.


#### Results
We found that the best-performing classifier was the ensemble model, achieving an F 1 -macro of 0.89
(95% CI: [0.67-1]; Table 1). The RoBERTa model had equal performance across epochs (F1-macro =
0.42; Table 1).

###### Table 1. Classifier performance at predicting fall type of our best model, an ensemble model, and RoBERTA.

|  Classifier |  Hyperparameters                                    |     F1-macro    |     95% CI      |
| ------------| --------------------------------------------------- | --------------- | --------------- |
| Ensemble    |  {NB, KNNa, SVM, RF, Adaboost, DTb} voting = ‘hard’ |       0.89      |  0.67 - 1       |
| RoBERTa     |  Epochs = 2                                         |       0.42      |  0.37 - 0.463   |




#### Conclusion
Our study demonstrated that it is possible to automate the laborious process of fall type identification by using
supervised classification methods that integrate structured and unstructured data. Despite the relatively small size of
annotated data, an ensemble classification approach produced excellent results, outperforming a state-of-the-art
transformer model.

#### References
+  B. E. Maki, P. J. Holliday, and A. K. Topper, “A Prospective Study of Postural Balance and Risk of Falling
in An Ambulatory and Independent Elderly Population,” J. Gerontol., vol. 49, no. 2, pp. M72–M84, Mar. 1994, doi:
10.1093/geronj/49.2.M72.
+  B. R. Bloem, Y. A. M. Grimbergen, M. Cramer, M. Willemsen, and A. H. Zwinderman, “Prospective
assessment of falls in Parkinson’s disease,” J. Neurol., vol. 248, no. 11, pp. 950–958, Nov. 2001, doi:
10.1007/s004150170047.
+ E. Stack and A. Ashburn, “Fall events described by people with Parkinson’s disease: implications for
clinical interviewing and the research agenda,” Physiother. Res. Int., vol. 4, no. 3, pp. 190–200, 1999, doi:
10.1002/pri.165.

#### Publications
Powell, J. M., Guo, Y., Sarker, A., McKay, J.L. (2023). Classification of Fall Types in Parkinson's Disease from Self-report Data Using Natural Language Processing. In: Juarez, J.M., Marcos, M., Stiglic, G., Tucker, A. (eds) Artificial Intelligence in Medicine. AIME 2023. Lecture Notes in Computer Science(), vol 13897. Springer, Cham. https://doi.org/10.1007/978-3-031-34344-5_20
[Read Paper] (https://link.springer.com/chapter/10.1007/978-3-031-34344-5_20)
