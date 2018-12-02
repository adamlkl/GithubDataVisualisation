# GithubDataVisualisation

## Set up ##
You will need <a href="http://flask.pocoo.org/">Flask</a>, 
<a href="https://pygithub.readthedocs.io/en/latest/introduction.html">PyGithub</a>, 
<a href = "https://api.mongodb.com/python/current/">PyMongo</a> for this program to work.

I have removed my access token to extract json information from Github, but if you want to try it,
you can request for it at <a href="https://github.com/settings/tokens">Github Access Token Generator Page</a>

## Running ##
`python app.py`

**_However, obviously this won't work by simply cloning my repo won't work._** As mentioned you need to download the above 
tools for it.

Another alternative that I have used is utilising PyCharm to make the assignment, to avoid downloading massive libraries.
Pycharm provide convenient interpreters so you dont have to go through a lot of work to set up your working directory and 
environment.

When a remote Python interpreter is added, at first the PyCharm helpers are copied to the remote host. PyCharm helpers are 
needed to run remotely the packaging tasks, debugger, tests and other PyCharm features. Next, the skeletons for binary 
libraries are generated and copied locally. Also all the Python library sources are collected from the Python paths on a 
remote host and copied locally along with the generated skeletons. Storing skeletons and all Python library sources locally
is required for resolve and completion to work correctly. PyCharm checks remote helpers version on every remote run, so if 
you update your PyCharm version, the new helpers will be uploaded automatically and you don't need to recreate remote interpreter. 
SFTP support is required for copying helpers to the server.

Python interpreters can be configured on the following levels:

Current project: selected Python interpreter will be used for the current project.

New project: selected Python interpreter will be used for the new project instead of the default one.

More explanation can be found at <a href="https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html">here</a>.

## Assignment Explanation ##
For this assignment, I have decided to compare the size of each repository in the <a href="https://www.google.ie/search?q=loomberg+github&oq=loomberg+github&aqs=chrome..69i57j0l5.4607j0j4&sourceid=chrome&ie=UTF-8">
Bloomberg repository</a> and then the languages they have used. <br />

Tools I have used for this assignment are <a href="https://d3js.org/">d3.js</a>, 
<a href="https://dc-js.github.io/dc.js/">dc.js, dc.css</a>, and 
<a href="http://square.github.io/crossfilter/">crossfilter.js</a>

<a href="https://d3js.org/">D3.js</a>, is a JavaScript library for manipulating documents based on data. D3 helps you bring data to life using HTML, SVG, and CSS. D3’s emphasis on web standards gives you the full capabilities of modern browsers without tying yourself to a proprietary framework, combining powerful visualization components and a data-driven approach to DOM manipulation.

<a href="https://dc-js.github.io/dc.js/">Dc.js</a> is a javascript charting library with native crossfilter support, allowing highly efficient exploration on large multi-dimensional datasets (inspired by crossfilter's demo). It leverages d3 to render charts in CSS-friendly SVG format. Charts rendered using dc.js are data driven and reactive and therefore provide instant feedback to user interaction.

<a href="https://dc-js.github.io/dc.js/">Dc.js</a> is an easy yet powerful javascript library for data visualization and analysis in the browser and on mobile devices.

<a href="http://square.github.io/crossfilter/">Crossfilter.js</a> is a JavaScript library for exploring large multivariate datasets in the browser. Crossfilter supports extremely fast (<30ms) interaction with coordinated views, even with datasets containing a million or more records; we built it to power analytics for Square Register, allowing merchants to slice and dice their payment history fluidly.

By leveraging crossfilter's exquisite filtering capabilities, I can show information of size of each repo, (in this case 
I have changed it to the top 10 since there are way too much repositories in Bloomberg Github Account). By clicking on each 
segments on the pie chart, **_you can see languages used in the corresponding repo_**(I am trying to make it work with loc of each languages
but it's not easy with crossfilter). **_You can also select the languages and display the repositories that uses them._**

If the pie chart came out empty, chances are I am prevented from accessing it when I
was extracting it, there are 2 instances that I have found to have this problem: Chromium.bb and TypeScript. I have removed
Chromium.bb as it's size is too big, approximately more than 10 times larger than the 2nd largest repository. So I decided 
to take it out to restore the balance between arcs in the pie chart.

## Pie Chart Display ##

`http://127.0.0.1:5000/`

This is the snapshot of the result program. 

* Pie chart displaying size and languages used in whole github repo. <br />
<img src="https://github.com/adamlkl/GithubDataVisualisation/blob/master/Results/pie%20origin.PNG">
* Pie chart displaying size and languages used in one github repo. <br />
<img src="https://github.com/adamlkl/GithubDataVisualisation/blob/master/Results/pie%20res1.PNG">
* Pie chart displaying size and languages used in combined github repo. <br />
<img src="https://github.com/adamlkl/GithubDataVisualisation/blob/master/Results/pie%20res2.PNG">
* Pie chart displaying repositories that uses the corresponding language selected.<br />
<img src="https://github.com/adamlkl/GithubDataVisualisation/blob/master/Results/pie%20res3.PNG">
* Pie chart displaying repositories that uses the corresponding languages selected.<br />
<img src="https://github.com/adamlkl/GithubDataVisualisation/blob/master/Results/pie%20res4.PNG">

I have also set up a database for the project using mongodb to store repo_data2.json. The advantage of setting up a database
is that eventually I wanted to display more than just one Github Repository, and this would require massive amount of fast 
querying, which we can let the database deal with, unless you want your program to crash. 

To view the stored json values, please set your link to 

## Repo_Data2.json Link

`http://127.0.0.1:5000/bloombergdata/repo_data2`

The result should come as below. <br />

<img src="https://github.com/adamlkl/GithubDataVisualisation/blob/master/Results/repo_data2%20in%20json.PNG">

## Remarks ##
As this program is not what I envisioned in the first place, there will be more upgrades to it such as displaying it on 
<a href="https://keen.github.io/dashboards/">dashboard</a>, displaying more data such as 
<a href="https://github.com/adamlkl/GithubDataVisualisation/blob/master/Contributors_Data.json">contributors</a>,
and multiple repo together. So stay tuned. 
