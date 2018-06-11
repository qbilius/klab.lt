---
title: Review of: Could a neuroscientist understand a microprocessor?
date: 2016-06-10
categories: Blog
tags: Reviews & Summaries
reviewof: Jonas & Kording (2016)
reviewof_link: http://biorxiv.org/content/early/2016/05/26/055624
datestamp: 2016-06-10 15:27:19
---

The motto of this website quotes Richard Feynman's famous "What I cannot create, I do not understand.", which, to be honest, I was very proud to come across until learning years later that basically everyone else knew this quote and many people shared a similar belief. So here we are, experiment by experiment gaining insights into the functioning of the brain and implicitly or explicitly reverse engineering it.

But [in their recent paper](http://biorxiv.org/content/early/2016/05/26/055624), Eric Jonas and Konrad Kording question whether neuroscientists are at all on the right track to the understanding of our brain. By applying standard neuroscience tools to a microprocessor, they demonstrate how surprisingly uninformative these techniques are. Six experiments – and yet nothing learned about the principles of a microprocessor.

The implications, if we consider these experiments a good representation of how neuroscientists approach understanding the brain, are serious in the era of big data and the general messing around doing random studies and claiming that somehow we're learning something useful about the brain.

So is the paper making a strong case against the current techniques? Upon a discussion at our journal club at DiCarlo lab, several key critical points were raised:

1. We *could* understand microprocessor if we really wanted to. We would use different tools than in neuroscience because early on we would observe much more regularity in the circuits than we see in the brain, and we also have much better-grounded theories that would drive our hypotheses and experiments. But in terms of understanding the brain, we don't even have a good idea what to look for and the brain is much more messy, so the techniques are different and do not transfer to microprocessor understanding. Perhaps a better analogy would be an [FPGA](https://en.wikipedia.org/wiki/Field-programmable_gate_array) – could we understand it at all if we knew nothing about it, even with the appropriate tools for the task?

2. But it doesn't seem that the authors even tried seriously to understand microprocessor even with the neuroscience tools at hand. None of the experiments seemed to tap into trying to understand circuits at a local level (for instance, the AND gate). Rather, the experiments were more like poking with a stick somewhere, showing some spurious effect and not trying to refine it further. In neuroscience, we wouldn't stop with a single observation and a single analysis but would continue asking how specific these observations are. Perhaps behaviors (booting games) was not the best approximation to the specificity of behaviors usually used in neuroscience. Though the authors point seems valid in the era of "let's map everything" without trying to relate to different levels of the system (e.g., functional / behavioral).

3. What does it even mean to **understand** a system? Build from scratch? Fix it? Or do we want to produce wiring diagrams shown in Figure 2? Or do we mean the functional role of various components? In other words, when Feynman says "create", what does he specifically mean? This point was not addressed in the paper, assuming instead that we know what understanding is. But if the success is not defined, how do we know if we achieved it?

4. One proxy for understanding (and that's a more general note) is how well we can **predict** system's behavior. Now a lot of people have an issue with that because they feel there is also a need for **parsimony**, that is, simpler models are better. But how do we measure this parsimony? Is a model a good one if you can predict it's behavior in your head? But not everything is reducible to simple principles. Some systems are complex. Short description length? Well, our favorite deep nets can be specified with very simple instructions yet many people claim they don't understand them. So predictability seems to be an objective measure whereas parsimony is more subjective and should come only later (after we can predict the system very well). Note though that when we talk about predictability, we mean particular instantiations of models, not just classes of models that keep expanding with new data and thus are not falsifiable ("sponge models").