<!DOCTYPE html>
<!--[if IE 8]><html class="no-js lt-ie9" lang="en" > <![endif]-->
<!--[if gt IE 8]><!-->
<html style="" class=" js flexbox canvas canvastext webgl no-touch geolocation postmessage no-websqldatabase indexeddb hashchange history draganddrop websockets rgba hsla multiplebgs backgroundsize borderimage borderradius boxshadow textshadow opacity cssanimations csscolumns cssgradients no-cssreflections csstransforms csstransforms3d csstransitions fontface generatedcontent video audio localstorage sessionstorage webworkers applicationcache svg inlinesvg smil svgclippaths" lang="en"><!--<![endif]--><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
  <meta charset="utf-8">
  
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <title>Performance Measurement and Improvement Techniques — OpenCV-Python Tutorials 1 documentation</title>
  

  
  

  

  
  
    

  

  
  

  
    <link rel="stylesheet" href="Performance%20Measurement%20and%20Improvement%20Techniques%20%E2%80%94%20OpenCV-Python%20Tutorials%201%20documentation_files/sphinx_rtd_theme.css" type="text/css">
  
    <link rel="stylesheet" href="Performance%20Measurement%20and%20Improvement%20Techniques%20%E2%80%94%20OpenCV-Python%20Tutorials%201%20documentation_files/readthedocs-doc-embed.css" type="text/css">
  

  
    <link rel="top" title="OpenCV-Python Tutorials 1 documentation" href="https://opencv-python-tutroals.readthedocs.org/en/latest/index.html">
        <link rel="up" title="Core Operations" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_core/py_table_of_contents_core/py_table_of_contents_core.html">
        <link rel="next" title="Mathematical Tools in OpenCV" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_core/py_maths_tools/py_maths_tools.html">
        <link rel="prev" title="Arithmetic Operations on Images" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html">
 
<!-- RTD Extra Head -->

    
    

<!-- 
Always link to the latest version, as canonical.
http://docs.readthedocs.org/en/latest/canonical.html
-->
<link rel="canonical" href="http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_core/py_optimization/py_optimization.html">
<script src="Performance%20Measurement%20and%20Improvement%20Techniques%20%E2%80%94%20OpenCV-Python%20Tutorials%201%20documentation_files/ga.js" async="" type="text/javascript"></script><script type="text/javascript">
  // This is included here because other places don't have access to the pagename variable.
  var READTHEDOCS_DATA = {
    project: "opencv-python-tutroals",
    version: "latest",
    language: "en",
    page: "py_tutorials/py_core/py_optimization/py_optimization",
    builder: "sphinx",
    theme: "sphinx_rtd_theme",
    docroot: "/source/",
    
    source_suffix: ".rst",
    
    api_host: "https://readthedocs.org/",
    commit: "43532856"
  }
  // Old variables
  var doc_version = "latest";
  var doc_slug = "opencv-python-tutroals";
  var page_name = "py_tutorials/py_core/py_optimization/py_optimization";
  var html_theme = "sphinx_rtd_theme";
</script>
<!-- RTD Analytics Code -->
<!-- Included in the header because you don't have a footer block. -->
<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-17997319-1']);
  _gaq.push(['_trackPageview']);

  // User Analytics Code
  _gaq.push(['user._setAccount', 'UA-15552566-2']);
  _gaq.push(['user._trackPageview']);
  // End User Analytics Code


  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>
<!-- end RTD Analytics Code -->
<!-- end RTD <extrahead> -->


  
  <script src="Performance%20Measurement%20and%20Improvement%20Techniques%20%E2%80%94%20OpenCV-Python%20Tutorials%201%20documentation_files/modernizr.js"></script>

</head>

<body class="wy-body-for-nav" role="document">

  <div class="wy-grid-for-nav">

    
    <nav data-toggle="wy-nav-shift" class="wy-nav-side">
      <div class="wy-side-scroll">
        <div class="wy-side-nav-search">
          

          
            <a href="https://opencv-python-tutroals.readthedocs.org/en/latest/index.html" class="icon icon-home"> OpenCV-Python Tutorials
          

          
            
            <img src="Performance%20Measurement%20and%20Improvement%20Techniques%20%E2%80%94%20OpenCV-Python%20Tutorials%201%20documentation_files/opencv-logo-white.png" class="logo">
          
          </a>

          
            
            
            
              <div class="version">
                latest
              </div>
            
          

          
<div role="search">
  <form id="rtd-search-form" class="wy-form" action="../../../search.html" method="get">
    <input name="q" placeholder="Search docs" type="text">
    <input name="check_keywords" value="yes" type="hidden">
    <input name="area" value="default" type="hidden">
  </form>
</div>

          
        </div>

        <div class="wy-menu wy-menu-vertical" data-spy="affix" role="navigation" aria-label="main navigation">
          
            
            
                <ul class="current">
<li class="toctree-l1 current"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_tutorials.html"><span class="toctree-expand"></span>OpenCV-Python Tutorials</a><ul class="current">
<li class="toctree-l2"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_setup/py_table_of_contents_setup/py_table_of_contents_setup.html">Introduction to OpenCV</a></li>
<li class="toctree-l2"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_table_of_contents_gui/py_table_of_contents_gui.html">Gui Features in OpenCV</a></li>
<li class="toctree-l2 current"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_core/py_table_of_contents_core/py_table_of_contents_core.html"><span class="toctree-expand"></span>Core Operations</a><ul class="current">
<li class="toctree-l3"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html">Basic Operations on Images</a></li>
<li class="toctree-l3"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html">Arithmetic Operations on Images</a></li>
<li class="toctree-l3 current"><a class="current reference internal" href=""><span class="toctree-expand"></span>Performance Measurement and Improvement Techniques</a><ul>
<li class="toctree-l4"><a class="reference internal" href="#goal">Goal</a></li>
<li class="toctree-l4"><a class="reference internal" href="#measuring-performance-with-opencv">Measuring Performance with OpenCV</a></li>
<li class="toctree-l4"><a class="reference internal" href="#default-optimization-in-opencv">Default Optimization in OpenCV</a></li>
<li class="toctree-l4"><a class="reference internal" href="#measuring-performance-in-ipython">Measuring Performance in IPython</a></li>
<li class="toctree-l4"><a class="reference internal" href="#more-ipython-magic-commands">More IPython magic commands</a></li>
<li class="toctree-l4"><a class="reference internal" href="#performance-optimization-techniques">Performance Optimization Techniques</a></li>
<li class="toctree-l4"><a class="reference internal" href="#additional-resources">Additional Resources</a></li>
<li class="toctree-l4"><a class="reference internal" href="#exercises">Exercises</a></li>
</ul>
</li>
<li class="toctree-l3"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_core/py_maths_tools/py_maths_tools.html">Mathematical Tools in OpenCV</a></li>
</ul>
</li>
<li class="toctree-l2"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html">Image Processing in OpenCV</a></li>
<li class="toctree-l2"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_feature2d/py_table_of_contents_feature2d/py_table_of_contents_feature2d.html">Feature Detection and Description</a></li>
<li class="toctree-l2"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_video/py_table_of_contents_video/py_table_of_contents_video.html">Video Analysis</a></li>
<li class="toctree-l2"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_calib3d/py_table_of_contents_calib3d/py_table_of_contents_calib3d.html">Camera Calibration and 3D Reconstruction</a></li>
<li class="toctree-l2"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_ml/py_table_of_contents_ml/py_table_of_contents_ml.html">Machine Learning</a></li>
<li class="toctree-l2"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_photo/py_table_of_contents_photo/py_table_of_contents_photo.html">Computational Photography</a></li>
<li class="toctree-l2"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_objdetect/py_table_of_contents_objdetect/py_table_of_contents_objdetect.html">Object Detection</a></li>
<li class="toctree-l2"><a class="reference internal" href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_bindings/py_table_of_contents_bindings/py_table_of_contents_bindings.html">OpenCV-Python Bindings</a></li>
</ul>
</li>
</ul>

            
          
        </div>
      </div>
    </nav>

    <section data-toggle="wy-nav-shift" class="wy-nav-content-wrap">

      
      <nav class="wy-nav-top" role="navigation" aria-label="top navigation">
        <i data-toggle="wy-nav-top" class="fa fa-bars"></i>
        <a href="https://opencv-python-tutroals.readthedocs.org/en/latest/index.html">OpenCV-Python Tutorials</a>
      </nav>


      
      <div class="wy-nav-content">
        <div class="rst-content">
          





<div role="navigation" aria-label="breadcrumbs navigation">
  <ul class="wy-breadcrumbs">
    <li><a href="https://opencv-python-tutroals.readthedocs.org/en/latest/index.html">Docs</a> »</li>
      
          <li><a href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_tutorials.html">OpenCV-Python Tutorials</a> »</li>
      
          <li><a href="https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_core/py_table_of_contents_core/py_table_of_contents_core.html">Core Operations</a> »</li>
      
    <li>Performance Measurement and Improvement Techniques</li>
      <li class="wy-breadcrumbs-aside">
        
          
            <a href="https://github.com/abidrahmank/OpenCV2-Python-Tutorials/blob/master/source/py_tutorials/py_core/py_optimization/py_optimization.rst" class="fa fa-github"> Edit on GitHub</a>
          
        
      </li>
  </ul>
  <hr>
</div>
          <div role="main" class="document" itemscope="itemscope" itemtype="http://schema.org/Article">
           <div itemprop="articleBody">
            
  <div class="section" id="performance-measurement-and-improvement-techniques">
<span id="optimization-techniques"></span><h1>Performance Measurement and Improvement Techniques<a class="headerlink" href="#performance-measurement-and-improvement-techniques" title="Permalink to this headline">¶</a></h1>
<div class="section" id="goal">
<h2>Goal<a class="headerlink" href="#goal" title="Permalink to this headline">¶</a></h2>
<p>In image processing, since you are dealing with large number of 
operations per second, it is mandatory that your code is not only 
providing the correct solution, but also in the fastest manner. So in 
this chapter, you will learn</p>
<blockquote>
<div><ul class="simple">
<li>To measure the performance of your code.</li>
<li>Some tips to improve the performance of your code.</li>
<li>You will see these functions : <strong>cv2.getTickCount</strong>, <strong>cv2.getTickFrequency</strong> etc.</li>
</ul>
</div></blockquote>
<p>Apart from OpenCV, Python also provides a module <strong>time</strong> which is helpful in measuring the time of execution. Another module <strong>profile</strong>
 helps to get detailed report on the code, like how much time each 
function in the code took, how many times the function was called etc. 
But, if you are using IPython, all these features are integrated in an 
user-friendly manner. We will see some important ones, and for more 
details, check links in <strong>Additional Resouces</strong> section.</p>
</div>
<div class="section" id="measuring-performance-with-opencv">
<h2>Measuring Performance with OpenCV<a class="headerlink" href="#measuring-performance-with-opencv" title="Permalink to this headline">¶</a></h2>
<p><strong>cv2.getTickCount</strong> function returns the number of 
clock-cycles after a reference event (like the moment machine was 
switched ON) to the moment this function is called. So if you call it 
before and after the function execution, you get number of clock-cycles 
used to execute a function.</p>
<p><strong>cv2.getTickFrequency</strong> function returns the frequency 
of clock-cycles, or the number of clock-cycles per second. So to find 
the time of execution in seconds, you can do following:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="n">e1</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">getTickCount</span><span class="p">(