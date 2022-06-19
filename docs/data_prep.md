# Data prepareation stage

- Convert my data into train and test.tsv in 70:30 ratio

'''
data.xml
     |-train.tsv
     |-test.tsv

```

- we are choosing only three tags in the xml data 1. row Id, 2.title and body 3.Tags(Stackoverflow tags specific to python)

|Tags|features names|
|-|-|
|row Id|row ID|
|title and body|text|
|stackoverflow tags|Label - python|


   
