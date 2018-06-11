---
title: A generic model architecture for perceptual grouping
authors: Jonas Kubilius, Johan Wagemans, Hans P. Op de Beeck
conference: Bernstein
location: Tübingen (Germany)
date: 2013-09-25
categories: Posters
datestamp: 2013-09-25 07:49:00
links:
    doi: 10.5281/zenodo.7118
    pdf: https://zenodo.org/record/7118/files/Kubilius_et_al_gmin_Bernstein2013.pdf
    code: https://github.com/qbilius/gmin
    Program: https://portal.g-node.org/abstracts/bc13/#/doi/nncn.bc2013.0012
---

Gestalt grouping principles provide important cues for organizing visual inputs into coherent percepts. While a number of models for each grouping principle have been proposed, a unifying architecture that would flexibly incorporate all of them is still lacking. Moreover, many of these models operate in mathematical terms, rendering them unsuitable for a wider testing on real input images. Here we present a generic biologically plausible unsupervised architecture, which we term gmin, geared towards a unified implementation of the grouping principles. The model operates by extracting a certain feature of interest from an input image (e.g., edges) and selecting maximally informative units to decrease computational load; then it proceeds to iteratively compute grouping strength between all pairs of units and update informative unit selection using a particular grouping principle (e.g., good continuation). This process is repeated for all features of interest. Finally, a segmentation of an image into (provisional) objects is provided by an unsupervised learning procedure on the computed grouping strengths, such as clustering or belief propagation. We illustrate the validity and the general usefulness of our approach by testing it on a few very different grouping displays. Using the cues of proximity, good continuation, or orientation similarity, we were able to obtain a satisfying model performance on the classic Gestalt displays of dot lattices, contour integration, and texture segregation.
