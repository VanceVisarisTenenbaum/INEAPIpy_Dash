
class SessionLogWriter{
    constructor(){
        this.key = 'LogStorage'
    }

    push(entry){
        // Entry is expected to be a json object.
        let logs = JSON.parse(sessionStorage.getItem(this.key)) || [];
        logs.push(entry);
        sessionStorage.setItem(this.key, JSON.stringify(logs));
        return null;
    }

    getLogs(){JSON.parse(sessionStorage.getItem(this.key)) || [];}
    clear(){sessionStorage.setItem(this.key, JSON.stringify([]));}
}

export default SessionLogWriter;