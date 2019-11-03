---
title: "HLR - Projects"
layout: gridlay
excerpt: "HLR - projects"
sitemap: false
permalink: /projects
---

# Projects

{% assign number_printed = 0 %}
 {% for project in site.data.projects %}
 {% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
<div class="well">
<pubtit><a href="{{ site.url }}{{ site.baseurl }}/projects" style="color: inherit"> {{ project.title }} </a></pubtit>
[//]: # (<p><img src="" class="img-responsive" width="33%" style="float: left"></p>)
<p> {{ project.description }} </p>
<p><em> {{ project.members }, {project.graduate_students}} </em></p>
<p><strong><a href="{{ project.webpage }}">{{ project.title }}</a></strong></p>
<p> </p>
</div>
 </div>

 
 {% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}


# Software

{% assign number_printed = 0 %}
 {% for software in site.data.softwares %}
 {% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
<div class="well">
<pubtit><a href="{{ site.url }}{{ site.baseurl }}/softwares" style="color: inherit"> {{ software.title }} </a></pubtit>
[//]: # (<p><img src="" class="img-responsive" width="33%" style="float: left"></p>)
<p> {{ software.description }} </p>
<p><em> {{ software.members }} </em></p>
<p><strong><a href="{{ software.webpage }}">{{ software.title }}</a></strong></p>
<p> </p>
</div>
 </div>

 
 {% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

