---
title: "HLR - Home"
layout: homelay
excerpt: "Heterogeneous Learning and Reasoning at Michigan State University."
sitemap: false
permalink: /
---

# Welcome to the **Heterogeneous Learning and Reasoning** Lab

<div class="row">
<div class="splide" id="splide01">
<div class="splide__track">
<ul class="splide__list">
{% for pic in site.data.home%}
<li class="splide__slide">
<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/Gallery/{{ pic.image}}" class="img-fluid gallery-image">
<figcaption>{{ pic.name }}</figcaption>
</li>
{% endfor %}
</ul>
</div>
</div>
</div>

We do research on natural language processing, machine learning and combining vision and language. We work on information and semantic extraction from language. We investigate methodologies to interplay between learning and reasoning and develop techniques to include declarative and procedural world knowledge in statistical/neural learning. We develop research software and build prototypes to facilitate designing AI systems. We also aim to apply our techniques and tools on real world-problems and conduct multi-disciplinary research to impact the society for making the world a better place to live.

#### Check out our research code and developed models, frameworks in Github. <a href="https://github.com/HLR/">https://github.com/HLR/</a>    


<script>
  document.addEventListener('DOMContentLoaded', function () {
    var swiper = new Swiper('.swiper-container', {
      loop: true,               // 无限循环模式
      autoplay: {               // 自动播放
        delay: 2500,
        disableOnInteraction: false,
      },
      pagination: {             // 如果需要分页器
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {             // 如果需要导航按钮
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      slidesPerView: 1,         // 每页展示一个
      spaceBetween: 30          // 每个幻灯片之间的间距
    });
  });
</script>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    new Splide('#splide01', {
      type   : 'loop',
      perPage: 1,
      autoplay: true,
      pagination: true,
      arrows: true,
      height: '400px',  // 确保轮播容器高度不超过 400px
    }).mount();
  });
</script>