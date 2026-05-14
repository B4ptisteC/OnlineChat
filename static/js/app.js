let input = document.getElementById("messageContent");
let value = input.value.trim();

if (value.includes("https://")) {
    let img = document.createElement("img");
    img.src = value;
    document.body.appendChild(img);
}
