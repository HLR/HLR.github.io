---
title: "HLR - Softwares"
layout: gridlay
excerpt: "HLR - softwares"
sitemap: false
permalink: /softwares
---


# Software
Jump to: {% for software in site.data.softwares %} [ {{ software.title }} ](#{{ software.id }}). {% endfor %}

{% assign number_printed = 0 %}
 {% for software in site.data.softwares %}
 {% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix" id="#{{ software.id }}">
<div class="well">
### {{ software.title }} 
<p> {{ software.description }} </p>
<p>Members: <em> {{ software.members }} </em></p>
<p>Github: <strong><a href="{{ software.webpage }}">{{ software.title }}</a></strong></p>
[//]: # (<p><img src="" class="img-responsive" width="33%" style="float: left"></p>)
<p> </p>
</div>
 </div>

 
 {% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

