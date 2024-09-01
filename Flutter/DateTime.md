## DateTime ##

- Date 저장 하는 Object
```dart
import 'package:intl/intl.dart'; // Intl 패키지 설치
final formatter = DateFormat.yMD(); // Year, Month, Day 형식
DateTime temp = DateTime.now(); // 현재 시간  
print(formatter.format(temp)); // Locale에 따라서 다르게 나옴 

showDatePicker(
	context: context,
	initialDate: now,
	firstDate: DateTime(now.year - 1), 
	// 현재 시간으로부터 year-1
	lastDate: DateTime(now.year, now.month +1)); 
	// 현재시간부터 month+1
}

```

Refers to : [[Intl]]

