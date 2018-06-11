---
title: Why model?
datestamp: 2013-03-22 09:52:06
categories: Blog
tags: gmin
---

My road to modeling has been a long and winding one. Despite five years at the sacred geek site, MIT, a master’s degree in artificial intelligence and 15 years of programming experience, only in the recent years I started celebrating the new brave digital world, leading to strong opinions about computational approach to understanding human brain / vision as both a desirable and superior method of investigation. My arguments boil down to the following:

-   **Models formalize knowledge**
    -   *Before:* “Our results suggest a feedforward emergence of this phenomenon.”
    -   *After:* “We provide a feedforward model that can account for our results. Future research will show if it holds for other phenomena or needs to be appended.”
    -   *Advantages:* You “are forced to specify all parts of [your] theory” ([Farrell & Lewandowsky, 2010](http://dx.doi.org/10.1177/0963721410386677))
-   **Models enable reproducibility **and accumulation of knowledge****
    -   *Before:* Verbal descriptions of what has been done. The picture of the whole gradually forms by reading a lot.
    -   *After:* A single model or a couple of competing models with the current knowledge built in.
    -   *Advantages:* Past results can be easily reproduced and new results / ideas build on them without breaking the model (similar to the concept of unit testing in computer science). Evolution of scientific thought comes by default with version control systems.
-   **Models reduce the amount of trivial experiments and incorrect reasoning**
    -   *Before:* Find an effect and claim it is novel because you do not see how current knowledge could explain it.
    -   *After:* Run model simulation on your hypothesis because maybe it can already account for it – models might have complex behavior. (Note that doing simulations using trivial models, e.g., pixel-wise or Gabor Jet similarity, is not nearly as informative even though popular in vision research.)
    -   *Advantages:* You do not suffer from your cognitive limitations (confirmation bias, limited capacity of working memory, incorrect / incomplete analogies etc; see [Farrell & Lewandowsky, 2010](http://dx.doi.org/10.1177/0963721410386677))
-   **Models drive hypotheses:**
    -   *Before:* (Contour) closure seems to drive [the configural superiority effect](http://klab.lt/2011/09/20/confsup/ "Emergence of perceptual Gestalts in the human visual cortex: The case of the configural superiority effect").
    -   *After:* Is it closure or is it convexity? Do we perceive a contour or a shape (surface)?
    -   *Advantages: *You think before you do (or “don’t go to fishing expeditions” – the philosophy of my former advisor [Danny Dilks](http://www.psychology.emory.edu/cognition/dilks/index.html)).
-   **Models can be employed for multiple purposes, including applications. Opinions cannot.**

## So why don’t we all make models?

-   **Poor background in modeling / stronger skills in something else and little interest in changing.** Well, that’s *your* problem:) [Udacity](https://www.udacity.com/) can help you to obtain the required background but the true change comes with your conviction that modeling is a better approach. As for me, I strongly believe in the emerging importance of technology. The future will inevitably combine the physical and the digital worlds, and I want to be in the front lines of this trend. [I also hate cooking.](http://klab.lt/2012/10/06/just-why-are-machines-so-stupid/ "Just why are machines so stupid?")
-   **We don’t know enough yet.** The argument goes that we don’t really have a good picture of how brain works so when modeling we’ll have to make choices (i.e., guess) how a particular process is implemented (view shared by [Frank Jäkel](http://cogsci.uni-osnabrueck.de/en/lectures?mode=pubs&type=o3_staff&sid=6325) and [Lee de-Wit](https://perswww.kuleuven.be/~u0064325/)). I agree with the argument but maintain that brain research and modeling are reciprocal activities: empirical research help models and models inform what questions need to be answered. While the empirical part is very much well and alive, where is the modeling part in vision sciences? You think we are beyond HMAX yet? I’m afraid for the most part we’re stuck with dumb models that do not help much.
