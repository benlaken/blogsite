Title: Monsoon madness
Date: 2016-02-24 13:55
Category: Post
Slug: monsoon_mad
Tags: Journals, Open Science, Sun, Climate
Author: Benjamin Laken
Email: benlaken@gmail.com
Summary: A case of peer-review gone awry

![alt text](./theme/images/monsoon_india.png "Original image by Jorge Chan")

This story starts around 2012, when I received a request to review a
paper on solar activity and the Indian Monsoon from the journal
[Advances in Space
Research](https://en.wikipedia.org/wiki/Advances_in_Space_Research). I
have reviewed many such papers (perhaps \~20) so this was nothing
unusual. A quick read revealed some tortured data, abused statistics,
and nonsense prose. All in all a fairly typical manuscript in its field.
A version of it can be found at [ArXiv](http://arxiv.org/abs/1412.1041).
(To get some idea of why I say this is a typical paper, have a look at
Barrie Pittocks 1978 piece ["Solar Cycles and the Weather: Successful
Experiments in
Autosuggestion?"](http://link.springer.com/chapter/10.1007/978-94-009-9428-7_18?no-access=true),
although it is, unfortunately, pay-walled.)

The authors were claiming that weak and strong Indian monsoons are
related to changes in [cosmic
rays](https://en.wikipedia.org/wiki/Cosmic_ray): energetic particles
which ionize the atmosphere. (There is a good review
[here](http://onlinelibrary.wiley.com/doi/10.1029/2009RG000282/abstract)
for those interested in background regarding their possible role in
climate.) The study took rainfall data from India and split into two
samples, representing the strongest and weakest monsoons recorded. Using
composites, they examined the linear change in cosmic rays over a period
of 5 months during their samples. The linear change in cosmic rays
during the weak and strong monsoon samples were of different sign. Based
on their observation that the cosmic ray changes during weak and strong
monsoons were 1) *anti-correlated*, and 2) *showing high correlation
coefficient values*. From this, they argued that cosmic rays affect the
monsoon via clouds, and also potentially impact global climate.

Now, something key for you to know about the cosmic rays: they vary with
a roughly 11-year period, as they are modulated by the [Solar
Cycle](https://en.wikipedia.org/wiki/Solar_cycle). Unfortunately for the
authors, this means that if you extract a period of several months of
cosmic ray data from a time-series, and examine the linear trend, it
will very likely show either a decreasing or increasing tendency
depending on the phase of the Solar Cycle. If you were to randomly pick
a few periods from these data and stack them together (as the authors
did with a [composite
method](http://www.swsc-journal.org/articles/swsc/abs/2013/01/swsc130020/swsc130020.html)),
you will end up with a trend depending on where the samples were taken
from in relation to the phase of the Solar Cycle.

To simplify things, assume the cosmic rays vary like a sine wave over
11-years with no long-term trend. By looking at two small random
composite samples and examining the 5-month linear changes you more or
less have a 50:50 chance of having either an increasing or decreasing
trend. If you don't make an *a priori* assumption about what direction
the trends should be assigned to (e.g. that weak monsoons should
correspond to increasing cosmic rays and strong monsoons should
correspond to decreasing cosmic rays), and only care that the samples
are anti-correlated, your chance of getting a positive result is 50%.
However, if you argue that only one specific configuration of samples
with changes supports your argument, then the chance of randomly getting
this drops to 25%. So that more-or-less takes care of the
anti-correlation, as alone it is clearly not evidence of something
unusual here.

But were high correlation coefficients unusual in this work? Because the
long term-changes in cosmic rays are determined by the Solar Cycle, the
correlation coefficient values from samples constructed the way they
authors made them tend to be high. In fact high-values are *the most
common type of values you can obtain from sampling the data in this
manner*. (This is the core argument I present in [my
paper](http://www.swsc-journal.org/articles/swsc/abs/2016/01/swsc150064/swsc150064.html)).
The authors made no real effort to test the probability values of these
data in detail, so they did not realise this. They simply applied an
out-of-the-box statistical test, and assumed the values were meaningful.

So, after pointing out this core problem with the paper in peer review
the editor for Advances in Space Research promptly rejected the paper
and thanked me. (I feel like noting that I rarely recommend straight
rejections in my reviews, I normally go out of my way to try to give
comments that will help people make a stronger analysis. Although the
more time goes on, the more empathise with
[Sisyphus](http://www.nyu.edu/classes/keefer/hell/camus.html).)

A year or more passed, and I received the same paper again from the
[Journal of Atmospheric and Solar Terrestrial
Physics](https://en.wikipedia.org/wiki/Journal_of_Atmospheric_and_Solar-Terrestrial_Physics),
unmodified, typos and all\*\*. This is not so uncommon in small fields,
and has happened to me several times. So, I submitted my same review and
moved on thinking all would be well.

(\*\* This, and other examples, lead to my feeling that in many
instances authors are willing to put more effort into pushing articles
through journal systems than they are into the underlying science.)

Alas, despite arguments that the study was total rubbish, the editors
decided that this paper did indeed prove that the climate system has a
heart of cosmic rays and published it. (Again, If the claims of this
paper were true they would totally re-shape climate science. The editors
were happy to accept this paradigm shattering paper despite a clear
explanation of why it was total nonsense!) It didn't take too long for
the story to be repeated, e.g. on [The Hockey
Schtick](http://hockeyschtick.blogspot.no/2014/12/new-paper-suggests-cosmic-rays-may.html).
Over the course of a year, I protested heavily to the editors, and
pursued what I thought was a 'proper' recourse, publishing a direct
reply in the same journal as the original article. After a year with the
editors however, they were effectively stonewalling my efforts. I don't
want to go into the often frustrating and ridiculous details of that,
other than to say the end result was a prompt submission and acceptance
to the EDP Open Science journal [Space Weather and Space
Climate](http://www.swsc-journal.org/articles/swsc/abs/2016/01/swsc150064/swsc150064.html).

This story, which out of kindness I only subjected you to an abridged
version of, certainly taught me some hard lessons. For one, due to the
inordinate amount of time-wasted, I mostly only accept reviews from
editors/authors I personally know, to try to ensure they are genuinely
motivated and not simply looking to fill quotas, gain rewards, or
pad-CVs. I am also trying hard not to get sucked into studies that most
sane researchers could spot as junk and simply ignore. Finally, I think
more than ever that publishing papers should be seen as the start of a
process, not the end of one, and adopting reproducible Open Science
methods should be seen as crucial to research credibility.
