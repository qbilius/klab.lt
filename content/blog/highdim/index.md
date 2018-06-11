---
title: Higher-dimensional spaces for feature representation
datestamp: 2012-06-08 10:51:31
categories: Blog
tags: gmin
---

When we think how to parse an image, we imagine a two-dimensional input array on which clever manipulations have to be applied. So we try to come up with strategies for edge extraction, grouping them, using that for figure-ground segmentation and so forth. Sometimes (often?) however this unnecessarily complicates things.

<figure>
<img src="banana.jpg" />
<figcaption>source: <a href="http://www.morguefile.com/archive/display/10665">morgueFile.com</a></figcaption>
</figure>

Consider an image on the right. Even performing some trivial figure-ground segmentation on it might be not a straightforward matter (I wouldn’t know where to start, actually). In their [2009 paper](http://dx.doi.org/10.1145/1518701.1518903) ([pdf](http://web.mit.edu/rruth/www/Papers/RosenholtzEtAlCHI2009PO.pdf)) and [recently in VSS](http://www.visionsciences.org/abstract_detail.php?id=1471) (thanks [Johan](http://gestaltrevision.be/en/about-us/principal-investigator)), [Ruth Rosenholtz](http://persci.mit.edu/people/rosenholtz) and [Nat Twarog](http://persci.mit.edu/people/ntwarog) put forward an idea that sometimes it is sufficient to blow up an image into a higher-dimensional space where relevant features would be represented. In the case of bananas, we could, for example, convert the image to greyscale and put the resulting luminance values in the third dimension of the image, as seen in the image below. Now you can easily see figure-ground segmentation with the (yellow) bananas being at the top, (brown) background on the bottom, and the table somewhat in between (red, green).

<figure>
<img src="banana-repr.png" width=1024 height=671 />
<figcaption>The view is as if the original image was lying flat and we were looking sideways at the image’s bottom side. For presentation purposes, each dot has been colored using its RGB value. [<a href="http://pastebin.com/sacXvH84">source code</a>]</figcaption>
</figure>

This is not stunning news, of course, it does not magically parse objects from the image. It is simply a different way of representing the same information. But notice how it simplifies the problem of parsing an image and enhances our understanding of the information present in the image. We can then think more clearly about ways to process this information.

Moreover, this idea quite naturally allows for grouping at multiple levels (hierarchical organization). Typically, there is no single grouping present in an image: bananas as a foreground and table plus wall as a background? Or is it bananas and table versus the wall? In the higher-dimensional representation, bananas go together if we only look at the top of the plot (group over luminance using a narrow filter). Bananas and table are grouped together using wider filters. Grouping scales emerge naturally in this representation and as Rosenholtz et al. (2009) show, this very simple approach can lead to a quite accurate parsing.

I think GMin should represent images immediately in higher dimensional spaces, allowing grouping mechanisms to act over various feature dimensions depending on the task at hand. Moreover, this representation seems as an early step of [Jim DiCarlo’s “manifold untangling” framework](http://dx.doi.org/10.1016/j.neuron.2012.01.010). First we could blow up the space using the immediately available features (such as color and orientation), then *using tricks* we gradually transform it into an untangled representation with perceptually relevant features (such as objects and their poses).
