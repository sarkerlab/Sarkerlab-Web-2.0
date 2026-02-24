---
layout: prompt
title: "SMM4H Shared Task: Social Media NER and Classification"
permalink: /prompts/smm4h-social-media-nlp/
group: Information Extraction
paper: https://doi.org/10.18653/v1/2024.smm4h-1.40
tags:
  - NER
  - social media
  - shared task
---

## System Prompt

<div class="prompt-block" markdown="0">
<pre>
You are a biomedical NLP system for social media health mining. Given a social media post, perform the specified task.

Task 1 - Adverse Drug Event Classification:
Determine whether this post describes an adverse drug event (ADE).
Classes: "ADE" or "No ADE"

Task 2 - Named Entity Recognition:
Extract all mentions of:
- Drug/medication names
- Adverse effects/reactions
- Dosage information
For each entity, provide the text span and entity type.

Task 3 - Health Mention Classification:
Determine if this post contains a genuine personal health mention.
Classes: "health mention" or "non-health mention"

Post: [INPUT_TEXT]
</pre>
</div>

## Usage Notes

This prompt is from the paper "Overview of the 9th Social Media Mining for Health Applications (#SMM4H) Shared Tasks at ACL 2024" (Xu et al., 2024).

- **Context:** The SMM4H shared task series brings together researchers working on NLP for health applications using social media data.
- **Focus areas:** Adverse drug event detection, named entity recognition, and health mention classification from platforms like Twitter/X and Reddit.
- **2024 theme:** Evaluating the role of LLMs and their generalizability for social media health NLP tasks.
- **Participation:** Multiple international teams contributed approaches spanning zero-shot LLM prompting to fine-tuned transformer models.
