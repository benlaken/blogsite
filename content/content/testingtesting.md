Title: Discovering the importance of automated code testing
Date: 2016-06-17 09:27
Category: Post
Slug: testing_code
Tags: automated testing, Python, code
Author: Benjamin Laken
Summary: Discovering the importance of code testing

Regression testing, unit tests, Test driven development, automated
testing, defensive programming. Despite years in research, these were
not terms I had heard, not from my supervisors or peers, nor at
conferences, and certainly not in journals or other scientific forums.
Yet after working for a few months in [UCL's
RITS](http://www.ucl.ac.uk/research-it-services) [Research Software
Development
team](http://www.ucl.ac.uk/research-it-services/about/research-software-development),
a group that emphasises software development to improve Science, I have
woken up to the reality that software developers have known for a long
time:

*"Code without tests is broken by design"* - [Jacob
Kaplan-Moss](https://jacobian.org)

Does this mean that all the scientific code written by myself and the
hundreds of thousands of other researchers globally that more-or-less
ignores testing is useless? Not at all. It does means that the code
might not be robust, may be unable to deal with edge cases, and may
(probably) hide bugs.

If you have ever tried to re-use a script written to produce data for a
specific publication, you will already know that it can take some work
to get it to run in a different environment or on different data. But
without tests there is know way to even know if the code works the way
in which the original authors intended it to.

For anyone interested in getting started with testing (it's never too
late), check out the course material from UCL's [MPHYG001: Research
software Engineering with
Python](http://development.rc.ucl.ac.uk/training/engineering/), by the
RSD team leader [Dr. James
Heatherington](https://iris.ucl.ac.uk/iris/browse/profile?upi=JHETH53).
There is also nice material from the [Test and Code
podcast](http://pythontesting.net/test-podcast/) by [Brian
Okken](https://twitter.com/brianokken), including a useful ebook. He can
also be heard discussing testing on the excellent [Talk Python to
Me](https://twitter.com/talkpython) podcast [Episode
\#45](https://talkpython.fm/episodes/show/45/the-python-testing-column-now-a-thing).

After my quick education in testing I would say that intentionally
writing code without tests is equivalent actively trying to ignore
problems. In a purely software development context this would simply be
passing on a [technical
debt](https://en.wikipedia.org/wiki/Technical_debt). In the context of
Science however, the negative impacts will land on you much more
directly. As it's your personal reputation that rests on the credibility
of your work. So start testing!

Banner photo credit [James
Clarke](https://www.flickr.com/photos/jc/2824253273/in/photolist-4FGR4v-5iz36X-8G1uXV-7w2Qiv-o5zxto-9AwFd3-3cpzbd-9AtL4n-48zoQq-9AwFjj-D3Ggt-DmzuR-pSfzW-xwTA7-7vnuo-pScys-zPTaq-7qd5hz-r7MxJ-qMjh4-a4wyn-r7MxK-zPRkT-pScyx-pScyw-unfhM-pScyu-pScyv-pScyt).
