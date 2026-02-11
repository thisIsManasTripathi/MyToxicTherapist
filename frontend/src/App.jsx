import { useEffect, useRef, useState } from 'react'
import ChatBox from './components/ChatBox'
import InputBox from './components/InputBox'
import ChatBubble from './components/ChatBubble'

function App() {

  const [messageArray, setMessageArray] = useState([])

  const [customDepArray, setCustomDepArray] = useState([{message:"ffm"}])

  // let customDepArray = [{ sender: "0" }]


  console.log(customDepArray)

  useEffect(() => {
    let response;
    console.log(customDepArray.length)
    if (customDepArray[0].message != "ffm") {
      console.log("this mf still ran")
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
      })
    }
  }, [customDepArray[0].message])


  function sendMessage(message) {
    setMessageArray((previousMessageArray) => {
      return [...previousMessageArray, { message: message, sender: "user" }]
    })

    setCustomDepArray((previousDepArray)=>{
      previousDepArray[0] = { message: message, sender: "user" }
      return previousDepArray
    })
    console.log("ran after set state")
  }

  const inputRef = useRef(null)


  return (
    <>
      <ChatBox
        messageArray={messageArray}
      />
      <InputBox
        ref={inputRef}
      />
      <button onClick={() => { sendMessage(inputRef.current.value) }}></button>
    </>
  )
}

export default App
