class: center

# Brain-Like Object Recognition with High-Performing Shallow Recurrent ANNs

***Jonas Kubilius***

Brain & Cognition / KU Leuven

ECVP / 2019-08-26

.license[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons license" style="border-width:0;" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
.logo[]
.logo-name[[klab.lt](http://klab.lt)]
]
.aside[Content: Creative Commons Attribution 4.0 International License]
.aside[Images: Fair use unless stated otherwise]


---
class: center, middle

## Martin Schrimpf

![](img/people/martin.jpg)

---
background-image: url(img/task.gif)
background-size: cover

---
class: center, middle

## Predictive models

![](img/brain_model.png)
![](img/hmo.jpg)
.source[Kubilius\*, Schrimpf\* et al. (under review)]
<span class="source"><a href="http://doi.org/10.1073/pnas.1403112111">Yamins\*, Hong\*, Cadieu, Solomon, Seibert, DiCarlo (PNAS, 2014)</a></span>

---
class: center, middle

## Brain-Score

--

![](img/brain-score.png)
.source[Kubilius*, Schrimpf* et al. (under review)]

---
class: center, bottom

## Feedforward models suffice?

.headshot[![](img/people/ko.jpg)]

![](img/control_vs_challenge.jpg)
.source[[Kar, Kubilius, Schmidt, Issa, DiCarlo (Nature Neuroscience, 2019)](https://doi.org/10.1038/s41593-019-0392-5)]


---
class: center, middle

## Feedforward models suffice?

![](img/neural_ost.jpg)
.source[[Kar, Kubilius, Schmidt, Issa, DiCarlo (Nature Neuroscience, 2019)](https://doi.org/10.1038/s41593-019-0392-5)]

<!-- ---
class: center, bottom

## Recurrent neural networks
.headshot[![](img/people/dan_bear.jpg)]
.headshot2[![](img/people/aran.jpg)]
![](img/neurips2018.png)

<span class="source"><a href="https://arxiv.org/abs/1807.00053">Nayebi\*, Bear\*, Kubilius\*, Kar, Ganguli, Sussillo, DiCarlo, Yamins (NeurIPS 2018)</a></span> -->

---
class: center, middle

## Deeper is better?

![](img/brain-score.png)
.img100[![](img/network_sizes.png)]

---
class: center, middle

## Deeper is better?

.img100[![](img/densenet.png)]
.source[Adapted from [Huang, Liu, van der Maaten, Weinberger (CVPR 2017)](https://arxiv.org/abs/1608.06993)]

---
class: center, middle

## Wrapping deep nets

.img100[![](img/densenet-rnn.png)]
.source[Adapted from [Huang, Liu, van der Maaten, Weinberger (CVPR 2017)](https://arxiv.org/abs/1608.06993)]

---
class: center, middle

## CORnet family of models

.cols2[
![](img/brain_model.png)
]

---
class: center, middle

## CORnet-Z

.cols2[
![](img/brain_model.png)
.img30[![](img/cornet_z.png)]
]

---
class: center, middle

## CORnet-Z

.cols2[
![](img/brain_model.png)
.img30[![](img/cornet_z.png)]

![](img/brain-score_z.png)
]

---
class: center, middle

## CORnet-S (feedforward only)

.cols2[
![](img/brain_model.png)
.img60[![](img/cornet_s_nonrec.png)]
]

---
class: center, middle

## CORnet-S (feedforward only)

.cols2[
![](img/brain_model.png)
.img30[![](img/cornet_s_nonrec.png)]

![](img/brain-score_s-nr.png)
]

---
class: center, middle

## CORnet-S

.cols2[
![](img/brain_model.png)
.img60[![](img/cornet_s.png)]
]

---
class: center, middle

## CORnet-S

.cols2[
![](img/brain_model.png)
.img30[![](img/cornet_s.png)]

![](img/brain-score_s.png)
]

---
class: center, middle

## Object Solution Times

.cols2[
![](img/neural_ost2.png)
]

---
class: center, middle

## Object Solution Times

.cols2[
![](img/neural_ost2.png)
![](img/ost.png)
]

---
class: center, middle

## CORnet-S

.cols2[
![](img/brain_model.png)
.img30[![](img/cornet_s.png)]

![](img/brain-score_s-ost.png)
]

---
class: center, middle

## CORnet search

.img40[![](img/cornet_search.png)]
.img80[![](img/ablation.png)]

---
class: center, middle

## Generalization

![](img/depth_vs_cifar.png)

---
class: center, middle

## Conclusion

.img100[![](img/main.png)]

[brain-score.org](http://brain-score.org)
[github.com/dicarlolab/cornet](https://github.com/dicarlolab/cornet)

<!-- ---
class: center, middle

## Towards understading

![](img/understanding.png)
.source[[Kubilius (NeuroImage, 2018)](https://doi.org/10.1016/j.neuroimage.2017.12.006)] -->

---
class: middle
## Thank you!

.split-60[
.column[
![](img/people/dicarlolab2.jpg)
**Collaborators elsewhere:**
- Daniel Yamins (Stanford)
- Aran Nayebi (Stanford)
- Dan Bear (Stanford)
- Surya Ganguli (Stanford / Google Brain)
- David Sussillo (Google Brain)

**Slides:** find them on [klab.lt](https://klab.lt/publications/talks/2019-ecvp/slides.html)

]

.column[
**Collaborators at MIT:**
- James DiCarlo
- Martin Schrimpf
- Kohitij Kar
- Rishi Rajalingham
- Pouya Bashivan
- Kailyn Schmidt
- Jonathan Prescott-Roy
- Elias Issa (now at Columbia)
- Ha Hong (now at Bay Labs)
- Najib Majaj (now at NYU)

**Funding:** .small-text[Horizon 2020, US National Eye Institute, Office of Naval Research, Simons Foundation, James S. McDonnell Foundation, US National Science Foundation, Semiconductor Research Corporation (SRC), DARPA]
]
]

