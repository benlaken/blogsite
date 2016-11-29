Title: Trust me, I'm a doctor
Date: 2016-09-30 14:23
Category: Post
Slug: Trust_me
Tags: Reproducibility, Journals, Research, Software
Author: Benjamin Laken
Email: benlaken@gmail.com
Summary: More-often-than-not researchers expect us to take their results on faith

![](./images/lego_banner.png)

It may surprise a few people to learn that this cliché is more-or-less accurate when it comes to most modern research. More-often-than-not researchers expect us to take their results on faith.

The workflows that researchers use to produce results are now, almost without exception, based on extremely complex software -- more complex than even than the researchers themselves usually appreciate! They typically involve multiple stages of data processing, perhaps spread across several people and several computer systems, with analysis scripts written in various languages, intermediate stages of manual file manipulations, maybe even the odd spreadsheet program. The core of an analysis may often be written in a rush to meet one deadline or another. And this is usually done without documentation, tests, or version control, to ultimately produce a figure or value that makes up 'a result'. The net effect of this creates a situation ominously named the [replication crisis](https://en.wikipedia.org/wiki/Replication_crisis).

An experienced software developer friend-of-mine once remarked, when looking at a typical example of a modern research pipeline[ref] A pipeline is a colloquial way of referring to all parts of the process of
turning raw data into a final analysis[/ref], that 'it was no better than a random number generator'. The pipeline was undoubtedly of significant importance to the group that made it. But he knew that no matter if you are an unpaid PhD student, or a highly-paid developer working for Google, code has bugs. Many bugs. They are hard enough to find when you use good software development practices, but an opaque research pipeline makes debugging virtually impossible. It is pure arrogance to think that as a researcher you have perfectly functional software on what is essentially a first release, and people should just be satisfied to accept your results at face value!

Most mainstream, respectable journals now support Open Access and also highlight a commitment to reproducibility to some degree, usually by advising the authors to place their data or code in accessible databases or supplying them as supplementary materials.

In my experience, reviewers almost never attempt to verify that they can reproduce an authors result, or examine whether the steps they have taken in their analysis pipeline are flawed in some way that might compromise the papers conclusions. In fact, as a reviewer, requesting data or code in order to check the work you have been given to check is usually met with quizzical and uncertain replies -- as if neither the editors or authors know what to do next!

Typically, authors want to avoid giving code out at all costs: they tend to view such requests as an unreasonable level of scrutiny, or even a loss of intellectual property. They are also well-aware that if people care to look in detail they are likely to find the metaphorical duct-tape holding their research together. (Duct-tape, which they rationalise, they will address in the next iteration of their work.) If a reviewer does ask to see code, usually what happens next is that they are treated like a biased or unreasonable reviewer, and the authors may try to encourage the editors to favour the opinions of the other reviewers who didn't rock the boat. Even if journals state in their publication policies sentiments that 'data and code used to produce results must be made available with publication of the manuscripts', this is rarely enforced.

Consequently, readers are usually left to fend for themselves when it comes to piecing together what authors have actually done (which may be all-but un-intuitable based on the text of a paper). The only ways skeptical readers can decide whether or not to put stock in what they are reading is usually by a mix of a papers logical consistency ([see here](https://blogs.scientificamerican.com/doing-good-science/evaluating-scientific-claims-or-do-we-have-to-take-the-scientists-word-for-it/)), agreement to meta-studies, or the reputation of the authors or institutes to which they are associated.

As [Raymond Hettinger](https://twitter.com/raymondh) says:
> "There has to be a better way!"

As analysis pipelines have become increasingly complex, simply saying X result was produced with Y is not useful. It is well understood that more information is needed, such as metadata about the researchers systems, library versions, automated workflows or makefiles. Many professions, including software developers, have reached the understanding that reproducing peoples results is a difficult problem. (Hence the enormous popularity of systems such as Docker and Vagrant.)

A difficult reality is that while most researchers are able to cobble together steps to go from raw data to a result, they are not able to do so in anything close to a reproducible manner -- this is important if they want to use their analysis as evidence to affect society! There are two options to address this:

*1. Improve the training and awareness of researchers, and enforce practices that allow for reproducibility.*

There are now many resources encouraging researchers to [publish their code](http://www.nature.com/news/2010/101013/full/467753a.html) or showing them how to adopt [better tools for reproducibility](http://www.nature.com/news/interactive-notebooks-sharing-the-code-1.16261). Training is being encouraged by non-profit groups such as [Software Carpentry](http://software-carpentry.org) and [Data Carpentry](http://www.datacarpentry.org), driving increased awareness is spreading across disciplines. However, it is not spreading evenly, leading almost to a two-tier system of 1) researchers who are updating their methods and attempting to work with best practices, vs. 2) old-school researchers, who stalwartly stick to old methods, and in turn pass those practices to their students (see my last blog post for more on this). Hopefully at some point a critical mass will be achieved, and the minority of hold-outs who refuse to support the reproducibility of their work will be ostracised. (Happy thoughts.)

*2. Create a specialist position, such as [Research Software Engineers](http://www.rse.ac.uk/who.html), and organisations such as the [Software Sustainability Institute](https://www.software.ac.uk),  whose purpose    
is to work with researchers, bringing their expertise in creating research software to domain specific problems as needed.*

For this, universities must essentially create a new class of position; one enticing enough to attract and retain talented people that understand both how research works, and also have a good grasp of software development.

In the meantime, we are in a state where you have no good option to determine the reliability of published results, short of spending an inordinate amount of time as a scientific Sherlock Holmes; painstakingly piecing together an analysis from a few public datasets and some lonely clues.

Banner image credit [Kevin spacebarpark](https://www.flickr.com/photos/spacebarpark/)
