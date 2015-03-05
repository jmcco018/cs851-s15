#!/bin/bash
for file in `ls ../../a2/warcs` ; do java -jar warc-indexer-2.0.1-20150116.110435-2-jar-with-dependencies.jar -s http://localhost:10080/discovery/ ../../a2/warcs/$file/warcreate/*; done
