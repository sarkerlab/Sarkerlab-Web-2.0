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

## System Prompt

<div class="prompt-block" markdown="0">
<pre>
You are a healthcare text classification system. Given a social media post, classify it according to the specified task.

Task: [TASK_DESCRIPTION]
Classes: [CLASS_1], [CLASS_2], ...

Instructions:
- Read the post carefully
- Consider the context and language used
- Classify the post into exactly one of the specified classes
- Respond with only the class label

Post: [INPUT_TEXT]
Classification:
</pre>
</div>

## Usage Notes

This prompt is from the paper "Benchmarking Open-Source Large Language Models on Healthcare Text Classification Tasks" (Guo & Sarker, 2025).

- **Tasks evaluated:** Adverse drug event detection, health mention classification, drug intake classification, and other health-related text classification tasks on social media data.
- **Models benchmarked:** Multiple open-source LLMs compared against proprietary models.
- **Approaches:** Zero-shot classification, few-shot with examples, and LLM-augmented data for fine-tuning.
