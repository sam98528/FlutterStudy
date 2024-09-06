## FadeImage ##
- Creates a widget that displays a [placeholder] while an [image] is loading, then fades-out the placeholder and fades-in the image.

```dart
import 'package:transparent_image/transparent_image.dart';
FadeInImage(
	placeholder: MemoryImage(kTransparentImage),
	image: NetworkImage(meal.imageUrl),
),
```