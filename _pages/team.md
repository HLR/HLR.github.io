---
title: "HLR Lab - Team"
layout: gridlay
excerpt: "HLR Lab: Team members"
sitemap: false
permalink: /team/
---

# Group Members

Jump to: [Faculty](#faculty), [Postdocs](#postdocs), [Phd Students](#phd-students), [Master Students](#master-students)
<div class="row">
<div class="col-lg-5 col-md-6 col-sm-12">
<a href="{{ site.url }}{{ site.baseurl }}/pictures/" >
<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/Gallery/main.jpg" width="100%">
</a>
</div>
</div>

Go to <a href="{{ site.url }}{{ site.baseurl }}/pictures/"> <b>Gallery</b> </a>

## Faculty
{% assign number_printed = 0 %}
<div class="row" style="display: block">
{% for member in site.data.faculty %}
<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/profiles/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4><a href="{{ member.webpage }}" style="color:inherit">{{ member.name }}</a></h4>
  <i>{{ member.bio }}</i><br><br>
  <i><b>Research Interest</b>: {{ member.research_interest }}. <br><b>Email</b>: <{{ member.email }}></i>
</div>
{% endfor %}
</div>

## Postdocs
<div class="row">
{% for member in site.data.postdocs %}
<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/profiles/{{ member.photo }}" class="img-responsive" width="25%"/>
  <h4><a href="{{ member.webpage }}" style="color:inherit">{{ member.name }}</a></h4>
  <i><b>Research Interests</b>: {{ member.research_interest }}<br><b>Email</b>: <{{ member.email }}></i>
</div>
{% endfor %}
</div>

## PhD Students
<div class="row">
{% for member in site.data.phd_students %}
<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/profiles/{{ member.photo }}" class="img-responsive" width="25%" />
  <h4><a href="{{ member.webpage }}" style="color:inherit">{{ member.name }}</a></h4>
  <i><b>Research Interests</b>: {{ member.research_interest }}<br><b>Email</b>: <{{ member.email }}></i>
</div>
{% endfor %}
</div>


## Master's Students
<div class="row">
{% for member in site.data.master_students %}
<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/profiles/{{ member.photo }}" class="img-responsive" width="25%" />
  <h4><a href="{{ member.webpage }}" style="color:inherit">{{ member.name }}</a></h4>
  <i><b>Email</b>: <{{ member.email }}></i>
</div>
{% endfor %}
</div>

## Undergrads
<div class="row">
{% for member in site.data.undergrads %}
<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/profiles/{{ member.photo }}" class="img-responsive" width="25%" />
  <h4><a href="{{ member.webpage }}" style="color:inherit">{{ member.name }}</a></h4>
  <i><b>Email</b>: <{{ member.email }}>
</div>
{% endfor %}
</div>

## Past Members

- Quan Guo as Postdoc. Currently a research associate at Sichuan University
