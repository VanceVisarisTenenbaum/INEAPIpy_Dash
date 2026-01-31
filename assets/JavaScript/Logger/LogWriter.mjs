import id_generator from '../UI/Common/Functions/id_generator.mjs';

class SessionLogWriter{
    constructor(){
        this.key = String(JSON.stringify(id_generator('Storage', 'Log')));
    }

    push(entry){
        // Entry is expected to be a json object.
        let logs = this.getLogs();
        logs.push(entry);
        sessionStorage.setItem(this.key, JSON.stringify(logs));
        return null;
    }

    getLogs(){return JSON.parse(sessionStorage.getItem(this.key)) || [];}
    clear(){sessionStorage.setItem(this.key, JSON.stringify([]));}
}

export default SessionLogWriter;