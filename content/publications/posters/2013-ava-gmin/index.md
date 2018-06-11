---
title: Towards a generic model for figure-ground segmentation
authors: Jonas Kubilius, Johan Wagemans, Hans P. Op de Beeck
conference: AVA
location: Leuven (Belgium)
date: 2013-12-19
categories: Posters
datestamp: 2013-12-19 17:00:19
links:
    doi: 10.5281/zenodo.7612
    pdf: http://zenodo.org/record/7612/files/Kubilius_et_al_gmin_AVA2013_small.pdf
    code: https://github.com/qbilius/gmin
---

While multiple studies investigate the properties of the earliest and final stages of visual information processing, the underlying transformations leading from simple edge detection to object recognition remain seemingly intractable. To tackle this problem, we take a step back and ask what mechanisms could lead to a successful figure-ground segmentation of a given image. We propose the following conceptual framework: (i) alternating steps of feature detection and feature pooling (grouping) in a hierarchical manner; (ii) segmentation into (provisional) objects by an unsupervised learning procedure using the computed feature grouping strengths. We present an initial implementation of this model where grouping principles such as proximity or good continuation are leveraged to discover grouped objects in an image. Model simulations reveal a promising performance on classical Gestalt displays of dot lattices, contour integration, and texture segregation.
