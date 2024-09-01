## Final & Const ##

- `Final`은 **런타임**에 값이 결정되며, 한번 할당된 후에는 변경 X
- `const`는 **컴파일타임**에 값이 결정되며, 변경 X
- 결정적인 차이는 Runtime에서 결정되느냐 아니면 Compiled time에서 결정되는냐의 차이 
``` dart
final DateTime now = DateTime.now() // 현재 시간 할당 , 런타임에 계산된다.
const a = 10 // 런타임이 아니고, Compiled Time에 정해져도 문제가 없음 
```
- `=` 은 정확히는 메모리를 할당하는것이기에, 값이 변경되는게 아니라, 주소가 변경되는것