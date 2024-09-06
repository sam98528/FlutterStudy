## SwitchListTile ##
- Switch가 기본적으로 제공되는 Widget
- title., vlaue, onchanged, subtitle를 설정해야함.
```dart
SwitchListTile(
  value: _glutenFliterSet, // 현재 스위치 상태를 저장하는 변수
  onChanged: (newValue) { // 스위치 값이 변경될 때 호출되는 함수
    setState(() {
      _glutenFliterSet = newValue; // 새로운 값으로 상태 업데이트
    });
  },
  title: Text( // 타이틀 설정
    'Gluten-Free',
    style: Theme.of(context).textTheme.titleLarge!.copyWith(
      color: Theme.of(context).colorScheme.onSurface, // 텍스트 색상 설정
    ),
  ),
  subtitle: Text( // 서브 타이틀 설정
    'Only Include Gluten-free meals.',
    style: Theme.of(context).textTheme.labelMedium!.copyWith(
      color: Theme.of(context).colorScheme.onSurface, // 서브 타이틀 색상 설정
    ),
  ),
  activeColor: Theme.of(context).colorScheme.tertiary, // 활성화된 스위치 색상
  contentPadding: const EdgeInsets.only(left: 24, right: 24), // 스위치 타일의 패딩 설정
)
```