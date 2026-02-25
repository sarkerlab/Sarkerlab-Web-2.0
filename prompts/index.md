---
title: Prompt Collections
nav:
  order: 7
  icon: fa-solid fa-terminal
  tooltip: LLM prompt templates
---

# Prompt Collections

Reusable prompt templates developed by our lab for biomedical NLP tasks.

{% include section.html %}

{% include search-box.html %}

{% include search-info.html %}

<div class="grid">
{% assign prompt_pages = site.pages | where: "layout", "prompt" %}
{% for prompt in site.data.prompts %}
  {% assign page = prompt_pages | where: "permalink", prompt.link | first %}
  {% assign card_title = page.title | default: prompt.title %}
<div class="card" data-style="">
  <div class="card-text">
    <a href="{{ prompt.link | relative_url }}" class="card-title">{{ card_title }}</a>
    {% if prompt.description %}
      <p>{{ prompt.description }}</p>
    {% endif %}
    <div class="prompt-card-footer">
      {% include tags.html tags=prompt.tags %}
      {% if prompt.paper %}
        <a href="{{ prompt.paper }}" class="prompt-paper-link" target="_blank" rel="noopener">
          <i class="fa-solid fa-file-lines fa-fw"></i> View Paper
        </a>
      {% endif %}
    </div>
  </div>
</div>
{% endfor %}
</div>
