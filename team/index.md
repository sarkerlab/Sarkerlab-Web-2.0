---
title: Team
nav:
  order: 2
  tooltip: Meet our team!
---

# Our Team


<!--
Our lab is a dynamic and collaborative team of researchers dedicated to pushing the boundaries of knowledge in our field. We are composed of postdocs, students at all levels, researchers, engineers and our lab mascots. Together, we work to drive innovation and make impactful contributions to our research domain.
-->

{% include section.html %}

## Members

{% include list.html data="members" component="portrait" filters="role: member, position: Principal Investigator" %}
{% include list.html data="members" component="portrait" filters="role: member, position: Postdoctoral Scholar" %}
{% include list.html data="members" component="portrait" filters="role: member, position: Software Engineer" %}
{% include list.html data="members" component="portrait" filters="role: member, position: PhD Candidate" %}
{% include list.html data="members" component="portrait" filters="role: member, position: PhD Student" %}
{% include list.html data="members" component="portrait" filters="role: member, position: Graduate Research Assistant" %}
{% include list.html data="members" component="portrait" filters="role: member, position: Undergraduate Research Assistant" %}
{% include list.html data="members" component="portrait" filters="role: member, position: mascot" %}



## Collaborators
{% include list.html data="members" component="portrait" filters="role: collaborator, position: Principal Investigator" %}
{% include list.html data="members" component="portrait" filters="role: collaborator, position: " %}



## Alumni
{% include list.html data="members" component="portrait" filters="role: alumni, position: alumni" %}
{% include list.html data="members" component="portrait" filters="role: alumni, position: mascot" %}






{% capture content %}



{% endcapture %}

{% include grid.html style="square" content=content %}






