---
layout: prompt
title: RAG-Based Dynamic Prompting for Biomedical NER
permalink: /prompts/rag-biomedical-ner/
group: Information Extraction
paper: https://doi.org/10.21203/rs.3.rs-7216581/v1
tags:
  - NER
  - RAG
  - few-shot
---

## System Prompt

<div class="prompt-block" markdown="0">
<pre>
You are a biomedical named entity recognition (NER) system. Your task is to identify and extract biomedical named entities from the given text.

Entity types to extract:
- Drug/Medication names
- Diseases/Conditions
- Adverse Drug Events (ADEs)
- Signs and Symptoms

For each entity found, output the entity text and its type.

Here are some examples:
[Dynamically retrieved examples based on similarity to the input text are inserted here]

Now, identify all biomedical named entities in the following text:
</pre>
</div>

## Usage Notes

This prompt is from the paper "Retrieval augmented generation based dynamic prompting for few-shot biomedical named entity recognition using large language models" (Ge et al., 2025).

- **Approach:** Uses RAG to dynamically select the most relevant annotated examples as in-context learning demonstrations for each input, rather than using a fixed set of examples.
- **Retrieval methods evaluated:** TF-IDF, SBERT, ColBERT, and DPR for selecting contextually relevant examples.
- **Key innovation:** The prompt is not static — for each input text, similar annotated examples are retrieved and inserted as few-shot demonstrations.
- **Datasets:** Evaluated on multiple biomedical NER benchmarks.
