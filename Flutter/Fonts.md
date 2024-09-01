## Fonts ##

- Font 설정하는 방법
- 기본 Font을 쓰는 경우에는
```dart
Text(
	currentQuestion.text,
	style: const TextStyle(color: Colors.white, fontSize: 16),
	textAlign: TextAlign.center,
)
```
- 아래는 Google Font 사용
```dart
import 'package:google_fonts/google_fonts.dart';

Text(
	currentQuestion.text,
	style: GoogleFonts.lato(
		color: Colors.white,
		fontSize: 24,
		fontWeight: FontWeight.bold),
		textAlign: TextAlign.center,
),

// pubspec.yaml
'''
'''
dependencies:
	flutter:
	sdk: flutter
# The following adds the Cupertino Icons font to your application.
# Use with the CupertinoIcons class for iOS style icons.
	cupertino_icons: ^1.0.8
	google_fonts: ^6.2.1
```


Refers to: [[Package]], [[Import]], [[Pubspec.yaml]]
