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
<div>
<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/projects/{{ project.logo }}" style="width: 90px; float: left; border: 10px; margin-right: 20px"/>
<br>



<!-- ([Members](#members), [Funding](#funding), [Publications](#pubs)) -->





## {{ project.title }} 
<p> {{ project.description }} </p>
</div>
<br>

### Menu

<ul>
<li> <a href="{{ site.url }}{{ site.baseurl }}/domiknows-nlp/">Demo</a> </li>
<li> <a href="#members">Team</a> </li>
<li> <a href="#fund">Funding</a> </li>
<li> <a href="#pubs">Publications</a> </li>
</ul>
<br><br>
<p> {{ project.info }} </p>
<p><img src="{{ site.url }}{{ site.baseurl }}/images/picpic/projects/{{ project.image }}" class="img-responsive" width="80%" style="margin:auto"></p>
<br>
<br>
<h4 id="members"><b>Team Members</b></h4>
<ul>
<li><em> {{ project.members }}. </em> </li>
<li><em>{{project.graduate_students}} </em> </li>
</ul>

<!-- (<p>Github: <strong><a href="{{ project.webpage }}">{{ project.title }}</a></strong></p>)  -->
<br>
<h4 id="fund"><b>Source of funding</b></h4>
<ul>
<li><i>{{ project.funding_resource }}</i> </li>
</ul>

<br>
{% if project.publications %}
<h4 id="pubs">List of <b>publications</b>: </h4>
<br>
{% for pub in project.publications %}
<ul>
<li><strong>{{ pub.title }}</strong>. {{ pub.authors }} {% if pub.webpage %} <a href="{{ pub.webpage }}">More detail</a>. {% endif %} {% if pub.github %} <a href="{{ pub.github }}">GitHub</a>. {% endif %} {% if pub.link %} <a href="{{ pub.link }}">Download</a>. {% endif %} </li>
</ul>
{% endfor %}
{% endif %}
<br>


