---
title: "HLR Lab - Team"
layout: gridlay
excerpt: "HLR Lab: Team members"
sitemap: false
permalink: /team/
---

# Group Members

Jump to: [Faculty](#faculty), [Postdocs](#postdocs), [Phd Students](#phd-students), [Master Students](#master-students)

<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/group-pic.jpg" width="60%">


## Faculty
{% assign number_printed = 0 %}
<div class="row">
{% for member in site.data.faculty %}
  <div class="col-sm-6 clearfix">
    <img src="{{ site.url }}{{ site.baseurl }}/images/profiles/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
    <h4><a href="{{ member.webpage }}" style="color:inherit">{{ member.name }}</a></h4>
    <i>{{ member.bio }}</i><br><br>
    <i><b>Research Interest</b>: {{ member.research_interest }}. <br><b>Email</b>: <{{ member.email }}></i>
    <ul style="overflow: hidden">

    </ul>
  </div>
{% endfor %}
</div>

## Postdocs
<div class="row">
{% for member in site.data.postdocs %}
  <div class="col-sm-6 clearfix">
    <img src="{{ site.url }}{{ site.baseurl }}/images/profiles/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
    <h4><a href="{{ member.webpage }}" style="color:inherit">{{ member.name }}</a></h4>
    <i><b>Research Interests</b>: {{ member.research_interest }}<br><b>Email</b>: <{{ member.email }}></i>
    <ul style="overflow: hidden">

    </ul>
  </div>
{% endfor %}
</div>

## PhD Students
<div class="row">
{% for member in site.data.phd_students %}
<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/profiles/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4><a href="{{ member.webpage }}" style="color:inherit">{{ member.name }}</a></h4>
  <i><b>Research Interests</b>: {{ member.research_interest }}<br><b>Email</b>: <{{ member.email }}></i>
  <ul style="overflow: hidden">

  </ul>
</div>
{% endfor %}
</div>


## Master Students
<div class="row">
{% for member in site.data.master_students %}
  <div class="col-sm-6 clearfix">
    <img src="{{ site.url }}{{ site.baseurl }}/images/profiles/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
    <h4><a href="{{ member.webpage }}" style="color:inherit">{{ member.name }}</a></h4>
    <i><b>Research Interests</b>: {{ member.research_interest }}<br><b>Email</b>: <{{ member.email }}></i>
    <ul style="overflow: hidden">

    </ul>
  </div>
{% endfor %}
</div>