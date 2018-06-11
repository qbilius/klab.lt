class: center, middle

# Using Goal-Driven Deep Neural Networks to Interpret Brain Data
***Jonas Kubilius***

- McGovern Institute for Brain Research / MIT (USA)
- Brain & Cognition / University of Leuven (Belgium)

Bernstein DNN workshop / 2016-09-21

.license[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons license" style="border-width:0;" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
.logo[]
.logo-name[[klab.lt](http://klab.lt)]
]
.aside[Creative Commons Attribution 4.0 International License]

???
Good morning. It's a great pleasure to be here but if you read the program you were probably expecting to see Dan Yamins here.

---
class: middle

![](img/dan.jpg)
<br />
Dan Yamins

???
Well, Dan has just started his faculty position at Stanford, and I guess he's slowly learning that professors have little time. But I'm still a postdoc, I have plenty of time for sightseeing Berlin and giving talks, so I gratiously accepted organizers last minute invitation. But what the organizers didn't know at the time, I believe, is that you're basically getting the same deal –

---
class: middle

.cols2[
![](img/dan.jpg)

Dan Yamins

![](img/jonas.jpg)

Jonas Kubilius
]

???
you see, I'm actually now sitting at Dan's old desk at MIT and even using his old monitor and keyboard.

Looking through the program, I found Dan's title quite interesting and I wanted to know more but Dan was gone, I couldn't ask him, so I decided to give a talk on the same topic. The majority of this talk will focus on our published work on the relation between deep neural nets and human shape judgments. Some of you may have seen me present these results earlier this year at VSS. In the second part of this talk, I wanted to show some of our recent work. I don't really have any results quite yet but, given the workshop format, I thought it would be important to give you a sense where I believe the field is headed, what are some of the interesting questions and how we're trying to tackle them.

Let me formulate the problem with the following example. Suppose you take the state-of-the-art deep neural net trained for object categorization and show it this image.

---
class: middle

.img_full[![](img/objects1.png)]
.source[&nbsp;]

???
It's gonna say this is a chair since it has seen many chairs during training.

---
class: middle

.img_full[![](img/objects2.png)]
.source[&nbsp;]

???
Then you show this. It's an apple, the model says, since it has seen many apple before.

---
class: middle

.img_full[![](img/objects3.png)]
.source[&nbsp;]

???
And that's a shoe.

---
class: middle

.img_full[![](img/objects4.png)]
.source[&nbsp;]

???
A bicycle.

---
class: middle

.img_full[![](img/objects5.png)]
.source[&nbsp;]

???
A schoolbus.

---
class: middle

.img_full[![](img/objects6.png)]
.source[[Jacky Alciné](https://mobile.twitter.com/jackyalcine/status/615329515909156865/photo/1)]

???
And if it has not encountered black people during training, what will this model say?

---
class: middle

.img_full[![](img/objects7.png)]
.source[[Jacky Alciné](https://mobile.twitter.com/jackyalcine/status/615329515909156865/photo/1), [The Wall Street Journal](http://blogs.wsj.com/digits/2015/07/01/google-mistakenly-tags-black-people-as-gorillas-showing-limits-of-algorithms/)]

???
Well, if you're Google, you're gonna say these are gorillas. This is what really happened, by the way.

---
class: middle

.img_full[![](img/objects8.png)]
.source[[Gizmodo](https://gizmodo.com/here-are-the-microsoft-twitter-bot-s-craziest-racist-ra-1766820160)]

???
And if you're Microsoft, you might go off on a racist rant. This is also a real example, although not in response to this image.

.img_full[![](img/objects8_backup.png)]
.source[[The Verge](http://www.theverge.com/2016/3/24/11297050/tay-microsoft-chatbot-racist)]

Joking aside, this is a serious issue.

---
class: middle
## Deep net training

![](img/mapping.png)

???
Remember, when we're training deep nets, they learn mapping between pixels in an image and a label. And the number of images is limited. And the number of labels is even more limited. In the usual training routine, models are exposed to 1000 categories from the ImageNet dataset. So what happens if the models encounter something new?

So we need to evaluate these models very carefully, not just on object categorization, the task they've been trained for, but also other task and other stimuli, and also using various metrics – performance, consistency with humans, explained variance in the IT cortex, and so on, and that's what we'll do in the majority of this talk.

But before we continue realize that this kind of evaluation is only part of the goal. We don't just want to know how good a given model is – we also want to know how to make them better. We want perhaps some principled way how to get a better model.

---
class: middle
## Representations

![](img/mapping2.png)

???
So my current favorit hypethisis is the following:

Given a good, biologically or evolutionary motivated training goal, somewhere in the hidden layers of a deep net, a rich high-level vocabulary of the visual world is learned that will be useful in novel situations with new stimuli.

So this is what is meant by "goal-driven approach".


So I showed you some failures, and many more are documented elsewhere, but overall could we somehow quantify how well or how bad deep nets are doing? Of course, they seem to be recognizing objects just fine – though there are things to say about this too, and we can talk about that during the questions if anybody is interested – but as vision researchers we want to know how comparable they are to humans. So let's give them a tricky task. Let's ask humans to do rate similarity of various objects. That's very subjective, of course. And then let's see whether deep nets can judge shapes similarly.



Arguably, *shape* is one of the most important such high-level descriptions, yet so far there has been no model that could adequately capture human judgments of shape. So we set out to explore whether deep convolutional neural nets could be a viable model of human shape representations.

---
class: center, middle

![](img/hans.jpg)

Hans Op de Beeck, *KU Leuven*

![](img/stefania_small.jpg)

Stefania Bracci, *KU Leuven*

???
This work has been done together with Hans Op de Beeck, who is here in the audience, and Stefania Bracci back at University of Leuven in Belgium.

---
class: middle
## Question

Can you get **shape for free** when optimizing for **category**?

???
In other words, just to state our goal very clearly here: If you took a deep net and optimized it for producing category labels using the standard ImageNet dataset and nothing else, would you get shape representations for free?

We tested this hypothesis in a series of three experiments.

---
class: middle
## Exp. 1: Novel shapes

![](img/hop2008_stim.png)
.source[[Op de Beeck et al. (J Neuro, 2008)](http://doi.org/10.1523/JNEUROSCI.2511-08.2008)]

???
In our first experiment, we used a set of nine stimuli from the study of Op de Beeck and colleagues in 2008. This stimulus set was designed with two orthogonal dimensions in mind. If you look at the columns, the stimuli are grouped in terms of their overall shape envelope, or aspect ratio: vertical, square, horizontal. If you look at the rows, stimuli are grouped in terms of their appearance: spiky shapes, smooth shapes, and cubie shapes.

---
class: middle
## Exp. 1: Novel shapes

![](img/hop2008_analysis0.png)

???
Eight participants performed a shape similarity judgment task. That is, they were asked to rate the similarity between each pair of stimuli. So, for instance, participants judged this smoothie and this spiky to be neither very similar nor dissimilar (as show by grayish colors) but these two smoothies were rated as highly similar (as shown by blueish colors). The average of all such pairwise comparisons is depicted in this nine-by-nine dissimilarity matrix. We can further visualize these similarities by projecting this eight-dimensional space down to two dimensions using multidimensional scaling. You can see how all spikies, all smoothies, and all cubies are forming clear clusters in this space, so we call the spiky/smoothie/cubie dimension the *perceived shape* dimension.

---
class: middle
## Exp. 1: Novel shapes

![](img/hop2008_analysis1.png)

???
On the other hand, we also computed a similarity of these stimuli based on the raw pixels. Again, we obtained another nine-by-nine dissimilarity matrix where each cell represents a particular pairwise comparison. Here you can see how a spiky and a smoothie are judged pretty similar, but the two smoothies are no longer similar, unlike what we saw in human jugdments. In the corresponding multidimensional scaling plot it is clear that stimuli group by their shape envelope, so we call this dimension the *physical form* dimension.

---
class: middle
## Exp. 1: Novel shapes

![](img/hop2008_analysis2.png)

???
By having decorrelated these two dimensions, we now have two competing hypotheses of shape representations: one - the physical form one - that corresponds to the lower levels of visual processing, and another one - the perceived shape one - that corresponds to the high level of visual processing.

---
class: middle
## Exp. 1: Novel shapes

![](img/hop2008_analysis3.png)

???
Now for any given computer vision model, using its responses to these stimuli, we can also construct a dissimilarity matrix just like before and ask whether it is closer (that is, correlates more) with the physical form or the perceived shape.

We tested three groups of models: shallow models, HMAX family of models, and deep nets.

---
class: middle

## Exp. 1: Shallow models

![](img/hop2008_res0.png)

???
Shallow models, whether V1-like GaborJet model or popular computer vision descriptors such as HoG or PHOG, were overall closer to the physical form than the perceived shape. Here error bars are 95% confidence intervals, and human level consistency is shown here by the gray bar.

---
class: middle
## Exp. 1: HMAX family

![](img/hop2008_res1.png)

???
Similarly, simple hierarchical models of the HMAX family were also not very good at capturing human shape judgments, but at least they were not representing physical form as much as shallow models.

---
class: middle
## Exp. 1: Deep nets

![](img/hop2008_res2.png)

???
With deep nets, we found that representations in higher layers were even less like physical form representations and even closer to human-level shape judgments. This is a good progress - we started here with pixelwise models and progressively got less of physical form representations and more of perceived shape representations with deep nets.

---
class: middle
## Exp. 1: Deep nets

![](img/hop2008_res3.png)

???
This progress is also nicely captured in these layer-by-layer plots where the dominance of the two dimensions is gradually reversed as we go from the inputs to the output layer.

So how far are we still from human performance? This stimulus set is a bit limited to answer this question as there were few stimuli and only two rather arbitrary dimensions.

---
class: middle
## Exp. 2: Novel fonts

![](img/fonts_stim.png)

???
So in our second experiment, we constructed the following larger set with no built-in dimensions. It was set of 36 novel characters from 6 artificial alphabets. Again, we asked participants to rate shape similarity without telling them anything about these fonts. On the right side, you can see how participants judged the similarity of these characters with colors indicating different fonts. Some fonts appear to easily cluster together whereas others are more spread around, so there is some interesting and non-trivial variance to explain.

---
class: middle
## Exp. 2: Novel fonts

![](img/fonts_res.png)

???
Now deep nets are very clearly and robustly outperforming other models. In fact, they are even reaching human-level consistency in this task.

Together, these two experiments demonstrate that deep nets are capturing a significant portion of variance in human shape judgments even without ever being trained for shape or having seen any of these stimuli before. In fact, our font stimuli are probably as far as you can get from natural images that deep nets have been trained on.

---
class: middle
## Exp. 3: Non-accidental properties

![](img/geons_stim2.png)
.source[[Kayaert et al. (J Neuro, 2003)](http://doi.org/10.1111/j.1460-9568.2005.04202.x)]

???
I have one more thing left. Remember Recognition-by-Components theory and non-accidental properties, that is, those properties of objects that remain invariant under various transformations, such as parallelism, curvature and so on? Irv Biederman and other researchers have shown that human and non-human observers are very sensitive to changes in these non-accidental shape properties. In the example shown here, although these two stimuli are equally far from the base stimulus, observers do not treat them as equivalent: they are much more sensitive to a change in the non-accidental property, that is, the sides becoming parallel.

Would deep nets also show the same sensitivity just out of the box without being trained for these properties at all?

In the figure you'll see next, I'm plotting how often various models judged non-accidental stimuli to be further away than the metric ones.

---
class: middle
## Exp. 3: Non-accidental properties

![](img/geons_res1.png)

???
We found that deep nets performed robustly above chance, unlike almost all other models. In particular, notice how far they are from the pixelwise, or metric, measures.

---
class: middle
## Exp. 3: Non-accidental properties

![](img/geons_res2.png)

???
Furthermore, here we're only looking at the output layers. The performance turned out to be nearly perfect intermediate layers.

---
class: middle
## Summary

- When trained for category, convnets learn human-like shape representations too
- Subjective human sensitivity to shape is captured by deep nets
- Complementary to [Hong, Yamins et al. (2016)](http://doi.org/10.1038/nn.4247): latent variables (size, pose, position, ...) in the top layers
- Feature representations in deep nets are general-purpose ([Yamins, Hong, et al., 2014](http://doi.org/10.1073/pnas.1403112111), [Khaligh-Razavi & Kriegeskorte, 2014](http://dx.doi.org/10.1371/journal.pcbi.1003915), [Güçlü & van Gerven, 2015](http://doi.org/10.1523/JNEUROSCI.5023-14.2015), [Gatys et al., 2016](http://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Gatys_Image_Style_Transfer_CVPR_2016_paper.html), Cichy et al., ...)


- *Read more:* [Kubilius et al. (*PLoS Computational Biology*, 2016)](http://doi.org/10.1371/journal.pcbi.1004896)
- *Code:* [osf.io/jf42a](https://osf.io/jf42a)
- *Reproduce:* `python run.py --bootstrap`

???
We found that when trained for category, deep nets learn human-like shape representations too. Moreover, subjective human sensitivity to shape is captured by deep nets. I want to stress this point as this is not trivial at all. These nets are trained for a very specific task that always has a correct answer: it's either an apple or a bus, or a bike. But when we put all spikies and all smoothies together, this not somehow an inherently correct answer. This is just our judgment. And nonetheless deep nets can capture these idiosyncracies.

These findings compliment another recent paper from our lab where Dan and others have shown that a bunch of latent parameters – size, pose, position and so on – are available in these deep nets. And there are quite a few other papers out there – many of them by people here – that establish that general-purpose visual features are learned by these deep nets.

But let's get back to the title of this talk again. Above all of that, this is the success of our goal-driven approach. Pushing deep nets to learn object categorization led to them being very good for all sorts of tasks – for free, without us doing any extra work.

So let's do more of this goal-driven approach.

---
class: middle
## Missing anything?

- Supervised learning is not biologically valid
--

- Temporal dynamics missing
--

- Deep net architecture is not tightly coupled with anatomy

???

Alright, so this was a very modest beginning of the goal-driven approach. We chose one very straightforward goal and got some promising results. But we haven't solve the entire vision, of course. So in the remainder of this talk, I wanted to show how the same idea -- goal-driven optimization -- could be applied to investigate other tasks. Again, as I mentioned at the beginning, this is only the proof of concept at the moment. I don't have any results yet.

---
class: middle

.cols3[
![](img/maryann.jpg)

**Maryann Rui**, *Berkeley*

![](img/dan.jpg)

Dan Yamins, *Stanford*

![](img/jim.jpg)

Jim DiCarlo, *MIT*
]



---
class: middle
## Deep feedforward model

![](img/feedforward.png)

---
class: middle
## Deep feedforward model

![](img/feedforward_1.png)

---
class: middle
## Deep feedforward model

![](img/feedforward_5.png)

---
class: middle
## Deep bypass model

![](img/bypass.png)

---
class: middle
## Deep bypass model

![](img/bypass0.png)

---
class: middle
## Deep bypass model

![](img/bypass1.png)

---
class: middle
## Deep bypass model

![](img/bypass2.png)

---
class: middle
## Deep bypass model

![](img/bypass3.png)

---
class: middle
## Deep bypass model

![](img/bypass4.png)

---
class: middle
## Deep bypass model

![](img/bypass5.png)

---
class: middle
## Deep bypass model

![](img/bypass6.png)

---
class: middle
## Deep bypass model

![](img/bypass7.png)

---
class: middle
## Deep bypass model

![](img/bypass8.png)

---
class: middle
## Deep bypass model

![](img/bypass_1.png)

---
class: middle
## Deep bypass model

![](img/bypass_5.png)

---
class: middle
## Deep recurrent model

![](img/memory.png)

---
class: middle
## Deep recurrent model

![](img/memory_5.png)

---
class: middle
## Deep feedforward model with retina

![](img/retina.png)

---
class: middle
## Full model

![](img/full.png)

---
class: middle
## Goal

Maximal categorization accuracy -> Maximal categorization accuracy *as fast as possible*

---
class: middle
## Loss function

![](img/loss.png)

---
class: middle
## Summary

- An architecture with temporal properties
- Jointly optimized for speed and accuracy
- Trainable on the ImageNet

---
class: bottom
# Thank you!

- *Slides:* [klab.lt](https://klab.lt/publications/talks/2016-bernstein-dnn/slides.html)


---
class: middle
count: false
# Extra slides

--
class: middle
count: false
## Exp. 4: Shape vs. category

![](img/stefania_stim.png)
.source[[Bracci & Op de Beeck. (J Neuro, 2016)](http://doi.org/10.1523/JNEUROSCI.2314-15.2016)]

???
Alright, so apparently, categorization is aided by developing sensitivity to shape. But is there anything beyond sensitivity to shape then that convnets develop? In other words, to what extent do these networks develop semantic representations similar to human categorical representations over and above mere shape information?

Once again, typically, shape and category are closely correlated, such that shape is predictive of category, making it hard to address this question. So again, we constructed a stimulus set where shape and category would be largely orthogonal. This is a beautiful work by Stefania Bracci, who investigated representations of these two dimensions neurally and found interesting dissociations in the brain.

So how much semantic information do deep nets capture?

---
class: middle
count: false
## Exp. 4: Shape vs. category

![](img/stefania_res.png)

???
Not a whole lot. There is remarkably more semantic information in them than in any other models we tested but it is far from human level judgments still.

Nonetheless, what is this little bit of categorical information that deep nets do acquire?

---
class: middle
count: false
## Exp. 4: Shape vs. category

![](img/stefania_gn.png)

???
If you projected dissimilarity matrix of our best model, GoogLeNet, you would see that there is a clear distinction between natural and man-made categories, but finer-grain clustering is not present yet.


---
class: center, middle
count: false
## Exp. 1: Feature generality

.img80[![](img/figure1_rev2.png)]
.source[cc-by – [Kubilius et al. (PLoS Comp Biol, 2016)](http://dx.doi.org/10.1371/journal.pcbi.1004896)]

---
class: center, middle
count: false
## Exp. 2a: Novel shapes

.img80[![](img/figure2.png)]
.source[cc-by – [Kubilius et al. (PLoS Comp Biol, 2016)](http://dx.doi.org/10.1371/journal.pcbi.1004896)]

---
class: center, middle
count: false
## Exp. 2b: Fonts

.img80[![](img/figure3.png)]
.source[cc-by – [Kubilius et al. (PLoS Comp Biol, 2016)](http://dx.doi.org/10.1371/journal.pcbi.1004896)]

---
class: center, middle
count: false
## Exp. 3: Geons

.img80[![](img/figure4.png)]
.source[cc-by – [Kubilius et al. (PLoS Comp Biol, 2016)](http://dx.doi.org/10.1371/journal.pcbi.1004896)]

---
class: center, middle
count: false
## Exp. 4: Shape vs. semantic

.img80[![](img/figure5_rev2.png)]
.source[cc-by – [Kubilius et al. (PLoS Comp Biol, 2016)](http://dx.doi.org/10.1371/journal.pcbi.1004896)]

---
class: middle

## Introduction

Recent sentiment: Can solve any task given enough data...

1. Where to get the data
2. What task to train for

???
Let me first unpack the title. As you already heard, deep nets are very powerful in that they can seemingly learn any complex task. That is, given enough training data, deep nets turn out to learn anything you want. This is by no means guarranteed but in practice that's what we've been seeing. So then as researchers we're left with the following two hard problems:

1. Where to get the data – I'm not going to talk about this one by I welcome questions at the end
2. What task to train for.

While an engineer might be satisfied that a system learned to perform a specific task, our goal is different here. We want to model human visual system and the visual system performs many tasks. So now what, should we train for all of them?

---
class: middle
## Training results

![](img/training_bypass.png)

---
class: middle
## Training results

![](img/bypass_time1.png)

![](img/bypass_time2.png)