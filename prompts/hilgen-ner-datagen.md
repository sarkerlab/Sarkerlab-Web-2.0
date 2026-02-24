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

## System Prompt

<div class="prompt-block" markdown="0">
<pre>
You are a biomedical text generation system. Your task is to generate realistic biomedical text that contains specific named entities.

Given the following entity information from a biomedical knowledge base:
- Entity: [ENTITY_NAME]
- Entity Type: [ENTITY_TYPE]
- Definition: [DEFINITION_FROM_KB]
- Hierarchical context: [PARENT_CONCEPTS → ENTITY]

Generate a natural, realistic sentence or short passage that:
1. Contains the specified entity in a natural context
2. Is consistent with biomedical literature style
3. Includes appropriate surrounding context
4. Could plausibly appear in a clinical note, research paper, or health forum

The generated text should be annotated with the entity boundaries.
</pre>
</div>

## Usage Notes

This prompt is from the paper "HILGEN: Hierarchically-Informed Data Generation for Biomedical NER Using Knowledgebases and Large Language Models" (Ge et al., 2025).

- **Approach:** Uses hierarchical information from biomedical knowledge bases (e.g., UMLS, MeSH) to guide LLM-based generation of training data for NER models.
- **Key innovation:** Leverages the hierarchical structure of knowledge bases to provide richer context for data generation, improving entity diversity and coverage.
- **Application:** Generates synthetic training data to augment limited annotated datasets for biomedical NER.
