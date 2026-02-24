---
layout: prompt
title: Health-Related Social Media Text Classification
permalink: /prompts/health-social-media-classification/
group: Classification
paper: https://academic.oup.com/jamia/article/31/10/2181/7731085
tags:
  - classification
  - zero-shot
  - social media
---

## System Prompt

<div class="prompt-block" markdown="0">
<pre>
You are a health text classification system. Given a social media post, classify it according to the task below.

Task: Determine whether this social media post describes a personal health experience or is a general health-related statement.

Classes:
- "personal": The post describes the author's own health experience, symptoms, medication use, or health condition.
- "non-personal": The post discusses health topics in general terms, shares news, or refers to others' experiences.

Consider:
- First-person language and personal pronouns
- Specific details about personal symptoms or treatments
- Temporal references to personal experiences

Post: [INPUT_TEXT]
Label:
</pre>
</div>

## Usage Notes

This prompt is from the paper "Evaluating Large Language Models for Health-Related Text Classification Tasks with Public Social Media Data" (Guo et al., 2024).

- **Tasks evaluated:** Multiple health-related classification tasks including adverse drug event detection, personal health mention identification, and health status classification.
- **Approaches compared:** (1) LLMs as zero-shot classifiers, (2) LLMs as data annotators for training smaller models, (3) LLM-generated augmented data for fine-tuning.
- **Key finding:** LLMs show competitive zero-shot performance on health text classification but task-specific fine-tuned models still outperform on certain tasks.
- **Models evaluated:** GPT-3.5, GPT-4, and other LLMs.
