---
layout: prompt
title: Medical Error Detection and Correction
permalink: /prompts/medical-error-correction/
group: Error Detection
paper: https://doi.org/10.18653/v1/2024.clinicalnlp-1.56
tags:
  - few-shot
  - clinical NLP
---

## Prompt Template

<div class="prompt-block" markdown="0">
<pre>
You are an AI trained in medical knowledge. Below are examples of clinical texts (delimited by triple quotes) and clinical texts divided into sentences (delimited by triple quotes) followed by an analysis of whether there is a diagnostic error and, if so, the sentence ID and the text span containing the error. The examples also show the corrected sentence that should have been the correct diagnosis.

Example 1:
Clinical Text: '''A 28-year-old man is brought to the emergency department[...]'''
Clinical Text Sentence: '''0 A 28-year-old man is brought to the emergency department[...]'''
Error: yes
Error Sentence ID: 15
Error Sentence Span: IV pyelogram was then performed.
Corrected Sentence: Retrograde urethrogram was then performed
..............
Example n:

Now, you are given a new clinical text and Clinical Text Sentences delimited by triple quotes. Carefully evaluate and analyse the information presented in clinical text such as symptoms, clinical examination findings, patient history and other details. Determine if any of the given sentences contain a diagnostic error or not. If an error is present, identify the specific sentence ID (and the sentence with that ID) that contains this error and also correct this erroneous sentence based on the rest of clinical text. Use your knowledge and the context provided to make your assessment. Provide the answers in JSON Format with the following keys: Error, Error Sentence ID, Error Sentence, Corrected Sentence

Clinical Text: '''[text]'''
Clinical Text Sentences: '''[clinical_sentences]'''
</pre>
</div>

## Usage Notes

This prompt is from the paper "EM_Mixers at MEDIQA-CORR 2024: Knowledge-Enhanced Few-Shot In-Context Learning for Medical Error Detection and Correction" (Rajwal et al., 2024).

- **Task:** MEDIQA-CORR 2024 shared task — detecting and correcting diagnostic errors in clinical text.
- **Structure:** Three sections — Introduction, In-Context Examples (n examples), and Natural Language Instructions with the new input.
- **Output:** JSON with keys: `Error`, `Error Sentence ID`, `Error Sentence`, `Corrected Sentence`.
- **Approach:** Knowledge-enhanced few-shot in-context learning with carefully curated examples covering diverse error types.
- **Model:** GPT-4.
