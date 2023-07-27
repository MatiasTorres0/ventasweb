// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyABS_MaHK1ylRbt2nwHGr2P5cBqxiKUSkU",
  authDomain: "ventas-514a8.firebaseapp.com",
  projectId: "ventas-514a8",
  storageBucket: "ventas-514a8.appspot.com",
  messagingSenderId: "492502627956",
  appId: "1:492502627956:web:db15a81dcfcda84a574321",
  measurementId: "G-T35G8W5YFP"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
  firebase.initializeApp(firebaseConfig);
  
  const auth = firebase.auth();
  
  const form = document.querySelector("form");
  
  form.addEventListener("submit", (e) => {
    e.preventDefault();
  
    const email = document.querySelector("input[name=email]").value;
    const password = document.querySelector("input[name=password]").value;
  
    auth.signInWithEmailAndPassword(email, password).then((user) => {
      console.log("User signed in successfully.");
    }, (error) => {
      console.log("Error signing in user:", error);
    });
  });
  