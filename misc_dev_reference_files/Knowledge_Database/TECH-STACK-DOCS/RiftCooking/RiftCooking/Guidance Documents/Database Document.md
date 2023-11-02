# Understanding Data Requirements of the RiftCooking Application

The RiftCooking application requires three main types of data: course photos, ingredient images, and recipe data. 

- **Course Photos:** These are images that represent the final presentation of a dish. They are likely to be accessed frequently as they will be displayed in the user interface whenever a recipe is viewed.

- **Ingredient Images:** These are images of individual ingredients used in a recipe. They may be accessed less frequently than course photos, but will still be important for users who want to understand what each ingredient looks like.

- **Recipe Data:** This includes information such as the name of the dish, the ingredients required, the cooking instructions, and any other relevant details. This data will be accessed every time a user views a recipe.

The relationships between these data types are as follows:

- Each recipe has one course photo that represents the final dish.
- Each recipe has multiple ingredient images, one for each ingredient required.
- Each ingredient image is associated with one or more recipes.

In terms of how the data will be used in the application, course photos and ingredient images will be displayed in the user interface to provide visual guidance to users. Recipe data will be used to provide detailed instructions for cooking each dish.

# Firebase Storage Schema Design

Given the data requirements of the RiftCooking application, we can design an optimal storage schema in Firebase using NoSQL and image storage strategies. 

## Recipe Data

For the recipe data, we can use Firebase's Cloud Firestore, a NoSQL document database. Each recipe can be stored as a document in a 'recipes' collection. The document can contain fields for the recipe name, ingredients, and cooking instructions.

Here is a code snippet showing the structure of a recipe document:

```json
{
  "name": "Spaghetti Bolognese",
  "ingredients": [
    "Spaghetti",
    "Ground Beef",
    "Tomato Sauce"
  ],
  "instructions": "Boil the spaghetti. Cook the ground beef. Mix with tomato sauce."
}
```

This design allows for efficient retrieval of recipe data, as each recipe can be fetched in a single document read.

## Course Photos and Ingredient Images

For the course photos and ingredient images, we can use Firebase's Cloud Storage, a powerful, simple, and cost-effective object storage service. 

We can create two separate buckets, one for course photos and one for ingredient images. Each image can be stored as an object in the relevant bucket, with the object name corresponding to the recipe name or ingredient name.

Here is a code snippet showing how to upload an image to Cloud Storage:

```javascript
const storage = firebase.storage();
const storageRef = storage.ref();
const coursePhotoRef = storageRef.child('course_photos/Spaghetti Bolognese.jpg');

let file = ... // use the Blob or File API
coursePhotoRef.put(file).then((snapshot) => {
  console.log('Uploaded a blob or file!');
});
```

This design allows for efficient retrieval of images, as each image can be fetched directly from Cloud Storage using the object name.

----
# Dataset Scope and Requirements

The dataset we aim to create will serve as a comprehensive resource for a language model to learn about cooking. To ensure the model has a broad understanding of the subject, the dataset will encompass a wide range of recipes, cuisines, and cooking techniques. 

## Types of Recipes

The dataset will include a diverse array of recipes to cover various meal types and dietary preferences. This will range from breakfast, lunch, dinner, to snacks and desserts. Additionally, we will incorporate recipes catering to various dietary restrictions such as vegetarian, vegan, gluten-free, dairy-free, and nut-free recipes. This will ensure our language model can provide cooking information to a wide range of users with different dietary needs.

## Cuisines

To ensure the language model has a global understanding of cooking, the dataset will include recipes from various world cuisines. This will include but not be limited to:

- American
- Italian
- Mexican
- Chinese
- Japanese
- Indian
- French
- Thai
- Mediterranean
- Middle Eastern

Including a wide range of cuisines will ensure the language model can provide diverse cooking information and cater to a global audience.

## Cooking Techniques

The dataset will also include a variety of cooking techniques. This will range from basic techniques like boiling, frying, and baking to more advanced techniques like sous-vide, smoking, and fermenting. Including a wide range of cooking techniques will ensure the language model can provide comprehensive cooking advice.

# Rationale

The decision to include a wide range of recipes, cuisines, and cooking techniques is to ensure the language model has a comprehensive understanding of cooking. By including various meal types and dietary preferences, the model can cater to a wide range of users with different dietary needs. Including a variety of cuisines ensures the model can provide diverse cooking information and cater to a global audience. Lastly, including a range of cooking techniques ensures the model can provide comprehensive cooking advice, from basic to advanced techniques.

# Firebase NoSQL Schema Design for RiftCooking Application

## Introduction

The Firebase NoSQL schema for the RiftCooking application is designed to ensure optimal storage and retrieval of data. The schema includes collections for recipes and ingredients, and documents for individual recipes and ingredients. Fields for images are included in the schema, which store references to the images stored in Firebase Storage.

## Schema Design

The schema design is divided into two main collections: `recipes` and `ingredients`. Each collection contains documents representing individual recipes and ingredients respectively. 

### Recipes Collection

Each document in the `recipes` collection represents an individual recipe. The document ID is the unique identifier for the recipe. Each recipe document contains the following fields:

- `name`: The name of the recipe.
- `description`: A brief description of the recipe.
- `instructions`: The cooking instructions for the recipe.
- `imageRef`: A reference to the image of the finished dish stored in Firebase Storage.

Here is a code snippet representing a recipe document:

```json
{
  "name": "Spaghetti Bolognese",
  "description": "A classic Italian dish with rich tomato and meat sauce.",
  "instructions": "1. Cook the spaghetti. 2. Prepare the Bolognese sauce. 3. Combine and serve.",
  "imageRef": "images/recipes/spaghetti_bolognese.jpg"
}
```

### Ingredients Collection

Each document in the `ingredients` collection represents an individual ingredient. The document ID is the unique identifier for the ingredient. Each ingredient document contains the following fields:

- `name`: The name of the ingredient.
- `quantity`: The quantity of the ingredient required for the recipe.
- `recipeId`: The ID of the recipe that the ingredient is used in.
- `imageRef`: A reference to the image of the ingredient stored in Firebase Storage.

Here is a code snippet representing an ingredient document:

```json
{
  "name": "Tomato",
  "quantity": "5",
  "recipeId": "spaghetti_bolognese",
  "imageRef": "images/ingredients/tomato.jpg"
}
```

## Schema Design Reasoning

The decision to separate the recipes and ingredients into two collections is based on the principle of data normalization. This design allows for efficient storage and retrieval of data, as well as flexibility in updating individual recipes or ingredients without affecting other data.

The inclusion of `imageRef` fields in both recipe and ingredient documents allows for efficient retrieval and display of images. By storing references to the images instead of the images themselves, we can take advantage of Firebase Storage's capabilities for handling large files, while keeping our Firestore database lightweight and performant.

## ER Diagram

Below is an ER diagram representing the schema design:

```
Recipes Collection
------------------
| ID | Name | Description | Instructions | ImageRef |
----------------------------------------------------
|    |      |             |              |          |
------------------

Ingredients Collection
----------------------
| ID | Name | Quantity | RecipeId | ImageRef |
----------------------------------------------
|    |      |          |          |          |
----------------------
```

In this diagram, each row in the `Recipes` and `Ingredients` tables represents a document in the respective collection. The `RecipeId` field in the `Ingredients` table is a foreign key linking to the `ID` field in the `Recipes` table.


# Firebase Storage Schema Design for RiftCooking Application

## Introduction

This document outlines the design of an optimal storage schema in Firebase for the RiftCooking application. The schema employs NoSQL and image storage strategies to ensure seamless management and retrieval of visual inputs (course photos, ingredient images) and recipe data.

## Firebase Storage for Image Management

Firebase Storage is a powerful, simple, and cost-effective object storage service built for Google scale. It provides secure file uploads and downloads for Firebase apps, regardless of network quality.

### Image Storage Strategies

Images in Firebase Storage will be organized in folders based on their type (course photos, ingredient images). This hierarchical structure will facilitate easy retrieval and management of images. 

The naming convention for images will be as follows:

- For course photos: `coursePhotos/<course_id>/<image_name>.<extension>`
- For ingredient images: `ingredientImages/<ingredient_id>/<image_name>.<extension>`

This naming convention ensures that images related to a specific course or ingredient are grouped together, making it easier to manage and retrieve them.

To ensure optimal image sizes for efficient storage and retrieval, images will be resized before being uploaded to Firebase Storage. The maximum width for images will be set to 1024px, which is a good balance between quality and file size.

Here is a sample code snippet for uploading an image to Firebase Storage:

```javascript
const storageRef = firebase.storage().ref();
const coursePhotoRef = storageRef.child(`coursePhotos/${course_id}/${image_name}.${extension}`);

// Resize image to optimal size
const resizedImage = resizeImage(image, 1024);

// Upload the file to the path
coursePhotoRef.put(resizedImage).then((snapshot) => {
  console.log('Uploaded a blob or file!');
});
```

## Firebase Firestore for Recipe Data Management

Firebase Firestore is a flexible, scalable NoSQL cloud database to store and sync data for client- and server-side development.

### Recipe Data Schema Design

The recipe data will be stored in a collection named `recipes`. Each document in the `recipes` collection will represent a single recipe and will have the following fields:

- `id`: Unique identifier for the recipe.
- `name`: Name of the recipe.
- `description`: Description of the recipe.
- `course_id`: Identifier for the course the recipe belongs to.
- `ingredient_ids`: Array of identifiers for the ingredients used in the recipe.
- `steps`: Array of steps to prepare the recipe.

Here is a sample code snippet for adding a recipe to Firestore:

```javascript
const db = firebase.firestore();

db.collection("recipes").add({
    name: "Chicken Curry",
    description: "A delicious chicken curry recipe",
    course_id: "course1",
    ingredient_ids: ["ingredient1", "ingredient2"],
    steps: ["Step 1", "Step 2", "Step 3"]
})
.then((docRef) => {
    console.log("Document written with ID: ", docRef.id);
})
.catch((error) => {
    console.error("Error adding document: ", error);
});
```

## Conclusion

This schema design ensures efficient storage and retrieval of images and recipe data for the RiftCooking application. The use of Firebase Storage and Firestore provides a scalable and cost-effective solution for managing the application's data.

## ER Diagram

Below is an ER diagram representing the schema design:

![ER Diagram](https://example.com/er_diagram.png)