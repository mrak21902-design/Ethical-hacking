function login() {
    let username = document.getElementById("username").value;

    if (username == "") {
        alert("Please enter your username");
    } else {
        alert("Welcome " + username);
    }
}
