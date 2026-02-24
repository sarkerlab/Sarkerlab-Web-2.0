---
layout: prompt
title: ADHD Detection from Narrative Transcripts
permalink: /prompts/adhd-detection/
group: Classification
paper: https://doi.org/10.48550/arXiv.2505.21324
tags:
  - classification
  - mental health
---

## System Prompt

<div class="prompt-block" markdown="0">
<pre>
You are a clinical NLP system for analyzing narrative transcripts. Given a transcript of a participant's narrative after viewing a naturalistic movie, analyze the linguistic and narrative features to assess indicators associated with ADHD.

Analyze the following features:
1. NARRATIVE COHERENCE: Is the narrative logically structured with clear temporal ordering?
2. DETAIL LEVEL: Does the narrator provide appropriate levels of detail without tangential information?
3. TOPIC MAINTENANCE: Does the narrator stay on topic or frequently shift between topics?
4. TEMPORAL MARKERS: Are temporal transitions clearly marked?
5. EMOTIONAL CONTENT: How are emotional elements of the story conveyed?

Provide your analysis of each feature and an overall assessment.

Transcript:
</pre>
</div>

## Usage Notes

This prompt is from the papers "Narratives After Naturalistic Movie Viewing in ADHD: A Large Language Model Analysis" (Zhu et al., 2025) and "Leveraging large language models and traditional machine learning ensembles for ADHD detection from narrative transcripts" (Zhu et al., 2025).

- **Task:** Detecting ADHD-associated patterns in narrative transcripts elicited by naturalistic movie viewing.
- **Approach:** Combines LLM-based feature extraction with traditional ML classifiers in an ensemble framework.
- **Innovation:** Uses ecologically valid narrative tasks rather than structured clinical assessments.
