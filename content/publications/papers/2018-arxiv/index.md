---
title: Task-driven convolutional recurrent models of the visual system
authors: Aran Nayebi*, Daniel Bear*, Jonas Kubilius*, Kohitij Kar, Surya Ganguli, David Sussillo, James J. DiCarlo, Daniel L. K. Yamins
journal: NeurIPS (poster)
year: 2018
categories: Papers
links:
    arXiv: https://arxiv.org/abs/1807.00053
    NeurIPS version: https://papers.nips.cc/paper/7775-task-driven-convolutional-recurrent-models-of-the-visual-system.pdf
    website+poster: https://neuroailab.github.io/convrnns/
    Cosyne 2018 poster: https://klab.lt/publications/posters/2018-cosyne/
    VSS 2018 talk: https://klab.lt/publications/talks/2018-vss/
datestamp: 2018-06-20 20:27:23
---

Feed-forward convolutional neural networks (CNNs) are currently state-of-the-art for object classification tasks such as ImageNet. Further, they are quantitatively accurate models of temporally-averaged responses of neurons in the primate brain's visual system. However, biological visual systems have two ubiquitous architectural features not shared with typical CNNs: local recurrence within cortical areas, and long-range feedback from downstream areas to upstream areas. Here we explored the role of recurrence in improving classification performance. We found that standard forms of recurrence (vanilla RNNs and LSTMs) do not perform well within deep CNNs on the ImageNet task. In contrast, custom cells that incorporated two structural features, bypassing and gating, were able to boost task accuracy substantially. We extended these design principles in an automated search over thousands of model architectures, which identified novel local recurrent cells and long-range feedback connections useful for object recognition. Moreover, these task-optimized ConvRNNs explained the dynamics of neural activity in the primate visual system better than feedforward networks, suggesting a role for the brain's recurrent connections in performing difficult visual behaviors.