---
title: "HLR - Softwares"
layout: gridlay
excerpt: "HLR - softwares"
sitemap: false
permalink: /software
---


# Software

{% assign number_printed = 0 %}
 {% for software in site.data.softwares %}
 {% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-12 clearfix">
<div>
### {{ software.title }} 
<p> {{ software.description }} </p>
<p>Github: <strong><a href="{{ software.webpage }}">{{ software.title }}</a></strong></p>

<p> </p>
</div>
 </div>

 
 {% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

