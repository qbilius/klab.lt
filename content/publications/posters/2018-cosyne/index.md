---
title: Convolutional recurrent neural network models of dynamics in higher visual cortex
authors: Aran Nayebi*, Jonas Kubilius*, Daniel Bear, Surya Ganguli, James J. DiCarlo, Daniel L. K. Yamins
conference: Cosyne
location: Denver (CO, USA)
date: 2018-03-01
categories: Posters
links:
    poster: nayebi-kubilius_cosyne2018_poster.pdf
    supplementary: nayebi-kubilius_cosyne2018_suppl.pdf
datestamp: 2018-01-22 14:45:23
---

Neurons in the ventral visual pathway exhibit behaviorally relevant temporal dynamics during image viewing. However, the most accurate existing computational models of this system are feedforward hierarchical convolutional neural networks (HCNNs), which capture neurons’ time-averaged responses, but do not account well for their complex temporal trajectories. Here we show that HCNNs augmented with both local and global recurrent connections are quantitatively accurate models of dynamics in higher visual cortex.

We began with a five-layer HCNN that achieved state-of-the-art predictions of temporally-averaged visual responses in macaque V4 and IT neurons. To model within-area dynamics, we replaced units in each layer with one of several local recurrent circuit motifs, including simple Recurrent Neural Networks (RNNs), Gated Recurrent Units (GRUs), and Long Short-Term Memory (LSTM) units. We also included combinations of global feedback connections, in which outputs of later convolutional layers were added to inputs of earlier layers. Using backpropagation through time, these new parameters were optimized to predict V4 and IT neural response patterns. Finally, we tested these networks’ ability to predict responses on held-out images and neurons not used for model optimization.

We found that the best network structure led to substantial improvements over the feedforward baseline, explaining close to 100% of the explainable variance in V4 neurons and above 75% in IT neurons on average across time points. This network made use of gated local recurrence, with LSTMs and GRUs proving superior to simple RNNs. Furthermore, the presence of specific global feedback connections in this network was critical for best predicting V4 neuron dynamics. In summary, we have developed a deep recurrent neural network architecture that accurately captures temporal dynamics in several ventral cortical areas, opening the door to more detailed computational study of the circuit structures underlying complex visual behaviors.