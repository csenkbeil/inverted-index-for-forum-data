Python Hadoop streaming MapReduce scripts - Inverted Index
=============================
This MapReduce script creates an inverted index for forum post data where the index includes, post title, tags, body text with the associated post id, word order and catagory (body_text, title or tag).

For demonstration purposes, it assumed that the input posts text file (forum_node.tsv) is a tab separated file with the following columns:

* "id": id of the node
* "title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty
* "tagnames": space separated list of tags
* "author_id": id of the author
* "body": content of the post
* "node_type": type of the node, either "question", "answer" or "comment"
* "parent_id": node under which the post is located, will be empty for "questions"
* "abs_parent_id": top node where the post is located
* "added_at": date added
* plus an additional ten columns of data

### Usage
You can simulate the execution using shell pipes
```shell
cat forum_node.tsv | ./mapper.py | sort | ./reducer.py > inverted_index.tsv
```  

To run this in a hadoop environment, first set up the alias in the .bashrc
```shell
run_mapreduce() {
        hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper $1 -reducer $2 -file $1 -file $2 -input $3 -output $4
}

alias hs=run_mapreduce
```

Once the alias has been setup you can either run the process as a MapReduce using the aliased command hs.

eg.

```shell
hs mapper.py reducer.py forum_data inverted_index
```


where:
* "forum_data" is the folder in the HDFS containing the forum node text records
* "inverted_index" is the output data folder, it is important that this folder doesn't already exist.

### Output

The reducer generates a text stream with a tab separated index containing the keyword followed by tab seperated word location groups. The word location group contains post_id, word order and location category identify where the keyword can be found.

* "keyword": The searchable keyword
* "post_id: The id of the forum post
* "word_order": the word location in the text, eg. 0 indicates that it's the first word in the text, 12 indicates that it's the 13th word in the text.
* "location_catagory": indicates if the word is in the body "B", tagnames "T" or the title "H"
 

```
keyword \t post_id, word_order, location_catagory [\t post_id, wordlocation, location_catagory]...  
```
