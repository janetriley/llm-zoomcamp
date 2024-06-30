# 01-Introduction

[Class Folder](../../01-intro)
[Lesson](../../01-intro/README.md)

[Homework notebook](module_1.ipynb)

[Submission](https://courses.datatalks.club/llm-zoomcamp-2024/homework/hw1)




# Cheat Sheet, TIL, crumbs

Restart elasticsearch
*TODO make an alias*
```bash
docker run -it \
    --rm \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```

# Fix jupyter error about missing nbclassic extension:
Modify the config file to stop loading it. From a cell in the notebook, 
run this to see where it's installed:
```jsx
!jupyter server extension list
```

