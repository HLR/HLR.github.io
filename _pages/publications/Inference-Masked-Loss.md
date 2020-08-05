---
title: "HLR - Publications"
layout: gridlay
excerpt: "Heterogeneous Learning and Reasoning at Michigan State University."
sitemap: false
permalink: /publications/Inference-Masked-Loss
---

# Inference-Masked Loss for Deep Structured Output Learning

[Quan Guo](http://guoquan.net),
[Hossein Rajaby Faghihi](https://github.com/hfaghihi15),
[Yue Zhang](https://github.com/zhangyuejoslin),
[Andrzej Uszok](https://github.com/auszok),
[Parisa Kordjamshidi](http://www.cse.msu.edu/~kordjams)

*This work has been accepted for publication in IJCAI 2020 (main track). Please refer to the [IJCAI Proceedings](https://www.ijcai.org/Proceedings/2020/382) for a [**full verison**](https://www.ijcai.org/Proceedings/2020/0382.pdf).*

## Abstract

Structured learning algorithms usually involve an inference phase that selects the best global output variables assignments based on the local scores of all possible assignments.
We extend deep neural networks with structured learning to combine the power of learning representations and leveraging the use of domain knowledge in the form of output constraints during training.
Introducing a non-differentiable inference module to gradient-based training is a critical challenge.
Compared to using conventional loss functions that penalize every local error independently, we propose an inference-masked loss that takes into account the effect of inference and does not penalize the local errors that can be corrected by the inference.
We empirically show the inference-masked loss combined with the negative log-likelihood loss improves the performance on different tasks, namely entity relation recognition on CoNLL04 and ACE2005 corpora, and spatial role labeling on CLEF 2017 mSpRL dataset. We show the proposed approach helps to achieve better generalizability, particularly in the low-data regime.

## Introduction

Structured learning considers learning to predict  output variables that are interdependent and need to obey some structural constraints.
Structured learning approaches involve an inference phase after computing local predictions along with their probabilities/scores which can be generally formulated by a Maximum A Posteriori (MAP) inference problem.
On one hand, structured learning are powerful in its flexibility to incorporate domain knowledge and requirement of fewer data.
On the other hand, deep neural networks have achieved significant results by using large number of parameters and examples.
Exploiting structured output in deep neural networks can help to combine the power of learning representations and leveraging the use of output structure during training.
It will enable deep neural networks in imposing explicit structural constraints on their predictions by using domain knowledge on top of the data.

In this work,
we present a new loss function to extend deep neural network to use inference and exploit the structure of the output.
Our proposed Inference-Masked Loss (IML) **allows neural networks to keep the local predictions, even if they are false, as much as the inference can correct them**.
IML allows the neural networks to make local predictions without the constraints, and rely on the inference to correct the false predictions. It helps to decompose the dependencies of the output variables and allows the (sub-) neural networks to focus on training for parts of the output locally.
The contribution of this paper is as follows:

- We propose the IML that utilizes the global inference not only for prediction but also to train the parameters for structured output learning with deep neural networks.
- We evaluate the proposed method with two different tasks on three datasets under various settings to show the effectiveness of the proposed approach, especially with low training data.

## Inference-Masked Loss

We assume training a deep neural network given a set of examples $\left\lbrace\left(X,Y\right)\right\rbrace$, that is, pairs of inputs $X$ and outputs $Y$.
Both inputs and outputs can have arbitrary structures. We assume the structure of the output variables can be expressed with a set of linear constraints among them, denoted by $\mathcal{C}\left(Y\right) \le 0$. The constraints can be represented with a set of inequalities without loss of generality.
These constraints originate from our knowledge about the domain and are expressed using logical expressions or in ontologies that are converted to linear constraints.
In this study, we focus on the case where all parts of the output structure are discrete values and can be associated with a collection of binary predicates $q\in \mathbf{Q}$ where $\mathbf{Q}$ is the set of all possible predicates.
Each component $Y_q$ of the structured output $Y$ is a binary random variable and indicates whether $q$ is true or not.

We are interested in the joint probability distribution of structured output variables $y$ given input $X$,
$P\left(y|X\right)$. The inference is finding the best assignment of $y$ that yields the maximum joint probability. Our framework and loss function are agnostic to the inference method. In this study, we exploit ILP, which solves the problems with constraints that are not satisfying first order Markov property, efficiently.
The joint probability distribution is estimated by a normalized exponential function with logarithm estimated by the total scoring function
$g\left(y,X;\theta\right)$ that $\log P\left(y|X\right) \propto g\left(y,X;\theta\right)$.
Given the linear constraints, the inference can be represented as an ILP problem as follows.

{% raw %}
$$
y^{*} = \arg\max_{y} g\left(y,X;\theta\right) \quad {s.t.} \quad \mathcal{C}\left(y\right)\le0.
$$
{% endraw %}

To train such a model, first, we make local predictions for each component of $y$. In other words, for each predicate $q\in \mathbf{Q}$, we make a local prediction $f_q\left(X;\theta\right)$ with deep neural networks, where $f_q$ is a local network and $\theta$ is the weights and biases.
Following the log-linear model formulation, we calculate a local scoring function $g_q = \log f_q\left(X;\theta\right)$ and a corresponding negative term $g_{\neg q} = \log \left(1 - f_q\left(X;\theta\right)\right)$. We calculate the total scoring function for the output $y$ by a linear model,

{% raw %}
$$
g\left(y,X;\theta\right) = \sum_{q\in \mathbf{Q}} g_q y_q + g_{\neg q} y_{\neg q}.
$$
{% endraw %}

The inference problem in the ILP problem can be solved efficiently by off-the-shelf solvers.

### The Loss Function

The commonly-used negative log-likelihood (NLL) loss function is given by

{% raw %}
$$
    \mathcal{L}_{NLL} = \sum_{q \in \mathbf{Q}}
        - Y_q \log f_q\left(X;\theta\right)
        - \left(1 - Y_q\right) \log{\left(1 - f_q\left(X;\theta\right)\right)}.
$$
{% endraw %}

In fact, the ground-truth $Y_q$ and the term $\left(1 - Y_q\right)$ serves as a selective mask to select penalizing the parameters of negative log-likelihood  $-\log f_q\left(X;\theta\right)$ or $-\log{\left(1 - f_q\left(X;\theta\right)\right)}$.

Inspired by the idea mentioned above, we introduce the IML.
For each predicate $q$, if the associated component in the global inference $y^{*}_q$ is correct according to the ground-truth $Y_q$, IML will nullify the corresponding terms by the mask. The resulting IML is as follows,

{% raw %}
$$
\begin{aligned}
\mathcal{L}_{IML}
& = \sum_{q \in \mathbf{Q}}
    - \left(1 - y^*_q\right) Y_q \log{ f_q\left(X;\theta\right) } \\
& \hphantom{{}=\sum_{q \in \mathbf{Q}}}
    - y^*_q \left(1 - Y_q\right) \log{\left(1 - f_q\left(X;\theta\right) \right)}. \\
\end{aligned}
$$
{% endraw %}

It can be observed that both masks $(1 - y^{\*}_q) Y_q$ and $y^{\*}_q \left(1 - Y_q\right)$ will be zero if $y^{\*}_q = Y_q$. When $y^{\*}_q \ne Y_q$, the masks will become $Y_q$ and $\left(1 - Y_q\right)$ as in the NLL that, consequently, selects either the $-\log f_q\left(X;\theta\right)$ or $-\log{\left(1 - f_q\left(X;\theta\right)\right)}$ to be penalized according to the ground-truth.

Table 1: Penalty term of NLL and IML regarding one predicate $q$.

|    | $Y_q$ | $f_q$ | NLL | IML $y_q^{*}=0$ | IML $y_q^{*}=1$ |
|--- | ----- | ----- | --- | ------------- | --------- |
| TP |   1   | $\uparrow$ | $-\log f_q\left(X;\theta\right)$ | $-\log f_q\left(X;\theta\right)$ | $0^-$ |
| TN | 0 | $\downarrow$ | $-\log\left(1-f_q\left(X;\theta\right)\right)$ | $0^-$ | $-\log\left(1-f_q\left(X;\theta\right)\right)$ |
| FP | 0 | $\uparrow$ | $-\log\left(1-f_q\left(X;\theta\right)\right)$ | $0^+$ | $-\log\left(1-f_q\left(X;\theta\right)\right)$ |
| FN | 1 | $\downarrow$ | $-\log f_q\left(X;\theta\right)$ | $-\log f_q\left(X;\theta\right)$ | $0^+$ |

Notations:

- $\uparrow$: a probability close to 1; $\downarrow$: a probability close to 0.
- $0^-$: a voided penalty in IML when the local prediction is correct;
- $0^+$: a voided penalty in IML when the false prediction is corrected by the inference.

Above table shows the term that is added to the total loss regarding a predicate $q$ based on NLL and IML, respectively.
The first column denotes the True/False Positive/Negative notations regarding the local prediction.
The $\uparrow$ in the third column indicates a probability close to 1 while a $\downarrow$ indicates that close to 0.

In the NLL, the term is selected by the ground-truth $Y_q$. Moreover, the magnitude is determined by how correct (or incorrect) the local prediction $f_q\left(X;\theta\right)$ is. As we introduced the inference to IML, the conditions become different.
$0^+$ and $0^-$ are the cases that the global inference gives the correct result ($H^{\*}_q = Y_q$), while the others are for the cases when the inference is wrong.
(FN, $y^{\*}_q=0$) and (FP, $y^{\*}_q=1$) are the criminals that we want to penalize.
The $0^+$ are the false local predictions that can be corrected by inference. Therefore, we do not need to penalize them.
The (TP, $y^{\*}_q=0$) and (TN, $y^{\*}_q=1$) are innocent cases because they were correct locally and inference changed them to be wrong. However, we argue that if they get a higher local score, they should be able to help in correcting other false predictions.
The $0^-$ are not problematic because they are correct, and they support the correct inference. No update needs to be applied in this case.

### Combination

Training solely with IML could lead to "lazy" update and is more likely to be trapped in a local minimum compared to traditional loss because IML would ignore many of the local errors.
The effect is two-fold. On one hand, with IML, the model receives fewer updates, which leads to a slower convergence. On the other hand, using IML would miss the opportunity to update a weak local model, which may cause trouble at testing time.
We combine NLL and IML to enforce accurate local prediction.
{% raw %}
$$
\begin{aligned}
& \hphantom{{}={}}
\mathcal{L}_{{IML}\left(\lambda\right)} \\
& = \lambda \mathcal{L}_{{NLL}} + (1-\lambda) \mathcal{L}_{{IML}} \\
& = \sum_{q \in \mathbf{Q}}
    - \left(1 - \left(1-\lambda\right)y^{*}_q\right) Y_q \log{ f_q\left(X;\theta\right) } \\
& \hphantom{{}=\sum_{q \in \mathbf{Q}}}
    - \left( \lambda + \left(1-\lambda\right)y^{*}_q \right)\left(1 - Y_q\right) \log{\left(1 - f_q\left(X;\theta\right) \right)}, \\
\end{aligned}
$$
{% endraw %}
where $\lambda$ is weighting the trade-off between NLL and IML, which is a hyper-parameter for the proposed loss.
$\lambda$ is also interpreted as the ratio of penalty to apply when the inference can resolve the errors on the local prediction and correct them in the global inference.
$\lambda$ times the corresponding NLL loss term will be penalized.
Otherwise, if there are still errors according to the ground-truth, the penalty term is the same as NLL.
This leads to having a better local prediction even if the inference can resolve the incorrectness. It is shown to be helpful in the Experiments Section and Analysis Section.
However, $\lambda$ is a new (and the only) hyper-parameter in this work.
Experimental results with different $\lambda$ will be reported and analyzed in Experiments Section.

### Structure and Domain Knowledge

To represent the structure of the output and the domain knowledge, we follow the line of study on declarative knowledge representation for inference. We consider three types of generic relations between the parts: *is-a* indicates sub-typing of categorical predicates; *disjoint-with* indicates mutual exclusiveness of categorical predicates; and *has-a* indicates the composition of parts. These relations can be expressed by logical expressions.
More specifically, *is-a* and *has-a* are mapped to implication $q_u \Rightarrow q_v$.
*disjoint-with* is implemented by alternative denial $\neg \left(q_u \land q_v \right)$.
Then we derive the linear constraints from the logical expressions by the rules in associated with each dataset.

## Experiments

We evaluate the proposed approach with several structured learning tasks:
Two different entity relation extraction (ER) tasks and spatial role labeling (SpRL) task. We investigate the entity and relation recognition corpora (CoNLL04) and ACE 2005 Corpus (ACE2005) for ER task. The two datasets contain different types of entities and relationships. For SpRL task, CLEF 2017 mSpRL dataset(SpRL2017) is investigated.

Please refer to our [GitHub repository](https://github.com/HLR/Inference-Masked-Loss) for the experiments associated with this work: [Inference-Masked-Loss](https://github.com/HLR/Inference-Masked-Loss).

## Conclusion

We investigated the combination of deep neural networks with structured output by introducing the inference-masked loss. The proposed structured output learning model imposes the structure of data and domain knowledge in the form of logical constraints that describe the correlations between output variables. Inference-masked loss takes the inference into account based on the domain knowledge compiled from logical expressions. It allows local deep neural networks to make false local predictions that can be corrected by the inference. The loss helps to decompose the learning task and let the neural networks focus on local representations and make local predictions. The inference collects the local predictions based on the structure of output and domain knowledge. One advantage of IML approach is being agnostic to the inference model and treating it as a black box. This helps to plug in any inference mechanism in the loop of deep learning iterations. The proposed approach improves the generalizability of the model and robustness of training, leading to state-of-the-art results on entity relation extraction and spatial role labeling tasks, with CoNLL04, ACE2005, and CLEF 2017 mSpRL datasets, respectively. In particular, it shows improvements when there is only a small set of annotated data available.

## Cite

```bibtex
@inproceedings{guo2020inference,
   Author = {Quan Guo and Hossein Rajaby Faghihi and Yue Zhang and Andrzej Uszok and Parisa Kordjamshidi},
   Title = {Inference-Masked Loss for Deep Structured Output Learning},
   Booktitle = {Proceedings of the Twenty-Ninth International Joint Conference on Artificial Intelligence (IJCAI 2020)},
   Year = {2020}
}
```

<!-- Mathjax Support -->
<script>
MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']]
  },
  svg: {
    fontCache: 'global'
  },
  options: {
    renderActions: {
      findScript: [10, function (doc) {
        for (const node of document.querySelectorAll('script[type^="math/tex"]')) {
          const display = !!node.type.match(/; *mode=display/);
          const math = new doc.options.MathItem(node.textContent, doc.inputJax[0], display);
          const text = document.createTextNode('');
          node.parentNode.replaceChild(text, node);
          math.start = {node: text, delim: '', n: 0};
          math.end = {node: text, delim: '', n: 0};
          doc.math.push(math);
        }
      }, '']
    }
  }
};
</script>
<script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js"></script>
