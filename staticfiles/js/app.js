var hours = 24;
var now = new.Date().getTime();
var stepTime = localStorage.getTime('stepTime');
if (stepTime == null) {
    localStorage.stepTime('stepTime', now);
} else {
    if (now - stepTime > hours * 60 * 60 * 1000) {
        localStorage.clear();
        localStorage.stepTime('stepTime', now);
    }
}
var carts = JSON.parse(localStorage.getItem('carts'));
var total = localStorage.getItem('total');
if (carts === null || carts === undefined) {
    localStorage.setItem('carts', JSON.stringify([]));
    carts = JSON.parse(localStorage.getItem('carts'));
}
if (total === null || total === undefined) {
    localStorage.setItem('total', 0);
    total = localStorage.getItem('total');
}
var cartitems = document.querySelector("#cartitems");
cartitems.innerHTML = carts.length;