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

## Prompt

<div class="prompt-block" markdown="0">
<pre>
You are a psychiatrist that is specialized in the diagnosis of ADHD.
Read the transcript of a conversation with an interviewed child, who just finished watching an animated emotionally evocative four-minute film, entitled "The Present", carefully:
{% raw %}{{Transcript Content}}{% endraw %}
Please assess the child on the following diagnostic criteria A and B for Attention-Deficit/Hyperactivity Disorder:
A. A persistent pattern of inattention and/or hyperactivity-impulsivity that interferes with functioning or development, as characterized by (1) and/or (2):
1. Inattention: Six (or more) of the following symptoms have persisted to a degree that is inconsistent with developmental level and that negatively impacts directly on social and academic/occupational activities:
Note: The symptoms are not solely a manifestation of oppositional behavior, defiance, hostility, or failure to understand tasks or instructions.
a. Often fails to give close attention to details or makes careless mistakes in schoolwork, at work, or during other activities (e.g., overlooks or misses details, work is inaccurate).
b. Often has difficulty sustaining attention in tasks or play activities (e.g., has difficulty remaining focused during lectures, conversations, or lengthy reading).
c. Often does not seem to listen when spoken to directly (e.g., mind seems elsewhere, even in the absence of any obvious distraction).
d. Often does not follow through on instructions and fails to finish schoolwork, chores, or duties in the workplace (e.g., starts tasks but quickly loses focus and is easily sidetracked).
e. Often has difficulty organizing tasks and activities (e.g., difficulty managing sequential tasks; difficulty keeping materials and belongings in order; messy, disorganized work; has poor time management; fails to meet deadlines).
f. Often avoids, dislikes, or is reluctant to engage in tasks that require sustained mental effort (e.g., schoolwork or homework; for older adolescents and adults, preparing reports, completing forms, reviewing lengthy papers).
g. Often loses things necessary for tasks or activities (e.g., school materials, pencils, books, tools, wallets, keys, paperwork, eyeglasses, mobile telephones).
h. Is often easily distracted by extraneous stimuli (for older adolescents and adults, may include unrelated thoughts).
i. Is often forgetful in daily activities (e.g., doing chores, running errands; for older adolescents and adults, returning calls, paying bills, keeping appointments).
2. Hyperactivity and impulsivity: Six (or more) of the following symptoms persisted to a degree that is inconsistent with developmental level and that negatively impacts directly on social and academic/occupational activities:
Note: The symptoms are not solely a manifestation of oppositional behavior, defiance, hostility, or a failure to understand tasks or instructions.
a. Often fidgets with or taps hands or feet or squirms in seat.
b. Often leaves seat in situations when remaining seated is expected (e.g., leaves his or her place in the classroom, in the office or other workplace, or in other situations that require remaining in place).
c. Often runs about or climbs in situations where it is inappropriate. (Note: In adolescents or adults, may be limited to feeling restless.)
d. Often unable to play or engage in leisure activities quietly.
e. Is often "on the go," acting as if "driven by a motor" (e.g., is unable to be or uncomfortable being still for extended time, as in restaurants, meetings; may be experienced by others as being restless or difficult to keep up with).
f. Often talks excessively.
g. Often blurts out an answer before a question has been completed (e.g., completes people's sentences; cannot wait for turn in conversation).
h. Often has difficulty waiting his or her turn (e.g., while waiting).
i. Often interrupts or intrudes on others (e.g., butts into conversations, or activities; may start using other people's things without asking or receiving permission; for adolescents and adults, may intrude into or take over what others are doing).
B. The symptoms do not occur exclusively during the course of schizophrenia or another psychotic disorder and are not better explained by another mental disorder (e.g., mood disorder, anxiety disorder, dissociative disorder, personality disorder, substance intoxication or withdrawal).
Upon completion of the assessment, you must answer whether the child that was being interviewed has ADHD followed by a detailed justification.
Your answer should be formatted as
'''
YES/NO.
My reasons are ...
'''
</pre>
</div>

## Usage Notes

This prompt is from the paper "Narratives After Naturalistic Movie Viewing in ADHD: A Large Language Model Analysis" (Zhu et al., 2025).

- **Task:** Detecting ADHD from narrative transcripts elicited after naturalistic movie viewing.
- **Approach:** Prompt mirrors DSM-5 diagnostic criteria for ADHD, instructing the model to act as a psychiatrist.
- **Input:** `{% raw %}{{Transcript Content}}{% endraw %}` is replaced with the full post-movie interview transcript for each participant.
- **Output format:** YES/NO followed by a detailed justification.
- **Refinement:** The prompt underwent three iterative refinement cycles on development data to sharpen symptom definitions and output formatting.
