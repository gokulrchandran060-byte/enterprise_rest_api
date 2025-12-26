let token = "";

function login() {
    fetch("http://127.0.0.1:8000/api/token/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: document.getElementById("username").value,
            password: document.getElementById("password").value
        })
    })
    .then(res => res.json())
    .then(data => {
        token = data.access;
        document.getElementById("output").textContent =
            "Logged in. Token stored.";
    });
}

function createMessage() {
    fetch("http://127.0.0.1:8000/api/v1/messages/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        },
        body: JSON.stringify({
            content: document.getElementById("content").value
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("output").textContent =
            JSON.stringify(data, null, 2);
    });
}

function listMessages() {
    fetch("http://127.0.0.1:8000/api/v1/messages/all/", {
        headers: {
            "Authorization": "Bearer " + token
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("output").textContent =
            JSON.stringify(data, null, 2);
    });
}
