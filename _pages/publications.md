---
title: "HLR - Publications"
layout: gridlay
excerpt: "Heterogeneous Learning and Reasoning at Michigan State University."
sitemap: false
permalink: /publications/
---


# Recent Publication
### For the full list see [here]: http://www.cse.msu.edu/~kordjams/publication.htm .
{% assign year = 0 %}
{% for publi in site.data.publist %}

  {% if year != publi.year %}
  <h2> {{ publi.year }} </h2>
  {% assign year = publi.year%}
  {% endif %}

  <b>{{ publi.title }}</b> <br />
  <em>{{ publi.authors }} </em><br />
  {{ publi.venue }} <br/>
  <a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endfor %}

