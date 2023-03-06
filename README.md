# Sarker lab website

This website is built with [Jekyll](https://jekyllrb.com/).
It is derived from the template at [ericdaat/research-lab-website](https://github.com/ericdaat/research-lab-website), originally provided by the
[Allan Lab](https://www.allanlab.org/aboutwebsite.html), at Leiden University.

## How the website is hosted
The website is not using Github Pages, and we use `Netlify` to host the website.
The `Netlify` service keeps monitoring the main branch. If there is any change, it will trigger the `Netlify` service to rebuild the website.
Similarly to Github Pages, the `Netlify` service gives a default domain name to the website like `xxxnetlify.com`.
We maps the default address to our website domain name `sarkerlab.org` via `Wordpress`, which is the domain provider.
The overall workflow is as below:
![flow](_src/images/other/flow.png)

## Directory structure
In general, the root folder `./` stores the html files and resources that the website literally runs on.
In other words, if the files in the root folder are updated, the website will be updated accordingly.
However, you should not directly change the files in the root foler. Instead, you should update the files in the `_src` folder where the files will be compiled and be synced to the root folder.
The `_src` folder is organized as below:
```
_src
├── _data 		# no need to update
├── _includes 		# html files for some special functions like the twitter api
├── _layouts 		# html files for setting the layouts of different pages
├── _pages              # the data for team members and reseach projects
│   ├── research
│   │   └── _posts
│   └── team
│       └── _posts
├── _plugins            # no need to update
├── _sass               # no need to update
│   └── bootstrap
│       └── mixins
├── assets              # no need to update
│   └── css
├── css                 # no need to update
├── fonts               # no need to update
├── images              # all the images in the website
│   ├── dashboard
│   ├── logo
│   ├── other
│   ├── research
│   ├── slider
│   └── team
└── js                  # no need to update
```
The folders marked as `no need to update` are more related to frontend programming and should not be changed for regular updates.
The `_includes` and `_layouts` should not be changed frequently either. The only file that needs regular update is `_includes/footer.html` where the year in the footer changes every year.
Most of the time, the update only involves `_pages` and `images`. More details will be described later.


## Setup

To setup the local development environment, first you need to install Ruby and jekyll.
``` bash
brew install ruby # brew only works for Mac OS
gem install bundler jekyll
```
We are using Ruby 2.7, but it may also work for Ruby 3+.

Then, clone this repository from GitHub and install the dependencies.
Because all the source files are stored in the folder `_src`, the following commands should be executed in the `_src` folder.
``` bash
cd _src
bundle install
```

## Test the website locally

It is a good practice to test your modification locally before pushing the code to the remote branch.
Run the local web server with:

``` bash
bundle exec jekyll serve --baseurl=""
```

If the website is successfully launched, you should see the following logs in your terminal.
Enter the address `http://127.0.0.1:4000/` to the broswer to open the website.
```
 Auto-regeneration: enabled for '/Users/gyt/Sarkerlab-Web-2.0'
    Server address: http://127.0.0.1:4000/
  Server running... press ctrl-c to stop.
```

## Update the website
The regular update includes updating team members, publications, and research projects.
The related files are stored in in `_src` folder and in the subfolders starting with `_`.
For example, the team member data are stored in `_src/_pages/team/_posts`.
The left of this section introduces the specific steps of updating the website.

### Add/edit a team member

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

### Add/edit research projects

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


<strong>Note for all the markdown files under `_posts` must be named following the format of `year-month-day-xxx` 
such as `2022-10-05-breast-cancer.md`. </strong>


## Troubleshooting
1.  What if the website is not updated after I pushed my changes?
There are several possible reasons that may cause this problem.
Try the following ways.
* clear the brower cache and re-launch the website;
* check the `Action` page and make sure that there is no errors in the new website code you pushed;
* check the Netlify and Wordpress service are working correctly.

2. When installing Ruby on Mac, it failed to write the Ruby directory.
* If you use Mac, you may meet the problem of failing to write the Ruby directory.
That is because Mac does not allow the user to modify its original Ruby even with a root account.
One solution is to use `conda` to create an independent dev environment for the website development.
If you can not solve the problem, try to follow the steps in this [blog](https://www.moncefbelyamani.com/how-to-install-xcode-homebrew-git-rvm-ruby-on-mac/) to re-install Ruby from scratch.


