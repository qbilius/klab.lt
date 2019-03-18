---
title: Using Brain-Score to Evaluate and Build Neural Networks for Brain-Like Object Recognition
authors: Martin Schrimpf*, Jonas Kubilius*, Ha Hong, Najib J. Majaj, Rishi Rajalingham, Corey Ziemba, Elias B. Issa, Kohitij Kar, Pouya Bashivan, Jonathan Prescott-Roy, Kailyn Schmidt, Aran Nayebi, Daniel Bear, Daniel Yamins, and James J. DiCarlo
conference: Cosyne
location: Lisbon (Portugal)
date: 2019-03-02 20:30
categories: Posters
links:
    poster: schrimpf-kubilius_cosyne2019.pdf
datestamp: 2019-03-02 20:30:00
---

The internal representations of early deep artificial neural networks (ANNs) were found to be remarkably similar to the internal neural representations measured experimentally in the primate brain. Here we ask, as ANNs have continued to evolve, are they becoming more or less brain-like? We therefore developed Brain-Score: a composite of multiple neural and behavioral benchmarks that score any ANN on how similar it is to the brain’s mechanisms for core object recognition. Evaluating state-of-the-art ANNs, we found that ResNet and DenseNet families of models are the closest models from the Machine Learning community to primate ventral visual stream. Curiously,best current ImageNet models, such as PNASNet, were not the top-performing models on Brain-Score.

Despite high scores, these deep models are often hard to map onto the brain due to their vast number of layers and missing biologically-important connections, such as recurrence. We thus built CORnet-S: a neural network developed by using Brain-Score as a guide with the anatomical constraints of compactness and recurrence. Although a shallow model with four anatomically mapped areas with recurrent connectivity, CORnet-S is a top model on Brain-Score and outperforms similarly compact models on ImageNet.

Finally, to further validate our claims, we are including new behavioral measurements that models have not yet been tested on. The scores on this novel data inform us about how well model rankings and specifically CORnet-S performance generalize to new benchmarks. Altogether, we propose that evaluating  and tracking model-benchmark correspondences through a Brain-Score can be used to guide machine network evolution, and machine networks as mechanistic hypotheses of the brain’s network can drive next experiments. To facilitate both of these, we release Brain-Score.org: a platform that hosts the neural and behavioral benchmarks, where ANN scan be submitted to receive a Brain-Score, and where new experimental data can be naturally incorporated.