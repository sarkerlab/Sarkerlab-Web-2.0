---
layout: prompt
title: Automated Thematic Analysis of Health Content
permalink: /prompts/thematic-analysis/
group: Text Analysis
paper: https://doi.org/10.1093/jamiaopen/ooaf102
tags:
  - thematic analysis
  - social media
---

## Prompt

The full prompts for this paper are provided in Appendix A1 of the supplementary materials available at JAMIA Open online. The paper describes an iterative prompt development process:

- Initial zero-shot experiments were conducted, followed by single-shot and multi-shot prompting strategies.
- Prompts were refined over multiple rounds, adjusting phrasing, task instructions, and exemplar formatting to align model predictions with expert-coded labels and maximize F1-score.
- Representative examples of each theme were incorporated as few-shot demonstrations.

## Usage Notes

This prompt is from the paper "Automating inductive thematic analyses of health content using large language models" (Hairston et al., 2025).

- **Task:** Automating the traditionally manual process of inductive thematic analysis on social media health data.
- **Model:** GPT-4.
- **Input:** Social media posts on health topics.
- **Approach:** Iterative prompt refinement from zero-shot to multi-shot with representative theme examples.
- **Key finding:** LLMs can produce thematic analyses comparable to human researchers for health-related social media content.
