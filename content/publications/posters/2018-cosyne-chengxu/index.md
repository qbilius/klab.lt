---
title: The virtual rat: Building a computational model of the rodent whisker trigeminal system
authors: Chengxu Zhuang, Nadina Zweifel, Jonas Kubilius, Mitra J. Z. Hartmann, Daniel L. K. Yamins
conference: Cosyne
location: Denver (CO, USA)
date: 2018-03-01
categories: Posters
links:
    poster: zhuang_cosyne2018_poster.pdf
    supplementary: zhuang_cosyne2018_suppl.pdf
datestamp: 2018-01-22 14:45:18
---

Rodents “see” the environment mostly through their whiskers. The exquisitely sensitive, actively-controllable whisker array receives raw sensory data in the form of mechanical signals. These signals are carried along the trigeminal pathway through a sequence of increasingly complex processing stages, from brainstem to somatosensory (“barrel”) cortex. Although many aspects of these processing stages have been characterized by a long history of experimental studies, the computational operations of the whisker-trigeminal system are poorly understood. In the present work, these computations are modelled through a goal-driven deep neural network (DNN) approach. Using a biophysically-realistic whisker array model (see companion poster, Zweifel et al., 2018), we sweep the array across a wide variety of 3D objects in highly-varying poses, angles, and speeds to generate a large dataset. Next, DNNs from several distinct architectural families are trained on this dataset to solve a shape recognition task. Each architectural family is based on a structurally-distinct hypothesis for processing in the whisker-trigeminal system. These hypotheses correspond to different ways in which spatial and temporal information can be integrated. After training, we find that reasonable performance levels on the challenging shape recognition task are only achieved by specific architectures from several families, while most networks perform poorly. Finally, we show that Representational Dissimilarity Matrices (RDMs), a tool for comparing population codes between neural systems, can separate these higher performing networks. And the data for computing RDMs is in a type that could plausibly be collected in an imaging or neurophysiological experiment. Our results are a proof-of-concept that DNN models of the whisker-trigeminal system are potentially within reach.