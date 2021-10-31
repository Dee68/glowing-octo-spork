const usernameField = document.querySelector('#usernameField');
const emailField = document.querySelector('#emailField');
const showPasswdToggle = document.querySelector(".showPasswdToggle");
const password1Field = document.querySelector("#passwordField1");

usernameField.addEventListener('keyup', (e) => {
    const usernameVal = e.target.value;
    if (usernameVal.length > 0) {
        fetch('/account/validate-username', {
            body: JSON.stringify({ 'username': usernameVal }),
            method: 'POST'
        }).then(res => res.json).then(data => {
            if (data.username_error) {
                usernameField.classList.add('is-invalid');
            }
        })

    }


});

// emailField.addEventListener('keyup', (e) => {
//     const emailVal = e.target.value;

//     emailField.classList.remove("is-invalid");
//     emailFeedback.style.display = 'none';
//     emailSuccess.textContent = `Checking ${emailVal}`;
//     emailSuccess.style.display = 'block';
//     if (emailVal.length > 0) {
//         fetch("/validate-email/", {
//             body: JSON.stringify({ "email": emailVal }),
//             method: "POST",
//         })
//             .then(res => res.json())
//             .then((data) => {
//                 console.log("data", data);
//                 emailSuccess.style.display = 'none';
//                 if (data.email_error) {
//                     signup.disabled = true;
//                     emailField.classList.add("is-invalid");
//                     emailFeedback.style.display = 'block';
//                     emailFeedback.innerHTML = `<p>${data.email_error}</p>`;
//                 } else {
//                     signup.disabled = false;
//                 }
//             });
//     }
// });

// const handleToggle = (e) => {
//     if (showPasswdToggle.textContent == 'SHOW') {
//         showPasswdToggle.textContent = 'HIDE';
//         password1Field.setAttribute("type", "password");
//     } else {
//         showPasswdToggle.textContent = 'SHOW';
//         password1Field.setAttribute("type", "text");
//     }
// }

// showPasswdToggle.addEventListener('click', handleToggle);
