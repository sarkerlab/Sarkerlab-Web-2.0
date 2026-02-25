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

## Prompts

This paper uses two prompts. `[X]` is replaced with task-specific wording at runtime.

### Zero-Shot Classifier / Annotator Prompt

<div class="prompt-block" markdown="0">
<pre>
You are a [X] system based on raw tweet data. The system should analyze the provided tweet and predict whether the user is [X] or not. Given a tweet as input, the system should output a 1 if the user is [X], and 0 otherwise. If a text response is generated, reanalyze the input until a 1 or 0 is generated.
</pre>
</div>

### Data Augmentation Prompt

Used to generate additional training examples. `[text]` is the original post and `[tweet]` is the placeholder for each generated post:

<div class="prompt-block" markdown="0">
<pre>
Write 5 tweets close to the tweet [text]. The output should follow this format:
tweet 1:[tweet]
tweet 2:[tweet]
tweet 3:[tweet]
tweet 4:[tweet]
tweet 5:[tweet]
</pre>
</div>

## Usage Notes

This prompt is from the paper "Evaluating Large Language Models for Health-Related Text Classification Tasks with Public Social Media Data" (Guo et al., 2024).

- **Tasks evaluated:** Six health-related classification tasks on social media data across multiple datasets.
- **Three LLM strategies compared:** (1) zero-shot classifier, (2) LLM as data annotator for training supervised models, (3) LLM-generated data augmentation for fine-tuning.
- **Key finding:** GPT-4 zero-shot classifiers outperformed SVMs in 5 out of 6 tasks; data augmentation with GPT-4 improved RoBERTa model performance.
- **Models:** GPT-3.5-turbo and GPT-4.
