---
title: "DomiKnowS"
layout: textlay
excerpt: "DomiKnowS"
sitemap: false
permalink: /domiknows/
---

{% for p in site.data.projects %}
{% if p.title == page.title %}
{% assign project = p %}
{% endif %}
{% endfor %}

{% assign project = site.data.projects | where: "title", page.title %}
{% assign project = project[0] %}


### {{ project.title }} 
<p> {{ project.description }} </p>
<p> {{ project.info }} </p>
<p><img src="{{ site.url }}{{ site.baseurl }}/images/picpic/projects/{{ project.image }}" class="img-responsive" width="80%" style="margin:auto"></p>
<p><b>Members</b>: <em> {{ project.members }}, {{project.graduate_students}} </em></p>
[//]: # (<p>Github: <strong><a href="{{ project.webpage }}">{{ project.title }}</a></strong></p>)
<p><b>Source of funding</b>: <i>{{ project.funding_resource }}</i> </p>
{% if project.publications %}
<p>List of <b>publications</b>: </p>
{% for pub in project.publications %}
<ul>
<li><strong>{{ pub.title }}</strong>. {{ pub.authors }}. <a href="{{ pub.link }}">Download</a> </li>
</ul>
{% endfor %}
{% endif %}


