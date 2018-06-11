---
title: Doing Science in the Open
categories: Blog
tags: Open Science
datestamp: 2011-10-04 12:41:49
slides: slides.pptx
---

Motivation
==========

Being a scientist brings not only fun to investigate things you care about, freedom, and a decent salary. There are also some *responsibilities*. Money poured into research comes from the public and ends up in the pockets of private publishers that are highly profitable (think *[Elsevier](http://en.wikipedia.org/wiki/Elsevier#Criticism_and_controversies)*) and limit who can access the findings. Why so? Shouldn’t we be the first ones to make science available: anywhere, anytime, for everybody?

This principle comprises *Open Science*. In this post, I argue that there is a lack of sharing, collaboration, and openness in science, and to support my claim, I will go over the typical scientific workflow, analyze current problems and propose ways to improve. Some of my suggestions are not ready for their prime time yet; however, a number of them can successfully be implemented today to the benefit of many.

Such openness and sharing is heavily inspired by [Michael Nielsen](http://michaelnielsen.org/blog/the-future-of-science-2/) who has recently published a book *[Reinventing Discovery: The New Era of Networked Science](http://michaelnielsen.org/blog/reinventing-discovery)* where such problems are discussed in detail. My goal is rather to provide practical solutions for scientists working in vision research (but hopefully useful for others too).

Our research habits
===================

**Come up with an experiment.** *You need to read journals to get inspired / replicate findings. What if you can’t access some of them? What if your institution is poor? What if you’re just a curious high school student?*

These questions raise the fundamental flaws in our current way of doing science. The next steps will help to answer them.

**Write code to run it (MATLAB, E-Prime).** *What if you want to reuse somebody’s code? How do you obtain it? Will it work on your machine? What if you don’t have the software?  Because it is expensive – MATLAB: € 360 / year (?);  E-Prime: \$ 795 / \$ 995,  and, oh,  Windows: € 200 / € 309 / € 319.*

While this reasoning might sound unimpressive – after all, who doesn’t have *MATLAB* these days? – there are examples of situations where it did become a problem. Zdenek Kalal from the University of Surrey (UK), for example, has developed an impressive computer model for object tracking, known as *[Predator](http://info.ee.surrey.ac.uk/Personal/Z.Kalal/tld.html)*. It received lots of media attention and thus kids all over the world got interested in trying it on their own. Kalal released the source code (as Open TLD) which was written in *MATLAB*. The third comment (!) in the [discussion group](http://groups.google.com/group/opentld/) already mentions porting it to C/C++, and the fourth complains about not having MATLAB to test it out. And thus, the coming months were spent by the community porting it to C++ rather than playing around and making the use of it.

Why C++ now? Because it is a *[free and open source software (FOSS)](http://en.wikipedia.org/wiki/Free_and_open_source_software)*. If you use free and open source solutions, you can rest assured that everybody can use your code – and, crucially, for free.

For our particular needs, we can code experiments in [Python](http://www.python.org/). It is [user-friendly](http://xkcd.com/353/), [fast](http://lbolla.info/blog/2007/04/11/numerical-computing-matlab-vs-pythonnumpyweave/), has psychophysics packages ([PsychoPy](http://www.psychopy.org/), [Vision Egg](http://www.visionegg.org/)) and even point-and-click interfaces (PsychoPy, [OpenSesame](http://www.cogsci.nl/software/opensesame)). Due to its huge popularity, *Python* is also extremely versatile:

-   got some C/C++ code? use [Cython](http://cython.org/)
-   want to go online? use [Pyjamas](http://pyjs.org/), [Sculpt](http://www.sculpt.org/)
-   need parallel computing? use [IPython](http://ipython.org/)
-   need more? somebody has probably done that already!

Furthermore, [Open-Source MATLAB-to-Python Compiler](http://ompc.juricap.com/) has made it simple to move your existing scripts to *MATLAB*.

But there is no need to limit yourself to just a FOSS programing language. In fact, all necessary tools for research (described in this post) are conveniently packaged in a FOSS operating system [NeuroDebian](http://neuro.debian.net/), maintained actively by Hanke/Halchenko’s team in [Jim Haxby’s group](http://haxbylab.dartmouth.edu).

**Collect data.** *Where do you get enough participants? Oh, and that’s expensive too!*

The internet is a great resource for large numbers of cheap participants. A number of experiments that do not require specific conditions or equipment can be partly or fully conducted online.  As mentioned in the previous section, Python can in principle be used to program such online experiments, though it is not straightforward at the moment.

But there is more. Why not make your experiments run *in a browser*, regardless whether or not you will be running them online? When you publish your findings, people will be able to do your experiment for real – and, as a result, get a better feeling of what it was like. Maybe they would unveil some problems with your design? Or maybe have great ideas how to improve or use it for a follow-up? In any case, experiencing the experiment first hand is much more informative than its descriptions in a paper.

Finally, if you decide to go online, make your experiments fun! You will not only attract more participants or get away by not even paying them. Making experiments game-like can really help to crack difficult problems. For example, [foldit](http://fold.it/) gaming platform announced having [resolved a crystal structure of an AIDS-related protein](http://dx.doi.org/10.1038/nsmb.2119) which has been bothering scientists for some 15 years – and all of that in 10 days, and all purely due to gamers.

**Analyze data (MATLAB, Excel, SPSS).** *How much time do you spend analyzing it manually? Programming trivial things?*

First of all, doing it manually on *Excel* is likely not efficient nor error-prone.

Now, if you write some code to analyze your data, [publish your computer code: it is good ](http://dx.doi.org/10.1038/467753a)[enough](http://dx.doi.org/10.1038/467753a) – even if you are not good at programming and don’t comment your code. It will definitely benefit people who are trying to replicate your analyses for their data.

You can also help yourself and others by organizing your code using [distributed version control systems](http://en.wikipedia.org/wiki/Distributed_revision_control) like [git](http://en.wikipedia.org/wiki/Git_(software)) or [mercurial](http://en.wikipedia.org/wiki/Mercurial). They allow you to track changes you make while coding (and always rewind back if you need!), while forcing you to comment your changes. Another important feature is seamless merging of various versions in your code. A standard situation where this is useful is when you code both at home and at work. Instead of carrying files back and forth and thinking what needs to be updated and what not, you simply submit your code to the online distributed version control system and retrieve it on another computer that you use. The systems merges changes automatically, you don’t have to thing much. Bonus: your code is online, available for an easy sharing.

In order to learn how to use these tools, [Software Carpentry](http://software-carpentry.org/) is an excellent resource.

*How much do you pay for your analysis software? MS Office: € 139 (student) / € 379.01 / € 699 (pro), SPSS: € 25 (student/year) / € 360*

You should first ask yourself what kinds of analyses you tipically do. If all you care about is a t-test, linear regression, and a correlation, then it may be more convenient to do it in *Python* already. For more advanced statistical tests, use [R](http://www.r-project.org/).

For fMRI analyses, there is [NiPy](http://nipy.sourceforge.net/) for Python users and [AFNI](http://afni.nimh.nih.gov/) and [FSL](http://www.fmrib.ox.ac.uk/fsl/) for everybody. For multi-voxel pattern analyses, you can use [PyMVPA](http://pymvpa.org/) or [LIBSVM](http://www.csie.ntu.edu.tw/~cjlin/libsvm/). Bottom line is that these tools are powerful enough to offer you one-line solutions to most of your analysis needs (e.g., search light).

**Present data at a conference (Powerpoint, Illustrator).** *Will you ever see anybody’s slides/poster again?*

For an immediate dissemination, use [QR codes](http://en.wikipedia.org/wiki/QR_code) (using, for examples, this [QR code generator)](http://zxing.appspot.com/) which can be easily put on your slides or posters and scanned by a smartphone/tablet.

Another simple solution is to put them on your lab’s website (in our lab, we even have a dedicated website called [Gestalt Revision](http://gestaltrevision.be/)).

Or how about [your own website](https://neuromokslai.wordpress.com/)? If you think it’s difficult to implement and you don’t have a clue of where to start with HTML, you’re *so* 2000s. Nowadays personal websites are known as blogs and are trivial to set up and to even look like a proper (ugly) lab website, as does mine. Check out [Wordpress](http://wordpress.com)or [Blogger](http://www.blogger.com) for the most popular solutions. As a bonus, having your own website allows you to know who cares about your stuff because most blogs keep track of user statistics.

Finally, why use *Powerpoint *to make your slides/poster? [Scribus](http://www.scribus.net/), [Inkscape](http://inkscape.org/), or [Beamer](http://en.wikipedia.org/wiki/Beamer_(LaTeX)) are all decent FOSS solutions.

**Write a paper (MS Word).** *Ever got lost among all different versions of your paper?*

When a number of authors collaborate on a paper, inevitably a number of different manuscript versions get emailed and start accumulating on your hard drive. This can easily turn into a mess and also must be organized in a serial fashion (first me, then my prof, then another prof, then me…) in order not to get lost across all the changes. Instead, [Google Docs](https://docs.google.com/) offers an online version of a word processor where you can revise, comment, see everybody’s changes and always go back to an earlier version. Thus, there is a single “master” copy that everybody can work on. Furthermore, it lives online, so you can access it anywhere.

*Hate formatting?*

A *Word* document is not a professionally looking journal article, unless you put a substantial amount of effort. If you care about generating papers that are well-structured and good-looking, [LaTeX](http://www.latex-project.org/) is the strongest (and FOSS) alternative. *LaTeX* is widely used in hard science and by publishers as it makes writing equations a snap. While writing text in *LaTeX* is not as straightforward as in Word (it’s not [WYSISYG](http://en.wikipedia.org/wiki/WYSIWYG)), [LyX](http://www.lyx.org) comes close. There are also online implementations of *LaTeX* for collaboration, for example, [ScribTeX](http://www.scribtex.com/).

**Submit it to a journal.** *How much time do you spend preparing your manuscript for submission? Figuring out journal’s particular requirements? Redoing all of that for another journal? How much do you pay for submission/publishing? For example, [Journal of Vision](http://www.journalofvision.org/site/misc/terms_conditions.xhtml): \$ 85 per page (\$ 510 for 6 pages),  [The Journal of Neuroscience](http://www.jneurosci.org/site/misc/ifa_charges.xhtml): \$ 950 / \$ 475 (brief), [PLoS One](http://www.plos.org/journals/pubfees.php): \$ 1350, Psychological Science: \$ 0.*

If high fees bother you, ask why do we need journals at all? What do they do for us? Some copy-editing, text-formating and putting that on paper (which is, arguably, a waste) and we pay exorbitant fees for that? Also, don’t forget that libraries across the world are paying to access the journals, so the publishers benefit that way too (thus a \$0 price tag on *Psychological Science*). Surely, some use the money to simply remain in business (although again, where does \$1350 go to in *PLoS One*?). But many are only concerned about their profits – because it’s a business, after all.

In this light, [arXiv](http://arxiv.org/) seems to me like a much more liberal publishing platform. Anybody can publish there, formatting is done by LaTeX (as *arXiv* focuses on hard science), no fees involved. This platform is highly popular in hard science and, in some cases, even the best publications on *arXiv* never end up in regular journals because *arXiv* is just good enough. A note of caution: some journals tend to treat publishing on *arXiv* as a proper publication and subsequently will not consider your manuscript for publication in their journal anymore.

Of course, arguably the most important publishers contribution comes from managing the peer-review system. They oversee its proper implementation and that is important. Surely, there are other ways to go about it and some ideas are presented at the next point.

**Get reviews\*.** *Stupid reviewers and unreasonable requests? 3 major revisions? How many years does it take from obtaining results to publishing them?*

**\*negative**

This is a very broad topic which I am not very familiar with, but it seems to me that publishing peer review along with the publication without any names attached could go a long way already. Some people, like [Nikolaus Kriegeskorte](http://futureofscipub.wordpress.com/), are arguing for an *Open access + Open post-publication peer review* model. Simply put, you publish on something like arXiv and people freely read it, comment on it and rate the paper. The best one could even be picked up by regular journals and published there. To make sure constructive feedback is given, real names could be used, people could gain or lose points according to whether other people think their comments were useful or not, in a similar way that forums are organized.

**Revise and get paper published.** *Who can read your paper? Did you know that you did not hold the copyright to your own creative work? And what did you publish? Just some text? Where is raw data, code, analyses? Maybe you made a mistake? Maybe you cheated?*

**The answer is simple – publish everything: data, analysis workflow, code that generated your figures, full text (after the paper gets published, and put a disclaimer like [this one](http://www.rowland.org/rjf/cox/publications/) to deal with copyrights)…

**Get media coverage.** *Will they see your paper? Will anybody see your paper? And if they do, what will they find on your website? A conveniently double-spaced paper in the Times New Roman typeface?*

There is no problem if you used *Google Docs* or *LaTeX* and created your website… Everything neccessary is easily available online already.In order to facilitate laymen, consider providing a simple explanation, just like it is done on the [Gallant Lab website](https://sites.google.com/site/gallantlabucb/publications/nishimoto-et-al-2011). It is also a nice way of showing your participants where all their efforts went to.

Concluding remarks
==================

**Moving to the cloud.**

The framework provided here can be summarized as *"moving to the [cloud](http://en.wikipedia.org/wiki/Cloud_computing)!"* By maintaining everything online you:

-   no longer depend on a particular platform
-   get free backup
-   can access to everything for everyone everywhere (use [Dropbox](https://www.dropbox.com/), ~~[Wuala](http://www.wuala.com/)~~)
-   can instantly collaborate, e.g., via *GMail-GTalk-Google Docs*

**Open issues:**

-   Where do you share your data? Maybe [Dryad](http://datadryad.org/), [Dataverse Network](http://thedata.org/)
-   No facebook for scientists… Maybe [Academia.edu](http://academia.edu/), [Research Gate](http://www.researchgate.net/) will catch on
-   There aren’t mature open alternatives for everything yet, e.g., *Powerpoint*, *SPM*
-   Privacy issues when moving to the cloud
-   Requires efforts: more coding, more command line interfaces, more things to do

**What to do.**

There is a lot that can be done and that may be overwhelming. Don’t stress. Simply start by publishing full data, your code, and full text. It’ll do plenty.

See also: [slides from a presentation at a lab meeting](http://neuromokslai.files.wordpress.com/2011/10/doing_science_in_the_open1.pdf)
