// ----------------------------- CITATION array -----------------------------------
var modalArray = document.getElementsByClassName("modal");
var citeButtonArray = document.getElementsByName("cite-button");
var closeButtonArray = document.getElementsByClassName("close");

// populate the map
var citeMap = new Map();
for (var i = 0; i < citeButtonArray.length; i++) {
    citeMap.set(citeButtonArray[i], modalArray[i]);
}

var closeMap = new Map();
for (var i = 0; i < closeButtonArray.length; i++) {
    closeMap.set(closeButtonArray[i], modalArray[i]);
}


for (var i = 0; i < citeButtonArray.length; i++) {
	citeButtonArray[i].onclick = function() {
		citeMap.get(this).style.display = "block";
	}
}

for (var i = 0; i < closeButtonArray.length; i++) {
	closeButtonArray[i].onclick = function() {
		closeMap.get(this).style.display = "none";
	}
}


// test get elements by class name
// var modal1 = document.getElementsByClassName("modal")[0];

// array of modals
// var modalArray = document.getElementsByClassName("modal");
      
// Get the button that opens the modal
// test get elements by class name
// var btn1 = document.getElementsByClassName("cite-button")[0];

// array of buttons
// var citeButtonArray = document.getElementsByClassName("cite-button");

// Get the <span> element that closes the modal
// create a map of cite buttons to modals

// var citeMap = new Map();

// // populate the map
// for (var i = 0; i < citeButtonArray.length; i++) {
//     citeMap.set(citeButtonArray[i], modalArray[i]);
// }

// When the user clicks the button, open the modal 

// for (var i = 0; i < citeButtonArray.length; i++) {
//     citeMap.set(citeButtonArray[i], modalArray[i]);
// }

// When the user clicks on <span> (x), close the modal
// When the user clicks anywhere outside of the modal, close it
// Get the modal
