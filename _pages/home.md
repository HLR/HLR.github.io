---
title: "HLR - Home"
layout: homelay
excerpt: "Heterogeneous Learning and Reasoning at Michigan State University."
sitemap: false
permalink: /
---

## Welcome to the **Heterogeneous Learning and Reasoning** Lab

[//]: # (<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/AI_web.jpg" width="100%">)


<div class="row">
{% for pic in site.data.home %}

<div class="col-lg-12 col-md-12 col-sm-12 clearfix" style="float: left">
<img src="{{ site.url }}{{ site.baseurl }}/images/home/{{ pic.image }}" class="img-responsive" width="100%" />
</div>

<!-- <div id="photoGallery" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    {% for image in site.data.home.gallery_images %}
      <li data-target="#photoGallery" data-slide-to="{{ forloop.index0 }}" {% if forloop.first %}class="active"{% endif %}></li>
    {% endfor %}
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner">
    {% for image in site.data.home.gallery_images %}
    <div class="item {% if forloop.first %}active{% endif %}">
      <img src="{{ site.url }}{{ site.baseurl }}/images/gallery/{{ pic.image }}" alt="{{ image.alt }}" class="img-responsive" width="100%">
    </div>
    {% endfor %}
  </div>

  <!-- Controls -->
  <a class="left carousel-control" href="#photoGallery" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#photoGallery" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>

{% endfor %} -->

</div>

We do research on natural language processing, machine learning and combining vision and language. We work on information and semantic extraction from language. We investigate methodologies to interplay between learning and reasoning and develop techniques to include declarative and procedural world knowledge in statistical/neural learning. We develop research software and build prototypes to facilitate designing AI systems. We also aim to apply our techniques and tools on real world-problems and conduct multi-disciplinary research to impact the society for making the world a better place to live.

#### Check out our research code and developed models, frameworks in Github. <a href="https://github.com/HLR/">https://github.com/HLR/<a/>    
