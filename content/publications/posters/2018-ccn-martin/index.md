---
title: Brain-Score: Which Artificial Neural Network Best Emulates the Brain’s Neural Network?
authors: Martin Schrimpf*, Jonas Kubilius*, James J. DiCarlo
conference: CCN
date: 2018-09-07 19:30
duration: 1:45
categories: Posters
links:
    url: https://ccneuro.org/2018/Papers/ViewPapers.asp?PaperNum=1297
datestamp: 2018-09-0 19:30
---

Prior work revealed that artificial neural networks (ANNs) for visual categorization are remarkably similar to the primate brain, both in terms of internal neural representations as well as behavioral output. Here we ask, as ANNs have continued to evolve in performance over the last years, are they also strong candidate models for the brain? To answer this question, we developed Brain-Score, a composite of neural and behavioral benchmarks that score any ANN on how brain-like it is, together with an online platform where ANNs can be submitted to receive a Brain-Score and their rank relative to other models. Deploying our framework on dozens of state-of-the-art ANNs, we found that ResNet and DenseNet families of models are the closest models from the Machine Learning community to primate ventral visual stream. Curiously, best current ImageNet models, such as PNASNet, were not the top-performing models on Brain-Score. Despite high scores, these deep models are often hard to map onto the brain's anatomy due to their vast number of layers and missing biologically-important connections, such as recurrence. We propose a small recurrent model, called CORnet, which beats all other models on Brain-Score and provides a more direct correspondence to the brain through simple anatomical mappings and recurrent connectivity.