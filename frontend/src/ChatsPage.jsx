
import { MultiChatSocket, MultiChatWindow, useMultiChatLogic, useSingleChatLogic} from 'react-chat-engine-advanced';

const ChatsPage = (props) =>{
    const chatProps = useMultiChatLogic(
        'd8b35fe2-a3b8-42dc-880b-687d72585f0d',
         props.user.username, 
         props.user.secret
        );

    return (<div style={{height: '100vh'}}>
    <MultiChatSocket {...chatProps}/>
    <MultiChatWindow {...chatProps}  style={{ height: '100%'}}/>
</div>);
}

export default ChatsPage;