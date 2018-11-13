class: center, middle
background-image: url(img/alexnet_bckg.png)

# Understanding and improving deep neural nets
*Jonas Kubilius*

Brain & Cognition / KU Leuven (Belgium)

LEP lab meeting / 2015-09-25

.license[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons license" style="border-width:0;" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
.logo[]
.logo-name[[klab.lt](http://klab.lt)]
]
.aside[except where otherwise noted, these slides are available under the Creative Commons Attribution 4.0 International License]

???
I will discuss three ideas for investigating deep nets that I want to pursue during my postdoc:

(i) Understanding human rapid visual perception by presenting manipulated versions of objects that need to be detected, and trying to understand which features are critical.
(ii) Training deep nets to match human performance on all these tasks.
(iii) Using summary statistics in deep nets to perform segmentation.

I need feedback which of these ideas are most interesting and how to pursue them best.

.source[fair use – [Krizhevsky et al. (NIPS, 2012)](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional)]

---
layout: true
class: middle

---
# Warm up
### or why get hooked on the latest fad

---
## Spiky smoothie cubie dataset

![](img/hop2008_intro.png)

---
## ...enter Deep Nets

![](img/hop2008_mds.png)

![](img/hop2008_clust.png)

---
## ...also correlates with behavior

![](img/hop2008_corr.png)

---
## Artistic style

.cols2[
![](img/vangogh_starry_night.jpg)
.source[public domain - [Van Gogh, The Starry Night, 1889](https://commons.wikimedia.org/wiki/File:Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg)]

![](img/leuven_vangogh_starry_night.png)
.source[cc by 2.0 - [Hühnerauge / flickr](https://www.flickr.com/photos/27086904@N03/3588305201/)]
.source[rendered using [Justin Johnson's implementation](https://github.com/jcjohnson/neural-style)]
]

---
## Artistic style

.cols2[
![](img/the_scream.jpg)
.source[public domain - [Munch, The Scream, 1893](https://en.wikipedia.org/wiki/The_Scream#/media/File:The_Scream.jpg)]

![](img/leuven_the_scream.png)
.source[cc by 2.0 - [Hühnerauge / flickr](https://www.flickr.com/photos/27086904@N03/3588305201/)]
.source[rendered using [Justin Johnson's implementation](https://github.com/jcjohnson/neural-style)]
]

---
## Artistic style

.cols2[
![](img/bacchus.jpg)
.source[public domain - [Rubens, Bacchus (1638-40)](http://www.ibiblio.org/wm/paint/auth/rubens/)]

![](img/leuven_bacchus.png)
.source[cc by 2.0 - [Hühnerauge / flickr](https://www.flickr.com/photos/27086904@N03/3588305201/)]
.source[rendered using [Justin Johnson's implementation](https://github.com/jcjohnson/neural-style)]
]

---
## Why deep nets: Summary

- General-purpose (black box) models
- Work for explaining data at neural and perceptual levels
- Easier to understand because they are feedforward
- But still not understood

---
background-image: url(img/alien.jpg)

# <span style="color:white;">Ideas</span>

---
## Outline

1. Human rapid perception
2. Comparing to deep nets
3. New architecture!

---
# Rapid perception

---
## What we know

- It's fast, probably feedforward (Delorme & Thorpe, 2001; VanRullen & Thorpe, 2002; VanRullen & Koch, 2003)
- Features:
  - shape first, texture second (Elder & Velisavljević, 2009)
  - amplitude spectrum (Gaspar & Rousselet, 2009)
  - canonical posture (Delorme et al., 2010)
  - size ratio (Delorme et al., 2010)
  - diagnostic features (eyes, mouth, limbs; Delorme et al., 2010)
  - edge co-occurence (Perrinet & Bednar, 2015)

???
Implications:

- A wrong task to understand vision
- We want to know what information is available over time, not solve animal detection

---
## Our approach

.full[![](img/exp1.png)]

---
class: center
## How to create stimuli

![](img/exp1_stim.png)

---
# Comparison to machines

???
- Just train for specific tasks
- A single architecture for all tasks

---
# Novel architecture

---
## What does feedforward look like?

.cols2[
![](img/deer.jpg)
.source[cc by 3.0 – [Nige Brown / flickr](https://www.flickr.com/photos/nigel_brown/9404238204)]

![](img/deer_paint.jpg)
]

---
## What does feedforward look like?

.cols2[
![](img/35.jpg)
.source[fair use – [LabelMe](http://labelme.csail.mit.edu/Release3.0/index.php)]

![](img/35_drawgist_08_0.jpg)
]

---
## What does feedforward look like?

1. Summary statistics is a V2 bottleneck for features
2. But some structure survives

---
## Metamers of rapid perception

.cols2[
![](img/04.jpg)
.source[fair use – [LabelMe](http://labelme.csail.mit.edu/Release3.0/index.php)]

![](img/04_fake.jpg)
]

---
class: middle

# Thank you!
<!--.aside[slides available at [klab.lt](https://klab.lt)]-->

---
class: middle

# Extra slides

---
class: center
## gmin layer 1

![](img/gmin_arch_0-1.png)
.source[cc by 4.0 – [Kubilius et al. (Frontiers in Computational Neuroscience, 2014)](http://doi.org/10.3389/fncom.2014.00158)]

---
class: center
## In practice

![](img/gmin_0-1.png)

---
class: center
## gmin layers 1 & 2

![](img/gmin_arch_0-2.png)
.source[cc by 4.0 – [Kubilius et al. (Frontiers in Computational Neuroscience, 2014)](http://doi.org/10.3389/fncom.2014.00158)]

---
class: center
## In practice

.full[![](img/gmin_0-2.png)]

---
class: center
## gmin full architecture

![](img/gmin_arch_full.png)
.source[cc by 4.0 – [Kubilius et al. (Frontiers in Computational Neuroscience, 2014)](http://doi.org/10.3389/fncom.2014.00158)]

---
class: center
## In practice

.full[![](img/35_gmin_output.png)]

(Try it online: [gmin.klab.lt](http://gmin.klab.lt))

---
## Tested on multiple tasks

![](img/rec_geons.png)

---
## Tested on multiple tasks

![](img/shape_cat.png)

---
class: center
## Basic building blocks

![](img/cnn.png)
