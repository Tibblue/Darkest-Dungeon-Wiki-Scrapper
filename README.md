# Darkest-Dungeon-Wiki-Scrapper
The Darkest Scrapper !!!

This little boy allows you to scrap the Wiki page for info and files.
I really like the wiki, but sometimes I just wanna mass download some good old narrator lines for meme purposes XD

And so I share this for anyone who might want the same.

Also useful in case you wanna learn some Scrapping with Python.

## Install

Firstly you need to install [Python3](https://www.python.org/downloads/).

~~Secondly we recommend to install [Anaconda](https://docs.anaconda.com/anaconda/install/linux/).
If you are not very familiar with Virtual Enviroments or you just wanna go fast, you can skip the Anaconda install.
Of course skip any steps where Anaconda is used latter on.~~

### Packages

~~First let's prepara the Virtual Enviroment.~~

~~`conda create -n Darkest_Env python=3.6`~~

~~`conda env list`~~

~~`conda activate Darkest_Env`~~

Now let's take care of the package requirements.

`pip install -r requirements.txt`



## Run

With all installed we need only to run `python3 main.py`

Use `python3 main.py --help` to see all the arguments you can use, to change the information you will scrap.

An example would be: `python3 main.py -n --toc -o results.txt`, where `-n` tells us we want to scrap the **Narrator** page, and `--toc` tells us we want the **Table of Contents**. Finaly `-o results.txt` means we want the results to go to the file `results.txt`, and not the terminal stdout.

### Current functionalities
Currently we allow results in partial HTML, and Lists or Dicts.
We can also download any files present in the results if desired.

Currently we only scrap the Narrator page. More will come in the future.

Here we have a bit more detailed info on each page, and what can be done:
* **Narrator** page, currently can scrap:
  * Table of Content (HTML, Dict)
  * Quotes and Audio Sources (HTML List, Dict)
    * HTML List has reesults ordered by appearance, but doesn't associate a quote to its audio
    * Dict uses the Quote as the key, and a list of Audio Sources as value
  * Quotes (HTML List, List)
  * Audio Sources (HTML List, List)



