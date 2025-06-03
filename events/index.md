---
layout: default
title: Lab News
nav:
  order: 5
permalink: /lab-news/
---

<section class="lab-news">
  <h1>Lab News & Highlights</h1>
  <div class="news-grid">
    {% for event in site.data.events %}
      <div class="news-item">
	{% assign image_file = event.image | default: "default.png" %}
	{% assign alt_text = event.title | default: "Lab event image" %}
	{% picture {{ image_file }} alt="{{ alt_text }}" %}

        <p class="meta">{{ event.categories | join: ', ' }} • {{ event.date }}</p>
        <h2>{{ event.title }}</h2>
      </div>
    {% endfor %}
  </div>
</section>


<style>

.lab-news {
  padding: 2em;
  max-width: 1200px;
  margin: auto;
}

.lab-news h1 {
  text-align: center;
  margin-bottom: 2em;
}

.news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(245px, 1fr));
  gap: 1.5em;
}

.news-item {
  border: 1px solid #ccc;
  padding: 1em;
  border-radius: 10px;
  background: #fff;
  font-size: 0.9em;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
}

.news-item picture,
.news-item img {
  width: 100%;
  height: auto;
  border-radius: 6px;
}

.news-item .meta {
  font-size: 0.75em;
  color: #666;
  margin-top: 0.5em;
}

.news-item h2 {
  font-size: 1em;
  margin: 0.5em 0;
  border-bottom: none;
}

.news-item p {
  font-size: 0.85em;
  margin-top: auto;
}
</style>


