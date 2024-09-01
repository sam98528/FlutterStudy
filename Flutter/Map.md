## Map ##

- map (함수) does not change the original List
```Dart
List<Int> a = [1,2,3,4];

a.map((num) {
	return num+1
});
// [2,3,4,5] 
// Type: Iterable<T>, Not List
```
- Map (Data Type) -> 하나의 Dictionary 같은것
```Dart
Map<String, int> mapTemp = {"TEMP" : 123}

List<Map<String, int>> listMap = [
	{"TEMP1" : 123},
	{"TEMP2" : 123},
	{"TEMP3" : 123}
]
```