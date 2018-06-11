---
title: Towards a generic model for figure-ground segmentation
authors: Jonas Kubilius, Johan Wagemans, Hans P. Op de Beeck
where: Roelfsema lab (NIN)
location: Amsterdam (The Netherlands)
date: 2013-12-02
categories: Talks
datestamp: 2013-12-02 11:45:26
links:
    slides: https://dl.dropboxusercontent.com/u/2498793/klab/gmin_lep_retreat_2014.svg
---

While multiple studies investigate the properties of the earliest and final stages of visual information processing, the underlying transformations leading from simple edge detection to object recognition remain seemingly intracktable. To tackle this problem, we take a step back and ask what mechanisms could lead to a successful figure-ground segmentation of a given image. We propose the following conceptual framework: (i) alternating steps of feature detection and feature pooling (grouping) in a hierarchical manner; (ii) segmentation into (provisional) objects by an unsupervised learning procedure using the computed feature grouping strengths. In this talk, I will concentrate on an initial implementation of this model where grouping principles such as proximity or good continuation are leveraged to discover grouped objects in an image. Model simulations reveal a promising performance on classical Gestalt displays of dot lattices, contour integration, and texture segregation. I will further discuss the implications of the proposed architecture and, in particular, what kind of evidence is necessary to improve model’s behavior.

<iframe src="https://dl.dropboxusercontent.com/u/2498793/2013\_gmin\_nin.svg" width="100%" height="480"></iframe>

*(Navigate through slides with left/right mouse clicks; for more options, check [Sozi’s tutorial](http://sozi.baierouge.fr/pages/40-play.html).)*
