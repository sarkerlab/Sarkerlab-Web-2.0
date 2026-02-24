---
layout: prompt
title: Two-Layer RAG for Medical Question Answering
permalink: /prompts/two-layer-rag-qa/
group: Question Answering
paper: https://www.jmir.org/2025/1/e66220/
tags:
  - RAG
  - question answering
---

## Layer 1: Individual Summary Prompt

<div class="prompt-block" markdown="0">
<pre>
You are a medical information specialist. Given a social media post from a health forum and a clinician's question, extract and summarize the relevant information from the post that helps answer the question.

Clinician's Question: [QUESTION]

Social Media Post: [POST_TEXT]

Provide a concise summary of the relevant information found in this post. If the post does not contain relevant information, state "No relevant information found."
</pre>
</div>

## Layer 2: Aggregated Summary Prompt

<div class="prompt-block" markdown="0">
<pre>
You are a medical information specialist. Given a clinician's question and a set of individual summaries extracted from social media posts, synthesize an aggregated answer.

Clinician's Question: [QUESTION]

Individual Summaries:
[SUMMARY_1]
[SUMMARY_2]
...

Synthesize these summaries into a comprehensive, coherent answer to the clinician's question. Highlight common patterns, note conflicting information, and indicate the strength of evidence based on the number of supporting posts.
</pre>
</div>

## Usage Notes

This prompt is from the paper "Two-Layer Retrieval-Augmented Generation Framework for Low-Resource Medical Question Answering Using Reddit Data" (Das et al., 2025).

- **Architecture:** A two-layer RAG approach — Layer 1 generates individual summaries from retrieved posts, Layer 2 aggregates them into a final answer.
- **Use case:** Answering clinicians' questions about emerging substances (xylazine, ketamine) using Reddit data.
- **Models compared:** Quantized Nous-Hermes-2-7B-DPO vs. GPT-4, showing comparable performance for low-resource deployment.
