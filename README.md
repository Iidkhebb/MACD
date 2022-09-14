<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="MACD_Indicator_0"></a>MACD Indicator</h1>
<h2 class="code-line" data-line-start=1 data-line-end=2 ><a id="_Easy_tool_for_find_MACD_signals_crossover__1"></a><em>Easy tool for find MACD signals crossover</em></h2>
<p class="has-line-data" data-line-start="4" data-line-end="5"><a href="https://travis-ci.org/joemccann/dillinger"><img src="https://travis-ci.org/joemccann/dillinger.svg?branch=master" alt="Build Status"></a></p>
<p class="has-line-data" data-line-start="6" data-line-end="9">MACD Indicator  is a tool that looks for bullish signals using MACD indicator that has already<br>
has over 65% sucess rate in backtest mode.<br>
You can use this tool for creating scalping or swing trading bots, creating signals groups and more.</p>
<h2 class="code-line" data-line-start=11 data-line-end=12 ><a id="Tech_11"></a>Tech</h2>
<p class="has-line-data" data-line-start="12" data-line-end="13">MACD Indicator uses a number of open source techs to work properly:</p>
<ul>
<li class="has-line-data" data-line-start="14" data-line-end="15">[Python3.8]</li>
<li class="has-line-data" data-line-start="15" data-line-end="16">[Yahoo Finance]</li>
<li class="has-line-data" data-line-start="16" data-line-end="17">[Pandas]</li>
<li class="has-line-data" data-line-start="17" data-line-end="18">[Numpy]</li>
<li class="has-line-data" data-line-start="18" data-line-end="19">[Flask]</li>
<li class="has-line-data" data-line-start="19" data-line-end="21">[Docker]</li>
</ul>
<h2 class="code-line" data-line-start=21 data-line-end=22 ><a id="Installation_21"></a>Installation</h2>
<h2 class="code-line" data-line-start=23 data-line-end=24 ><a id="Docker_23"></a>Docker</h2>
<p class="has-line-data" data-line-start="25" data-line-end="26">MACD Indicator is very easy to install and deploy in a Docker container.</p>
<p class="has-line-data" data-line-start="27" data-line-end="30">By default, the Docker will expose port 8080, so change this within the<br>
Dockerfile if necessary. When ready, simply use the Dockerfile to<br>
build the image.</p>
<pre><code class="has-line-data" data-line-start="32" data-line-end="35" class="language-sh"><span class="hljs-built_in">cd</span> <span class="hljs-string">"YOUR ROOT FOLDER"</span>
docker compose up
</code></pre>
<p class="has-line-data" data-line-start="36" data-line-end="37">This will create the flask-api and a backend images and pull in the necessary dependencies.</p>
<p class="has-line-data" data-line-start="38" data-line-end="41">Once done, run the Docker image and map the port to whatever you wish on<br>
your host. In this example, we simply map port 8000 of the host to<br>
port 4000 of the Docker (or whatever port was exposed in the Dockerfile):</p>
<p class="has-line-data" data-line-start="42" data-line-end="44">Verify the deployment by navigating to your server address in<br>
your preferred browser.</p>
<pre><code class="has-line-data" data-line-start="46" data-line-end="49" class="language-sh">To get all the signals <span class="hljs-keyword">in</span> a JSON Format response use :
<span class="hljs-number">127.0</span>.<span class="hljs-number">0.1</span>:<span class="hljs-number">4000</span>/api
</code></pre>
<pre><code class="has-line-data" data-line-start="50" data-line-end="54" class="language-sh">To look <span class="hljs-keyword">for</span> a trading pair <span class="hljs-keyword">in</span> <span class="hljs-keyword">for</span> exemple BTC/USD :
Use the search keyword :
<span class="hljs-number">127.0</span>.<span class="hljs-number">0.1</span>:<span class="hljs-number">4000</span>/api?search=YOURPAIR
</code></pre>
<h2 class="code-line" data-line-start=55 data-line-end=56 ><a id="License_55"></a>License</h2>
<p class="has-line-data" data-line-start="57" data-line-end="58">Iidkhebb</p>
<p class="has-line-data" data-line-start="59" data-line-end="60"><strong>Free Software, Hell Yeah!</strong></p>
