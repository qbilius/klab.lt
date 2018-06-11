---
title: Testing models
datestamp: 2012-09-04 09:11:01
categories: Blog
tags: gmin
---

There seems to be a problem for testing any general purpose model of vision: how should one devise a task such that it would faithfully test model’s ability to process stimuli of interest? (Thanks to [Hans](http://ppw.kuleuven.be/lbp/lbpMembers/u0029058) for pointing it out to me.) And if you fail to devise it properly, you may think you’re model is failing when it’s in fact well and sound.

This problem does not exist with human observers. For example, suppose that you want to test if your model can tell a difference between x’s and o’s. How would you explain to it that this is its task? You can tell that to a human but not a computer.

Of course, the problem is hardly new. You also cannot explain anything to a monkey, for example, yet people are able to train monkeys to do the task at hand. What happens is that monkeys somehow learn by trial and error what the experimenter wants them to do. That is a form of an unsupervised (or reinforcement) learning that happens in the brain. However, perhaps contrary to what it sounds like, such learning does not happen magically out of nowhere. There are certain learning rules hardwired to make this learning possible, such as [Oja’s rule](http://en.wikipedia.org/wiki/Oja%27s_rule) (or [Hebbian learning](http://en.wikipedia.org/wiki/Hebbian_theory) in neuroscience).

Now the problem arises not because we cannot come up with a way for a model to come up with some classification but because there are so many tasks that a general purpose model of vision must be able to come up with a correct classification for each task. Suppose we have a task not unlike one we have in [L-POST](http://gestaltrevision.be/tests/lpost_consent.php). You are presented with a screen with one stimulus at a top and three at a bottom:

<span style="text-align:center; font-weight:bold;">O</span>
<span style="text-align:center; font-weight:bold;">X T Q</span>

You’re asked to indicate which shape at the bottom matches best the one at the top. I suppose most people would choose ‘Q’. But now imagine I slightly change the stimuli:

<span style="text-align:center; font-weight:bold; color: #800000;">O</span>
<span style="text-align:center; font-weight:bold;"><span style="color: #800000;">X</span> <span style="color: #000080;">T</span> <span style="color: #003300;">Q</span></span>

I would guess most people would now go for ‘X’. But how would a model know? It should somehow take it into account that the colors of ‘O’ and ‘X’ match while ‘T’ and ‘Q’ have some other colors and it should also know that color is more important to the visual system than shape. The latter is my responsiblity and the former is not difficult to implement… except that when you think about all different tasks that are out there. This would amount to implementing basic cognitive reasoning which is first of all difficult and moreover not a part of visual cognition which I am here trying to address.

For the moment, I do not know a good answer. [Serre et al. (2007)](http://dx.doi.org/10.1073/pnas.0700622104) tune their model to their one task at hand and given that the model works, they don’t have to worry. [Fleuret et al. (2011)](http://dx.doi.org/10.1073/pnas.1109168108) show that their model is failing but then again their point is to show that the model is performing poorly. So my solution for now is to simply build in the various tasks that I need to test the model.
