---
title: "HLR - Publications"
layout: gridlay
excerpt: "Heterogeneous Learning and Reasoning at Michigan State University."
sitemap: false
permalink: /publications/
---


# Recent Publication
### For the full list see [here](http://www.cse.msu.edu/~kordjams/publication.htm).
#### You can download the Bibtex file of all below publications [here]({{ site.url }}{{ site.baseurl }}/downloads/hlr.bib).

{% assign year = 0 %}
{% for publi in site.data.publist %}

  {% if year != publi.year %}
  <h2> {{ publi.year }} </h2>
  {% assign year = publi.year%}
  {% endif %}

  <b>{{ publi.title }}</b> <br />
  <em>{{ publi.authors }} </em><br />
  {{ publi.venue }} <br/>
  {% for link in publi.links -%}
  {%- if link.display -%}
  <a href="{{ link.url }}">[{{ link.display }}]</a>
  {%- endif-%}
  {%- endfor %}
  {% if publi.bibtex %}
  <a href="" id = "bibtex-button" > [BibTex]  </a> 
  <p id = "bibtex"> {{ publi.bibtex }}</p> 

  {% endif %}
  
  
{% endfor %}


<!-- $(document).ready(function(){
  $("#bibtex-button").click(function(){
    $("#bibtex").toggle();
  });
}); -->