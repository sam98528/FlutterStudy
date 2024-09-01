## List ##

```dart
// List<object> name = []
List<Int> a = [1,2,3];

final List<Int> b = [1,2,3,4];
// 이걸 셔플 하고 싶다면?

final c = List.of(b); // List 복사하는 코드 
c.shuffle();
print(c) // [2,3,1,4] 랜덤하게 나옴
//Shuffle은 기존 리스트를 변경하지만, 
// Final은 Value를 변경하는것은 가능하지만, 할당된 메모리를 전체 변경, 수정 하는것이 아니기에 가능함.

a.add(4) // [1,2,3,4]
```

Refers to : [[Final & Const]]
