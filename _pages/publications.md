---
title: "Allan Lab - Publications"
layout: gridlay
excerpt: "Allan Lab -- Publications."
sitemap: false
permalink: /publications/
---


# Publications
{% for publi in site.data.publist %}

  <b>{{ publi.title }}</b> <br />
  <em>{{ publi.authors }} </em><br />
  {{ publi.venue }} <br/>
  <a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endfor %}

