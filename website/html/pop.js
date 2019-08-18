
var firebaseConfig = {
    apiKey: "AIzaSyDTGCh2DIxLDrvZCAUyVdps3SEKKm7h2pw",
    authDomain: "missing-1565944907373.firebaseapp.com",
    databaseURL: "https://missing-1565944907373.firebaseio.com",
    projectId: "missing-1565944907373",
    storageBucket: "",
    messagingSenderId: "912349228258",
    appId: "1:912349228258:web:d45bac3ffb451ded"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
var db = firebase.firestore();
var geo = firebase.firestore.GeoPoint(latitude = -33.22058,longitude = 22.94105);
var geo2 = firebase.firestore.GeoPoint(latitude = -5.73368, longitude = -40.68843);
db.collection("Missing People").add({
    "Age": "21",
    "Image": "https://image.shutterstock.com/image-photo/face-beautiful-young-girl-clean-260nw-328676489.jpg",
    "Last Seen": new firebase.firestore.GeoPoint(-33.22058, 22.94105),
    "Miss Place": new firebase.firestore.GeoPoint(-5.73368, -40.68843),
    "Name": "Animesh",
    "Months Elapsed": 1,
    "Reports sent": 12 
})
.then(function(docRef) {
    console.log("Document written with ID: ", docRef.id);
})
.catch(function(error) {
    console.error("Error adding document: ", error);
});