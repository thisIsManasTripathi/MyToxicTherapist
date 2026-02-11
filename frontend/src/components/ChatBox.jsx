import ChatBubble from "./ChatBubble"
import { nanoid } from 'nanoid'
export default function ChatBox(props) {

  let chatBubbleArray = props.messageArray.map(messageObj => {
    return <ChatBubble
      key={nanoid()}
      content={messageObj.message}
      sender={messageObj.sender}
    />
  })

    return (
        <div id="ChatBox">
            {chatBubbleArray}
        </div>
    )
}