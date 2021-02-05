---
title: "Allan Lab - Pictures"
layout: piclay
excerpt: "Allan Lab -- Pictures"
permalink: /pictures/
---

# Gallery
{% assign number_printed = 0 %}
<div class="row">
{% for pic in site.data.gallery %}

<div class="col-lg-4 col-md-6 col-sm-12 clearfix" style="float: left">
<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/Gallery/{{ pic.image }}" class="img-responsive" width="100%" />
</div>

{% endfor %}

</div>

