## Spreading ##

- List를 Comma로 나눠져있는 List로 변형하려면?
```Dart
List<Int> a = [1,2,3,4];
// List<Int> b = [a, 5] 
// 에러 [[1,2,3,4],5] 이렇게 되기 때문
List<Int> b = [...a, 5] 
// [1,2,3,4,5]
// ...이 Spreading

a.map((num) {
	return num+1
});
// [2,3,4,5]

...a.map((num) {
	return num+1
});
// 2,3,4,5
```
Refers to : [[Map]], [[List]]

