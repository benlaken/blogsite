Title: How can I begin to improve my workflow?
Date: 2016-10-01 09:49
Category: Post
Slug: how_to_begin
Tags: Reproducibility, Open Science, Software
Author: Benjamin Laken
Email: benlaken@gmail.com
Summary: How to begin on the path to an Open Science workflow

![alt text](./images/journey_banner.jpg "Original image by Hanna Norlin")

### A familiar situation?

Are you are toiling away at your project with nothing but your wits, a few hand-me-down scripts, and a supervisor who only has time to interact with you as they hurriedly walk down the corridor on their way to their next meeting? Perhaps it seems like it will be much easier to just get to work hammering away at your task, the way you were originally shown?

Maybe you saw a talk or read an article about the world of Open Science, and you are starting to have a strong suspicion that there must be a better way to work than the approach you have been using up-till-now: one that may even give you skills that people in the land that lays beyond academia will find attractive! You have heard about tools like Python, version control, and this vague idea of Open Science. But in practical terms, how can you begin?

You might have a project with a file structure that looks something like this:

```
└── my_project
    │
    ├── Code
    │   ├── process_raw_data.f77  <--- Heart of the project, written in 90's by, uh, someone...
    │   └── calculate_result.mat  <--- The postdoc who wrote this already left to work for a bank...
    │
    ├── Data
    │   ├── raw_experiment1.txt  <--- This is the raw data from my instrument
    │   ├── raw_experiment2.txt
    │   ├── raw_experiment3.txt
    │   └── processed_data.dat  <--- Postdoc's code makes this, which I can put into Excel!
    │
    ├── output1.txt             <--- The postdocs code made this, which I can put into excel to examine...
    ├── experiment1.xlsx        <--- Finally, I can do something useful with this $*#@!
    ├── experiment2.xlsx
    ├── my_report_v3.docx       <--- The start of my thesis, or new paper
    └── summary_results.xlsx    <--- Summary excel sheet, so I can clean up my final results

```


In this folder, there is an old FORTRAN program (`Code/process_raw_data.f77`) that you got from your supervisor, it was written several decades ago and there is no one around who you can ask about this code. (Maybe there is no one even left alive who worked on it...) To get results you start by editing that file: maybe all you really need to do is change one line to point the code at some raw data you got from an instrument (e.g. `Data/raw_experiment1.txt`) and compile/run the program. On your first day your supervisor told you the exact commands to type to do this.

The old program might create an intermediate file, something like `Data/processed_data.dat`. That file is a mess, way to complicated to deal with (Big Endian? Binary what? carriage control characters?). Luckily a postdoc who used to be in your group left behind a Matlab script to process that data into something you can read into Excel. So you run `Code/calculate_result.mat`, and get `output.txt`, after some cut-and-paste skills you then have your comprehensible data in a spreadsheet and can begin the real task of analysing it, which was the reason you are doing your work in the first place!

You make some analysis, spread across multiple pages of your Excel workbook, and end up producing some figures and tables which you put into your word document, write your text, send to your supervisor, await comments and pray they don't ask for any changes that would send you back to square 1!

This is probably the most common workflow you will find at Universities and companies the world over. Working in this way is really labour intensive, and also incredibly irreproducible, [error-prone](http://www.popularmechanics.com/science/a22577/genetics-papers-excel-errors/)! (The [bus-factor](http://modeling-languages.com/whats-bus-factor-software-project/) of projects like these are usually very low.) It would be almost impossible for you to ensure someone could recreate the results presented in your final document without you sat beside them.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">You can download our code from the URL supplied. Good luck downloading the only postdoc who can get it to run, though <a href="https://twitter.com/hashtag/overlyhonestmethods?src=hash">#overlyhonestmethods</a></p>&mdash; Ian Holmes (@ianholmes) <a href="https://twitter.com/ianholmes/status/288689712636493824">January 8, 2013</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

The good news is there is no where to go but up, and any change to this workflow would be a positive one! If you need to produce results quickly, then it likely isn't feasible to just learn some new tools, snap-your fingers, and immediately change this workflow. Instead, you will have to gradually migrate towards a fully Open Science approach, perhaps over the course of several projects (like I did).

### Starting the journey

The best place to start is to download [Anaconda Python](https://www.continuum.io/downloads) from Continuum Analytics, you don't need administrator privileges, and it works on Windows, Mac, and Nix* systems. Get one with Python version 3, not 2. (If you need to switch later on that will be easy, but by default you should try to work in Python 3.) Also download [Git](https://git-scm.com) (and [Git-Bash](https://git-for-windows.github.io) if you are on windows).

With that trifecta of the shell, a high-level programming language and a version control system you are ready to begin! The next step is to run through a couple of tutorials. If you cant get yourself to a [Software Carpentry course](http://software-carpentry.org), you can run through their materials on their website. Also have a look at [CodeAcademy](https://www.codecademy.com/learn/all) (particularly their *'Command Line'*, *'Learn Git'*, and *'Learn Python'* lessons). You will probably pick up the basics of Python and Bash in just a few days sufficiently to begin using these tools for your own work.

### Project triage
#### Step 1: Moving from Excel to a few bad bits of code

The easiest place to start improving your workflow is on the part that is most labour-intensive and least reproducible: usually this means the Excel workbooks. Instead of reading the data into Excel, read it with Python, and try to create some scripts that can do your analysis tasks. I realise this sounds like me explaining how to play the piano by saying *"Step 1: sit in front of a piano. Step 2: play the piano"*, and perhaps at first you will struggle a little to do tasks which you know you could do in a couple of clicks in Excel. However, after following a few online tutorials you will see that you can copy and paste large portions of code from tutorials with small changes that will let you read data from a file, do many cool operations (using tools like [Pandas](http://pandas.pydata.org) for example), and then plot (e.g. using [Matplotlib](http://matplotlib.org)). Even if your code is awful at least it is automated, and can be tracked with version control tools and improved later. Maybe you will even keep a few Excel files while you are still going through a transition, and that is totally fine.

#### Step 2: Minor improvements = big time-saving

Let's assume you've started adding a few simple Python scripts to your project that just look like a long list of *"Read this data, do X and Y then make a plot"*. And maybe you're starting to see a few small benefits, like saving time when you have to re-run your workflow to add more data or tweak something small. But on the whole, you might feel like this hasn't really saved you much time yet. You may even feel like you've lost time learning Python, and have gotten quite frustrated a few times along the way wrapping your mind around new ways of thinking about your data.

Don't despair! Imagine you are going to start a new project, and you start to notice that there are a few similarities with your old one. You get the feeling you can start to re-use bits of your old python code again, maybe even improve them a little. Now you will start to see one of the powerful benefits of working like this: **abstraction**.

For the sake of explanation, imagine your task is multiplying two numbers together thousands of times. The first time you solved this problem, you only knew enough Python to write it out like this:

```python
result_1 = value_1 * value_2
result_2 = value_3 * value_4
result_3 = value_5 * value_6
...etc
```

Now you have been working with Python for a little while, you realise you can make an abstract solution, that will solve this problem once-and-for-all, a solution you can re-use. It might look like this:

```python

def my_tool(input_1, input_2):
    return input_1 * input_2

```

Much simpler! and when you call your inputs in a loop and feed them into this function it seems to works brilliantly! But actually, it is a little fragile like this. As you learn more, you will find that if you add a few more pieces to the code, you can get really important benefits:

``` python
import pytest

def my_tool(input_1, input_2):
    if int(input_1) and int(input_2):
        return input_1 * input_2
    else:
        raise ValueError("Error: inputs are not numbers")

def test_my_tool():
    assert my_tool(10, 10) == 100
    assert(my_tool(3.5, 5.5) == 19.25)
    with pytest.raises(ValueError):
        my_tool('NA', 10)
```
It is really remarkable what's going on in these few lines of code: Your tool starts by checking that it has been given the right type of data (numerical data), by seeing if it can convert it to an integer.  If the inputs are good, it will do your task. If it can't, the program will stop, giving an Error: so you wont accidentally process bad values and wind up with junk values in your results that you have to hunt down later!

Things get more interesting when we see what comes next - a test! This is a reality check, to make sure that no matter how you extend or change your tool in the future, it will always produce results that make sense. It even checks that the tool fails when it should, so you know that despite changes you may make tomorrow, it wont start giving back unexpected results, adding errors into your results. This is really important, as projects change over time, and it is guaranteed you won't write a perfect program first time. So when you go back in the future and change your functions, you can be relatively confident you wont inadvertently introduce errors into your work. You can run this test with [pytest](http://docs.pytest.org/en/latest/).

It is difficult to over-state the time-saving and productivity boosting potential of making small, easy-to-understand solutions, that are re-useable, and include tests: your final workflow should be a daisy-chain of tools like this. If you can get this far into updating your working approach, you will be making great progress, and will be poised to take advantage of some really amazing tools in the future, and share with [communities of people](https://www.software.ac.uk) already using them!

This post was part 2 in a series.

Banner image by [Hanna Norlin](https://www.flickr.com/photos/hanorlin/).
