---
title: gmin specification (first draft)
datestamp: 2013-09-30 15:05:34
categories: Blog
tags: gmin
---

Goal
====

Image segmentation without relying on stored representations of familiar objects. Here, image segmentation is understood as parsing a scene into (complete) objects and a background with an appropriate depth ordering. Note that this definition is different from a common definition in computer vision literature where segmentation is treated as a [“process of partitioning a digital image into multiple segments”](http://en.wikipedia.org/wiki/Image_segmentation).

Scope/Assumptions
=================

-   Only the perceptual part of the visual system is considered (no “vision for action”).
-   No saccades since we can correctly parse a given scene without moving the eyes no matter where we’re fixating.
-   Uniform receptive field sizes, which holds approximately true for central vision within a 4 deg radius (Fig. 1a in [Freeman & Simoncelli, 2011](http://dx.doi.org/10.1038/nn.2889)). Importantly, this assumption simplifies the problem of dealing with cluttered scenes to one where only a few (possibly incomplete) objects are present at a time.
-   Grayscale processing (i.e., magnocellular pathway only). Color can be included later by choosing an appropriate transformation (color-opponent channels or the [DKL space](http://alexholcombe.wordpress.com/2011/07/11/color-space-pictured-and-animated-derrington-krauskopf-lennie/); milestone for version 2.0).
-   No motion for now (milestone for version 3.0).
-   No 3D reconstructions, only depth ordering of surfaces.
-   No object recognition (since we’re avoiding top-down effects).
-   No attention. Coarse segmentation is assumed to occur pre-attentively. Finer segmentation might involve incremental grouping ([Roelfsema, 2006](http://dx.odi.org/10.1146/annurev.neuro.29.051605.112939)) but the goal of this model is to provide the initial segmentation.
-   No explicit task. Segmentation should happen pre-attentively.

Proposed processing sequence
============================

A similar, yet not as complete, approach has been taken in [Regan (2000)](http://www.yorku.ca/dregan/index.php?p=books), [Self & Roelfsema (2013)](http://gestaltrevision.be/pdfs/oxford/Self&Roelfsema-The_neural_mechanisms_of_figure-ground_segregation.pdf), [Geisler & Super (2000)](http://klab.lt/2013/09/22/perceptual-organization-of-two-dimensional-patterns/ "Perceptual organization of two-dimensional patterns"), [Shi & Malik (2000)](http://dx.doi.org/10.1109/34.868688).

1.  **Feature detection** Features are detected at every pixel by convolving with appropriate filters. Currently, this step is limited to a convolution with odd and even Gabors at multiple scales for orientation, polarity, and contrast magnitude detection. A maximum is computed over this space to extract features at the best scale.
2.  **Center-surround suppression** Since features usually span more than a single pixel, many nearly identical features are detected in a local neighborhood (possibly equivalent to the classical receptive field). This information is redundant and can be coarsened by computing a maximum within a local neighborhood and suppressing the remaining locations (see [Sharon et al. (2006)](http://dx.doi.org/10.1038/nature04977) for a similar approach).
3.  **Pooling over features (similarity grouping)** Various statistics over the extracted features are computed in the extra-classical receptive field. For example, features could be grouped using the **proximity assumption**: things close in spacetime / feature space are more likely to belong to the same collection ([Földiák, 1991](http://dx.doi.org/10.1162/neco.1991.3.2.194)), giving rise to Gestalt grouping principles. [Portilla & Simoncelli (2000)](http://www.cns.nyu.edu/lcv/texture/), [Rosenholtz et al. (2009)](http://dx.doi.org/10.1145/1518701.1518903) and [Balas et al. (2009)](http://dx.doi.org/10.1167/9.12.13) explored other possible pooling statistics. The outcome of this step is the grouping strength, i.e., a probability of features belonging to the same collection.
4.  **More complex feature detection and pooling** The above-described steps could be performed again, at multiple levels of hierarchy, using more complex features (such as curved contours). These steps might be necessary for first- (e.g., orientation-defined) and [second-order grouping displays](http://klab.lt/2013/09/22/perceptual-organization-of-two-dimensional-patterns/ "Perceptual organization of two-dimensional patterns"). For example, in the orientation-defined displays, boundaries at texture discontinuities are detected at this stage of processing.
5.  **Segmentation into objects / collections** So far, grouping has occurred only locally. In the final step, we compute which elements go with which ones globally: if A and B go together, and B and C go together, then A and C go together even if they do not group well directly. This computation could be done by connecting all pairs that group above a certain threshold. Belonging to a collection can mean an increase the firing rate ([Roelfsema et al., 2004](http://dx.doi.org/10.1038/nn1304)), an activation of collection units (similar to the [“grandmother cell”](http://en.wikipedia.org/wiki/Grandmother_cell) concept), firing synchronization ([von der Malsburg, 1981](http://cogprints.org/1380/)) or aligning temporal sequence ([Wehr & Laurent, 1996](http://dx.doi.org/10.1038/384162a0)).
6.  **Border ownership** Once collections of features are found, border ownership computation can proceed using the **convexity bias assumption**: objects tend to be convex ([Kogo et al., 2010](http://dx.doi.org/10.1037/a0019076)).
7.  **Depth assignment / occlusion computation** Upon border ownership computation, parts of objects might appear to be missing. These missing parts potentially inform about the depth ordering and are relevant for *predicting* the possible shape behind the occluder. These predictions might be used later on to refine the segmentation.

[caption id=“attachment\_747” align=“alignnone” width=“475”][![gmin architecture](architecture_nolabels-792x1024.png "Proposed architecture (rough sketch)")](architecture_nolabels.png) **Proposed architecture of *gmin* (rough sketch).** Partial (current) implementation is available on [github](https://github.com/qbilius/gmin).[/caption]
