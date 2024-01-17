# Sarker lab website
**The README file is out of date. It will be updated soon.**

This website is built with [Jekyll](https://jekyllrb.com/).
It is derived from the template at [/greenelab/lab-website-template](https://github.com/greenelab/lab-website-template) originally provided by the [Greene Lab](https://greenelab.com/).


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
├── _data 		# contains projects,yaml, types.yaml and sources.yaml
├── _includes 		# html files for some special functions 
├── _layouts 		# html files for setting the layouts of different pages
├── _members              # the data for team members 
│── _posts #conatins research page posts
│   
├── _plugins            # no need to update
├── _scripts             # no need to update
│ 
├── _styles            # no need to update
│   └── css
├── dbsubpages    # contains dashboard pages
├── images              # all the images in the website
│   ├── dashboard
│   ├── other
│   ├── research
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

Then, clone this repository from GitHub and install the dependencies and run
``` bash
bundle install
```

## Test the website locally
It is a good practice to test your modification locally before pushing the code to the remote branch.
Run the local web server with:
``` bash
 bundle exec jekyll serve 
```

If the website is successfully launched, you should see the following logs in your terminal.
Enter the address `http://127.0.0.1:4000/` to the broswer to open the website.
```
  Server address: http://127.0.0.1:4000/
  Server running... press ctrl-c to stop.
```
The server address can be different from the example.

## Update the website
The regular update includes updating team members, publications, and research projects. The resources related to each part is listed below:
* team members: `_memebers`, `images/team`
* publications: `_data`
* research projects: `_posts`, `images/research`


### Add/edit a team member
To add or remove a team member, create or delete a Markdown file in `_members`.
Each file will automatically generate its own page according to its filename. For example, a file with the name tim-smith.md will generate a page at /members/tim-smith.
After adding members, you can display them on the site by editing .md file.

Each new member `.md` file must look like this:
``` yaml
---
name: Abeed Sarker
image: images/team/some-image.jpg
role: member
description: Principal Investigator
links:
 email: tim-member@email.com
 twitter: tims_twitter
---

Add more details here.
```
Parameter details:
+ name - Name of member
+ image - Link to image of member
+ role - member/collaborator/alumni
+ description - The member's job on the team (Ph.D. student, Software Engineer, etc.)
+ links - Social media links, don’t put the whole url, just their username
Check types.yaml in `_data` to see which social media links are available

### Add/edit research projects
To add or remove a research post, create or delete a Markdown file in `_posts`.
The filename should be in the format YYYY-MM-DD-your-post-title.md, which Jekyll uses for the post's URL and date. Each file will automatically generate its own page based on its filename.

Each `.md` file must look like this:

``` yaml
---
title: PM Abuse
image:  images/team/some-image.jpg
tags:
  - biology
  - big data
  - medicine
---
Add more details here.
```
To edit the date of the last modification, change the date of .md file.
<strong>Note for all the markdown files under `_posts` must be named following the format of `year-month-day-xxx` 
such as `2022-10-05-breast-cancer.md`. </strong>

### Add/edit Publications
To create a paper go to `_data`. Use one of the source files to add a paper. For example, to add a publication in 2020, you would add it to the sources-2020.yaml file. If a file for the year you are looking for does not exist, create one with this naming convention: sources-year.yaml. Once you have added the publication to the sources file as shown below, make sure to add that exact same publication to citations.yaml as well

Each publication must look like this:
``` yaml
- id: ‘Towards Real-Time Opioid Abuse Surveillance: Machine Learning for Automatic Characterization of Opioid-Related Tweets’
title: 'Towards Real-Time Opioid Abuse Surveillance :Machine Learning for Automatic Characterization of Opioid-Related Tweets'
authors:
- Abeed Sarker
- Graciela Gonzalez-Hernandez
- Francis DeRoos
- Jeanmarie Perrone
description: 'A Sarker, G Gonzalez-Hernandez, F DeRoos, J Perrone. Towards Real-Time Opioid Abuse Surveillance: Machine Learning for Automatic Characterization of Opioid-Related Tweets. Proceedings of the 39th International Congress of the European Association of Poisons Centres and Clinical Toxicologists (EAPCCT). 2019. Naples, Italy.'
date: 'May 2019'
link: https://link.springer.com/article/10.1007/s13181-019-00699-x
```

Parameter details:
+ id - Name of the paper, basically a unique identifier for each paper
+ title - the name of the paper
+ authors - each author must have a bullet point, no comma
+ description - citation
+ date - published date, format: name of month, and year
+ links - link to paper
  

### Add/edit a Dashboard page
individual dasboards can be found under dbsubpages.
To add a new dashboard:
1. Create a .md file under dbsubpages
  ``` yaml
---
layout: dashboardsubpage
title: Overview: United States
permalink: /overview-US/
---


add dashboard here
```
2. Add that page to projects.yaml, located in _data folder.
``` yaml
- title: "Overview: United States"
group: Non-Medical Usage of PM
image: images/dashboard/overview-us.png
link: /overview-US/
```
3. Add that page to drop-down menu by adding it to dashboarddropdown.html in _includes folder.



## Troubleshooting
1.  What if the website is not updated after I pushed my changes?
There are several possible reasons that may cause this problem.
Try the following ways.
* clear the brower cache and re-launch the website;
* check the `Action` page on this Github repository and make sure that there is no errors in the new website code you pushed;
* check if the Netlify and Wordpress service are working correctly.

2. When installing Ruby on Mac, it failed to write the Ruby directory.
* If you use Mac, you may meet the problem of failing to write the Ruby directory.
That is because Mac does not allow the user to modify its original Ruby even with a root account.
One solution is to use `conda` to create an independent dev environment for the website development.
If you can not solve the problem, try to follow the steps in this [blog](https://www.moncefbelyamani.com/how-to-install-xcode-homebrew-git-rvm-ruby-on-mac/) to re-install Ruby from scratch.


