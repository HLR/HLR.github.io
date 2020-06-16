---
title: "SpLang"
layout: textlay
excerpt: "SpLang"
sitemap: false
permalink: /splang/
---

{% for p in site.data.projects %}
{% if p.title == page.title %}
{% assign project = p %}
{% endif %}
{% endfor %}

{% assign project = site.data.projects | where: "title", page.title %}
{% assign project = project[0] %}
<div>
<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/projects/{{ project.logo }}" style="width: 90px; float: left; border: 10px; margin-right: 20px"/>
<br>

### {{ project.title }} 
<p> {{ project.description }} </p>
</div>
<br>
<p> {{ project.info }} </p>
<p><img src="{{ site.url }}{{ site.baseurl }}/images/picpic/projects/{{ project.image }}" class="img-responsive" width="60%" style="margin:auto"></p>
<p><b>Members</b>: <em> {{ project.members }}, {{project.graduate_students}} </em></p>
[//]: # (<p>Github: <strong><a href="{{ project.webpage }}">{{ project.title }}</a></strong></p>)
<p><b>Source of funding</b>: <i>{{ project.funding_resource }}</i> </p>
{% if project.publications %}
<p>List of <b>publications</b>: </p>
{% for pub in project.publications %}
<ul>
<li><strong>{{ pub.title }}</strong>. {{ pub.authors }} {% if pub.webpage %} <a href="{{ pub.webpage }}">More detail</a>. {% endif %} {% if pub.webpage %} <a href="{{ pub.webpage }}">GitHub</a>. {% endif %} {% if pub.link %} <a href="{{ pub.link }}">Download</a>. {% endif %} </li>
</ul>
{% endfor %}
{% endif %}
