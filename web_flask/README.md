<h1>AirBnB clone - Web framework</h1>
<div class="panel panel-default">
<div class="panel-heading">
<h3 class="panel-title">Concepts</h3>
</div>
<div class="panel-body">
<p><em>For this project, we expect you to look at this concept:</em></p>
<ul>
<li><a href="https://intranet.hbtn.io/concepts/865">AirBnB clone</a></li>
</ul>
</div>
</div>
<div id="project-description" class="panel panel-default">
<div class="panel-body">
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="What is a Web Framework?" href="https://intranet.hbtn.io/rltoken/qk3bO45DSY-P4qmdnEX93w" target="_blank" rel="noopener">What is a Web Framework?</a></li>
<li><a title="A Minimal Application" href="https://intranet.hbtn.io/rltoken/MpPJIP84fdw2Mj4xclTn8g" target="_blank" rel="noopener">A Minimal Application</a></li>
<li><a title="Routing" href="https://intranet.hbtn.io/rltoken/7hTn4ZTNN4FovR4Mfnrr3A" target="_blank" rel="noopener">Routing</a>&nbsp;(<em>except &ldquo;HTTP Methods&rdquo;</em>)</li>
<li><a title="Rendering Templates" href="https://intranet.hbtn.io/rltoken/FsnX6in3OXcX2uXFD6lNSw" target="_blank" rel="noopener">Rendering Templates</a></li>
<li><a title="Synopsis" href="https://intranet.hbtn.io/rltoken/TrJfUguYuS-MI9IfzwvcRQ" target="_blank" rel="noopener">Synopsis</a></li>
<li><a title="Variables" href="https://intranet.hbtn.io/rltoken/wFqulSZjYrsZEPj7kB7Pdw" target="_blank" rel="noopener">Variables</a></li>
<li><a title="Comments" href="https://intranet.hbtn.io/rltoken/NjTPr3eCOY_BDS0-3Z_xtw" target="_blank" rel="noopener">Comments</a></li>
<li><a title="Whitespace Control" href="https://intranet.hbtn.io/rltoken/iajkEdDEmO0Bda2tB8xRLw" target="_blank" rel="noopener">Whitespace Control</a></li>
<li><a title="List of Control Structures" href="https://intranet.hbtn.io/rltoken/sqUAVb5CylKytVU_Z6Fq5Q" target="_blank" rel="noopener">List of Control Structures</a>&nbsp;(<em>read up to &ldquo;Call&rdquo;</em>)</li>
<li><a title="Flask" href="https://intranet.hbtn.io/rltoken/OMqE9vlalgkWcT_3fu4Hvg" target="_blank" rel="noopener">Flask</a></li>
<li><a title="Jinja" href="https://intranet.hbtn.io/rltoken/UVC1Bw_-nfa_0T2gv1MuQg" target="_blank" rel="noopener">Jinja</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/lVg3jl6IEzhNeQiHwhC-Fg" target="_blank" rel="noopener">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>What is a Web Framework</li>
<li>How to build a web framework with Flask</li>
<li>How to define routes in Flask</li>
<li>What is a route</li>
<li>How to handle variables in a route</li>
<li>What is a template</li>
<li>How to create a HTML response in Flask by using a template</li>
<li>How to create a dynamic template (loops, conditions&hellip;)</li>
<li>How to display in HTML data from a MySQL database</li>
</ul>
<h2>Requirements</h2>
<h3>Python Scripts</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using&nbsp;<code>python3</code>&nbsp;(version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the&nbsp;<code>PEP 8</code>&nbsp;style (version 1.7)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using&nbsp;<code>wc</code></li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code>&nbsp;and&nbsp;<code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>
<h3>HTML/CSS Files</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>A&nbsp;<code>README.md</code>&nbsp;file at the root of the folder of the project is mandatory</li>
<li>Your code should be W3C compliant and validate with&nbsp;<a title="W3C-Validator" href="https://intranet.hbtn.io/rltoken/dhCIocUxbqoTcq0KHtJE4Q" target="_blank" rel="noopener">W3C-Validator</a>&nbsp;(except for jinja template)</li>
<li>All your CSS files should be in the&nbsp;<code>styles</code>&nbsp;folder</li>
<li>All your images should be in the&nbsp;<code>images</code>&nbsp;folder</li>
<li>You are not allowed to use&nbsp;<code>!important</code>&nbsp;or&nbsp;<code>id</code>&nbsp;(<code>#...</code>&nbsp;in the CSS file)</li>
<li>All tags must be in uppercase</li>
<li>Current screenshots have been done on&nbsp;<code>Chrome 56.0.2924.87</code>.</li>
<li>No cross browsers</li>
</ul>
<h2>More Info</h2>
<h3>MySQL Default charset issues</h3>
<ul>
<li>If you get Flask errors after executing the&nbsp;<code>curl ...</code>&nbsp;commands, it might be because of the&nbsp;<code>DEFAULT CHARSET</code>. If it&rsquo;s&nbsp;<code>DEFAULT CHARSET=latam1</code>, you might want to change it to&nbsp;<code>DEFAULT CHARSET=utf8mb4</code>, either on the server&rsquo;s config file (/etc/mysql/my.cnf commonly) orm on the CREATE DATABASE statement.</li>
</ul>
</div>
</div>
