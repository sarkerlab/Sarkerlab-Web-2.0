---
layout: prompt
title: Blood Pressure Extraction from Literature
permalink: /prompts/blood-pressure-extraction/
group: Information Extraction
paper: https://arxiv.org/abs/2402.01826
tags:
  - information extraction
  - literature mining
---

## Prompt

<div class="prompt-block" markdown="0">
<pre>
You are an AI assistant that helps people find information in scientific publications.
Read the abstract carefully:
{{abstract}}
Please answer the mean and deviation of blood pressure values based on sex.
N is the number of patients, and summaries of SBP and DBP include mean ± standard deviation.
Your answer should be formatted as
'''
N_male=[number]
N_female=[number]
SBP_in_male=[mean ± standard deviation]
SBP_in_female=[mean ± standard deviation]
DBP_in_male=[mean ± standard deviation]
DBP_in_female=[mean ± standard deviation]
'''
Answer "NA" if the information is not found.
</pre>
</div>

## Usage Notes

This prompt is from the paper "Leveraging Large Language Models for Analyzing Blood Pressure Variations Across Biological Sex from Scientific Literature" (Guo et al., 2024).

- **Task:** Automated extraction of sex-disaggregated blood pressure data from PubMed abstracts.
- **Model:** GPT-3.5-turbo in a zero-shot configuration.
- **Input:** `{{abstract}}` is replaced with the plain text of each PubMed article abstract.
- **Pipeline:** Abstracts are first filtered by keywords ("blood pressure", "mmHg") before prompt-based extraction.
- **Application:** Enables large-scale meta-analysis of blood pressure variations across biological sex from published literature.
