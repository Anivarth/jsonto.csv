# What is jsontocsv?
Consider you are having a json code as follows:

```python
'anivarth':{
  'test1':{
    'project1':{
       'pull_request': 'value1'
    }
  },
  'test2':{
    'project2':{
       'pull_request': 'value2'
    }
  },
  'test3': "directvalue"
}
```

Now this will be converted as follows:

| column 1      | column 2      |  column 3   | column 4     | column 5 |
| ------------- | ------------- | ----------- | ------------ | -------- |
| anivarth      | test1         | project1    | pull_request | value1   |
| anivarth      | test2         | project2    | pull_request | value2   |
| anivarth      | test3         | directvalue |              |          |

# How to use the code?
Download/Clone the folder. After you download, open the terminal in the folder, and you can do the following:

```python
>>> from jtc import Json
>>> # get your json data into python
>>> json_data = {......}
>>> convert = Json(json_data)
>>> convert.convert_to_csv(filename = "some_file_name.csv", delimeter = '|')
