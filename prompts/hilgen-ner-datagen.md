---
layout: prompt
title: "HILGEN: NER Data Generation with Knowledge Bases"
permalink: /prompts/hilgen-ner-datagen/
group: Data Augmentation
paper: https://doi.org/10.48550/arXiv.2503.04930
tags:
  - NER
  - data augmentation
---

## Prompts

HILGEN uses four prompts (Figure 3) applied sequentially to generate and annotate synthetic NER training data. `[entities]` is replaced with the target entity at runtime.

### (a) Generate sentences using related concepts

<div class="prompt-block" markdown="0">
<pre>
Please give me 10 sentences that keep the meaning of the original input sentence basically unchanged and use related concepts of [entities] in the original text based on hierarchical information of UMLS.
</pre>
</div>

### (b) Generate sentences using parents and children

<div class="prompt-block" markdown="0">
<pre>
Based on your knowledge of hierarchical information of UMLS, please find the parents and children of [entities] in the input sentence by using SNOMEDCT_US dictionary. Then, please give me 10 sentences that keep the meaning of the original input sentence basically unchanged and use parents and children of [entities] in the original text.
</pre>
</div>

### (c) Generate sentences using siblings

<div class="prompt-block" markdown="0">
<pre>
Based on your knowledge of hierarchical information of UMLS, please find the siblings of [entities] in the input sentence by using SNOMEDCT_US dictionary. Then, please give me 10 sentences that keep the meaning of the original input sentence basically unchanged and use siblings of [entities] in the original text.
</pre>
</div>

### (d) Convert generated sentences to IOB format

<div class="prompt-block" markdown="0">
<pre>
Please mark the 10 generated sentences into IOB format, and mark the words or phrases with similar meanings to entities in the original text as its corresponding entity types according to IOB format.
</pre>
</div>

## Usage Notes

This prompt is from the paper "HILGEN: Hierarchically-Informed Data Generation for Biomedical NER Using Knowledgebases and Large Language Models" (Ge et al., 2025).

- **Approach:** Uses hierarchical information from UMLS/SNOMEDCT_US to guide LLM-based generation of synthetic NER training data.
- **Pipeline:** Prompts (a)–(c) generate sentence variations using related concepts, parent/child, and sibling terms; prompt (d) converts them to IOB annotation format.
- **Key innovation:** Leverages the hierarchical structure of biomedical knowledge bases to improve entity diversity and coverage in generated data.
- **Application:** Generates synthetic training data to augment limited annotated datasets for biomedical NER.
