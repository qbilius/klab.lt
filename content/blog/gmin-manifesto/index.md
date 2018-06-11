---
title: GMin, a standard model of grouping principles
datestamp: 2012-05-21 00:55:18
categories: Blog
tags: gmin
---

In vision research, I see a lack of attempts to build **a unifying model of human vision**. It is not that nothing has been done. We have some really simple models like [HMAX](http://dx.doi.org/10.1038/14819), some really complex ones like [LAMINART](http://en.wikipedia.org/wiki/Stephen_Grossberg), some in between like [VisNet](http://www.oxcns.org/), and so on. They all are nice and good at the first sight yet when I ask how much we know about vision, I can hear David Marr turning in his grave.

You see, building a really good model of vision is actually a daunting task. There is a plethora of phenomena reported and you, as the architect of the model, have to accommodate all of them. There is just too much literature for one person to know! So everybody nowadays is so specialized that V1 doesn’t talk to V2 and “what” doesn’t talk to “where” (and neither talks to “vision for action” and “vision for perception”). As if there were different visions.

I, for one, only see a single percept at a time.

So I want a single model. The one that begins with asking [“What is the purpose of vision”](http://klab.lt/blog/surfaces/), is then build with that purpose in mind and choices based on available data. **Transparent, flexible, and open architecture** is a must because this is the only way to test our model’s assumptions.

When you try building a model of this kind, suddenly you research is no longer informed by “this has not been investigated before” and “this might be a nice variation of the same kind”, but rather by a practical concern that you don’t know how to build some part of your model and thus you got to go and ask some participants. No more [biases for positive results](http://dx.doi.org/10.1038/485298a) because the model either works or not. And you *know* that eventually it **will work** – because, well, *I can seez you*.

Let me be bold here. I am not interested in [solving problems that do not exist](http://tmblr.co/Z2uRRvLmqKKW) only to advance my career. I am a creator more than a researcher. The only acceptable state of existence for me is creation of things I **wholeheartedly believe** in. And thus, in the midst of my PhD, I choose to create a **standard model of grouping principles, GMin**.

GMin will be based on the following (practical) principles:

-   **Easy to understand:** main architecture written in Python, uses Numpy, OpenCV and GPU for fast computations, intuitive (phenomenologically accurate) outputs
-   **Easy to test**: runs online as a web service, pleasant HCI, free and open source ([GNU GPL 3.0](http://www.gnu.org/licenses/gpl.html)), publications released under [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/)
-   **Flexible (modular) architecture:** add/change things easily when I/we know more
-   **Easy to expand:** branch and make your own!
-   **Focus on qualitative** rather than quantitative match to human data
