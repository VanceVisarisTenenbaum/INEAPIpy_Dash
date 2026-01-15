
import SessionLogWriter from './LogWriter.js'


class Logger {
    constructor(Writer=SessionLogWriter){
        this.LogWriter = Writer;
    }

    log(message, categories='', level='info', data=null){
        const entry = {
            'Message': message,
            'Categories': categories,
            'Level': level,
            'Data': data,
            'timestamp': new Date()
        };
        this.LogWriter.push(entry);
        return null;
    }
    getLogs(){return this.LogWriter.getLogs();}
    clear(this.LogWriter.clear();)
}