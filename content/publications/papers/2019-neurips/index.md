---
title: Brain-like object recognition with high-performing shallow recurrent ANNs
authors: Jonas Kubilius*, Martin Schrimpf*, Ha Hong, Najib J. Majaj, Rishi Rajalingham, Elias B. Issa, Kohitij Kar, Pouya Bashivan, Jonathan Prescott-Roy, Kailyn Schmidt, Aran Nayebi, Daniel Bear, Daniel L. K. Yamins, James J. DiCarlo
journal: NeurIPS (oral)
year: 2019
location: Vancouver, Canada
date: 2019-12-12 10:05
duration: 15 min
categories: Papers, Talks, Posters
links:
    paper: http://papers.nips.cc/paper/9441-brain-like-object-recognition-with-high-performing-shallow-recurrent-anns
    arxiv version: https://arxiv.org/abs/1909.06161
    code + figures + slides: https://github.com/dicarlolab/neurips2019
    video: https://cbmm.mit.edu/video/brain-object-recognition-high-performing-shallow-recurrent-anns
    media: https://mcgovern.mit.edu/2020/01/15/tidying-up-deep-neural-networks/
    ECVP 2019 Symposium Talk: https://klab.lt/publications/talks/2019-ecvp/
---

Deep convolutional artificial neural networks (ANNs) are the leading class of candidate models of the mechanisms of visual processing in the primate ventral stream. While initially inspired by brain anatomy, over the past years, these ANNs have evolved from a simple eight-layer architecture in AlexNet to extremely deep and branching architectures, demonstrating increasingly better object categorization performance, yet bringing into question how brain-like they still are. In particular, typical deep models from the machine learning community are often hard to map onto the brain's anatomy due to their vast number of layers and missing biologically-important connections, such as recurrence. Here we demonstrate that better anatomical alignment to the brain and high performance on machine learning as well as neuroscience measures do not have to be in contradiction. We developed CORnet-S, a shallow ANN with four anatomically mapped areas and recurrent connectivity, guided by Brain-Score, a new large-scale composite of neural and behavioral benchmarks for quantifying the functional fidelity of models of the primate ventral visual stream. Despite being significantly shallower than most models, CORnet-S is the top model on Brain-Score and outperforms similarly compact models on ImageNet. Moreover, our extensive analyses of CORnet-S circuitry variants reveal that recurrence is the main predictive factor of both Brain-Score and ImageNet top-1 performance. Finally, we report that the temporal evolution of the CORnet-S "IT" neural population resembles the actual monkey IT population dynamics. Taken together, these results establish CORnet-S, a compact, recurrent ANN, as the current best model of the primate ventral visual stream.