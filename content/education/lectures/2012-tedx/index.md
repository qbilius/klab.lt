---
title: Just why are machines so stupid?
event: TEDxVilnius 2012
event_link: http://www.tedxvilnius.lt/en
date: 2012-10-06
venue: ŪB theatre arena, Vilnius (Lithuania)
venue_link: http://www.teatroarena.lt/
categories: Lectures
datestamp: 2012-10-06 18:00:37
links:
    slides: http://www.slideshare.net/qbilius/kubilius-stupid-machinestedxwithurls-15628922
    video: http://www.youtube.com/watch?v=uYgQClEfYuI
---

A young company called [*Kiva Systems*](http://www.kivasystems.com/) has solved a difficult problem. If you were in a large business of selling items online, such as *Amazon*, you’d probably have a large warehouse where you store your stuff. In order to fulfill and order, a worker would have to find an appropriate shelf, pick the item, and ship it. If you were really serious, you might stuff your warehouse with conveyor belts to speed up the process. Needless to say, this is very expensive and still not that much efficient.

So *Kiva Systems* decided to turn the whole process upside down.

Instead of workers going to the shelves, they said that shelves should come to the worker. That way, the worker just has to keeping pick the right item without wasting a moment to look for the correct shelf. This solution turned out to be so efficient that Amazon ended up acquiring *Kiva Systems* earlier this year for \$775 million *in cash*.

When a journalist from *IEEE Spectrum* visited the company in 2008, something interesting caught his attention:

> *It’s fun to watch the robots, but the human workers filling the orders are also impressive: they watch for the laser dot, pick a product, scan its bar code, throw it into a box, and start over. The humans are rather robotic themselves. I ask D’Andrea [co-founder of Kiva Sytems]: Why not automate this job too? (…) He says that because products vary so much in size and shape and because of the way they sit on shelves, robotic manipulators still can’t beat real arms and hands.*

> [“Thee Engineers, Hundreds of Robots, One Warehouse” | IEEE Spectrum](http://spectrum.ieee.org/robotics/robotics-software/three-engineers-hundreds-of-robots-one-warehouse/2)

“Robotic manipulators still can’t beat real arms and hands.” Let that sink in for a moment. We’re used to hearing that machines are awesome. They can beat people at chess! They can perform the most complex computations super fast! Some of you may even believe that machines will soon take over the world.

And yet, they appear inferior in some ridiculously easy task that none of us have any problems to do.

Why?

Well, there have been some problems in trying to create those kind of general purpose robots. Let me just focus on one of them: vision, the ability to see. You see, I’m doing a PhD on human vision. Now, many people ask me what does that mean, what do I do? I tell them that my job is to look at human brain. “Really? And what do you see there?”, they ask. Well, I don’t know about you, but what I see there is this.

<figure>
    <img alt="Brain vs Lithuania" src="img/brain_lithuania.png" />
    <figcaption style="text-align:right; width:480px; font-style:italic">Source: <a href="http://commons.wikimedia.org/wiki/File:LietuvaMiestams.png">Wikimedia Commons</a> [public domain]</figcaption>
</figure>

Alright, alright, now seriously why I work on vision. Vision is the most important of human senses. It’s so powerful and so fluent that we don’t even notice it.

<figure>
    <img alt="Cat" src="img/cat.jpg" />
    <figcaption style="text-align:right; width:480px; font-style:italic">Source: <a href="http://www.flickr.com/photos/celesterc/444784759/">Celeste</a> <a href="http://creativecommons.org/licenses/by-nc/2.0/deed.en">[CC BY-NC 2.0]</a></figcaption>
</figure>

You didn’t have to think hard whether or not there was a cat in this image, did you? No, vision is so immediate that people assume it’s a very easy task, probably just done in your eyes. So if you wanted to make a computer see, all you had to do was to attach a camera, right?

Well, I now want you to give vision its due credit.

Look at this image again. I will zoom in to just a small portion of it, the cat’s ear, so that we can see pixels.

<figure>
    <img alt="Cat ear" src="img/cat_ear.jpg" />
</figure>

Your eye, in effect, is registering the intensity of each. In other words, your eye basically receives a value from 0 to 255 representing how dark or how bright each pixel is. These numbers, they are the only information the eye receives. In effect, it receives this:

<figure>
    <img alt="Cat ear in numbers" src="img/num_color.png" />
</figure>

I have not changed the amount of information here, I merely replaced each pixel by its intensity value. But suddenly you don’t know what is before your eyes. Where’s the cat? Is there a cat? For a moment, I removed the immediacy of your vision and left you with just the information that the eye receives. You can now understand the problem of vision: how do we get from these numbers to an understanding that there is a cat behind them?

It may strike you but the fact is that nobody knows how we can see. Nobody knows what kinds of computations are required to get from these numbers to cats! And as long as nobody knows that, we can’t make machines see. Now you don’t really want a blind robot bumping its way around your house, do you?

We don’t know how to solve the problem of vision, but somebody does. Or, rather, something does. It’s your brain.

I say, let’s steal that solution!

Here is what your brain does.

<figure>
    <img alt="Ventral visual stream" src="img/visual_stream_small.png" />
    <figcaption style="text-align:right; width:480px; font-style:italic">After <a href="http://dx.doi.org/10.1016/j.tics.2007.06.010">DiCarlo & Cox (2007)</a> / Source: <a href="http://dx.doi.org/10.6084/m9.figshare.106794">figshare</a> <a href="http://creativecommons.org/licenses/by/3.0/">[CC BY 3.0]</a></figcaption>
</figure>

Here you see a picture of a human brain as seen from a side. Light from the outside world is registered by the eyes and then step by step processed in this hierarchy of visual areas which we call the ventral visual stream. Since we already said that the input is nothing but a bunch of numbers, processing that is performed in each of these brain regions could be understood as some mathematical transformation function, one that is aimed at gradually extracting the relevant information from this pile of numbers. The picture is much more complicated, of course, you can see feedback and recurrent loop arrows here, but I’d argue that the primary problem of vision for now is to figure out those transformation functions here.

To make it more concrete, in the primary visual cortex, denoted here as V1, the computation is roughly that of detecting edges. Each neuron in V1 is responding to a particular orientation of an edge. So, for example, a neuron that likes an oblique orientation might detect an edge here:

<figure>
    <img alt="Cat one edges" src="img/cat_edges_one.jpg" />
</figure>

And if we allow all neurons to detect their prefered orientation of an edge, we might end up having this:

<figure>
    <img alt="Cat edges" src="img/cat_edges.jpg" />
</figure>

If you keep looking at this “output” of the primary visual cortex, you may think we’re doing pretty well. This line drawing looks quite like a cat so we must be close to solving vision. But things are not that simple, unfortunately: how do you put this cat together? Just look at the pawn region here:

<figure>
    <img alt="Cat edge grouping" src="img/cat_grouping.png" />
</figure>

How do you know that only half of the horizontal edge goes together with the vertical bar, forming cat’s pawn? How do you know that these edges go together with the one at the top, forming a cat?

In my opinion, that’s the major question in vision research today. We just don’t know how to put the cat together.

But everybody and their aunt has a theory about it. For example, my colleagues and I [at KU Leuven in Belgium](http://www.gestaltrevision.be) believe that the way we put these parts together is by using some sort of rules, which are known as Gestalt laws of grouping. To illustrate what I mean, I will show you just one example which comes from the [Bio Motion Lab at Queen’s University, Canada](http://www.biomotionlab.ca), courtesy of Prof. Niko Troje.

What is depicted here?

<figure>
    <img alt="Cat edges" src="img/bmg.png" />
</figure>

Well, it’s hard to tell. But let me set it in motion… [[click here](http://www.biomotionlab.ca/Demos/BMLgender.html)] Okay, so it takes eleven dots and some motion to make you see clearly a walking human figure. That’s the power of grouping, or so called Gestalt, processes in the brain. There is only eleven dots but you could swear there is a human there. And you’re sensitive this this, oh, yes [try changing to a woman or a man]. Hey, don’t get too excited! It’s just eleven dots, mind you!

So far, I have provided you with a single example of improving machines by exploring the underpinnings of the human visual system. But really I want to make a much broader statement here. Understanding the underlying principles of human brain, understanding the principles that guide our actions will allow us to use the same principles in creating machines. And then we will be able to recognize ourselves in the patterns of behavior that these machines exhibit.

Remember Tamagotchis – those little digital pets that many of you had some years ago?

<figure>
    <img alt="Tamagotchi" src="img/tamagotchi.jpg" />
    <figcaption style="text-align:right; width:480px; font-style:italic">Source: <a href="http://commons.wikimedia.org/wiki/File:Tamagotchi_0124_ubt.jpeg">Wikimedia Commons</a> [public domain]</figcaption>
</figure>

If you don’t entertain them, they become unhappy, if you don’t feed them, they may die. Now that’s a very simple way of making machines act just a bit more like us, but people all over the world go crazy for these pets, bringing a Japanese company called Bandai a fortune!

So that’s what I’m talking about. I want people to embrace machines. I want them to trust machines. Because my goal, you see, is to transfer the most mundane, the most boring tasks to a machine.

Think of a task, any task that you perform yourself. Could a machine, in principle, do it for you? Could it do it just as well as you do it? If yes – then it has do it instead of you. I refuse to be a slave to my body’s needs.

This is the manifesto for the world I want to have.

Thank you.
