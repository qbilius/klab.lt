class: center, middle

# Deep nets as a computational model for human shape sensitivity

*Jonas Kubilius*

Brain & Cognition / KU Leuven (Belgium)

DiCarlo lab meeting / 2015-05-27

.license[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons license" style="border-width:0;" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
.logo[]
.logo-name[[klab.lt](http://klab.lt)]
]
.aside[except where otherwise noted, these slides are available under the Creative Commons Attribution 4.0 International License]

???
Theories of object recognition agree that shape is of primordial importance, but there is no consensus about how shape might be represented and so far attempts to implement a model of shape perception that would work with realistic stimuli have largely failed. Here we demonstrate that the sensitivity for shape features characteristic to human and primate vision emerge in state-of-the-art convolutional neural networks when trained for a generic object recognition from natural photographs. We show that these models explain human shape judgments for several benchmark behavioral and neural stimulus sets on which earlier models failed. In particular, although never explicitly trained for, these models develop sensitivity to non-accidental properties that have long been implicated to form the basis for object recognition. Even more strikingly, when tested with a challenging stimulus set in which shape and category membership are dissociated, the most complex model architectures capture human shape sensitivity as well as some aspects of the category structure which emerges from human judgments. As a whole, these results indicate that convolutional neural networks not only learn physically correct representations of object and scene categories but also develop perceptually accurate representational spaces of shapes. An even fuller model of human object representations might be in sight by training deep architectures for multiple tasks, which is so characteristic in human development.

---
layout: true
class: middle

---
class: center
## PhD

![](img/outline1.png)

---
class: center
## Recent research

![](img/outline2.png)

---
# CNNs

---
## CNNs learn categories

![](img/alexnet.png)
.source[fair use - [Krizhevsky et al. (NIPS, 2012)](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional)]

![](img/places_segment.png)
.source[fair use - [Zhou et al. (ICLR, 2015)](http://arxiv.org/abs/1412.6856)]

---
class: center
## CNNs match neural data

![](img/yamins.jpg)
.source[fair use – [Yamins et al. (PNAS, 2014)](http://doi.org/10.1073/pnas.1403112111)]

---
class: center

.full[![](img/dnn_hope.gif)]

---
class: center, middle

# I want machines to .strike[.strike-fix[see]]
.strike-new[perceive]

---
class: center

## The dress

.cols2[
![](img/The_Dress.png)
.source[fair use – [Wikipedia](https://en.wikipedia.org/wiki/File:The_Dress_(viral_phenomenon).png)]

![](img/dress_color.png)
.source[cc by-nc 2.5 – [xkdc](http://xkcd.com/1492/)]
]

---
## CaffeNet

- 5 convolutional layers (conv1 - conv5)
- 3 fully connected layers (fc6 - fc8)

![](img/alexnet.png)
.source[fair use - [Krizhevsky et al. (NIPS, 2012)](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional)]

---
## Case 1: Recognition from shape

![](img/snodgrass.png)
.source[[Snodgrass & Vanderwart (1980)](http://www.ncbi.nlm.nih.gov/pubmed/7373248)]

- Snodgrass & Vanderwart dataset of **260** drawings of common objects
- **61** of these objects are included in the ImageNet training set, or
- **147** of these objects are in the ImageNet training set if more specific concepts are included too

---
class: center
## Can CNNs abstract?

![](img/snodgrass_manip.png)

---
class: center
## Results

![](img/snodgrass_exact.png)

---
class: center
## Results

![](img/snodgrass_all.png)

---
class: center
## Case 2: Physical vs. perceived

### Op de Beeck et al. (2008)

![](img/hop2008_stim.png)

---
class: center
## Human vs. model

.full[![](img/hop2008.png)]
.source[fair use – [Op de Beeck et al. (Journal of Neuroscience, 2008)](http://doi.org/10.1523/JNEUROSCI.2511-08.2008)]

---
class: center
## Shape is hard

![](img/plot_lin_hop2008_all.png)

---
class: center
## CNNs pick up shape

.full[![](img/plot_mds_hop2008_CaffeNet.png)]


---
class: center
## CNNs pick up shape

![](img/plot_lin_hop2008_CaffeNet.png)

---
class: center
## CNNs pick up shape (top layer)

![](img/plot_corr_mod_hop2008_CaffeNet.png)

---
class: center
## Case 3: NAPs and geons

.small[![](img/geon_examples.png)]
.source[fair use – [Ori Amir](http://geon.usc.edu/~ori/)]

### 66 geon triplets

---
class: center
## Geons are hard

![](img/plot_acc_geons_all.png)

---
class: center
## CaffeNet performance

![](img/geons.png)

---
class: center
## Case 4: Shape vs category 

### Bracci & Op de Beeck (submitted)

![](img/stefania-stimuli.jpg)
.source[Bracci & Op de Beeck (submitted)]

---
class: center
## Shape vs. category

.full[![](img/plot_lin_stefania_all.png)]

---
class: center
## Comparison to perception

.full[![](img/plot_corr_human_model_stefania.png)]

---
class: center
## Comparison to neural data

.full[![](img/plot_corr_neural_human_stefania.png)]

---
class: center
## Comparison to neural data

.full[![](img/plot_corr_neural_model_stefania.png)]

<!------->
<!--class: center-->
<!--## Model representations-->

<!--.full[![](img/plot_mds_stefania_CaffeNet.png)]-->

---
class: center
## Available information

.full[![](img/plot_lin_stefania_CaffeNet.png)]

---
class: center
## Available information

.full[![](img/plot_ssize_stefania_HMO.png)]

---
class: center
## Why natural / manmade?

![](img/plot_nat_man_stefania_HMO.png)

---
class: center
## Case 5: Second-order edges

.cols2[
![](img/vonderheydt_1984-1.png)
.source[fair use – [von der Heydt et al. (Science, 1984)](http://doi.org/10.1126/science.6539501)]

.small[![](img/field.png)]
![](img/poort.jpg)
.source[fair use – [Poort et al. (Neuron, 2012)](http://doi.org/10.1016/j.neuron.2012.04.032)]
]

---
class: center
## Cue-invariant processing

![](img/rats.png)
.source[fair use – De Keyser et al. (submitted)
]

---
class: center
## Luminance- vs. orientation-defined

.cols2[
.img50[![](img/lum_0_00.png)]
.img50[![](img/lum_1_00.png)]

.img50[![](img/lamme_0_00.png)]
.img50[![](img/lamme_1_00.png)]
]

---
class: center
## Luminance- vs. orientation-defined

.full[![](img/plot_gen2_2ndorder_CaffeNet.png)]

---
class: center
## Receptive field properties

![](img/plot_conv1_2ndorder_CaffeNet.png)

**conv1**

---
class: center
## Receptive field properties
![](img/plot_conv2_2ndorder_CaffeNet.png)

**conv2**

---
class: center
## Receptive field properties

![](img/plot_conv5_2ndorder_CaffeNet.png)

**conv5**

---
# Are CNNs almighty?

---
class: center
## Offset-defined

.cols2[
.img50[![](img/offset_0_00.png)]

.img50[![](img/offset_1_00.png)]
]

---
class: center

.full[![](img/plot_gen_2ndorder_CaffeNet.png)]

---
class: center
## Receptive field properties

![](img/plot_conv12_2ndorder_CaffeNet.png)

**conv1**

---
class: center
## Receptive field properties
![](img/plot_conv22_2ndorder_CaffeNet.png)

**conv2**

---
class: center
## Receptive field properties

![](img/plot_conv52_2ndorder_CaffeNet.png)

**conv5**

---
## Other issues

- Poor match to categorical decisions
- No filling-in with occlusions

![](img/random.png)

---
## Conclusions

- CNNs reflect perceptual shape similarity
- Categorization is mostly due to shape
- Semantical information may be available at the train time
- Poor inference / integrations

---
## Future directions

- Training on more tasks
- Training not only for categorization, but also semantics
- Need to work out integration
- Unsupervised learning?
 
---
# Thank you!
<!--.aside[slides available at [klab.lt](https://klab.lt)]-->

---
# Extra slides

---
## Featural vs. configural

- Dynamic linking rules = less parameters

.small[![](img/configural.png)]

- Feature inference

.small[![](img/field.png)]

---
# gmin
.subtitle[an open, minimalist mid-level framework]

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
## In practice

.full[![](img/35_gmin_output.png)]

???
Note also that this kind of segmentation is done in a completely feedforward way, so the fact that we get any structure at all stands in contrast with rapid object detection or scene gist ideas.

---
class: center
## What does feedforward look like?

![](img/drawgist_paradigm.png)

--

.cols3[
![](img/35.jpg)
.source[fair use – [LabelMe](http://labelme.csail.mit.edu/Release3.0/index.php)]

![](img/35_gmin_output2.png)

![](img/35_drawgist_08_180.jpg)

]