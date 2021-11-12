// var now = new Date().getTime();
// var stepTime = localStorage.getItem('stepTime');

// if (stepTime == null) {
//     localStorage.setItem('stepTime', now);
// } else {
//     if (now - stepTime > (24 * 60 * 60 * 1000)) {
//         localStorage.clear();
//         localStorage.setItem('stepTime', now);
//     }
//

window.onload = function () {
    //cart box
    const cartBtn = document.querySelector("#cartBtn");

    //console.log(cartBtn.firstChild);
    const cartBox = document.querySelector(".cartBox");
    cartBtn.addEventListener("click", function (e) {
        cartBox.classList.add('active');
    });

}

if (typeof (Storage) !== 'undefined') {
    console.log("local storage is working");
} else {
    console.log("local storge not working");
}
