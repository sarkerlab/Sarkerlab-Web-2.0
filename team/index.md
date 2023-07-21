---
title: Team
nav:
  order: 4
  tooltip: Meet our team!
---

# Our Team


<!--
Our lab is a dynamic and collaborative team of researchers dedicated to pushing the boundaries of knowledge in our field. We are composed of postdocs, students at all levels, researchers, engineers and our lab mascots. Together, we work to drive innovation and make impactful contributions to our research domain.
-->

{% include section.html %}

## Members

{% include list.html data="members" component="portrait" filters="role: member" %}



## Collaborators
{% include list.html data="members" component="portrait" filters="role: collaborator" %}

{% include section.html background="images/" dark=true %}
## We Are Hiring!
We are currently setting up the lab and are keen to speak to potential postdoctoral researchers, software engineers and doctoral students. Please contact Dr. Abeed Sarker via email (abeed@dbmi.emory.edu) if you are interested.

{% include section.html %}

## Alumni
{% include list.html data="members" component="portrait" filters="role: alumni" %}




{% capture content %}



{% endcapture %}

{% include grid.html style="square" content=content %}






