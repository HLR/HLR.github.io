---
title: "HLR - Projects"
layout: gridlay
excerpt: "HLR - projects"
sitemap: false
permalink: /projects
---

# Projects

<ul>
{% for project in site.data.projects %}<li><a href="#{{ project.id }}"> {{ project.title }}. </a> ( {{ project.description }} )</li>{% endfor %}
</ul>

<br><br>
{% assign number_printed = 0 %}
 {% for project in site.data.projects %}
 {% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-12 clearfix" id="#{{ project.id }}">
<div class="well">
### {{ project.title }} 
<p> {{ project.description }} </p>
<p> {{ project.info }} </p>
<p><img src="{{ site.url }}{{ site.baseurl }}/images/picpic/projects/{{ project.image }}" class="img-responsive" width="60%" style="margin:auto"></p>
<p>Members: <em> {{ project.members }}, {{project.graduate_students}} </em></p>
[//]: # (<p>Github: <strong><a href="{{ project.webpage }}">{{ project.title }}</a></strong></p>)
<p>Source of funding: <i>{{ project.funding_resource }}</i> </p>
{% if project.publications %}
<p>List of publications: </p>
{% for pub in project.publications %}
<ul>
<li><strong>{{ pub.title }}</strong>. {{ pub.authors }}. <a href="{{ pub.link }}">Download</a> </li>
</ul>
{% endfor %}
{% endif %}
</div>
 </div>

 
 {% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

