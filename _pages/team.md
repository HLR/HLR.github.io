---
title: "HLR Lab - Team"
layout: gridlay
excerpt: "HLR Lab: Team members"
sitemap: false
permalink: /team/
---

# Group Members

<!-- Jump to: [Faculty](#faculty), [Postdocs](#postdocs), [Phd Students](#phd-students), [Master Students](#master-students) -->

Jump to: [Faculty](#faculty), [Phd Students](#phd-students), [Visiting Scholars](#visiting-scholars), [Undergrads](#undergrads)

<!-- <div class="row">
<div class="col-lg-5 col-md-6 col-sm-12">
<a href="{{ site.url }}{{ site.baseurl }}/pictures/" >
<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/Gallery/gathering_2024.jpg" width="100%">
</a>
</div>
</div> -->

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

<!-- ## Postdocs
<div class="row">
{% for member in site.data.postdocs %}
<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/profiles/{{ member.photo }}" class="img-responsive" width="25%" style="float: left"/>
  <h4><a href="{{ member.webpage }}" style="color:inherit">{{ member.name }}</a></h4>
  <i><b>Joined</b>: {{ member.joined }}</i><br>
  <i><b>Email</b>: <{{ member.email }}></i><br>
  <i><b>Research Interests</b>: {{ member.research_interest }}<br></i>
</div>
{% endfor %}
</div> -->

## PhD Students
<div class="row">
{% for member in site.data.phd_students %}
<div class="col-sm-6 clearfix" style="min-height: 250px;">
  <img src="{{ site.url }}{{ site.baseurl }}/images/profiles/{{ member.photo }}" class="img-responsive" width="25%" style="float: left;"/>
  <h4><a href="{{ member.webpage }}" style="color:inherit">{{ member.name }}</a></h4>
  <i><b>Joined</b>: {{ member.joined }}</i><br>
  <i><b>Email</b>: <{{ member.email }}></i><br>
  <i><b>Research Interests</b>: {{ member.research_interest }}</i>
</div>
{% endfor %}
</div>

<!-- ## Visiting Scholars
<div class="row">
{% for member in site.data.visiting_scholars %}
<div class="col-sm-6 clearfix" style="min-height: 250px;">
  <img src="{{ site.url }}{{ site.baseurl }}/images/profiles/{{ member.photo }}" class="img-responsive" width="25%" style="float: left;"/>
  <h4><a href="{{ member.webpage }}" style="color:inherit">{{ member.name }}</a></h4>
  <i><b>Joined</b>: {{ member.joined }}</i><br>
  <i><b>Email</b>: <{{ member.email }}></i><br>
  <i><b>Research Interests</b>: {{ member.research_interest }}</i>
</div>
{% endfor %}
</div> -->


<!-- ## Master's Students -->
<!--<div class="row">
{% for member in site.data.master_students %}
<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/profiles/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4><a href="{{ member.webpage }}" style="color:inherit">{{ member.name }}</a></h4>
  <i><b>Joined</b>: {{ member.joined }}</i><br>
  <i><b>Email</b>: <{{ member.email }}></i>
</div>
{% endfor %}
</div>-->

## Undergrads
<div class="row">
{% for member in site.data.undergrads %}
<div class="col-sm-6 clearfix" style="min-height: 200px;">
  <img src="{{ site.url }}{{ site.baseurl }}/images/profiles/{{ member.photo }}" class="img-responsive" width="25%" style="float: left"/>
  <h4><a href="{{ member.webpage }}" style="color:inherit">{{ member.name }}</a></h4>
  <i><b>Joined</b>: {{ member.joined }}</i><br>
  <i><b>Email</b>: <{{ member.email }}></i><br>
  <i><b>Research Interests</b>: {{ member.research_interest }}</i>
</div>
{% endfor %}
</div>

## Alumni & Past Members
- Ph.D. graduates: 
- Yue Zhang (Joslin), PhD Graduate (2020-2025). Post-doctoral researcher at North Carolina at Chapel Hill.
- Hossein Faghihi, PhD Graduate (2019-2024). ML Engineer at Google.
- Guangyue Xu, PhD Graduate (2019-2024). Senior Data Scientist at Target.
- Roshanak Mirzaee, PhD Graduate (2019-2024). Applied Scientist at Qualtrics.
- Chen Zheng, PhD Graduate (2018-2022). Senior Research Scientist at Byte Dance.

- Post-doctoral researchers:
- Elham Barezi, Postdoc (2022-2024). Research associate at University of Purdue.
- Quan Guo, Postdoc (Feb 2019 - Nov 2020). Associate Professor at Sichuan University.
- Elaheh Raisi, Postdoc (Nov 2020 - May 2021). Applied Researcher, eBay.

- Masters, Undergraduates, Visiting scholars: 
- Sushanta K. Pani, Master student (Aug 2019 - Sep 2021)
- Luan Thanh Nguyen, Visiting Scholar (Aug 2024 - Nov 2024)
- Drew Hayward, Research assistant (Aug 2019 - May 2021)
- Ailin Patimar, Undergraduate (2023-2024)
- Trevor Stevens, Undergraduate (2024-2025)
- Divyalakshmi Varadha Rajan Prem Sudha, undergraduate professorial assistant (Fall 2023)
- Joseph Romain, undergraduate research intern (Aug 2022 - Dec 2022)
- Tim Moran, undergraduate professorial assistant (Fall 2020 - Spring 2022)
- Lemuel Agur Mensah,  undergraduate professorial assistant (2022 - 2023)
- Tolu Oshin as undergraduate professorial assistant (2022 - 2023)
