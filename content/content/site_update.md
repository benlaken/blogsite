Title: Pelican + Github = A better way to website!
Date: 2017-01-02 15:52
Category: Post
Slug: New_static_site
Tags: Python
Author: Benjamin Laken
Email: benlaken@gmail.com
Summary: A note on my new website, using Pelican, Travis, and Github

![](./images/pelican_banner.png)

As the astute recurring visitor may have noticed, I have a new site! I have been told that it doesn't look as impressive as my old one just yet. But I assure you that the new site is certainly forward progress,as it will be much easier for me to maintain and develop in the future.

Since around 2010, I hosted my website with Dreamhost, and made it using [Django](https://en.wikipedia.org/wiki/Django_(web_framework) and SQL.
While it was fun to have a reason to play with those tools, it was definitely overkill for my needs, and publishing new content was harder than it needed to be. Not to mention I never quite managed to find time to debug the site fully, or keep it's code it up-to-date.

Fortunately, those days are now over thanks to Github, [Pelican](https://github.com/getpelican/pelican/), and [Travis](https://travis-ci.org)! My new site is static, generated using Pelican, with [Jninja2](http://jinja.pocoo.org) templates. The posts are all written in markdown, and creating new content is now as easy as typing out a quick plain-text doc, pushing it to the [blogs Github repo](https://github.com/benlaken/blogsite), and then letting Travis do the work of automatically pulling the repo, building the site, and pushing the actual web pages to gh-pages branch on Github, where they are served with my old top-level domain!

All this means the site is much simpler, cheaper, and more lightweight, and, more importantly, I should be able to focus much more on content. Horray!  

If you want to see a guide of how to do this for yourself, I found a few, such as [this one](https://marpat.github.io/python-anaconda-and-pelican-on-windows.html). You can also grab a copy of my repo, and play with it. Feel free to use the template, a forked version of the [Pure theme](https://github.com/benlaken/pure) and adapted. If you are looking for an even easier solution you can also do the same thing using the [Jekyll](https://jekyllrb.com/docs/github-pages/), but personally I wanted a Python-based solution.

One complication of this set up is that you have to give Travis an ssh key to push to your repo, so this requires you to set up Travis deploy key, but it is straightforward ([details here](https://docs.travis-ci.com/user/private-dependencies/)).

A nice feature has been Pelican's plugins, which are easy to use. I simply added the plugin repo as a submodule to my blogsite, then declare which one I want to use in the settings file, and
viola: simple YouTube embedding, Tag-clouds, footnotes, formatted code with syntax highlighting, and loads of other nice features to play with!
