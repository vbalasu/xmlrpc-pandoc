sudo docker run -i --rm -v $(pwd):/source jagregory/pandoc -f $1 -t $2 -o /dev/stdout $3
#SYNTAX: ./l1_run.sh {FROM} {TO} {INPUT_FILE} >{OUTPUT_FILE} 
#EXAMPLE: ./l1_run.sh markdown docx README.md >README.docx

#sudo docker run -i --rm -v $(pwd):/source jagregory/pandoc README.md -o README.docx
