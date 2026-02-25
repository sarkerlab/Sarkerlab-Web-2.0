---
layout: prompt
title: Healthcare Text Classification
permalink: /prompts/healthcare-text-classification/
group: Classification
paper: https://www.semanticscholar.org/paper/29db094f3bd4757300167efd94286fca04921d73
tags:
  - classification
  - social media
---

## Prompts

This paper uses three task-specific prompt templates (Table 2). `{{task}}` and `{{text}}` are replaced at runtime with the task label and input text respectively.

### Social Media Tasks

Used for breast cancer, medication regimen changes, adverse pregnancy outcomes, and potential COVID-19 cases:

<div class="prompt-block" markdown="0">
<pre>
Read the following tweet. Answer if the user is self-reporting {{task}} and explain why.
Tweet:{{text}}
Your answer should state "the tweet is self-reporting {{task}}" or "the tweet is not self-reporting potential".
</pre>
</div>

### Stigma Labeling (Clinical Note)

<div class="prompt-block" markdown="0">
<pre>
Read the following clinical note.
Clinical note:{{text}}
Answer if this note involves language about the patient which could result in the stigmatization or negative labeling of a patient, which could lead to further status loss/discrimination in the context of the patient-provider relationship. Your answer should state "the note involves ..." or "the note does not involve ...".
</pre>
</div>

### Medication Change Discussion (Clinical Note)

<div class="prompt-block" markdown="0">
<pre>
Read the following clinical note.
Clinical note:{{text}}
Answer if the presence of a medication change is discussed. Your answer should state "the presence of a medication change is discussed" or "the presence of a medication change is not discussed".
</pre>
</div>

## Usage Notes

This prompt is from the paper "Benchmarking Open-Source Large Language Models on Healthcare Text Classification Tasks" (Guo & Sarker, 2025).

- **Models benchmarked:** GEMMA-3-27B-IT, LLaMA3-70B, LLaMA4-109B, DeepSeek-R1-Distill-LLaMA-70B, and DeepSeek-V3-0324-UD-Q2_K_XL.
- **Tasks:** Six binary classification tasks — four involving social media data (breast cancer, medication regimen changes, adverse pregnancy outcomes, potential COVID-19 cases) and two involving clinical notes (stigma labeling, medication change discussion).
- **Setting:** All evaluation experiments conducted in zero-shot settings.
- **Key finding:** DeepSeek-V3 emerged as the strongest overall performer, achieving the highest F1 scores in four out of six tasks.
