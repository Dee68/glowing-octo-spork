// var now = new Date().getTime();
// var stepTime = localStorage.getItem('stepTime');

// if (stepTime == null) {
//     localStorage.setItem('stepTime', now);
// } else {
//     if (now - stepTime > (24 * 60 * 60 * 1000)) {
//         localStorage.clear();
//         localStorage.setItem('stepTime', now);
//     }
// }
const addTocartBtns = document.getElementsByClassName("update-cart");
setTimeout(() => {
    this.convertToArray();
});

function convertToArray() {
    const addTocartBtns = document.getElementsByClassName("update-cart");
    const addBtnArr = Array.from(addTocartBtns);
    return addBtnArr;
}
const addBtnArr = convertToArray();

for (let index = 0; index < addTocartBtns.length; index++) {
    addTocartBtns[i].addEventListener("click", function (e) {
        console.log(e.target);
    });

}

