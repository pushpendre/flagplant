Like most GUI toolkits, Kivy is mostly event-based. The framework responds to user keypresses, mouse events, and touch events. Kivy has the concept of a Clock that you can use to schedule function calls for some time in the future.

Kivy also has the concept of Properties, which works with the EventDispatcher. Properties help you do validation checking. They also let you fire events whenever a widget changes its size or position.


In order to function, fdroidserver requires that the Android SDK's
"Build-tools" and "Platform-tools" are installed.  Also, it is best if the
base path of the Android SDK is set in the standard environment variable
ANDROID_HOME.  To install them from the command line, run:
android update sdk --no-ui --all --filter tools,platform-tools,build-tools-25.0.0
