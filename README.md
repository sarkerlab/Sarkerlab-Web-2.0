# Welcome to the [Sarker Lab](https://sarkerlab.org/) Website!

This document will explain how to modify the website content

The website is hosted on [Netlify](https://www.netlify.com/), please use this github account to log in.

---

# Updating the Website

Since this is a simple HTML website, you can easily download the whole project and make changes on top of it through Github.

For more information about updating: [Link](https://docs.github.com/en/github/managing-files-in-a-repository/adding-a-file-to-a-repository)

## Add New Page

For example, if you want a new url: sarkerlab.org/example.html, you can leave example.html in the root directory.

For sarkerlab.org/dir/example.html, you can create a directory and put example.html in it.

## Add Home Page, People, or Publications

Just simply copy paste and change the content.

Remember:

1. Image should save in the folder assets/img

2. 4 people in one row for people page

3. Publication font can be change and found at: [link](https://fontawesome.com/)

## Add Blog Page

In the folder blogs, there is a template html called "sample_blog.html" that you can modify and add as a new page.

All content should be added between

```html
<div class="blog-post"></div>
```

## Sample Code

### Title

```html
<h1 class="blog-post-title">Title</h1>
```

### Headding Level 1 (Subtitle)

```html
<h3 class="mt-5">Subtitle</h3>
```

### Headding Level 2 (Sub-Subtitle)

```html
<h5 class="mt-4">Sub-Subtitle</h5>
```

### Divider

```html
<hr>
```

### Time

```html
<p class="blog-post-meta text-secondary">Last Update: Dec 11, 2020</p>
```

### Text

```html
<p>
    Some Text Here    
</p>
```

### Link Example

```html
<p class="text-center">
    Center: <a class="text-secondary" target="_blank" href="https://www.google.com"><u>Google</u></a>
</p>

<p>
    Not Center: <a class="text-secondary" target="_blank" href="https://www.google.com"><u>Google</u></a>
</p>
```

### List Example

```html
<li>
    List Example Here
</li>
```
