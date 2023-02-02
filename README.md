# Research lab website template

This website is built with [Jekyll](https://jekyllrb.com/).
It is derived from the template at [ericdaat/research-lab-website](https://github.com/ericdaat/research-lab-website), originally provided by the
[Allan Lab](https://www.allanlab.org/aboutwebsite.html), at Leiden University.

## Setup

``` bash
brew install ruby
gem install bundler jekyll
```

* If you use Mac, you may meet the problem of failing to write the Ruby directory.
That is because Mac does not allow the user to modify its original Ruby even with a root account.
One solution is to use `conda` to create an independent dev environment for the website development.
This way you need to run `conda install ruby` instead of `brew install ruby`.

Clone this repository, then install the dependencies.
``` bash
bundle install
```

## Run the website locally

It is a good practice to test your modification locally before pushing the code to the remote branch.
Run the local web server with:

``` bash
bundle exec jekyll serve
```

## Update the website

### Add a new member

New members are stored as markdown files under
[_pages/team/_posts](_pages/team/_posts).

Each new member `.md` file must look like this:

``` yaml
---
layout: member
category: Team-Memebers
title: Researcher Name
image: researcher.png
role: Lab Director
permalink: 'team/researcher-name'
social:
    twitter: https://twitter.com/
    linkedin: https://www.linkedin.com/
    google-scholar: https://scholar.google.fr/
    github: https://github.com/
    website:
    orcid: https://orcid.org/
    research-gate: https://www.researchgate.net/
---

Add more detials here.
```

### Add/Edit research projects

Research projects are stored as markdown files under
New members are stored as markdown files under
[_pages/research/_posts](_pages/research/_posts).
Each `.md` file must look like this:

``` yaml
---
layout: default
title: research project title
cover: image-for-the-project.png
description: a short introduction.
weight: 3
category: blog
---


Add more detials here.
```

`weight` decides the order of the articles shown at the research page.
The article with the smallest weight would be shown at the top.


<strong>Note for all the markdown files under `_posts` must be named following the format of `year-month-day-your-content` 
such as `2022-10-05-breast-cancer.md`. </strong>
