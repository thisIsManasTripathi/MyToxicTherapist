async function sleep(time) {
    return new Promise((res, rej) => {
        setTimeout(() => res("done"), time)
    })
}
async function sendMessage() {
    inputBar = document.getElementById('inputBar')
    message = inputBar.value
    const response = fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    })
    addTextBubble(message, 'user')
    inputBar.value = ""
    inputBar.focus()

    let data = (await response);
    await sleep(1000)
    data.json().then(data => addTextBubble(data.reply, 'therapist'))
    div = document.getElementById('displayChatBox')
    requestAnimationFrame(() => {
        div.scrollTop = div.scrollHeight
        behavior = "smooth"
    });
}

function addTextBubble(text, sender) {
    chatArea = document.getElementById('displayChatBox')
    const textNode = document.createTextNode(text)
    const chatBubble = document.createElement("span")
    chatBubble.className = `chatBubble ${sender}`
    chatBubble.appendChild(textNode)
    chatArea.appendChild(chatBubble)
}

function appendMessage() { }