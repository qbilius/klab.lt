---
title: Building temporal convolutional neural networks: How predictability and parsimony can help each other
authors: Jonas Kubilius, Kohitij Kar, Daniel L. K. Yamins, James J. DiCarlo
conference: ICON
date: 2017-08-08 15:00
categories: Talks
location: Amsterdam (The Netherlands)
duration: 30 min
links:
    url: http://www.icon2017.org/program.html
    slides: slides.html
datestamp: 2017-08-04 08:25:36
---

In the recent years, feedforward deep neural networks have surpassed other classes of models in predicting neural responses in the primate inferior temporal (IT) cortex (Yamins et al., 2014) and in providing response patterns consistent with primate behavior in several object judgment tasks (e.g, Kubilius et al., 2016). However, despite a strong promise for bringing better predictive models for many phenomena in cognitive sciences, deep nets remain poorly adopted by cognitive researchers. A common argument against using them is that deep nets are too complex and do not provide an adequate understanding of the processes occurring in the system. In this talk, I will argue that predictability and understanding, or perhaps more concretely, the parsimony of the models that we build are not necessarily inconsistent goals and can in fact enhance each other. To illustrate this idea, I will describe how investigating the performance patterns of object identification in deep nets in our recent work lead to the predictions of response decoding latencies in the monkey IT cortex. Specifically, we observed that the images that deep nets found hard to identify lead to the longer response decoding latencies in the IT cortex, presumably reflecting the lack of recurrent connections in these feedforward architectures. Next, I will demonstrate how we used these empirical observations to inform and constrain new classes of models. I will discuss how we built a general-purpose temporal convolutional neural network architecture that can be defined for any network topology, including within-layer recurrence, feedback and bypass connections. Such a multi-pathway architecture and its time-varying outputs, while built out of the needs of a particular task, also provide a more plausible model of the visual system, opening a possibility for investigating dynamic processes in machines and primates using deep architectures.