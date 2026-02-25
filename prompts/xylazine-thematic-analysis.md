---
layout: prompt
title: Xylazine Wound Management Thematic Analysis
permalink: /prompts/xylazine-thematic-analysis/
group: Text Analysis
paper: https://doi.org/10.48550/arXiv.2507.10803
tags:
  - thematic analysis
  - opioids
---

## Prompts

The paper iteratively developed three prompt versions (Appendix 1). `{{post}}` is replaced with the Reddit post at runtime.

### Initial Prompt (zero-shot, single theme per call)

<div class="prompt-block" markdown="0">
<pre>
You are a binary classification system based on raw Reddit post data. You are performing a content analysis of social media posts and determining their relevance to Xylazine-associated wounds.
I want you to review the following Reddit post:
{{post}}
Analyze the post's content, looking for themes and concepts as they relate to xylazine.
Now please answer the following questions one by one.
1. Please answer if the post is relevant to 'Xylazine Use Habits'. 'Xylazine Use Habits' is defined as posts where people identify how they personally use xylazine, injection vs. snort (it should exclude people talking about how other people use it).
If there is relevance to 'Xylazine Use Habits', answer "1".
If there is no relevance to 'Xylazine Use Habits', answer "0".
Your answer should be formatted as "A=[answer]".
If a text response is generated, reanalyze the post until a 1 or 0 is generated.
</pre>
</div>

### Major Revision (all 13 categories in one call)

<div class="prompt-block" markdown="0">
<pre>
You are a binary classification system based on raw Reddit post data. You are performing a content analysis of social media posts and determining their relevance to Xylazine-associated wounds.
I want you to review the following Reddit post:
{{post}}
Assess the relevance of the Reddit post to various topics related to Xylazine by answering the following prompts with "1" for relevant and "0" for not relevant.
1. Xylazine Use Habits: Identify if the post discusses personal use methods of Xylazine, such as injection or snorting, excluding mentions of others' use habits. Format: "A=[answer]".
2. Other Drugs Use Habits: Determine if the post mentions the use of other drugs alongside Xylazine, like fentanyl, oxycodone, or benzodiazepines. Format: "B=[answer]".
[... categories 3–12 follow the same pattern ...]
13. Not About Xylazine: Determine if the post doesn't mention Xylazine in any context, indicating irrelevance to the topics above. Format: "X=[answer]".
Ensure each question is answered with "1" for relevance or "0" for non-relevance. Compile all responses in a single line, separated by ', '. If a question doesn't initially yield a binary response, reanalyze until one is provided.
</pre>
</div>

### Final Prompt (structured output with few-shot examples)

<div class="prompt-block" markdown="0">
<pre>
Task: You are a binary classification system analyzing raw Reddit posts for relevance to Xylazine (commonly called tranq)-associated wounds and use. Your job is to assess the relevance of this post to 13 specific topics. For each topic, answer with "1" if relevant or "0" if not. Format each answer as specified (e.g., A=1, B=0, etc.). Output all answers on a single line, separated by commas.
- Review the Reddit post below.
- For each category (A through X), output "1" if the post is relevant or "0" if it is not.
- Output the results as a single line, strictly in the format:
  A=_, B=_, C=_, D=_, E=_, F=_, G=_, H=_, I=_, J=_, K=_, L=_, X=_
- Do not include explanations in the output. Only the classification line.
Reddit Post:
{{post}}
Relevance Categories:
A. Xylazine Use Habits
Does the post describe the author's personal use of Xylazine (e.g., injecting or snorting)? Exclude mentions of others' use.
[... categories B through K follow the same pattern ...]
L. Geography or Locale
Does it mention specific cities, states, or regions where Xylazine is found or used?
X. Not About Xylazine
Is the post entirely unrelated to Xylazine (i.e., no mention at all)?
Examples:
1. Post:
"Yes clonidine is the best drug I'd say for coming off tranq... I wanted to scratch off my own skin... blocks NPI release making you feel totally calm..."
Classification:
A=0, B=1, C=0, D=0, E=0, F=0, G=1, H=1, I=0, J=1, K=0, L=0, X=0
[... additional few-shot examples follow ...]
</pre>
</div>

## Usage Notes

This prompt is from the paper "Automated Thematic Analyses Using LLMs: Xylazine Wound Management Social Media Chatter Use Case" (Hairston et al., 2025).

- **Task:** Binary classification of Reddit posts across 13 thematic categories related to xylazine-associated wounds and use.
- **Prompt evolution:** Three iterations — single-theme per call → all 13 themes in one call → structured output with few-shot examples.
- **Data source:** Reddit posts discussing xylazine wounds and care.
- **Public health relevance:** Xylazine ("tranq") is increasingly found in the illicit drug supply and causes severe skin wounds; understanding patient experiences aids harm reduction efforts.
