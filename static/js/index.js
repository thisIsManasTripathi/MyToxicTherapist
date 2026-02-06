async function sendMessage(){
    inputBar = document.getElementById('inputBar')

    const response = fetch("/chat", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        message: inputBar.value
    })
    })
    let data = await response.json()
    console.log(data.reply)
   
}