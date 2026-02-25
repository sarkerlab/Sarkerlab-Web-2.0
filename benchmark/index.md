---
title: Benchmarks
nav:
  order: 6
  icon: fa-solid fa-ranking-star
  tooltip:
---

# LLM BENCHMARKS


{% include section.html %}
{% include benchmark.html %}

{% include section.html %}
## Task Information
All tasks listed are binary classification tasks. Please refer to our paper (https://arxiv.org/pdf/2503.15169) or their original publication for more detailed information.
{% for task in site.data.benchmark_tasks %}
### {{ task.title }}
{{ task.citation }} {% if task.doi %} [DOI Link](https://doi.org/{{ task.doi }}) {% endif %}
{% endfor %}

{% include section.html %}
## Contact
For any questions or requests related to benchmarking new models or new tasks, please contact Yuting Guo (yguo262@emory.edu).
