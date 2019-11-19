---
title: "HLR - News"
layout: textlay
excerpt: "HLR - News Page"
sitemap: false
permalink: /allnews.html
---

# News

{% for article in site.data.news %}
<span style="font-size:15px; color: #333">{{ article.date }}</span> <br>
<p>
<em>{{ article.headline }}</em></p>
{% if article.link %}
<p><a href="{{ article.link }}">[ More Info ]</a></p>
{% endif %}

{% assign number_printed = 0 %}
{% for pic in article.pictures %}

{% assign even_odd = number_printed | modulo: 4 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-3 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/newspic/{{ pic.image }}" class="img-responsive" width="95%" style="float: left" />
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd > 2 %}
</div>
{% endif %}


{% endfor %}

{% assign even_odd = number_printed | modulo: 4 %}
{% if even_odd == 1 %}
</div>
{% endif %}

{% if even_odd == 2 %}
</div>
{% endif %}

{% if even_odd == 3 %}
</div>
{% endif %}



{% endfor %}
