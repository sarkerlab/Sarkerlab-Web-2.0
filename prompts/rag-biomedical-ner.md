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

## Prompt Structure

The full dataset-specific prompts are provided in supplementary materials (Tables 8–12) of the paper. The base prompt begins with:

<div class="prompt-block" markdown="0">
<pre>
You are a medical AI ...
[Dynamically retrieved annotated examples inserted here via RAG]
Input: ['token1', 'token2', ...]
Output: ['token1-TAG', 'token2-TAG', ...]
</pre>
</div>

### Input/Output Format

The paper uses two equivalent I/O formats. Example from the paper:

**Token-level format:**
<div class="prompt-block" markdown="0">
<pre>
Input: ['I', 'was', 'a', 'codeine', 'addict.']
Output: ['I-O', 'was-O', 'a-O', 'codeine-B-Clinical_Impacts', 'addict.I-Clinical_Impacts']
</pre>
</div>

**Sentence-level format:**
<div class="prompt-block" markdown="0">
<pre>
Input: ['I was a codeine addict.']
Output: ['I-O', 'was-O', 'a-O', 'codeine-B-Clinical_Impacts', 'addict.I-Clinical_Impacts']
</pre>
</div>

## Usage Notes

This prompt is from the paper "Retrieval augmented generation based dynamic prompting for few-shot biomedical named entity recognition using large language models" (Ge et al., 2025).

- **Approach:** Uses RAG to dynamically select the most relevant annotated examples as in-context learning demonstrations for each input, rather than using a fixed set of examples.
- **Retrieval methods evaluated:** TF-IDF, SBERT, ColBERT, and DPR for selecting contextually relevant examples.
- **Key innovation:** The prompt is not static — for each input text, similar annotated examples are retrieved and inserted as few-shot demonstrations.
- **Full prompts:** Dataset-specific prompts are available in supplementary materials (Tables 8–12) of the paper.
