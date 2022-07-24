# fixjatos

The most robust way to save [jsPsych](https://www.jspsych.org/) data is JSON, and data in JSON format is easy to turn into a dataframe in R using the `jsonlite` package. Unfortunately, if you are running on a [JATOS](https://www.jatos.org/) server, the exported files are not valid JSON, even though each individual subject's file is valid JSON.

This program converts a JATOS results `.txt` file to a valid `.json` file which can then be loaded into R using the `fromJSON` function provided by `jsonlite`.

This is for data written by jsPsych using the `jsPsych.data.get().json())` method.

# Usage

`fixjatos.py FILE.txt`  

produces a corresponding `FILE.json` which contains correct JSON. 

# Warning!

`FILE.json` will be overwritten!

# Licence

MIT License 

# Bugs and redistribution

Please use the issue tracker to report bugs, and feel free to fix them too if you can, as Python isn't my native language. :)