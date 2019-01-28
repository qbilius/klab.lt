---
title: Doing science in the open, 2013 edition
categories: Blog
tags: Open Science
datestamp: 2013-03-06 12:03:06
---

*(For the 2011 edition, see [Doing science in the open](http://klab.lt/2011/10/04/doing-science-in-the-open/).)*

Understanding open science
--------------------------

**Open science is about sharing** — papers, data, software, ideas… Sharing promotes replicability, transparency, knowledge accumulation, love… But it is only meaningful when **open standards** are implemented. Examples:

-   If you share your code in E-Prime, I can only use it if I own a copy of E-Prime ([\$795](http://www.pstnet.com/eprime.cfm?tabID=Pricing)). That’s not very useful.
-   If you publish a paper under a traditional license, I can read it but cannot (easily) reuse your data or figures.

**General idea — **Use tools that are as independent as possible:

-   Mature tools are preferred to beta since the developer(s) might abandon the project
-   Free and open source (F/OSS) projects are preferred to proprietary because you can trust the code, change it to your needs and it will never vanish.
-   Text files are more accessible than binary files since the latter may require proprietary software to use them.

*Note:* This is a general preference, not absolute. Your particular problem might have different requirements.

Tools
-----

*(dev)* indicates that I do not consider the tool to be mature yet. It may change (e.g., become paid or change its API), it may disappear, or better (more widely accepted) tools of the same sort may emerge soon.)*

### Open Science Framework ###

[A project](http://openscienceframework.org/) *(dev)* closely related to the [Reproducibility Project](http://openscienceframework.org/reproducibility/) (Brian Nosek and friends):

-   Organize your research (esp. important when collaborating)
-   Keep it in the cloud
-   Share it (if you want)
-   Be honest: everything gets recorded (version control), e.g., your a priori hypotheses
-   Your contributions are tracked and citable

### Licenses (my recommendations) ###

-   **Copyright (c):** all rights reserved
-   **Copyleft:** all rights reversed
    -   Permissive (anybody can use your stuff for anything they like – even sell it):
        -   Software: [BSD 3-clause](http://opensource.org/licenses/BSD-3-Clause)
        -   Else: [Creative Commons Attribution (CC BY)](http://creativecommons.org/licenses/by/3.0/); NonCommercial and NoDerivs are also possible but think whether you really need these limitations)
    -   Viral (reciprocal – anything based on your work will be of the same same license type, ensuring perpetual access to it):
        -   Software: [GNU General Public License](http://www.gnu.org/licenses/quick-guide-gplv3.html) (recommended for scientific software so that it always remains open)
        -   Else: [Creative Commons ShareAlike](http://creativecommons.org/licenses/by-sa/3.0/) (CC BY-SA; think twice…)
-   **Public domain:** no rights reserved
    -   [Creative Commons Zero (CC0)](http://creativecommons.org/about/cc0) if you need to want to put it in the public domain sooner than it would get there legally

### Google Scholar

-   [Copy-paste citations in the APA style](http://googlescholar.blogspot.be/2012/10/cite-from-search-results.html)
-   Create your own profile ([here is mine](http://scholar.google.com/citations?user=g7c_OQMAAAAJ)) where publications are automatically accumulated
-   Get notified about relevant papers: [My updates](http://googlescholar.blogspot.be/2012/08/scholar-updates-making-new-connections.html)

*Alternatives: *[ResearchGate](http://www.researchgate.net/) (and here’ how [my profile](https://www.researchgate.net/profile/Jonas_Kubilius/) looks like), [Academia.edu](http://academia.edu/), Facebook Profile / Facebook Page, [Mendeley (my profile)](http://www.mendeley.com/profiles/jonas-kubilius/)

### Reading publications

Limitations of PDFs:

-   not pleasant to read on tablets since they don’t fit on screen
-   figures are all over the place rather than next to their first mention

(You may want to try *text reflow* for converting a PDF into text on the fly as a possible solution but I’m not aware of an app that would do the job well.) But even worse is reading papers online in the HTML format :

-   not available offline
-   does not have the same “stable” feel as a PDF
-   difficult to make notes

(For a magazine-like HTML experience, try PubMed’s [PubReader](http://www.ncbi.nlm.nih.gov/pmc/about/pubreader/) on your browser.) Best solution so far is **epub** (an experimental paper format from PubMed):

-   reformats itself to fit the screen and still looks great
-   looks and feels like a book
-   note taking works just like on a PDF

Since 2008, NIH-funded scientists are [required to submit their manuscripts](http://publicaccess.nih.gov/FAQ.htm#753) and they’re published on PubMed within 12 months of the initial journal publication. Thus, epubs are already available for recent publications and appear pretty fast but, unfortunately, not instantaneously for the new ones.

### Experiments on tablets

-   iOS / Android: usual psychophysics packages won’t work
-   [Install Ubuntu](https://wiki.ubuntu.com/Nexus7) and get Python/Psychopy running ([Sebastiaan Mathôt | OpenSesame example](http://www.cogsci.nl/blog/miscellaneous/208-running-psychological-experiments-on-a-tablet-with-opensesame))

*Alternative: *online experiments (like [L-POST](http://gestaltrevision.be/tests/index.php?language=en)) which you can learn to create them [at Udacity](https://www.udacity.com/course/cs255)

### Papers

**For collaboration: [Google Drive](http://drive.google.com)**

-   Real-time updates for all users
-   Google Scholar integrated

**Writing, formatting, commenting: [LyX](http://www.lyx.org/)**

-   It’s LaTeX, so you get more robust formatting, exporting to many formats (useful for self-archiving, incl. Lirias), and F/OSS
-   Track Changes just like in MS Word
-   This blog entry was first written LyX for a lab presentation and then exported to a text format

**[IPython](http://ipython.org/) for papers**

-   Easy format for running analyzes and sharing full papers
-   LaTeX is integrated
-   [Run R using Rmagic](http://www.randalolson.com/2013/01/14/filling-in-pythons-gaps-in-statistics-packages-with-rmagic/) (via rpy2 and with pandas; see more on the [Gestalt Revision wiki](http://gestaltrevision.be/wiki/python/rpy))

    import pandas
    %load_ext rmagic
    data = pandas.read_csv("data.csv")
    # -i sends the variable to R, the rest is R code
    %R -i data print(summary(data))

-   Share notebooks on [IPython Notebook Viewer](http://nbviewer.ipython.org/)
-   Soon: work in the cloud with [wakari.io](http://wakari.io) *(dev)*

**[Open Science Paper](https://github.com/cpfaff/Open-Science-Paper) *(dev)*:**

-   Easily generate a [beautiful paper](https://github.com/cpfaff/Open-Science-Paper/blob/master/open_science_paper.pdf) with the power of LaTeX and a great template
-   Can include R code for an automatic figure generation (via Knitr)

**[PythonTeX](https://github.com/gpoore/pythontex) *(dev)***

-   LaTeX-based
-   Can include Python code for an automatic figure generation
-   [demo](https://www.youtube.com/watch?v=yIO4l0zHGjw)<span style="font-size: 13px;"> </span>

If you still prefer Word documents, at least stop sending multiple versions around. [**Dropbox**](https://www.dropbox.com/) is your true friend:

-   Collaborate: Right click \> Dropbox \> Share Folder \> Browser window opens, choose your victim
-   Share (give access): Right click \> Dropbox \> Share Link… \> Browser window opens, copy the link

### Presentations ###

**Traditional: [Scribus](http://www.scribus.net/)**

-   Produces vector graphics, meaning a text-based image (svg), good for easy manipulation, perfect rescaling, and googling
-   Perfect for posters and presentations
-   Images are easy to manipulate unlike in the next two options

*Alternative:* [Inkscape](http://inkscape.org/) **LaTeX-based**: **[Beamer](https://bitbucket.org/rivanvx/beamer/wiki/Home)**

-   All advantages of LaTeX
-   Easy user interface in LyX
-   Easy export to other formats

**Browser-based (usually HTML+JS)**

-   Immediately publish online!
-   Can embed videos (youtube)
-   Prezi-like experience: impress.js

(but you may share pdfs of your presentations on [figshare](http://figshare.com/) or [slideshare](http://www.slideshare.net) ([see my own example](http://www.slideshare.net/qbilius/kubilius-stupid-machinestedxwithurls-15628922)))

### [figshare](http://figshare.com/) *(dev)* ###

-   Citable: each figure gets a DOI ([see my example](http://dx.doi.org/10.6084/m9.figshare.106794))
-   Resources available under the *[Creative Commons Attribution 3.0](http://creativecommons.org/licenses/by/3.0/)* license, so you always retain the copyright (or at least you can always use it in your other papers)
-   Also accepts posters, media, papers, and datasets (the latter under [CC0](http://creativecommons.org/publicdomain/zero/1.0/))

*Disclaimer: I am a [figshare advisor](http://figshare.com/advisors)* *Alternative: *Your own website with copyright information (use [CC BY](http://creativecommons.org/licenses/by/3.0/))

### Keeping file history ###

-   **For text-based files:** use version control systems (*git*, *hg*) via online repositories ([github](https://github.com/), [bitbucket](https://bitbucket.org)). Notice that this is where text files win over binary.
-   **Dropbox keeps file history** (for 30 days, unlimited for Pro): Go to Dropbox online, click on the trash can to see deleted files or on the file to see its change history
