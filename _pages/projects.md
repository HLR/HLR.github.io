---
title: "HLR - Projects"
layout: textlay
excerpt: "HLR - projects"
sitemap: false
permalink: /projects
---

# Projects

 {% for project in site.data.projects %}
<p>{{ project.date }} <br>
<em>{{ project.headline }}</em></p>
{% endfor %}
