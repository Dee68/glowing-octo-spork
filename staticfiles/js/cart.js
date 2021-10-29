// var updateBtns = document.getElementsByClassName("update-cart");
// for (var i = 0; i < updateBtns.length; i++) {
//     updateBtns[i].addEventListener("click", function () {
//         var productId = this.dataset.product
//         var action = this.dataset.action
//         console.log('ProductId:', productId, 'Action:', action)
//         console.log('User:', user)
//         if (user == 'AnonymousUser') {
//             console.log('user is not authenticated')
//         } else {
//             updateUserOrder(productId, action)
//         }
//     })

// }
// console.log('updateBtns length:', updateBtns.length);
// function updateUserOrder(productId, action) {
//     console.log('user is authenticated, sending data..');
//     var url = "/product/update_item/"

//     const data = { "productId": productId, "action": action }

//     fetch(url, {
//         // mode: "cors",
//         // credentials: "include",
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//             "Accept": "application/json",
//             "X-CSRFToken": csrftoken
//         },
//         body: JSON.stringify(data)
//     })
//         .then(response => response.json())
//         .then((data) => {
//             console.log("data", data);
//             location.reload();
//         })
//         .catch((error) => {
//             console.log('Error:', error);
//         })




// }