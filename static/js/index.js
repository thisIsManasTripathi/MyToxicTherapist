async function sleep(time) {
    return new Promise((res, rej)=>{
        setTimeout(()=>res("done"), time)
    })
}
async function sendMessage(){
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
    let data = (await response);
    await sleep(700)
    data.json().then(data => addTextBubble(data.reply, 'therapist'))
}

function addTextBubble(text, sender){
    chatArea = document.getElementById('displayChatBox')
    const textNode = document.createTextNode(text)
    const chatBubble = document.createElement("span")
    chatBubble.className = `chatBubble ${sender}`
    chatBubble.appendChild(textNode)
    chatArea.appendChild(chatBubble)
}

function appendMessage(){}