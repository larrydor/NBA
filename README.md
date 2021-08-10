[![Maintainability](https://api.codeclimate.com/v1/badges/17097606dbcde4fa4d37/maintainability)](https://codeclimate.com/github/larrydor/NBA/maintainability)

# GM Assist: NBA Free Agent Tracker Tool!

A Python application that utilizes National Basketball Association (NBA) focused APIs from sportradar.us to retrieve all team rosters and available free agents. This application allows a user to easily retrieve key information on team players and search for available free agents with an experience requirement if desired. Furthermore, we have added CSV functionality to seamlessly allow a user to export the free agents data.

## Group Members
* Alex Fleshner
* Larry Doroger
* Meghana Reddy

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/larrydor/NBA) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd ~/Desktop/NBA
```
Use Anaconda to create and activate a new virtual environment, perhaps called "nba-env":

```sh
conda create -n nba-env python=3.8
conda activate nba-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).

## Setup

### Sportradar.us API Setup

Signup for [Sportradar.us API](https://developer.sportradar.com/member/register):
  1) Obtain a Sportradar.us API Key to be entered in the .env file as (`api_key`).


### Environmental Variables Setup

Create a new file called ".env" in the root directory of this repo, then copy the contents below into it, adapting the values to match the `api_key` from Sportradar.us.

```sh
# the .env file

api_key="abc123"
```

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [".gitignore"](/.gitignore) file). This means we need to instruct each person who uses our code needs to create their own local ".env" file.

## Usage

Run the Python script:

```py
python app/nba_search.py
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.

## Reference
Thank you to Professor Rossetti for providing great instruction and assistance during this course! As well as a reference README file and CSV module configuration instructions within GitHub.

1. Source: https://raw.githubusercontent.com/prof-rossetti/my-first-python-app/main/README.md
1. Source: https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/modules/csv.md