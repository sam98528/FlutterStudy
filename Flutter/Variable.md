## Variable ##

```dart
var a = 10 // Varible이니깐 변경이 가능함 (Type Infer)
// Dart에서는 Var를 최대한 피해야 한다고 한다. 
Int b = 10 // Variable
const c = 10 // Immutable


Int d // 에러 NUll 처리 못함
Int? d // Null 값

print(d) // 에러 Null 값 일수도 있어서
print(d!) // 강제 Unrapping
print(d ?? 10) // Default값 제공
```