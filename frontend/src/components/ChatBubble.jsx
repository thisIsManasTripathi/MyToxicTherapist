export default function ChatBubble(props){
    return (
        <span className={`chat-bubble ${props.sender}`}>{props.content}</span>
    )
}