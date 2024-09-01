## Cupertino ##

- Flutter 에서 iOS-Like Design을 만든 Package
- Material -> Android , Cupertino -> iOS
- 따라서 만약에 각각의 Native-Like기능을 보여주고 싶다면

```dart
import 'dart:io';

if (Platform.isIOS) {
	'''
	'''
	showCupertinoDialog();
}else{
	showDialog();
}
```

Officail Website: [Cupertino Widgets](https://docs.flutter.dev/ui/widgets/cupertino)
