
# Flutter Components Structure for RiftCooking App

## Login Screen

The login screen will be the first screen that the user sees. It will have two text fields for the username and password, and a button to submit the login details.

```dart
class LoginScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: EdgeInsets.all(20.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            TextField(
              decoration: InputDecoration(labelText: 'Username'),
            ),
            TextField(
              decoration: InputDecoration(labelText: 'Password'),
              obscureText: true,
            ),
            RaisedButton(
              child: Text('Login'),
              onPressed: () {
                // Handle login
              },
            ),
          ],
        ),
      ),
    );
  }
}
```

## Onboarding Screen

The onboarding screen will guide the user through the main functionalities of the app. It will have a series of slides that the user can swipe through, each describing a different feature.

```dart
class OnboardingScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return PageView(
      children: <Widget>[
        _buildPage('Chat with Chef', 'Engage in text-based conversation with a virtual master chef.'),
        _buildPage('Image-to-Recipe', 'Input images of ingredients and receive a recipe along with a tutorial.'),
        _buildPage('Course Recognition', 'Input an image of a main course, receive its name, description, ingredients, and a cooking recipe.'),
      ],
    );
  }

  Widget _buildPage(String title, String description) {
    return Padding(
      padding: EdgeInsets.all(20.0),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Text(title, style: TextStyle(fontSize: 30.0, fontWeight: FontWeight.bold)),
          Text(description, textAlign: TextAlign.center),
        ],
      ),
    );
  }
}
```

## Account Management Screen

The account management screen will allow the user to view and edit their account details. It will have a form with fields for the username, email, and password.

```dart
class AccountManagementScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Account Management'),
      ),
      body: Padding(
        padding: EdgeInsets.all(20.0),
        child: Form(
          child: Column(
            children: <Widget>[
              TextFormField(
                decoration: InputDecoration(labelText: 'Username'),
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Email'),
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Password'),
                obscureText: true,
              ),
              RaisedButton(
                child: Text('Save Changes'),
                onPressed: () {
                  // Handle save changes
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

---- 

Here's a detailed Flutter code snippet for the 'Chat with Chef' functionality. This code includes the UI elements and interactions for engaging in a text-based conversation with a virtual master chef. 

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(ChatWithChef());
}

class ChatWithChef extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Chat with Chef',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: ChatPage(),
    );
  }
}

class ChatPage extends StatefulWidget {
  @override
  _ChatPageState createState() => _ChatPageState();
}

class _ChatPageState extends State<ChatPage> {
  final List<ChatMessage> _messages = [];
  final TextEditingController _textController = TextEditingController();

  void _handleSubmitted(String text) {
    _textController.clear();
    ChatMessage message = ChatMessage(
      text: text,
    );
    setState(() {
      _messages.insert(0, message);
    });
  }

  Widget _buildTextComposer() {
    return IconTheme(
      data: IconThemeData(color: Theme.of(context).accentColor),
      child: Container(
        margin: EdgeInsets.symmetric(horizontal: 8.0),
        child: Row(
          children: <Widget>[
            Flexible(
              child: TextField(
                controller: _textController,
                onSubmitted: _handleSubmitted,
                decoration:
                    InputDecoration.collapsed(hintText: "Send a message"),
              ),
            ),
            Container(
              margin: EdgeInsets.symmetric(horizontal: 4.0),
              child: IconButton(
                  icon: Icon(Icons.send),
                  onPressed: () => _handleSubmitted(_textController.text)),
            ),
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Chat with Chef')),
      body: Column(
        children: <Widget>[
          Flexible(
            child: ListView.builder(
              padding: EdgeInsets.all(8.0),
              reverse: true,
              itemBuilder: (_, int index) => _messages[index],
              itemCount: _messages.length,
            ),
          ),
          Divider(height: 1.0),
          Container(
            decoration: BoxDecoration(color: Theme.of(context).cardColor),
            child: _buildTextComposer(),
          ),
        ],
      ),
    );
  }
}

class ChatMessage extends StatelessWidget {
  ChatMessage({this.text});
  final String text;

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.symmetric(vertical: 10.0),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          Container(
            margin: EdgeInsets.only(right: 16.0),
            child: CircleAvatar(child: Text('C')),
          ),
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Text('Chef', style: Theme.of(context).textTheme.subtitle1),
              Container(
                margin: EdgeInsets.only(top: 5.0),
                child: Text(text),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
```

This code creates a chat interface where users can send messages to a virtual chef. The messages are displayed in a list view, with the most recent messages appearing at the bottom. The user's input is handled by a text controller, which clears the input field after the message is sent. The sent messages are displayed as chat bubbles on the screen, with the chef's avatar and name appearing next to each message. 

This design ensures a user-friendly experience by providing a clear and intuitive interface for text-based conversation. The use of a list view for displaying messages allows for easy navigation through the chat history, and the text controller ensures that the input field is always ready for the user's next message.

----

Here's a detailed Flutter code snippet for the 'Image-to-Recipe' functionality. This includes the UI elements and interactions for inputting images of ingredients and receiving a recipe along with a tutorial.

```dart
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

class ImageToRecipe extends StatefulWidget {
  @override
  _ImageToRecipeState createState() => _ImageToRecipeState();
}

class _ImageToRecipeState extends State<ImageToRecipe> {
  PickedFile _imageFile;
  final ImagePicker _picker = ImagePicker();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Image to Recipe'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            _imageFile == null
                ? Text('No image selected.')
                : Image.file(File(_imageFile.path)),
            RaisedButton(
              child: Text('Select Image'),
              onPressed: () {
                _getImage();
              },
            ),
          ],
        ),
      ),
    );
  }

  Future _getImage() async {
    final pickedFile = await _picker.getImage(source: ImageSource.gallery);

    setState(() {
      _imageFile = pickedFile;
    });

    // Here, you would typically make a call to your backend service, sending the image
    // and receiving the recipe and tutorial in response. For the sake of this example,
    // we'll just show a dialog with a placeholder message.
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Recipe and Tutorial'),
          content: Text('Here is where you would display the recipe and tutorial for the selected image.'),
          actions: <Widget>[
            FlatButton(
              child: Text('Close'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }
}
```

This code creates a new Flutter screen with a button for selecting an image from the user's gallery. Once an image is selected, it is displayed on the screen. In a real-world application, you would then send this image to your backend service, which would process the image and return a recipe and tutorial. For the sake of this example, we're just showing a dialog with a placeholder message.

This approach ensures a user-friendly experience by allowing users to easily select images from their device and receive immediate feedback. The use of a dialog to display the recipe and tutorial also ensures that this information is presented in a clear and concise manner.
