#Intro
This python script exports notes from [Laverna](laverna.cc) to markdown files by extracting the content from the JSON files that Laverna uses to store notes.
The notes are saved in directories corresponding to notebooks.

#Usage
Once you have the directory of JSON files ready to go, edit the directory locations at the top of the script and specify an output directory.
Then run the script:

```$ python export.py```

#Limitations
This is a simple script that has some limitations. However, it could easily be extended to handle more complex use cases.

- Flat notebook structure: the exporter ignores the notebook hierarchy
- Ignores other fields: only `title`, `content`, and `notebookId` are used, so
  `tags` are ignored, for example
