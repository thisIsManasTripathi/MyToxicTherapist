import { useEffect, useRef, useState } from 'react'
import ChatBox from './components/ChatBox'
import InputBox from './components/InputBox'
import ChatBubble from './components/ChatBubble'
import { nanoid } from 'nanoid'

function App() {

  const [messageArray, setMessageArray] = useState([])

  const [customDepArray, setCustomDepArray] = useState([{ id: 0 }])

  useEffect(() => {
    let response;
    if (customDepArray[0].id != 0) {
      fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          message: messageArray[messageArray.length - 1].message
        })
      }).then(resp => {
        resp = resp.json()
        return resp
      }).then(data => {
        setMessageArray(previousMessageArray => {
          return [...previousMessageArray, { message: data.reply, sender: "therapist" }]
        })
        const div = document.getElementById('ChatBox')
        requestAnimationFrame(() => {
          div.scrollTop = div.scrollHeight
        });
      })
    }
  }, [customDepArray[0].id])


  function sendMessage(message) {
    document.getElementById("InputBox").value = ""
    document.getElementById("InputBox").focus()
    setMessageArray((previousMessageArray) => {
      return [...previousMessageArray, { message: message, sender: "user" }]
    })

    setCustomDepArray((previousDepArray) => {
      previousDepArray[0] = { id: nanoid() }
      return previousDepArray
    })
    const div = document.getElementById('ChatBox')
    requestAnimationFrame(() => {
      div.scrollTop = div.scrollHeight
    });

  }

  const inputRef = useRef(null)


  return (
    <>
      <div className="super">


        <div id="label">
          <h1>Dr. Frank Cold's Office</h1>
        </div>
        <div className="main">
          <ChatBox
            messageArray={messageArray}
          />
          <div id="typingArea">
            <InputBox
              ref={inputRef}
            />
            <button onClick={() => { sendMessage(inputRef.current.value) }} id='sendBtn'> <img src="src/assets/right-arrow.png" /></button>
          </div>
        </div>
      </div>
    </>
  )
}

export default App
